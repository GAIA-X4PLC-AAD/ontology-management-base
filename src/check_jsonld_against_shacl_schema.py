#!/usr/bin/env python3
"""
JSON-LD to SHACL Validation with Automated Ontology Discovery.

This script validates JSON-LD instance files against SHACL shapes by dynamically
resolving and loading the required ontology dependencies. It is designed to work
within a structured repository where ontology definitions (.ttl), SHACL shapes (.ttl),
and instance data (.json/.jsonld) are organized by namespace or domain.

Key Features:
  1. **Dynamic Dependency Resolution**:
     - Analyzes JSON-LD `@context` and `rdf:type` usage to identify required namespaces.
     - Automatically locates and loads corresponding ontology and SHACL files from the project root.
     - Resolves transitive ontology dependencies (e.g., if Ontology A imports Ontology B).

  2. **Offline Context Resolution**:
     - Intercepts remote context IRIs (e.g., "https://w3id.org/...") and maps them to
       local files, enabling fully offline validation and stability.

  3. **Optimized Performance (Hybrid Strategy)**:
     - **Loading**: Prioritizes `oxrdflib` (Oxigraph) for fast parsing.
     - **Inference**: Uses customized SPARQL updates for instant RDFS inference in Rust,
       bypassing the slow Python-based `owlrl` engine.
     - **Validation**: Automatically switches to standard in-memory graphs for validation
       to avoid Python-Rust FFI overhead during high-frequency triple iteration.

  4. **Robust Path Handling**:
     - Built on `pathlib` for cross-platform compatibility.
     - Enforces relative path reporting in logs to ensure consistent, readable output
       that matches expected test baselines.

  5. **In-Memory Processing**:
     - Performs JSON-LD context rewriting in-memory to ensure thread safety and
       avoid temporary file artifacts.

Usage:
    python3 check_jsonld_against_shacl_schema.py [paths...] [--root <dir>] [--force-load]

Arguments:
    paths:          One or more JSON-LD files or directories to validate.
    --root:         Root directory of the ontology repository (default: current dir).
    --context-root: Directory containing local context files (default: <root>/contexts).
    --force-load:   Force load all ontologies from 'generated/' and 'gx/' directories, bypassing discovery.
    --inference:    Inference mode for PySHACL (rdfs, owlrl, none, both).
    --debug:        Enable debug logging (Script logs to Console; PySHACL logs to File if --logfile provided).
    --logfile:      Write validation report (and PySHACL debug logs if --debug) to file.
"""

import json
import logging
import re
import sys
import time
from argparse import ArgumentParser
from collections import Counter, defaultdict
from contextlib import contextmanager
from io import BytesIO, StringIO
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple, Union
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
except ImportError as e:  # pragma: no cover
    validate = None  # type: ignore
    PYSHACL_IMPORT_ERROR = e
else:
    PYSHACL_IMPORT_ERROR = None

from utils.print_formatting import print_validate_jsonld_against_shacl_result

DEFAULT_ROOT_DIRECTORY = Path(".")
CACHE_FILENAME = ".ontology_iri_cache.json"

# ---------------------------------------------------------------------------
# Configurable Directory Names
# ---------------------------------------------------------------------------
DIR_NAME_BASE_ONTOLOGIES = "base-ontologies"
DIR_NAME_BASE_REFERENCES = "base-references"
DIR_NAME_CONTEXTS = "contexts"
DIR_NAME_GENERATED = "generated"
DIR_NAME_ONTOLOGY_MANAGEMENT_BASE = "ontology-management-base"

# Professional: Allow-list for URI schemes to distinguish absolute URIs from CURIEs
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
    "ipfs",
}


# ---------------------------------------------------------------------------
# Timing Helper (Context Manager)
# ---------------------------------------------------------------------------


class StepTimer:
    """
    A context manager to measure execution time of specific workflow steps.
    Prints directly to stdout to ensure timing info is visible immediately.
    """

    def __init__(self):
        self.start_time = time.perf_counter()
        self.last_step_time = self.start_time

    @contextmanager
    def step(self, step_name: str):
        """
        Usage:
            with timer.step("Step Name"):
                do_work()
        """
        # Update start time for this specific step
        self.last_step_time = time.perf_counter()
        yield
        now = time.perf_counter()
        duration = now - self.last_step_time
        total = now - self.start_time
        msg = (
            f"⏱️  [STEP DONE: {step_name}] took {duration:.3f}s (Total: {total:.3f}s)\n"
        )
        print(msg)
        sys.stdout.flush()


# ---------------------------------------------------------------------------
# Path Helper
# ---------------------------------------------------------------------------


def to_rel_path(path: Union[Path, str], root: Path) -> str:
    """Safely converts a path to be relative to root for cleaner logging."""
    p = Path(path)
    try:
        # Resolve to absolute first to ensure relative_to works correctly
        if not p.is_absolute():
            p = p.resolve()
        if not root.is_absolute():
            root = root.resolve()
        return str(p.relative_to(root))
    except ValueError:
        # Fallback if path is not relative to root
        return str(path)


# ---------------------------------------------------------------------------
# Optimization Helper: SPARQL Inference
# ---------------------------------------------------------------------------


def perform_fast_rdfs_inference(graph: Graph):
    """
    Executes SPARQL Updates to materialize common RDFS inferences (subClassOf, subPropertyOf).
    This replaces the 'owlrl' Python engine for the most common use-case ('rdfs'),
    avoiding compatibility crashes with Oxigraph and providing massive speedups.
    """
    logging.info("⚡ Running optimized SPARQL RDFS inference...")

    # 1. Resolve SubClasses: ?s a ?child . ?child subClassOf+ ?parent . -> ?s a ?parent
    # This is the 99% use case for SHACL validation (matching types).
    query_subclass = """
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    INSERT {
        ?s a ?parent .
    }
    WHERE {
        ?s a ?child .
        ?child rdfs:subClassOf+ ?parent .
    }
    """
    graph.update(query_subclass)

    # 2. Resolve SubProperties (Optional but good for completeness):
    # ?s ?subProp ?o . ?subProp subPropertyOf+ ?superProp . -> ?s ?superProp ?o
    query_subprop = """
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    INSERT {
        ?s ?superProp ?o .
    }
    WHERE {
        ?s ?subProp ?o .
        ?subProp rdfs:subPropertyOf+ ?superProp .
    }
    """
    graph.update(query_subprop)


# ---------------------------------------------------------------------------
# Local JSON-LD @context resolver
# ---------------------------------------------------------------------------


def iri_to_namespace_hint(iri: str) -> Optional[str]:
    """
    Extracts a likely namespace string (hint) from a remote URL.
    Example: "https://schema.ascs.digital/SimpulseId/v1/..." -> "simpulseid"
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
    Handles resolution of remote JSON-LD @context IRIs to local files.
    Scans multiple directories (generated, ontology-base, contexts) to find matching namespaces.
    """

    def __init__(self, root_dir: Path):
        self.root_dir = root_dir.resolve()
        self.namespace_map: Dict[str, Path] = {}

        # Define directories to search for context subfolders
        # The script will look for: root/<search_dir>/<namespace>/<namespace>_context.jsonld
        search_dirs = [
            DIR_NAME_GENERATED,  # e.g. root/generated/simpulseid/...
            DIR_NAME_ONTOLOGY_MANAGEMENT_BASE,  # e.g. root/ontology-management-base/gx/...
            DIR_NAME_CONTEXTS,  # e.g. root/contexts/some-lib/...
            ".",  # e.g. root/my-lib/...
        ]

        logging.debug(f"Initializing LocalContextResolver with root: {self.root_dir}")

        for dir_name in search_dirs:
            base_path = self.root_dir / dir_name
            if not base_path.is_dir():
                continue

            # Iterate over subdirectories (potential namespaces)
            for entry in base_path.iterdir():
                if entry.is_dir():
                    ns = entry.name.lower()

                    # We expect the file to be named <namespace>_context.jsonld inside the folder
                    expected_file = entry / f"{ns}_context.jsonld"

                    if expected_file.exists():
                        if ns not in self.namespace_map:
                            self.namespace_map[ns] = expected_file
                            logging.debug(
                                f"✅ Registered local context for '{ns}': {to_rel_path(expected_file, self.root_dir)}"
                            )
                        else:
                            logging.debug(
                                f"Skipping duplicate context for '{ns}' in {dir_name}"
                            )

    def _load_local_context_object(self, namespace: str) -> Optional[dict]:
        local_path = self.namespace_map.get(namespace.lower())
        if not local_path:
            return None

        try:
            with local_path.open("r", encoding="utf-8") as f:
                ctx_data = json.load(f)
        except Exception as e:
            logging.warning("Failed to read local context file %s: %s", local_path, e)
            return None

        if isinstance(ctx_data, dict):
            if "@context" in ctx_data and isinstance(ctx_data["@context"], dict):
                return ctx_data["@context"]
            return ctx_data

        logging.warning("Local context file %s is not a JSON object.", local_path)
        return None

    def _resolve_context_entry(self, entry: Any) -> Any:
        if isinstance(entry, str) and entry.startswith("http"):
            namespace = iri_to_namespace_hint(entry)

            # If we found a local file for this namespace, use it
            if namespace and namespace.lower() in self.namespace_map:
                ctx_obj = self._load_local_context_object(namespace)
                if ctx_obj is not None:
                    logging.debug(
                        "Resolved remote @context %s -> inline from %s",
                        entry,
                        self.namespace_map[namespace.lower()].name,
                    )
                    return ctx_obj

            logging.debug(
                "No local file found for remote @context %s (Hint: %s). Leaving unchanged.",
                entry,
                namespace,
            )
        return entry

    def resolve_jsonld_content(self, jsonld_path: Path) -> Tuple[bool, Any]:
        """
        Reads a JSON-LD file and attempts to resolve remote contexts.
        Returns: (was_modified: bool, content: dict/list)
        """
        try:
            with jsonld_path.open("r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            logging.error(f"Failed to load JSON-LD file {jsonld_path}: {e}")
            return False, {}

        ctx = data.get("@context")
        if ctx is None:
            return False, data

        rewritten = False
        new_ctx = None

        if isinstance(ctx, list):
            new_ctx = []
            for entry in ctx:
                resolved = self._resolve_context_entry(entry)
                if resolved != entry:
                    rewritten = True
                new_ctx.append(resolved)
        elif isinstance(ctx, str):
            resolved = self._resolve_context_entry(ctx)
            if resolved != ctx:
                rewritten = True
                new_ctx = resolved
        elif isinstance(ctx, dict):
            new_ctx = {}
            for k, v in ctx.items():
                resolved = self._resolve_context_entry(v)
                if resolved != v:
                    rewritten = True
                new_ctx[k] = resolved

        if rewritten:
            data["@context"] = new_ctx
            return True, data

        return False, data


# ---------------------------------------------------------------------------
# Logging Setup
# ---------------------------------------------------------------------------


def setup_logging(
    debug: bool = False,
    buffer_stream: Optional[StringIO] = None,
    logfile: Optional[Path] = None,
) -> None:
    """
    Configures logging.
    - Script logs (root) -> Console (and Buffer).
    - PySHACL logs -> Logfile ONLY (if debug is enabled).
    """
    root_logger = logging.getLogger()
    # Ensure Root level captures DEBUG if debug is enabled
    root_logger.setLevel(logging.DEBUG if debug else logging.INFO)

    # Reset handlers to avoid duplicates
    root_logger.handlers = []

    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

    # 1. Console Handler (Script output)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    # CASE 3 FIX: If we have debug=True AND a logfile, we want the CONSOLE to stay clean (INFO only).
    # The debug logs will be routed to the file via the file_handler attached to root.
    if debug and logfile:
        console_handler.setLevel(logging.INFO)
    else:
        # Case 4 (debug only) or Case 1/2 (no debug): Console follows root level
        console_handler.setLevel(logging.NOTSET)

    root_logger.addHandler(console_handler)

    # 2. Buffer Handler (Capture for return value)
    if buffer_stream:
        stream_handler = logging.StreamHandler(buffer_stream)
        stream_handler.setFormatter(formatter)
        root_logger.addHandler(stream_handler)

    # 3. Logfile Handler (Script output to file)
    file_handler = None
    if logfile:
        # Open in 'w' mode to clear previous logs on startup
        file_handler = logging.FileHandler(logfile, mode="w", encoding="utf-8")
        file_handler.setFormatter(formatter)
        # We attach the file handler to Root so it captures Script DEBUG logs (Prefix Extension)
        root_logger.addHandler(file_handler)

    # 4. PySHACL Logger Configuration
    # We explicitly control pyshacl logger.
    pyshacl_logger = logging.getLogger("pyshacl")

    if debug:
        pyshacl_logger.setLevel(logging.DEBUG)
        # Requirement: Pyshacl debug output must NOT go to console.
        # We stop propagation so it doesn't hit the Root->ConsoleHandler.
        pyshacl_logger.propagate = False

        if file_handler:
            # Case 3: Pyshacl debugs go to file (via the handler we created above).
            pyshacl_logger.addHandler(file_handler)
        else:
            # Case 4: --debug only -> Pyshacl debugs suppressed from console.
            # (User didn't ask for pyshacl logs on console in Case 4, only "logger.debug" from script).
            pyshacl_logger.addHandler(logging.NullHandler())
    else:
        # Case 1 & 2: No debug -> Pyshacl stays silent.
        pass


# ---------------------------------------------------------------------------
# Generic Helpers
# ---------------------------------------------------------------------------


def ensure_folder_entry(ontology_dict: Dict[str, Dict], folder_name: str) -> None:
    if folder_name not in ontology_dict:
        ontology_dict[folder_name] = {
            "instance": [],
            "reference": [],
            "ontologies": [],
            "shacle_shapes": [],
            "prefixes": {},
            "context_issues": {},
        }


def _extract_ids_from_json_file(file_path: Path) -> Set[str]:
    """Helper to extract defined @ids from a JSON-LD file (supports flat or graph)."""
    ids = set()
    try:
        with file_path.open("r", encoding="utf-8") as f:
            data = json.load(f)

        # Support single object or @graph array
        objs = data.get("@graph", [data]) if isinstance(data, dict) else [data]
        if isinstance(objs, list):
            for obj in objs:
                if isinstance(obj, dict) and "@id" in obj:
                    ids.add(obj["@id"])
    except Exception:
        pass
    return ids


# ---------------------------------------------------------------------------
# Prefix Extraction
# ---------------------------------------------------------------------------


def extract_prefixes_from_ttl(file_path: Path) -> Dict[str, str]:
    g = Graph(store=FAST_STORE)
    g.parse(str(file_path), format="turtle")
    prefixes = {prefix: str(namespace) for prefix, namespace in g.namespaces()}
    logging.debug("Extracted prefixes from TTL %s: %s", file_path, prefixes)
    return prefixes


def extract_prefixes_from_jsonld(
    file_path: Path, context_resolver: Optional[LocalContextResolver] = None
) -> Dict[str, str]:
    # UPDATED: Use context_resolver to get the resolved content first
    data = None
    if context_resolver:
        try:
            _, data = context_resolver.resolve_jsonld_content(file_path)
        except Exception:
            pass

    # Fallback to reading file directly if resolver didn't work or wasn't provided
    if data is None:
        with file_path.open("r", encoding="utf-8") as f:
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
    base: Dict[str, str], additions: Dict[str, str], source: str = ""
) -> Dict[str, str]:
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
# JSON-LD Context Coverage (Professional)
# ---------------------------------------------------------------------------


def _collect_used_prefixes_in_json_value(value: Any) -> Set[str]:
    used: Set[str] = set()

    def _extract_scheme(text: str) -> Optional[str]:
        """Strictly safe URI scheme extraction."""
        # FIX: Ignore text with spaces (URIs/CURIEs typically don't have spaces)
        if " " in text:
            return None

        if ":" not in text or text.startswith("@"):
            return None
        try:
            parsed = urlparse(text)
            scheme = parsed.scheme
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
            prefix = _extract_scheme(k)
            if prefix:
                used.add(prefix)
            used |= _collect_used_prefixes_in_json_value(v)

    elif isinstance(value, list):
        for item in value:
            used |= _collect_used_prefixes_in_json_value(item)

    return used


def check_jsonld_context_coverage(
    file_path: Path, context_resolver: Optional[LocalContextResolver] = None
) -> Dict[str, Set[str]]:
    
    # 1. Try to load RESOLVED content (uses local *_context.jsonld files if available)
    data = None
    if context_resolver:
        try:
            _, data = context_resolver.resolve_jsonld_content(file_path)
        except Exception:
            pass
            
    # 2. Fallback to raw load if resolver missing or failed
    if data is None:
        with file_path.open("r", encoding="utf-8") as f:
            data = json.load(f)

    context = data.get("@context", {})
    declared_prefixes: Set[str] = set()

    # Helper to extract keys whether context is a dict or list of dicts
    def _extract_keys(ctx):
        if isinstance(ctx, dict):
            return {k for k in ctx.keys() if isinstance(k, str)}
        return set()

    if isinstance(context, dict):
        declared_prefixes = _extract_keys(context)
    elif isinstance(context, list):
        for item in context:
            declared_prefixes.update(_extract_keys(item))

    used_prefixes = _collect_used_prefixes_in_json_value(data)
    missing = used_prefixes - declared_prefixes
    unused = declared_prefixes - used_prefixes

    if missing:
        # Use relative path for cleaner logging
        logging.warning(
            "JSON-LD context in %s is missing prefixes: %s",
            file_path.name,
            ", ".join(sorted(missing)),
        )

    return {
        "declared": declared_prefixes,
        "used": used_prefixes,
        "missing": missing,
        "unused": unused,
    }


# ---------------------------------------------------------------------------
# Type Resolution (Professional)
# ---------------------------------------------------------------------------


def resolve_json_type(
    json_type: str,
    namespace_prefixes: Dict[str, str],
    manifest_dir_url: Optional[str] = None,
) -> str:
    """
    Resolves a type string to a full IRI.
    Correctly handles CURIEs vs Absolute URIs.
    """
    parsed = urlparse(json_type)

    # 1. Absolute URI check (has scheme, and scheme is standard)
    if parsed.scheme and parsed.scheme in KNOWN_URI_SCHEMES:
        return json_type

    # 2. CURIE check (has scheme, scheme is NOT standard -> likely a prefix)
    if parsed.scheme and parsed.scheme in namespace_prefixes:
        # urlparse treats 'name' in 'prefix:name' as path
        return namespace_prefixes[parsed.scheme] + parsed.path

    # 3. Fallback / Manifest Logic (Legacy)
    if manifest_dir_url is not None:
        # ... logic for manifest resolution if needed ...
        pass

    return json_type


def extract_used_types(
    data_graph: Graph,
    namespace_prefixes: Dict[str, str],
    file=None,
) -> Set[str]:
    if file is None:
        file = sys.stdout
    print("📌 Extracting all rdf:type from data graph...", file=file)

    used_types: Set[str] = set()
    type_counts: Counter[str] = Counter()
    rdf_type_pred = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")["type"]

    for _, _, obj in data_graph.triples((None, rdf_type_pred, None)):
        # Provide None for manifest_dir_url as it's legacy/brittle
        resolved_type = resolve_json_type(str(obj), namespace_prefixes)
        used_types.add(resolved_type)
        type_counts[resolved_type] += 1

    print("✅ Found the following rdf:type values:", file=file)
    for rdf_type, count in sorted(type_counts.items(), key=lambda x: x[0]):
        print(f"   {rdf_type} (used {count} times)", file=file)

    return used_types


# ---------------------------------------------------------------------------
# RDF Loading (In-Memory Professional)
# ---------------------------------------------------------------------------


def load_rdf_files(
    rdf_files: List[Path],
    root_dir: Path,
    rdf_format: str = "json-ld",
    file=None,
    context_resolver: Optional[LocalContextResolver] = None,
) -> tuple[Graph, int, int]:

    if file is None:
        file = sys.stdout
    data_graph = Graph(store=FAST_STORE)
    loaded_count = 0
    failed_count = 0

    for i, rdf_file in enumerate(rdf_files, start=1):
        try:
            # Professional: Use BytesIO for in-memory modification if needed
            parse_source = None

            if rdf_format.lower() in {"json-ld", "jsonld"} and context_resolver:
                modified, content = context_resolver.resolve_jsonld_content(rdf_file)
                if modified:
                    # Parse from memory
                    parse_source = BytesIO(json.dumps(content).encode("utf-8"))

            if parse_source:
                data_graph.parse(parse_source, format=rdf_format)
            else:
                # Parse directly from disk
                data_graph.parse(str(rdf_file), format=rdf_format)

            loaded_count += 1
            logging.debug("Loaded %s file: %s", rdf_format, rdf_file)
            print(
                f"✅ [{i}/{len(rdf_files)}] Loaded: {to_rel_path(rdf_file, root_dir)}",
                file=file,
            )

        except Exception as e:
            failed_count += 1
            logging.error("Failed to load %s: %s", rdf_file, e)
            print(
                f"❌ [{i}/{len(rdf_files)}] Failed: {to_rel_path(rdf_file, root_dir)} -> {e}",
                file=file,
            )

    return data_graph, loaded_count, failed_count


# ---------------------------------------------------------------------------
# Discovery and Collection
# ---------------------------------------------------------------------------


def build_dict_for_ontologies(
    root_dir: Union[Path, str], paths: List[str]
) -> Dict[str, Dict[str, object]]:
    # 1. Type robustness: Ensure root_dir is a Path object
    root_dir = Path(root_dir).resolve()

    ontology_dict: Dict[str, Dict[str, object]] = {}
    collected_files: List[Path] = []

    # [UPDATED] Use constant for directory name
    base_refs_dir = root_dir / DIR_NAME_BASE_REFERENCES

    # 2. Collect files
    for p_str in paths:
        path = Path(p_str)
        # Ensure we work with absolute paths for globbing/discovery stability
        if not path.is_absolute():
            path = path.resolve()

        if path.is_dir():
            collected_files.extend(path.glob("*_instance.json"))
            collected_files.extend(path.glob("*_reference.json"))
        elif path.is_file() and path.suffix in {".json", ".jsonld"}:
            collected_files.append(path)

            # Legacy sibling check
            if path.name.endswith("_instance.json") and not path.name.endswith(
                "_inline_instance.json"
            ):
                collected_files.extend(path.parent.glob("*_reference.json"))

    if not collected_files:
        return {}

    # 3. Categorize
    instance_files = [
        f for f in collected_files if not f.name.endswith("_reference.json")
    ]
    reference_files = [f for f in collected_files if f.name.endswith("_reference.json")]

    for key, files in (("instance", instance_files), ("reference", reference_files)):
        for f in files:
            # Use relative path from root for the dictionary key
            try:
                rel_dir = f.parent.relative_to(root_dir)
            except ValueError:
                # If file is outside root, use its name as folder?
                # Or relative to common prefix? Fallback to parent name.
                rel_dir = f.parent

            folder_name = rel_dir.as_posix()  # Normalized forward slashes
            ensure_folder_entry(ontology_dict, folder_name)
            ontology_dict[folder_name][key].append(f)

    # 4. Auto-Resolve Base References (Smart Scan)
    if base_refs_dir.is_dir():

        # 4a. Pre-scan "Global" references (starting with 'gx_') for their defined @ids
        # This allows us to only load them if referenced in the instance file.
        global_ref_map: List[Tuple[Path, Set[str]]] = []
        for ref_file in base_refs_dir.glob("gx*reference.json"):
            found_ids = _extract_ids_from_json_file(ref_file)
            if found_ids:
                global_ref_map.append((ref_file, found_ids))

        for inst_file in instance_files:
            try:
                rel_dir = inst_file.parent.relative_to(root_dir)
            except ValueError:
                rel_dir = inst_file.parent
            folder_name = rel_dir.as_posix()

            # Robust prefix extraction: take everything before the first underscore
            prefix_match = re.match(r"^([^_]+)_", inst_file.name)
            prefix = prefix_match.group(1) if prefix_match else inst_file.stem

            # A. Local/Sibling Reference matching (e.g. hdmap -> hdmap_manifest)
            matching_refs = set(base_refs_dir.glob(f"{prefix}*reference.json"))

            # B. Smart Global Reference matching (Replaces the blind "load all gx*")
            # Only load gx_ references if their IDs are actually used in the file.
            if prefix != "gx":
                try:
                    # Read file content once to check for ID usage
                    # (Simple string check is usually sufficient and fast for DIDs)
                    content_str = inst_file.read_text(encoding="utf-8")

                    for ref_path, defined_ids in global_ref_map:
                        # Optimization: if already matched by prefix (unlikely for 'gx' vs 'hdmap'), skip
                        if ref_path in matching_refs:
                            continue

                        # Check if any ID defined in the ref file is present in the instance
                        for ref_id in defined_ids:
                            if ref_id in content_str:
                                matching_refs.add(ref_path)
                                break
                except Exception as e:
                    logging.debug(f"Skipping smart ref scan for {inst_file}: {e}")

            for ref_path in matching_refs:
                if ref_path not in ontology_dict[folder_name]["reference"]:
                    ontology_dict[folder_name]["reference"].append(ref_path)
                    print(
                        f"🔗 Auto-linked reference: {ref_path.name} -> {inst_file.name}"
                    )

    return ontology_dict


def collect_instance_and_reference_files(
    ontology_dict: Dict[str, Dict[str, object]],
) -> Tuple[List[Path], List[Path]]:
    """
    Flattens the per-folder lists of files into two master lists:
    one for instances and one for references.
    """
    instance_files: List[Path] = []
    reference_files: List[Path] = []

    for contents in ontology_dict.values():
        # In the professional version, these lists contain Path objects
        # We use explicit type casting/checks to satisfy type checkers if needed,
        # but runtime Python is duck-typed.
        insts = contents.get("instance", [])
        refs = contents.get("reference", [])

        instance_files.extend(insts)  # type: ignore
        reference_files.extend(refs)  # type: ignore

    # Deduplicate and sort
    # Path objects are hashable, so set() works fine.
    instance_files = sorted(list(set(instance_files)))
    reference_files = sorted(list(set(reference_files)))
    return instance_files, reference_files


def add_jsonld_prefixes_and_context_info(
    ontology_dict: Dict[str, Dict[str, object]],
    context_resolver: Optional[LocalContextResolver] = None,
) -> None:
    for folder_key, contents in ontology_dict.items():
        files_to_process: List[Path] = []
        context_issues: Dict[Path, Dict[str, Set[str]]] = {}

        for key in ("instance", "reference"):
            for file_path in contents.get(key, []):
                files_to_process.append(file_path)
                if file_path.suffix in {".json", ".jsonld"}:
                    # UPDATED: Pass the context_resolver here
                    coverage = check_jsonld_context_coverage(file_path, context_resolver)
                    context_issues[file_path] = coverage

        prefixes: Dict[str, str] = {}
        for json_file in files_to_process:
            # UPDATED: Pass context_resolver
            mapping = extract_prefixes_from_jsonld(json_file, context_resolver)
            merge_prefix_mappings(prefixes, mapping, source=folder_key)

        contents["prefixes"] = prefixes
        contents["context_issues"] = context_issues
        logging.debug("Folder '%s': prefixes=%s", folder_key, prefixes)


def extend_prefixes_with_schema_files(
    ontology_dict: Dict[str, Dict[str, object]],
) -> None:
    for folder_key, contents in ontology_dict.items():
        ttl_files: List[Path] = []
        ttl_files.extend(contents.get("ontologies", []))
        ttl_files.extend(contents.get("shacle_shapes", []))

        ttl_prefixes: Dict[str, str] = {}
        for ttl in ttl_files:
            try:
                mapping = extract_prefixes_from_ttl(ttl)
                merge_prefix_mappings(ttl_prefixes, mapping, source=str(ttl))
            except Exception as e:
                logging.warning("Failed to extract prefixes from TTL %s: %s", ttl, e)

        merge_prefix_mappings(
            contents["prefixes"], ttl_prefixes, source=f"{folder_key} (TTL)"
        )


def build_global_prefix_mapping(
    ontology_dict: Dict[str, Dict[str, object]],
) -> Dict[str, str]:
    global_prefixes: Dict[str, str] = {}
    for folder_key, contents in ontology_dict.items():
        folder_prefixes = contents.get("prefixes", {})
        merge_prefix_mappings(global_prefixes, folder_prefixes, source=folder_key)
    return global_prefixes


# ---------------------------------------------------------------------------
# Ontology Dependency Graph (Professional Caching)
# ---------------------------------------------------------------------------


def normalize_iri(iri: str) -> str:
    return iri.rstrip("#/")


def _build_ontology_iri_index(root_dir: Path) -> Dict[str, Path]:
    cache_path = root_dir / CACHE_FILENAME
    cache = {}
    if cache_path.exists():
        try:
            with cache_path.open("r", encoding="utf-8") as f:
                cache = json.load(f)
        except Exception:
            pass

    iri_to_file: Dict[str, Path] = {}
    ontology_files = list(root_dir.rglob("*_ontology.ttl"))

    updated_cache = {}
    cache_dirty = False

    # Regex to find IRI quickly without parsing
    # Looks for: <http://...> a owl:Ontology
    iri_regex = re.compile(r"^\s*<([^>]+)>\s+a\s+(?:owl:)?Ontology", re.MULTILINE)

    for onto_path in ontology_files:
        try:
            stat = onto_path.stat()
            mtime = stat.st_mtime
        except OSError:
            continue

        # Check cache
        str_path = str(onto_path)
        cached_entry = cache.get(str_path)

        if cached_entry and cached_entry.get("mtime") == mtime:
            # FIX: Use relative path in cache hit log
            logging.debug(f"📦 Cache hit for: {to_rel_path(onto_path, root_dir)}")
            iri = cached_entry.get("iri")
            if iri:
                iri_to_file[iri] = onto_path
                updated_cache[str_path] = cached_entry
                continue

        # Cache miss: Fast scan first
        found_iri = None
        try:
            # Read first 4KB to find ontology declaration
            with onto_path.open("r", encoding="utf-8") as f:
                head = f.read(4096)
            match = iri_regex.search(head)
            if match:
                found_iri = normalize_iri(match.group(1))
        except Exception:
            pass

        # Fallback: Full Parse if regex failed
        if not found_iri:
            g = Graph(store=FAST_STORE)
            try:
                g.parse(str(onto_path), format="turtle")
                for s in g.subjects(RDF.type, OWL.Ontology):
                    found_iri = normalize_iri(str(s))
                    break
            except Exception as e:
                logging.warning(
                    "Failed to parse ontology %s: %s",
                    to_rel_path(onto_path, root_dir),
                    e,
                )

        if found_iri:
            if found_iri in iri_to_file:
                logging.warning(
                    "Duplicate Ontology IRI %s in %s and %s",
                    found_iri,
                    to_rel_path(iri_to_file[found_iri], root_dir),
                    to_rel_path(onto_path, root_dir),
                )

            iri_to_file[found_iri] = onto_path
            updated_cache[str_path] = {"mtime": mtime, "iri": found_iri}
            cache_dirty = True

    if cache_dirty or len(updated_cache) != len(cache):
        try:
            with cache_path.open("w", encoding="utf-8") as f:
                json.dump(updated_cache, f, indent=2)
        except Exception as e:
            logging.warning("Failed to write cache: %s", e)

    return iri_to_file


def _build_ontology_dependencies(
    root_dir: Path, iri_to_file: Dict[str, Path]
) -> Dict[Path, Set[Path]]:
    deps: Dict[Path, Set[Path]] = defaultdict(set)
    ontology_files = list(root_dir.rglob("*_ontology.ttl"))

    for onto in ontology_files:
        g = Graph(store=FAST_STORE)
        try:
            g.parse(str(onto), format="turtle")
        except Exception:
            continue

        for _, ns in g.namespaces():
            ns_str = normalize_iri(str(ns))
            target_file = iri_to_file.get(ns_str)
            if target_file:
                deps[onto].add(target_file)
    return deps


def _expand_ontology_dependencies_from(
    initial_files: List[Path], deps: Dict[Path, Set[Path]]
) -> List[Path]:
    closure: Set[Path] = set(initial_files)
    queue: List[Path] = list(closure)

    while queue:
        current = queue.pop()
        for dep in deps.get(current, set()):
            if dep not in closure:
                closure.add(dep)
                queue.append(dep)
    return sorted(list(closure))


# ---------------------------------------------------------------------------
# Loading Logic
# ---------------------------------------------------------------------------


def load_shacl_and_ontologies(
    root_dir: Path,
    used_types: Set[str],
    global_prefixes: Dict[str, str],
    force_load_generated: bool = False,
    file=None,
) -> Tuple[Graph, Graph, List[Path], List[Path]]:

    if file is None:
        file = sys.stdout
    relevant_shacl_files: List[Path] = []
    initial_ontology_files: List[Path] = []

    # [UPDATED] Robust: Force-load all generated schemas and core GX if flag is set
    if force_load_generated:
        print(
            "⚠️  Force Load Enabled: Loading all schemas in 'generated' and 'gx'...",
            file=file,
        )

        # 1. Load everything from 'generated' (Project specific)
        generated_dir = root_dir / DIR_NAME_GENERATED
        if generated_dir.is_dir():
            relevant_shacl_files.extend(generated_dir.rglob("*_shacl.ttl"))
            initial_ontology_files.extend(generated_dir.rglob("*_ontology.ttl"))

        # 2. Load 'gx' from ontology-management-base (Core)
        gx_dir = root_dir / DIR_NAME_ONTOLOGY_MANAGEMENT_BASE / "gx"
        if gx_dir.is_dir():
            relevant_shacl_files.extend(gx_dir.rglob("*_shacl.ttl"))
            initial_ontology_files.extend(gx_dir.rglob("*_ontology.ttl"))

    else:
        # Standard Smart Discovery (Default)
        target_namespaces = set(global_prefixes.keys())

        # Check for missing namespaces in used_types
        for rdf_type in used_types:
            _ = urlparse(rdf_type)
            pass

        # Map prefixes to folders
        search_paths = [
            root_dir,
            root_dir / DIR_NAME_GENERATED,
            root_dir / DIR_NAME_ONTOLOGY_MANAGEMENT_BASE,
            root_dir / DIR_NAME_ONTOLOGY_MANAGEMENT_BASE / DIR_NAME_BASE_ONTOLOGIES,
        ]

        for ns in target_namespaces:
            folder_path = None
            for base_path in search_paths:
                candidate = base_path / ns
                if candidate.is_dir():
                    folder_path = candidate
                    break

            if folder_path and folder_path.is_dir():
                relevant_shacl_files.extend(folder_path.rglob("*_shacl.ttl"))
                initial_ontology_files.extend(folder_path.rglob("*_ontology.ttl"))

    # Resolve Dependencies (Always run, even if forced, to get transitive imports like SKOS/DCTERMS)
    iri_index = _build_ontology_iri_index(root_dir)
    deps = _build_ontology_dependencies(root_dir, iri_index)
    relevant_ontology_files = _expand_ontology_dependencies_from(
        initial_ontology_files, deps
    )

    # Add Support Ontologies (Dynamic Scan)
    # [UPDATED] Use constant and scan recursively for any *_ontology.ttl
    # We check standard location AND submodule location
    potential_base_dirs = [
        root_dir / DIR_NAME_BASE_ONTOLOGIES,
        root_dir / DIR_NAME_ONTOLOGY_MANAGEMENT_BASE / DIR_NAME_BASE_ONTOLOGIES,
    ]

    for base_ontologies_dir in potential_base_dirs:
        if base_ontologies_dir.is_dir():
            for support_file in base_ontologies_dir.rglob("*_ontology.ttl"):
                if support_file not in relevant_ontology_files:
                    relevant_ontology_files.append(support_file)

    # Sort
    relevant_ontology_files.sort()
    relevant_shacl_files = sorted(list(set(relevant_shacl_files)))

    # Output
    if relevant_shacl_files:
        print("📌 Relevant SHACL files to load:", file=file)
        for path in relevant_shacl_files:
            print(f"   {to_rel_path(path, root_dir)}", file=file)

    if relevant_ontology_files:
        print("📌 Relevant ontology files to load:", file=file)
        for path in relevant_ontology_files:
            print(f"   {to_rel_path(path, root_dir)}", file=file)

    # Load Graphs
    ont_graph = Graph(store=FAST_STORE)
    for onto_file in relevant_ontology_files:
        try:
            ont_graph.parse(str(onto_file), format="turtle")
            print(
                f"✅ Loaded Ontology file into ontology graph: {to_rel_path(onto_file, root_dir)}",
                file=file,
            )
        except Exception as e:
            print(
                f"❌ Failed to parse ontology {to_rel_path(onto_file, root_dir)}: {e}",
                file=file,
            )

    shacl_graph = Graph(store=FAST_STORE)
    for sh_file in relevant_shacl_files:
        try:
            shacl_graph.parse(str(sh_file), format="turtle")
            print(
                f"✅ Loaded SHACL file into shacl graph: {to_rel_path(sh_file, root_dir)}",
                file=file,
            )
        except Exception as e:
            print(
                f"❌ Failed to parse SHACL file {to_rel_path(sh_file, root_dir)}: {e}",
                file=file,
            )

    return shacl_graph, ont_graph, relevant_shacl_files, relevant_ontology_files


# ---------------------------------------------------------------------------
# Main Orchestrator
# ---------------------------------------------------------------------------


def validate_jsonld_against_shacl(
    root_dir: Union[Path, str],
    ontology_dict: Dict[str, Dict[str, object]],
    debug: bool = False,
    inference_mode: str = "rdfs",
    context_resolver: Optional[LocalContextResolver] = None,
    logfile: Optional[str] = None,
    force_load: bool = False,
) -> Tuple[int, str]:

    # Ensure root_dir is Path
    root_dir = Path(root_dir).resolve()

    output_buffer = StringIO()
    timer = StepTimer()

    # Helper to print to both buffer and stdout (preserving user experience)
    def print_out(*args, **kwargs):
        print(*args, **kwargs, file=output_buffer)
        print(*args, **kwargs, file=sys.stdout)
        sys.stdout.flush()

    setup_logging(
        debug,
        buffer_stream=output_buffer,
        logfile=Path(logfile) if logfile else None,
    )

    if FAST_STORE == "oxigraph":
        print_out("🚀 Performance: Oxigraph (oxrdflib) is loaded and active.")
    else:
        print_out("🐢 Performance: Oxigraph not found, using default rdflib store.")

    if PYSHACL_IMPORT_ERROR:
        print_out(f"Error: pyshacl not installed: {PYSHACL_IMPORT_ERROR}")
        return 99, output_buffer.getvalue()

    if not ontology_dict:
        print_out("Error code 100: No valid files found.")
        return 100, output_buffer.getvalue()

    # Step 1
    print("🚀 Step 1: Analyzing JSON-LD contexts and prefixes...")
    with timer.step("JSON-LD Prefix Analysis"):
        # UPDATED: Pass context_resolver
        add_jsonld_prefixes_and_context_info(ontology_dict, context_resolver)

    # Step 2
    print("🚀 Step 2: Building Data Graph (Parsing JSON-LD files)...")
    data_graph = Graph(store=FAST_STORE)
    loaded_count = 0
    with timer.step("Data Graph Loading"):
        instance_files, reference_files = collect_instance_and_reference_files(
            ontology_dict
        )
        data_graph, loaded_count, failed = load_rdf_files(
            instance_files + reference_files,
            root_dir=root_dir,
            file=output_buffer,
            context_resolver=context_resolver,
        )

    if loaded_count == 0:
        return 101, output_buffer.getvalue()
    if len(data_graph) == 0:
        return 102, output_buffer.getvalue()

    # Step 3
    print("🚀 Step 3: Extracting RDF types to determine dependencies...")
    with timer.step("RDF Type Extraction"):
        jsonld_prefixes = build_global_prefix_mapping(ontology_dict)
        used_types = extract_used_types(data_graph, jsonld_prefixes, file=output_buffer)

    # Step 4
    print("🚀 Step 4: Loading relevant SHACL shapes and Ontologies...")
    with timer.step("Schema Loading (SHACL/OWL)"):
        shacl_graph, ont_graph, rel_shacl, rel_onto = load_shacl_and_ontologies(
            root_dir,
            used_types,
            jsonld_prefixes,
            force_load_generated=force_load,
            file=output_buffer,
        )

    # Step 5
    print("🚀 Step 5: Final Prefix Extension...")
    with timer.step("Prefix Extension"):
        # Update ontology_dict structure for final reporting
        for path in rel_onto:
            # Reverse map path to folder key
            try:
                folder_name = path.parent.relative_to(root_dir).as_posix()
            except ValueError:
                folder_name = path.parent.name
            ensure_folder_entry(ontology_dict, folder_name)
            ontology_dict[folder_name]["ontologies"].append(path)

        for path in rel_shacl:
            try:
                folder_name = path.parent.relative_to(root_dir).as_posix()
            except ValueError:
                folder_name = path.parent.name
            ensure_folder_entry(ontology_dict, folder_name)
            ontology_dict[folder_name]["shacle_shapes"].append(path)

        extend_prefixes_with_schema_files(ontology_dict)

    # Step 6
    print(f"🚀 Step 6: Performing SHACL validation (Inference: {inference_mode})...")
    with timer.step("PySHACL Validation Engine"):
        # Professional: Don't swallow output. Capture return values.
        # Note: We rely on pyshacl's own logging or return values.

        # LOGIC FOR INFERENCE STRATEGY
        # 1. 'rdfs' -> Optimized manual SPARQL update (inplace=True)
        # 2. 'owlrl'/'both' -> Standard slow pyshacl (inplace=False) to avoid crashes
        # 3. 'none' -> Optimized (inplace=True)

        pyshacl_inference_option = inference_mode
        # OPTIMIZATION: Default to inplace=False (copying to Memory graph)
        # because PySHACL iterates much faster over Python Memory triples
        # than via the Oxigraph FFI bridge.

        if FAST_STORE == "oxigraph":
            if inference_mode == "rdfs":
                # STRATEGY 1: Hybrid RDFS (Manual SPARQL + Oxigraph)
                print_out(
                    "⚡ Hybrid Mode: Merging graphs and running fast SPARQL inference on Oxigraph."
                )

                # 1. Merge ontologies into data (Fast in Rust)
                data_graph += ont_graph

                # 2. Run Inference (Fast in Rust)
                perform_fast_rdfs_inference(data_graph)

                # 3. Disable pyshacl's slow internal inference
                pyshacl_inference_option = "none"

                # 4. We will allow inplace=False below to copy this inferred graph
                # to a fresh Memory graph for the fastest possible validation loop.

            elif inference_mode in ["owlrl", "both"]:
                # STRATEGY 2: Fallback for Complex Inference
                print_out(f"⚠️  Complex inference '{inference_mode}' detected.")
                print_out(
                    "   Oxigraph does not support complex OWLRL inference in-place."
                )
                print_out(
                    "   Falling back to standard (slower) processing to avoid crashes."
                )

        # EXECUTE VALIDATION
        # inplace=False ensures we validate on a Memory graph (Fast iteration),
        # regardless of whether we loaded using Oxigraph or not.
        conforms, report_graph, v_text = validate(
            data_graph,
            shacl_graph=shacl_graph,
            ont_graph=ont_graph,  # safe to pass even if merged, pyshacl handles it
            abort_on_first=False,
            inference=pyshacl_inference_option,
            validation_mode="strict",
            debug=debug,
            inplace=False,  # <--- FORCE COPY TO MEMORY FOR SPEED
        )
        # Increased loglevel for internal tracking (goes to root logger)
        logging.debug(v_text)

    if logfile:
        # If debug is True, pyshacl logs have already been written to the file (via setup_logging).
        # We append the validation report to the end.
        # If debug is False, the file was not touched by setup_logging, so we open in 'w' to create it.
        mode = "a" if debug else "w"
        with open(logfile, mode, encoding="utf-8") as f:
            f.write(v_text)

    # Convert paths back to str for the legacy printer function, ensuring they are relative
    all_files_str = [
        to_rel_path(f, root_dir) for f in (instance_files + reference_files)
    ]

    if not conforms:
        # Pass empty string for v_text to suppress detailed report in console output
        print_validate_jsonld_against_shacl_result(
            False, all_files_str, "", report_graph, exit_code=None, file=output_buffer
        )
        return 210, output_buffer.getvalue()
    else:
        print_validate_jsonld_against_shacl_result(
            True, all_files_str, v_text, exit_code=None, file=output_buffer
        )
        return 0, output_buffer.getvalue()


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main() -> None:
    parser = ArgumentParser(
        description="Validate JSON-LD instance/reference files against SHACL with ontology dependency resolution."
    )
    parser.add_argument("paths", nargs="+", help="JSON/JSON-LD files or directories.")
    parser.add_argument(
        "--root",
        "--root-dir",
        dest="root_dir",
        default=DEFAULT_ROOT_DIRECTORY,
        help="Root directory.",
    )
    parser.add_argument(
        "--context-root",
        dest="context_root",
        default=None,
        help="Local context directory (Legacy).",
    )
    parser.add_argument("--debug", action="store_true", help="Enable debug logging.")
    parser.add_argument("--logfile", help="Write output to file.")
    parser.add_argument(
        "--inference",
        default="rdfs",
        choices=["none", "rdfs", "owlrl", "both"],
        help="Inference mode.",
    )
    # [UPDATED] Add Force Load Flag
    parser.add_argument(
        "--force-load",
        action="store_true",
        help="Force load all ontologies in generated/ and gx/ directories, bypassing discovery.",
    )

    args = parser.parse_args()
    root_dir = Path(args.root_dir).resolve()

    # context_root logic removed as it was unused and causing flake8 F841

    ontology_dict = build_dict_for_ontologies(root_dir, args.paths)

    if not ontology_dict:
        print(
            f"Error code 100: No valid files found in given paths {args.paths}.",
            file=sys.stderr,
        )
        sys.exit(100)

    # UPDATED: Initialize the smarter resolver with root_dir
    context_resolver = LocalContextResolver(root_dir=root_dir)

    return_code, message = validate_jsonld_against_shacl(
        root_dir,
        ontology_dict,
        debug=args.debug,
        inference_mode=args.inference,
        context_resolver=context_resolver,
        logfile=args.logfile,
        force_load=args.force_load,  # Pass the flag down
    )

    print(message)
    sys.exit(return_code)


if __name__ == "__main__":
    main()
