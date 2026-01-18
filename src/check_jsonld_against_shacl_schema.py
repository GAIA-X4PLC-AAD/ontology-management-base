#!/usr/bin/env python3
"""
Validate JSON-LD instance/reference files against SHACL with
ontology dependency resolution driven by the data graph.

New behaviour:

- Accepts arbitrary *.json / *.jsonld instance files.
- Automatically resolves dependency reference files from a 'base-references'
  directory based on the naming prefix of the loaded instance file.
- Optional --root / --root-dir argument controls where SHACL,
  ontology TTL files, and base-references are searched.
"""

import contextlib
import glob
import json
import logging
import os
import sys
import tempfile
import time
from argparse import ArgumentParser
from collections import Counter, defaultdict
from io import StringIO
from typing import Dict, List, Set, Tuple
from urllib.parse import urlparse

from rdflib import OWL, RDF, Graph, Namespace

# Optimization: Attempt to use Oxigraph for much faster graph operations
try:
    import oxrdflib  # noqa: F401

    FAST_STORE = "oxigraph"
except ImportError:
    FAST_STORE = "default"

try:
    from pyshacl import validate
except ImportError as e:  # pragma: no cover - environment might not have pyshacl
    validate = None  # type: ignore
    PYSHACL_IMPORT_ERROR = e
else:
    PYSHACL_IMPORT_ERROR = None

from utils.print_formatting import print_validate_jsonld_against_shacl_result

DEFAULT_ROOT_DIRECTORY = "."
CACHE_FILENAME = ".ontology_iri_cache.json"
# Standard IANA URI schemes that should be treated as absolute URIs,
# not missing CURIE prefixes, if they appear in the data.
KNOWN_URI_SCHEMES = {
    "http",
    "https",
    "ftp",
    "mailto",
    "did",
    "urn",
    "tel",
    "geo",
    "ssh",
    "git",
    "file",
}


class StepTimer:
    """
    A utility to measure and display the execution time of specific workflow steps.
    It prints directly to stdout to ensure timing info is visible immediately
    and not hidden in buffered output reports.
    """

    def __init__(self):
        self.start_time = time.perf_counter()
        self.last_step_time = self.start_time

    def mark_step(self, step_name: str):
        """
        Calculates the duration since the last mark, prints it to the console,
        and updates the timestamp for the next step.
        """
        now = time.perf_counter()
        duration = now - self.last_step_time
        total = now - self.start_time
        msg = (
            f"⏱️  [STEP DONE: {step_name}] took {duration:.3f}s (Total: {total:.3f}s)\n"
        )

        # Always print to the actual terminal, regardless of the 'file' buffer
        print(msg, file=sys.stdout)
        sys.stdout.flush()

        self.last_step_time = now


# ---------------------------------------------------------------------------
# Local JSON-LD @context resolver (minimal integration)
# ---------------------------------------------------------------------------


def iri_to_namespace_hint(iri: str) -> str | None:
    """
    Extracts a likely namespace string (hint) from a remote URL.

    Example:
        "https://schema.ascs.digital/SimpulseId/v1/credentials" -> "simpulseid"

    Used to map remote Context URLs to local folder names.
    """
    try:
        parsed = urlparse(iri)
    except Exception:
        return None

    path = parsed.path or ""
    parts = [p for p in path.split("/") if p]
    if not parts:
        return None
    return parts[0].lower()


class LocalContextResolver:
    """
    Handles the resolution of JSON-LD @context fields.

    Its primary purpose is to intercept remote URLs in @context (which often
    fail to load due to firewall or DNS issues) and replace them with the
    contents of local .jsonld files stored in a 'contexts' directory.
    """

    def __init__(self, context_root: str):
        """
        Scans the context_root directory to identify which namespaces
        are available locally.
        """
        self.context_root = os.path.abspath(context_root)
        self.available_namespaces: Set[str] = set()

        if os.path.isdir(self.context_root):
            for entry in os.listdir(self.context_root):
                p = os.path.join(self.context_root, entry)
                if os.path.isdir(p):
                    self.available_namespaces.add(entry.lower())

        logging.debug(
            "LocalContextResolver initialized with context_root=%s, available_namespaces=%s",
            self.context_root,
            sorted(self.available_namespaces),
        )

    def _local_context_file_path(self, namespace: str) -> str:
        """Constructs the expected filesystem path for a local context file."""
        ns = namespace.lower()
        filename = f"{ns}_context.jsonld"
        return os.path.join(self.context_root, ns, filename)

    def _load_local_context_object(self, namespace: str) -> dict | None:
        """
        Reads a local JSON-LD context file and extracts the dictionary
        that should replace the remote URL reference.
        """
        local_path = self._local_context_file_path(namespace)
        if not os.path.exists(local_path):
            return None

        try:
            with open(local_path, "r", encoding="utf-8") as f:
                ctx_data = json.load(f)
        except Exception as e:
            logging.warning("Failed to read local context file %s: %s", local_path, e)
            return None

        if isinstance(ctx_data, dict):
            if "@context" in ctx_data and isinstance(ctx_data["@context"], dict):
                return ctx_data["@context"]
            # Some projects store the context mapping as the root object.
            return ctx_data

        logging.warning("Local context file %s is not a JSON object.", local_path)
        return None

    def _resolve_context_entry(self, entry):
        """
        Checks a specific @context entry. If it is a URL and matches a local
        namespace, returns the local JSON object; otherwise returns the entry as-is.
        """
        if isinstance(entry, str) and entry.startswith("http"):
            namespace = iri_to_namespace_hint(entry)
            if namespace and namespace.lower() in self.available_namespaces:
                ctx_obj = self._load_local_context_object(namespace)
                if ctx_obj is not None:
                    logging.debug(
                        "Resolved remote @context %s -> inline context from %s",
                        entry,
                        self._local_context_file_path(namespace),
                    )
                    return ctx_obj

                logging.warning(
                    "Namespace '%s' is available, but context file could not be loaded: %s",
                    namespace,
                    self._local_context_file_path(namespace),
                )
            else:
                logging.debug(
                    "No matching local namespace for remote @context %s (derived=%s). Leaving unchanged.",
                    entry,
                    namespace,
                )

        return entry

    def rewrite_jsonld_file(self, jsonld_path: str) -> str:
        """
        Reads a JSON-LD file. If it contains remote context URLs that can be
        resolved locally, it writes a modified copy to a temporary file
        (with contexts inlined) and returns the path to that temporary file.
        """
        with open(jsonld_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        ctx = data.get("@context")
        if ctx is None:
            return jsonld_path

        rewritten = False

        # If context is already an inline dict, no resolving is needed.
        if isinstance(ctx, dict):
            return jsonld_path

        if isinstance(ctx, list):
            new_ctx = []
            for entry in ctx:
                resolved = self._resolve_context_entry(entry)
                if resolved != entry:
                    rewritten = True
                new_ctx.append(resolved)
            data["@context"] = new_ctx
        elif isinstance(ctx, str):
            resolved = self._resolve_context_entry(ctx)
            if resolved != ctx:
                rewritten = True
            data["@context"] = resolved
        else:
            # Unexpected structure; keep unchanged.
            return jsonld_path

        if not rewritten:
            return jsonld_path

        fd, tmp_path = tempfile.mkstemp(prefix="jsonld_rewritten_", suffix=".json")
        os.close(fd)
        with open(tmp_path, "w", encoding="utf-8") as out:
            json.dump(data, out, ensure_ascii=False, indent=2)

        return tmp_path


# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------


def setup_logging(debug: bool = False, stream=None) -> None:
    """
    Sets up the logging configuration. It allows redirecting logs to a
    specific stream (like a StringIO buffer) to capture output for reports.
    """
    if stream is None:
        stream = sys.stdout
    handlers = [logging.StreamHandler(stream)]
    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO,
        handlers=handlers,
        format="%(asctime)s [%(levelname)s] %(message)s",
        force=True,
    )


# ---------------------------------------------------------------------------
# Generic helpers
# ---------------------------------------------------------------------------


def ensure_folder_entry(ontology_dict: Dict[str, Dict], folder_name: str) -> None:
    """
    Initializes a standardized dictionary entry for a specific ontology folder
    if it doesn't already exist.
    """
    if folder_name not in ontology_dict:
        ontology_dict[folder_name] = {
            "instance": [],
            "reference": [],
            "ontologies": [],
            "shacle_shapes": [],
            "prefixes": {},
            "context_issues": {},
        }


# ---------------------------------------------------------------------------
# Prefix extraction helpers
# ---------------------------------------------------------------------------


def extract_prefixes_from_ttl(file_path: str) -> Dict[str, str]:
    """
    Parses a Turtle (TTL) file and extracts the @prefix / @base definitions
    into a dictionary.
    """
    # Suggestion 3: Use fast store
    g = Graph(store=FAST_STORE)
    g.parse(file_path, format="turtle")
    prefixes = {prefix: str(namespace) for prefix, namespace in g.namespaces()}
    logging.debug("Extracted prefixes from TTL %s: %s", file_path, prefixes)
    return prefixes


def extract_prefixes_from_jsonld(file_path: str) -> Dict[str, str]:
    """
    Parses a JSON-LD file and extracts prefix mappings defined in its @context.
    Only handles inline definitions, not remote ones.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    context = data.get("@context", {})
    prefix_mapping: Dict[str, str] = {}

    def _add_from_ctx(ctx_obj: dict) -> None:
        for key, value in ctx_obj.items():
            if isinstance(value, str) and value.endswith(("#", "/")):
                prefix_mapping[key] = value

    if isinstance(context, dict):
        _add_from_ctx(context)
    elif isinstance(context, list):
        for ctx in context:
            if isinstance(ctx, dict):
                _add_from_ctx(ctx)

    logging.debug("Extracted prefixes from JSON-LD %s: %s", file_path, prefix_mapping)
    return prefix_mapping


def merge_prefix_mappings(
    base: Dict[str, str],
    additions: Dict[str, str],
    source: str = "",
) -> Dict[str, str]:
    """
    Merges new prefix definitions into a base dictionary.
    Warns if the same prefix key maps to a different URI.
    """
    for prefix, uri in additions.items():
        if prefix in base and base[prefix] != uri:
            logging.warning(
                "Prefix collision for '%s': '%s' (kept) vs '%s' (from %s)",
                prefix,
                base[prefix],
                uri,
                source,
            )
            continue
        base[prefix] = uri
    return base


# ---------------------------------------------------------------------------
# JSON-LD context coverage checking
# ---------------------------------------------------------------------------


def _collect_used_prefixes_in_json_value(value) -> Set[str]:
    """
    Recursively checks a JSON object to find potential CURIEs (e.g. "prefix:Value")
    and collects the used prefixes, filtering out known absolute URI schemes.
    """
    used: Set[str] = set()

    def _extract_scheme(text: str) -> str | None:
        """Helper to safely extract a valid scheme/prefix from a string."""
        if ":" not in text or text.startswith("@"):
            return None
        try:
            # urlparse is robust and handles standard URI syntax (RFC 3986)
            parsed = urlparse(text)
            scheme = parsed.scheme
            # A valid scheme/prefix must be a non-empty string.
            # We filter out known IANA schemes (like 'did', 'http') so they
            # aren't flagged as 'missing prefixes'.
            if scheme and scheme not in KNOWN_URI_SCHEMES:
                return scheme
        except Exception:
            pass
        return None

    if isinstance(value, str):
        prefix = _extract_scheme(value)
        if prefix:
            used.add(prefix)

    elif isinstance(value, dict):
        for k, v in value.items():
            # Check the property key (e.g., "gx:name")
            prefix = _extract_scheme(k)
            if prefix:
                used.add(prefix)
            # Recursively check the value
            used |= _collect_used_prefixes_in_json_value(v)

    elif isinstance(value, list):
        for item in value:
            used |= _collect_used_prefixes_in_json_value(item)

    return used


def check_jsonld_context_coverage(file_path: str) -> Dict[str, Set[str]]:
    """
    Analyzes a JSON-LD file to ensure all prefixes used in the data
    (as CURIEs) are actually declared in the @context.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    context = data.get("@context", {})
    declared_prefixes: Set[str] = set()

    # NOTE: This coverage check only handles inline dict contexts.
    if isinstance(context, dict):
        declared_prefixes = {k for k in context.keys() if isinstance(k, str)}
    else:
        logging.warning(
            "Unexpected @context structure in %s (type: %s)",
            file_path,
            type(context),
        )

    used_prefixes = _collect_used_prefixes_in_json_value(data)

    missing = used_prefixes - declared_prefixes
    unused = declared_prefixes - used_prefixes

    if missing:
        logging.warning(
            "JSON-LD context in %s is missing prefixes: %s",
            file_path,
            ", ".join(sorted(missing)),
        )

    return {
        "declared": declared_prefixes,
        "used": used_prefixes,
        "missing": missing,
        "unused": unused,
    }


# ---------------------------------------------------------------------------
# Manifest / type resolution helpers (from original script)
# ---------------------------------------------------------------------------


def resolve_manifest_local_path(
    name: str, file_type: str, root_dir: str = DEFAULT_ROOT_DIRECTORY
) -> str:
    """
    Constructs a local file path based on a standard naming convention
    (folder/folder_type.ttl).
    """
    filename = f"{name}_{file_type}.ttl"
    local_path = os.path.join(root_dir, name, filename)
    print(f"Resolved manifest local path for {name} ({file_type}): {local_path}")
    return local_path


def resolve_json_type(
    json_type: str,
    namespace_prefixes: Dict[str, str],
    manifest_dir_url: str | None = None,
    root_dir: str = DEFAULT_ROOT_DIRECTORY,
) -> str:
    """
    Converts a JSON-LD @type value (which might be a CURIE) into a full IRI
    using the available prefix mappings.
    """
    if ":" in json_type and "://" not in json_type:
        prefix, local_name = json_type.split(":", 1)
        if prefix in namespace_prefixes:
            return namespace_prefixes[prefix] + local_name
    elif manifest_dir_url is not None:
        # Legacy logic for resolving types via manifest manifests (mostly unused now)
        parsed_url = urlparse(manifest_dir_url)
        if parsed_url.path.endswith("/"):
            manifest_dir_url = manifest_dir_url.rstrip("/")
            parsed_url = parsed_url._replace(path=manifest_dir_url)
            manifest_dir_url = parsed_url.geturl()
        local_ontology = os.path.join(root_dir, parsed_url.path.lstrip("/"))
        if os.path.exists(local_ontology):
            with open(local_ontology, "r", encoding="utf-8") as f:
                try:
                    manifest_data = json.load(f)
                except json.JSONDecodeError:
                    return json_type
            manifests = manifest_data.get("manifest", [])
            for manifest in manifests:
                manifest_name = manifest.get("name")
                manifest_type = manifest.get("@type")
                if manifest_name == json_type and manifest_type:
                    type_prefix, type_local_name = manifest_type.split(":", 1)
                    if type_prefix in namespace_prefixes:
                        return namespace_prefixes[type_prefix] + type_local_name
                    if manifest_dir_url.endswith("/"):
                        manifest_dir_url = manifest_dir_url.rstrip("/")
                    resolved = f"{manifest_dir_url}#{type_local_name}"
                    print(
                        f"Resolved unknown @type for {json_type} "
                        f"from manifest file via hash-style IRI: {resolved}"
                    )
                    return resolved
            return json_type
    return json_type


# ---------------------------------------------------------------------------
# RDF type extraction
# ---------------------------------------------------------------------------


def extract_used_types(
    data_graph: Graph,
    namespace_prefixes: Dict[str, str],
    root_dir: str,
    file=None,
) -> Set[str]:
    """
    Scans the loaded data graph for all 'rdf:type' triples and resolves them
    to full IRIs. Used to determine which ontologies are needed.
    """
    if file is None:
        file = sys.stdout
    print("📌 Extracting all rdf:type from data graph...", file=file)
    used_types: Set[str] = set()
    type_counts: Counter[str] = Counter()

    rdf_type_pred = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")["type"]

    manifest_dir_url = None
    for _, _, obj in data_graph.triples((None, rdf_type_pred, None)):
        resolved_type = resolve_json_type(
            str(obj), namespace_prefixes, manifest_dir_url, root_dir
        )
        used_types.add(resolved_type)
        type_counts[resolved_type] += 1

    print("✅ Found the following rdf:type values:", file=file)
    for rdf_type, count in sorted(type_counts.items(), key=lambda x: x[0]):
        print(f"   {rdf_type} (used {count} times)", file=file)

    return used_types


# ---------------------------------------------------------------------------
# RDF loading
# ---------------------------------------------------------------------------


def load_rdf_files(
    rdf_files: List[str],
    rdf_format: str = "json-ld",
    file=None,
    context_resolver: LocalContextResolver | None = None,
) -> tuple[Graph, int, int]:
    """
    Aggregates content from multiple RDF files into a single rdflib Graph.
    Includes logic to rewrite JSON-LD files via the context_resolver to
    prevent network calls.
    """
    if file is None:
        file = sys.stdout

    # Suggestion 3: Use fast store
    data_graph = Graph(store=FAST_STORE)
    loaded_count = 0
    failed_count = 0
    temp_files_to_cleanup: List[str] = []

    for i, rdf_file in enumerate(rdf_files, start=1):
        try:
            parse_target = rdf_file
            if rdf_format.lower() in {"json-ld", "jsonld"} and context_resolver:
                # Rewrite remote contexts to inline local contexts when possible.
                rewritten = context_resolver.rewrite_jsonld_file(rdf_file)
                if rewritten != rdf_file:
                    temp_files_to_cleanup.append(rewritten)
                parse_target = rewritten

            data_graph.parse(parse_target, format=rdf_format)
            loaded_count += 1
            logging.debug("Loaded %s file: %s", rdf_format, rdf_file)
            print(f"✅ [{i}/{len(rdf_files)}] Loaded: {rdf_file}", file=file)
        except Exception as e:  # pragma: no cover - defensive
            failed_count += 1
            logging.error("Failed to load %s: %s", rdf_file, e)
            print(f"❌ [{i}/{len(rdf_files)}] Failed: {rdf_file} → {e}", file=file)

    # Best-effort cleanup of rewritten temp files.
    for tmp in temp_files_to_cleanup:
        try:
            os.remove(tmp)
        except Exception:
            pass

    return data_graph, loaded_count, failed_count


# ---------------------------------------------------------------------------
# Ontology & JSON-LD discovery
# ---------------------------------------------------------------------------


def build_dict_for_ontologies(
    root_dir: str,
    paths: List[str],
) -> Dict[str, Dict[str, object]]:
    """
    Scans the provided paths to organize files by their containing folder.

    NEW FUNCTIONALITY:
    When an instance file is found, it extracts the file's prefix (e.g., 'envited-x'
    from 'envited-x_instance.json') and automatically scans the 'base-references'
    directory for any corresponding reference files (e.g., 'envited-x_manifest_reference.json')
    and adds them to the validation set.
    """
    ontology_dict: Dict[str, Dict[str, object]] = {}

    collected_files: List[str] = []

    # Define the base-references directory
    base_refs_dir = os.path.join(root_dir, "base-references")

    for p in paths:
        # Interpret paths relative to current working directory, not root_dir.
        full_path = os.path.normpath(p)

        if os.path.isdir(full_path):
            # Legacy behaviour: directories with *_instance.json / *_reference.json.
            collected_files.extend(
                glob.glob(os.path.join(full_path, "*_instance.json"))
            )
            collected_files.extend(
                glob.glob(os.path.join(full_path, "*_reference.json"))
            )
        elif os.path.isfile(full_path) and (
            full_path.endswith(".json") or full_path.endswith(".jsonld")
        ):
            # Generic single JSON/JSON-LD file
            collected_files.append(full_path)

            # Old pattern: from an explicit *_instance.json we still auto-add
            # sibling *_reference.json files in the same directory, UNLESS
            # it is an *_inline_instance.json file.
            if full_path.endswith("_instance.json") and not full_path.endswith(
                "_inline_instance.json"
            ):
                directory = os.path.dirname(full_path)
                collected_files.extend(
                    glob.glob(os.path.join(directory, "*_reference.json"))
                )

    if not collected_files:
        return {}

    # Classify generic JSON files
    instance_files: List[str] = []
    reference_files: List[str] = []

    for f in collected_files:
        if f.endswith("_reference.json"):
            reference_files.append(f)
        else:
            instance_files.append(f)

    # Group JSON-LD by folder
    for key, files in (("instance", instance_files), ("reference", reference_files)):
        for file_path in files:
            rel_dir = os.path.relpath(os.path.dirname(file_path), root_dir)
            folder_name = rel_dir.replace(os.sep, "/")
            ensure_folder_entry(ontology_dict, folder_name)
            ontology_dict[folder_name][key].append(os.path.normpath(file_path))

    # -----------------------------------------------------------------------
    # NEW: Resolve Reference Files from 'base-references' based on Prefix
    # -----------------------------------------------------------------------
    if os.path.isdir(base_refs_dir):
        for inst_file in instance_files:
            # Determine the key/folder for this instance
            rel_dir = os.path.relpath(os.path.dirname(inst_file), root_dir)
            folder_name = rel_dir.replace(os.sep, "/")

            # Determine prefix: 'envited-x_instance.json' -> 'envited-x'
            filename = os.path.basename(inst_file)
            prefix = filename.split("_")[0]

            # Determine prefix: 'envited-x_instance.json' -> 'envited-x'
            filename = os.path.basename(inst_file)
            prefix = filename.split("_")[0]

            # PATTERN STRATEGY:
            # 1. Always look for references matching the instance prefix (e.g. 'envited-x')
            # 2. Always include 'gx' references as they are the shared base layer (LegalPerson, etc.)
            search_patterns = {f"{prefix}*reference.json"}
            if prefix != "gx":
                search_patterns.add("gx*reference.json")

            matching_refs = []
            for pattern in search_patterns:
                matching_refs.extend(glob.glob(os.path.join(base_refs_dir, pattern)))

            # Add them to the dictionary for this folder if not already present
            for ref_path in matching_refs:
                ref_norm = os.path.normpath(ref_path)
                if ref_norm not in ontology_dict[folder_name]["reference"]:
                    ontology_dict[folder_name]["reference"].append(ref_norm)
                    print(
                        f"🔗 Auto-linked reference: {os.path.basename(ref_norm)} -> {filename}"
                    )

    return ontology_dict


# ---------------------------------------------------------------------------
# Enrich dict with JSON-LD prefixes and context coverage
# ---------------------------------------------------------------------------


def add_jsonld_prefixes_and_context_info(
    ontology_dict: Dict[str, Dict[str, object]],
) -> None:
    """
    Iterates through all collected instance and reference files to:
    1. Extract their JSON-LD prefixes.
    2. Check for missing prefix declarations in their @context.
    """
    for folder_key, contents in ontology_dict.items():
        files_to_process: List[str] = []
        context_issues: Dict[str, Dict[str, Set[str]]] = {}

        for key in ("instance", "reference"):
            for file_path in contents.get(key, []):  # type: ignore[arg-type]
                files_to_process.append(file_path)
                if file_path.endswith(".json") or file_path.endswith(".jsonld"):
                    coverage = check_jsonld_context_coverage(file_path)
                    context_issues[file_path] = coverage

        prefixes: Dict[str, str] = {}
        for json_file in files_to_process:
            mapping = extract_prefixes_from_jsonld(json_file)
            merge_prefix_mappings(prefixes, mapping, source=folder_key)

        contents["prefixes"] = prefixes
        contents["context_issues"] = context_issues

        logging.debug(
            "Folder '%s': JSON-LD prefixes=%s, context_issues for %d files",
            folder_key,
            prefixes,
            len(context_issues),
        )


def extend_prefixes_with_schema_files(
    ontology_dict: Dict[str, Dict[str, object]],
    root_dir: str,
) -> None:
    """
    Extracts prefixes from the loaded ontology and SHACL TTL files and
    merges them into the dictionary's prefix list.
    """
    for folder_key, contents in ontology_dict.items():
        ttl_files: List[str] = []
        ttl_files.extend(contents.get("ontologies", []))  # type: ignore[list-item]
        ttl_files.extend(contents.get("shacle_shapes", []))  # type: ignore[list-item]

        if not ttl_files:
            continue

        ttl_prefixes: Dict[str, str] = {}
        for ttl in ttl_files:
            try:
                mapping = extract_prefixes_from_ttl(ttl)
                merge_prefix_mappings(ttl_prefixes, mapping, source=ttl)
            except Exception as e:  # pragma: no cover - defensive
                logging.warning("Failed to extract prefixes from TTL %s: %s", ttl, e)

        merge_prefix_mappings(
            contents["prefixes"], ttl_prefixes, source=f"{folder_key} (TTL)"
        )
        logging.debug(
            "Folder '%s': extended prefixes with TTL files: %s",
            folder_key,
            ttl_prefixes,
        )


def build_global_prefix_mapping(
    ontology_dict: Dict[str, Dict[str, object]],
) -> Dict[str, str]:
    """
    Consolidates prefix mappings from all folders into a single global
    map for IRI resolution.
    """
    global_prefixes: Dict[str, str] = {}
    for folder_key, contents in ontology_dict.items():
        folder_prefixes = contents.get("prefixes", {})  # type: ignore[assignment]
        merge_prefix_mappings(global_prefixes, folder_prefixes, source=folder_key)
    logging.debug("Global dynamic prefixes: %s", global_prefixes)
    return global_prefixes


def print_prefix_mapping(prefixes: Dict[str, str], file=None) -> None:
    """
    Helper function to print the resolved prefix-to-namespace mapping
    in a readable table format.
    """
    if file is None:
        file = sys.stdout

    print("\n✅ Resolved Dynamic Prefix Mapping:", file=file)
    if not prefixes:
        print("   (no prefixes found)", file=file)
        return

    # Compute alignment width on printable label (treat empty prefix as '(default)')
    labels = [(p if p else "(default)") for p in prefixes.keys()]
    max_len = max(len(label) for label in labels)

    header_prefix = "Prefix".ljust(max_len)
    print(f"   {header_prefix}    → Namespace", file=file)
    print(f"   {'-' * max_len}    ─ {'-' * 60}", file=file)

    for prefix, ns in sorted(prefixes.items(), key=lambda x: (x[0] or "")):
        label = prefix if prefix else "(default)"
        print(f"   {label.ljust(max_len)}    → {ns}", file=file)
    print("", file=file)


# ---------------------------------------------------------------------------
# Helpers for instance/reference collection & data graph
# ---------------------------------------------------------------------------


def collect_instance_and_reference_files(
    ontology_dict: Dict[str, Dict[str, object]],
) -> Tuple[List[str], List[str]]:
    """
    Flattens the per-folder lists of files into two master lists:
    one for instances and one for references.
    """
    instance_files: List[str] = []
    reference_files: List[str] = []
    for contents in ontology_dict.values():
        instance_files.extend(contents.get("instance", []))  # type: ignore[list-item]
        reference_files.extend(contents.get("reference", []))  # type: ignore[list-item]
    # deduplicate and sort for stable order
    instance_files = sorted(set(instance_files))
    reference_files = sorted(set(reference_files))
    return instance_files, reference_files


def build_data_graph_from_dict(
    ontology_dict: Dict[str, Dict[str, object]],
    output_buffer: StringIO,
    context_resolver: LocalContextResolver | None = None,
) -> tuple[Graph, int, int]:
    """
    Orchestrates the loading of the Data Graph by collecting all instance
    and reference files and parsing them.
    """

    def print_out(*args, **kwargs) -> None:
        print(*args, **kwargs, file=output_buffer)

    instance_files, reference_files = collect_instance_and_reference_files(
        ontology_dict
    )
    all_jsonld_files = instance_files + reference_files

    if not all_jsonld_files:
        print_out("Error code 100: No instance/reference JSON-LD files found.")
        # Suggestion 3: Fast Store
        return Graph(store=FAST_STORE), 0, 0

    print_out("📌 Loading JSON-LD files into data graph...")
    # NOTE: This loads only the JSON(-LD) files discovered from the CLI args.
    return load_rdf_files(
        all_jsonld_files,
        rdf_format="json-ld",
        file=output_buffer,
        context_resolver=context_resolver,
    )


# ---------------------------------------------------------------------------
# Ontology graph dependency helpers (ontology IRI based, with normalization)
# ---------------------------------------------------------------------------


def normalize_iri(iri: str) -> str:
    """
    Standardizes IRIs by removing trailing slashes or hash signs to
    ensure reliable string comparisons.
    """
    while iri.endswith("#") or iri.endswith("/"):
        iri = iri[:-1]
    return iri


def _build_ontology_iri_index(root_dir: str) -> Dict[str, str]:
    """
    Scans for all *_ontology.ttl files and builds a map where:
    Key = Ontology IRI (from owl:Ontology)
    Value = File path

    Uses a cache file to avoid re-parsing unchanged TTL files.
    """
    cache_path = os.path.join(root_dir, CACHE_FILENAME)
    cache: Dict[str, Dict[str, object]] = {}

    # Load cache if exists
    if os.path.exists(cache_path):
        try:
            with open(cache_path, "r", encoding="utf-8") as f:
                cache = json.load(f)
        except Exception as e:
            logging.warning("Failed to load ontology cache: %s. Rebuilding.", e)

    iri_to_file: Dict[str, str] = {}
    ontology_files = glob.glob(f"{root_dir}/**/*_ontology.ttl", recursive=True)

    updated_cache = {}
    cache_dirty = False

    for onto in ontology_files:
        onto_norm = os.path.normpath(onto)
        try:
            mtime = os.path.getmtime(onto_norm)
        except OSError:
            continue  # File might have vanished

        # Check cache
        cached_entry = cache.get(onto_norm)
        if cached_entry and cached_entry.get("mtime") == mtime:
            # Cache hit
            print(f"📦 Cache hit for: {onto_norm}")
            iri = cached_entry.get("iri")
            if iri:
                # Add to current index
                if iri in iri_to_file and iri_to_file[iri] != onto_norm:
                    logging.warning(
                        "Ontology IRI %s defined by multiple files: %s, %s",
                        iri,
                        iri_to_file[iri],
                        onto_norm,
                    )
                else:
                    iri_to_file[iri] = onto_norm

                # Keep in updated cache
                updated_cache[onto_norm] = cached_entry
                continue

        # Cache miss or stale: Parse file
        # Suggestion 3: Fast Store
        g = Graph(store=FAST_STORE)
        try:
            g.parse(onto_norm, format="turtle")
        except Exception as e:
            logging.warning(
                "Failed to parse ontology %s for IRI index: %s", onto_norm, e
            )
            continue

        found_iri = None
        for s in g.subjects(RDF.type, OWL.Ontology):
            iri_raw = str(s)
            found_iri = normalize_iri(iri_raw)

            if found_iri in iri_to_file and iri_to_file[found_iri] != onto_norm:
                logging.warning(
                    "Ontology IRI %s defined by multiple files: %s, %s",
                    iri_raw,
                    iri_to_file[found_iri],
                    onto_norm,
                )
            else:
                iri_to_file[found_iri] = onto_norm

            # Optimization: usually only one ontology per file.
            break

        if found_iri:
            updated_cache[onto_norm] = {"mtime": mtime, "iri": found_iri}
            cache_dirty = True

    # Check if we need to save cache (if entries changed or files removed)
    if cache_dirty or len(updated_cache) != len(cache):
        try:
            with open(cache_path, "w", encoding="utf-8") as f:
                json.dump(updated_cache, f, indent=2)
            logging.debug("Updated ontology IRI cache at %s", cache_path)
        except Exception as e:
            logging.warning("Failed to write ontology cache: %s", e)

    logging.debug("Ontology IRI index: %s", iri_to_file)
    return iri_to_file


def _build_ontology_dependencies(
    root_dir: str,
    iri_to_file: Dict[str, str],
) -> Dict[str, Set[str]]:
    """
    Constructs a dependency graph between ontology files.
    A dependency exists if Ontology A defines a prefix that points
    to the IRI of Ontology B.
    """
    deps: Dict[str, Set[str]] = defaultdict(set)
    ontology_files = glob.glob(f"{root_dir}/**/*_ontology.ttl", recursive=True)

    for onto in ontology_files:
        # Suggestion 3: Fast Store
        g = Graph(store=FAST_STORE)
        try:
            g.parse(onto, format="turtle")
        except Exception as e:  # defensive
            logging.warning(
                "Failed to parse ontology %s for dependency graph: %s", onto, e
            )
            continue

        for _, ns in g.namespaces():
            ns_str_raw = str(ns)
            ns_str = normalize_iri(ns_str_raw)
            target_file = iri_to_file.get(ns_str)
            if target_file:
                deps[onto].add(target_file)

    logging.debug("Ontology dependency graph: %s", deps)
    return deps


def _expand_ontology_dependencies_from(
    initial_files: List[str],
    deps: Dict[str, Set[str]],
) -> List[str]:
    """
    Performs a transitive closure on the dependency graph to find all
    ontology files required by the initial set.
    """
    closure: Set[str] = set(os.path.normpath(f) for f in initial_files)
    queue: List[str] = list(closure)

    while queue:
        current = queue.pop()
        for dep in deps.get(current, set()):
            dep_norm = os.path.normpath(dep)
            if dep_norm not in closure:
                closure.add(dep_norm)
                queue.append(dep_norm)

    return sorted(closure)


# ---------------------------------------------------------------------------
# SHACL + ontology loading based on context namespaces AND used types
# ---------------------------------------------------------------------------


def _get_namespace_from_iri(iri: str, prefix_mapping: Dict[str, str]) -> str | None:
    """
    Reverse look-up: Given a full IRI, determines the associated prefix
    (namespace key) from the mapping.
    """
    for prefix, namespace_url in prefix_mapping.items():
        if iri.startswith(namespace_url):
            return prefix
    return None


def load_shacl_and_ontologies(
    root_dir: str,
    used_types: Set[str],
    global_prefixes: Dict[str, str],
    file=None,
) -> Tuple[Graph, Graph, List[str], List[str]]:
    """
    Determines which SHACL and Ontology files to load.

    Strategy:
    1. Identify namespaces used in the Data Graph (via global_prefixes).
    2. Load all files in folders matching those namespaces.
    3. Resolve transitive dependencies using OWL imports/prefixes.
    4. Validate that all used rdf:types map to a known namespace.
    """
    if file is None:
        file = sys.stdout

    logging.debug("Starting to load SHACL and ontology files based on context.")

    # Step 1: Identify all namespaces referenced in the JSON-LD context
    # These become the "targets" for loading folders.
    target_namespaces = set(global_prefixes.keys())

    # Step 2: Check coverage of used_types
    # If a type's namespace is NOT in the context, warn the user.
    for rdf_type in used_types:
        ns_key = _get_namespace_from_iri(rdf_type, global_prefixes)
        if ns_key and ns_key not in target_namespaces:
            print(
                f"⚠️  WARNING: rdf:type '{rdf_type}' belongs to namespace '{ns_key}' "
                "which was NOT found in the global @context prefixes. "
                "Validation rules for this type might be missing.",
                file=file,
            )
        elif not ns_key:
            # Type might be a full IRI not covered by any prefix, or a local IRI.
            logging.debug("Could not determine namespace key for type: %s", rdf_type)

    # Step 3: Collect files from the targeted folders
    # We assume folder name matches the namespace prefix key (e.g. "gx" -> "./gx")
    relevant_shacl_files: List[str] = []
    initial_ontology_files: List[str] = []

    for ns in target_namespaces:
        folder_path = os.path.join(root_dir, ns)
        if os.path.isdir(folder_path):
            # Load all SHACL and Ontology files in this namespace folder
            # Recursively finding files ensures we get nested structures if any
            shacl_in_folder = glob.glob(f"{folder_path}/**/*_shacl.ttl", recursive=True)
            onto_in_folder = glob.glob(
                f"{folder_path}/**/*_ontology.ttl", recursive=True
            )
            relevant_shacl_files.extend(shacl_in_folder)
            initial_ontology_files.extend(onto_in_folder)
        else:
            logging.debug(
                "Namespace '%s' in context does not match any local folder '%s'. Skipping.",
                ns,
                folder_path,
            )

    # Step 4: Resolve ontology dependencies transitively
    # Even if we load 'gx', it might depend on 'skos' which isn't in the context.
    iri_index = _build_ontology_iri_index(root_dir)
    deps = _build_ontology_dependencies(root_dir, iri_index)
    relevant_ontology_files = _expand_ontology_dependencies_from(
        initial_files=initial_ontology_files, deps=deps
    )

    # FORCE RELATIVE TO ROOT & HARMONIZE PATHS
    def _harmonize_path(p: str) -> str:
        rel = os.path.relpath(p, root_dir)
        norm = os.path.normpath(rel)
        if (
            not os.path.isabs(norm)
            and not norm.startswith(".")
            and not norm.startswith("/")
        ):
            return f".{os.sep}{norm}"
        return norm

    # 2b) Always include core base ontologies (support vocabularies) if present
    support_ontologies = [
        "base-ontologies/rdf/rdf_ontology.ttl",
        "base-ontologies/rdfs/rdfs_ontology.ttl",
        "base-ontologies/owl/owl_ontology.ttl",
        "base-ontologies/sh/sh_ontology.ttl",
        "base-ontologies/skos/skos_ontology.ttl",
        "base-ontologies/foaf/foaf_ontology.ttl",
        "base-ontologies/org/org_ontology.ttl",
        "base-ontologies/prov/prov_ontology.ttl",
    ]

    final_ontology_paths = []
    seen = set()

    # Add relevant ontologies + support ontologies
    for path in relevant_ontology_files:
        h = _harmonize_path(path)
        if h not in seen:
            seen.add(h)
            final_ontology_paths.append(h)

    for rel in support_ontologies:
        full = os.path.normpath(os.path.join(root_dir, rel))
        if os.path.exists(full):
            h = _harmonize_path(full)
            if h not in seen:
                seen.add(h)
                final_ontology_paths.append(h)

    relevant_ontology_files = sorted(final_ontology_paths)
    relevant_shacl_files = sorted(
        [_harmonize_path(p) for p in set(relevant_shacl_files)]
    )

    # Logging / human-readable summary
    if relevant_shacl_files:
        print("📌 Relevant SHACL files to load (Context-Driven):", file=file)
        for path in relevant_shacl_files:
            print(f"   {path}", file=file)
    else:
        print(
            "📌 No relevant SHACL files found for the namespaces in @context.",
            file=file,
        )

    if relevant_ontology_files:
        print("📌 Relevant ontology files to load (Context-Driven):", file=file)
        for path in relevant_ontology_files:
            print(f"   {path}", file=file)
    else:
        print(
            "📌 No relevant ontology files found for the namespaces in @context.",
            file=file,
        )

    # Suggestion 3: Fast Store Initialization
    ont_graph = Graph(store=FAST_STORE)
    for ontology_file in relevant_ontology_files:
        tmp_graph = Graph(store=FAST_STORE)
        try:
            tmp_graph.parse(ontology_file, format="turtle")
            ont_graph += tmp_graph
            print(
                f"✅ Loaded Ontology file into ontology graph: {ontology_file}",
                file=file,
            )
        except Exception as e:
            # FIX: Explicitly print the error to the output buffer so the user can see it
            # even if debug logging is disabled.
            print(f"❌ Failed to parse ontology {ontology_file}: {e}", file=file)
            logging.warning(
                "Failed to parse ontology %s when building ontology graph: %s",
                ontology_file,
                e,
            )

    # Suggestion 3: Fast Store Initialization
    shacl_graph = Graph(store=FAST_STORE)
    for shacl_file in relevant_shacl_files:
        tmp_graph = Graph(store=FAST_STORE)
        try:
            tmp_graph.parse(shacl_file, format="turtle")
            shacl_graph += tmp_graph
            print(f"✅ Loaded SHACL file into shacl graph: {shacl_file}", file=file)
        except Exception as e:
            # FIX: Explicitly print the error to the output buffer.
            print(f"❌ Failed to parse SHACL file {shacl_file}: {e}", file=file)
            logging.warning("Failed to parse SHACL file %s: %s", shacl_file, e)

    logging.debug("Completed loading SHACL and ontology files.")
    return shacl_graph, ont_graph, relevant_shacl_files, relevant_ontology_files


# ---------------------------------------------------------------------------
# Main validation orchestrator
# ---------------------------------------------------------------------------
def validate_jsonld_against_shacl(
    root_dir: str,
    ontology_dict: Dict[str, Dict[str, object]],
    debug: bool = False,
    inference_mode: str = "rdfs",
    context_resolver: LocalContextResolver | None = None,
    logfile: str | None = None,
) -> Tuple[int, str]:
    """
    The master controller function that orchestrates the entire validation pipeline:
    1. Analysis of JSON-LD contexts.
    2. Construction of the Data Graph.
    3. Discovery of required Ontologies/Shapes based on data types.
    4. Execution of the PySHACL validator.
    """
    output_buffer = StringIO()
    timer = StepTimer()

    def print_out(*args, **kwargs) -> None:
        # We print to the buffer for the return value/logfile
        print(*args, **kwargs, file=output_buffer)
        # We also print to stdout immediately so the user sees progress
        print(*args, **kwargs, file=sys.stdout)
        sys.stdout.flush()

    setup_logging(debug, stream=output_buffer)
    logger = logging.getLogger()
    if not debug:
        # FIX: Do not disable the logger completely, as it hides warnings.
        # Set level to WARNING to show critical issues while hiding INFO/DEBUG.
        logger.setLevel(logging.WARNING)

    if PYSHACL_IMPORT_ERROR is not None:
        print_out(
            f"Error: pyshacl is not installed. Import error: {PYSHACL_IMPORT_ERROR}"
        )
        return 99, output_buffer.getvalue()

    if not ontology_dict:
        print_out("Error code 100: No valid files found.")
        return 100, output_buffer.getvalue()

    # --- Step 1: JSON-LD Analysis ---
    print("🚀 Step 1: Analyzing JSON-LD contexts and prefixes...")
    sys.stdout.flush()
    add_jsonld_prefixes_and_context_info(ontology_dict)
    timer.mark_step("JSON-LD Prefix Analysis")

    # --- Step 2: Build Data Graph ---
    print("🚀 Step 2: Building Data Graph (Parsing JSON-LD files)...")
    sys.stdout.flush()
    data_graph, loaded_count, failed_count = build_data_graph_from_dict(
        ontology_dict, output_buffer, context_resolver=context_resolver
    )

    if loaded_count == 0:
        return 101, output_buffer.getvalue()
    if len(data_graph) == 0:
        return 102, output_buffer.getvalue()

    timer.mark_step("Data Graph Loading")

    # --- Step 3: Extract RDF Types ---
    print("🚀 Step 3: Extracting RDF types to determine dependencies...")
    sys.stdout.flush()
    jsonld_prefixes = build_global_prefix_mapping(ontology_dict)
    used_types = extract_used_types(
        data_graph, jsonld_prefixes, root_dir, file=output_buffer
    )
    timer.mark_step("RDF Type Extraction")

    # --- Step 4: Load SHACL & Ontologies ---
    print("🚀 Step 4: Loading relevant SHACL shapes and Ontologies...")
    sys.stdout.flush()
    shacl_graph, ont_graph, relevant_shacl_files, relevant_ontology_files = (
        load_shacl_and_ontologies(
            root_dir,
            used_types,
            global_prefixes=jsonld_prefixes,
            file=output_buffer,
        )
    )
    timer.mark_step("Schema Loading (SHACL/OWL)")

    # --- Step 5: Final Prefix Extension ---
    print("🚀 Step 5: Final Prefix Extension...")
    sys.stdout.flush()
    for path in relevant_ontology_files:
        rel_dir = os.path.relpath(os.path.dirname(path), root_dir)
        folder_name = rel_dir.replace(os.sep, "/")
        ensure_folder_entry(ontology_dict, folder_name)
        ontology_dict[folder_name]["ontologies"].append(os.path.normpath(path))

    for path in relevant_shacl_files:
        rel_dir = os.path.relpath(os.path.dirname(path), root_dir)
        folder_name = rel_dir.replace(os.sep, "/")
        ensure_folder_entry(ontology_dict, folder_name)
        ontology_dict[folder_name]["shacle_shapes"].append(os.path.normpath(path))

    extend_prefixes_with_schema_files(ontology_dict, root_dir)
    timer.mark_step("Prefix Extension")

    # --- Step 6: Core Validation (The main bottleneck) ---
    print(f"🚀 Step 6: Performing SHACL validation (Inference: {inference_mode})...")
    sys.stdout.flush()
    instance_files, reference_files = collect_instance_and_reference_files(
        ontology_dict
    )

    # Note: we redirect pyshacl internal logs to our buffer
    with contextlib.redirect_stdout(output_buffer), contextlib.redirect_stderr(
        output_buffer
    ):
        # Suggestion 2: Use inplace=True to significantly reduce memory/time overhead
        # Note: We reverted to inplace=False because Oxigraph is strict about RDF correctness,
        # and standard reasoners (like owlrl) might generate triples (e.g. literal subjects)
        # that are technically invalid in strict RDF, causing a crash.
        conforms, report_graph, v_text = validate(
            data_graph,
            shacl_graph=shacl_graph,
            ont_graph=ont_graph,
            abort_on_first=False,
            inference=inference_mode,
            validation_mode="strict",
            debug=debug,
            inplace=False,
        )

    timer.mark_step("PySHACL Validation Engine")

    # Final reporting
    if logfile:
        with open(logfile, "w", encoding="utf-8") as f:
            f.write(v_text)

    if not conforms:
        print_validate_jsonld_against_shacl_result(
            False,
            instance_files + reference_files,
            "",
            report_graph=report_graph,
            exit_code=None,
            file=output_buffer,
        )
        return 210, output_buffer.getvalue()
    else:
        print_validate_jsonld_against_shacl_result(
            True,
            instance_files + reference_files,
            v_text,
            exit_code=None,
            file=output_buffer,
        )
        return 0, output_buffer.getvalue()


# ---------------------------------------------------------------------------
# CLI entrypoint
# ---------------------------------------------------------------------------


def main() -> None:
    parser = ArgumentParser(
        description=(
            "Validate JSON-LD instance/reference files against SHACL with "
            "ontology dependency resolution driven by the data graph."
        )
    )
    parser.add_argument(
        "paths",
        nargs="+",
        help=(
            "JSON/JSON-LD files and/or directories. "
            "Files are treated as instances; directories are scanned for "
            "*_instance.json and *_reference.json."
        ),
    )
    parser.add_argument(
        "--root",
        "--root-dir",
        dest="root_dir",
        type=str,
        default=DEFAULT_ROOT_DIRECTORY,
        help=(
            "Root directory used to search for SHACL and ontology TTL files "
            "(default: current directory)."
        ),
    )
    parser.add_argument(
        "--context-root",
        dest="context_root",
        type=str,
        default=None,
        help=(
            "Directory containing local JSON-LD context files used to resolve remote @context IRIs. "
            "Default: <root>/contexts if it exists, otherwise <root>."
        ),
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug logging",
    )
    parser.add_argument(
        "--logfile",
        type=str,
        help="Write full validator output to this file.",
    )
    parser.add_argument(
        "--inference",
        type=str,
        default="rdfs",
        choices=["none", "rdfs", "owlrl", "both"],
        help="Inference mode for pyshacl (default: rdfs)",
    )

    args = parser.parse_args()

    # Resolve root_dir once and pass it through
    root_dir = os.path.normpath(args.root_dir)

    # Default context root: <root>/contexts if present, else <root>.
    if args.context_root:
        context_root = os.path.abspath(args.context_root)
    else:
        candidate = os.path.join(root_dir, "contexts")
        context_root = candidate if os.path.isdir(candidate) else root_dir

    ontology_dict = build_dict_for_ontologies(root_dir, args.paths)
    if not ontology_dict:
        print(
            f"Error code 100: No valid files found in given paths {args.paths}.",
            file=sys.stderr,
        )
        sys.exit(100)

    context_resolver = LocalContextResolver(context_root=context_root)

    return_code, message = validate_jsonld_against_shacl(
        root_dir,
        ontology_dict,
        debug=args.debug,
        inference_mode=args.inference,
        context_resolver=context_resolver,
        logfile=args.logfile,
    )

    # Print the final message once (to stdout)
    sys.stdout.flush()
    print(message)

    sys.exit(return_code)


if __name__ == "__main__":
    main()
