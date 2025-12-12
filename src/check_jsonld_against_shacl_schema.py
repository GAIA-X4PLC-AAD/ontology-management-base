#!/usr/bin/env python3
"""
Validate JSON-LD instance/reference files against SHACL with
ontology dependency resolution driven by the data graph.

New behaviour:

- Accepts arbitrary *.json / *.jsonld instance files, e.g.
    python check_jsonld_against_shacl.py \
        examples/simpulseid-administrator-credential.json \
        --root generated

- Optional --root / --root-dir argument controls where SHACL and
  ontology TTL files are searched (e.g. ./generated).

- Old *_instance.json / *_reference.json pattern still works when
  you pass directories as paths.
"""

import contextlib
import glob
import json
import logging
import os
import sys
from argparse import ArgumentParser
from collections import Counter, defaultdict
from io import StringIO
from typing import Dict, List, Set, Tuple
from urllib.parse import urlparse

from rdflib import OWL, RDF, RDFS, Graph, Namespace

try:
    from pyshacl import validate
except ImportError as e:  # pragma: no cover - environment might not have pyshacl
    validate = None  # type: ignore
    PYSHACL_IMPORT_ERROR = e
else:
    PYSHACL_IMPORT_ERROR = None

# Optional pretty printer from the original repo
try:
    from utils.print_formatting import print_validate_jsonld_against_shacl_result
except ImportError:  # pragma: no cover - allow running outside repo

    def print_validate_jsonld_against_shacl_result(
        conforms: bool,
        files: List[str],
        validation_text: str,
        exit_code: int | None = None,
        file=None,
    ) -> None:
        if file is None:
            file = sys.stdout
        status = "PASSED" if conforms else "FAILED"
        print(f"[{status}] Files: {', '.join(files)}", file=file)
        if validation_text:
            print(validation_text, file=file)


DEFAULT_ROOT_DIRECTORY = "."


# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------


def setup_logging(debug: bool = False, stream=None) -> None:
    """
    Configure logging. If 'stream' is provided, logs go there
    (we use output_buffer inside validate_jsonld_against_shacl).
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
    """Make sure a folder key exists in ontology_dict with all expected subfields."""
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
    g = Graph()
    g.parse(file_path, format="turtle")
    prefixes = {prefix: str(namespace) for prefix, namespace in g.namespaces()}
    logging.debug("Extracted prefixes from TTL %s: %s", file_path, prefixes)
    return prefixes


def extract_prefixes_from_jsonld(file_path: str) -> Dict[str, str]:
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
    Merge 'additions' into 'base'. If a prefix already exists with
    a different URI, log a warning but keep the original mapping.
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
    used: Set[str] = set()
    if isinstance(value, str):
        # crude CURIE detection: "prefix:local", but not full IRIs or JSON-LD keywords
        if ":" in value and "://" not in value and not value.startswith("@"):
            prefix = value.split(":", 1)[0]
            if prefix:
                used.add(prefix)
    elif isinstance(value, dict):
        for k, v in value.items():
            if (
                isinstance(k, str)
                and ":" in k
                and "://" not in k
                and not k.startswith("@")
            ):
                used.add(k.split(":", 1)[0])
            used |= _collect_used_prefixes_in_json_value(v)
    elif isinstance(value, list):
        for item in value:
            used |= _collect_used_prefixes_in_json_value(item)
    return used


def check_jsonld_context_coverage(file_path: str) -> Dict[str, Set[str]]:
    """
    Check whether @context of file_path defines all prefixes that are actually used
    in the JSON-LD document.

    Returns a dict with keys:
        - 'declared': set[str]
        - 'used': set[str]
        - 'missing': set[str]
        - 'unused': set[str]
    """
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    context = data.get("@context", {})
    declared_prefixes: Set[str] = set()

    # NOTE: This coverage check only handles inline dict contexts. If @context is a list
    # (e.g., remote contexts + local dict), this warning is expected and the result is
    # conservative (declared_prefixes may be incomplete).
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
    Resolve a JSON-LD @type into a fully qualified IRI if possible,
    otherwise return the original string.

    NOTE: This resolver primarily handles CURIEs (prefix:local) using the
    dynamically extracted prefix mapping. The manifest-based branch is
    currently only used if 'manifest_dir_url' is provided by the caller.
    """
    if ":" in json_type and "://" not in json_type:
        prefix, local_name = json_type.split(":", 1)
        if prefix in namespace_prefixes:
            return namespace_prefixes[prefix] + local_name
    elif manifest_dir_url is not None:
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
    if file is None:
        file = sys.stdout
    print("📌 Extracting all rdf:type from data graph...", file=file)
    used_types: Set[str] = set()
    type_counts: Counter[str] = Counter()

    rdf_type_pred = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")["type"]

    # NOTE: manifest_dir_url is currently unused by this pipeline (kept for
    # compatibility with the original script's manifest resolution logic).
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
) -> tuple[Graph, int, int]:
    """
    Load a list of RDF files into a single rdflib.Graph.

    Args:
        rdf_files: List of file paths or URLs to RDF files.
        rdf_format: Format of the RDF files (e.g., "json-ld", "turtle").
        file: Optional file-like object to print output messages.

    Returns:
        (Graph, loaded_count, failed_count):
            - Graph: The RDF graph with all loaded data.
            - loaded_count: number of files that parsed successfully
            - failed_count: number of files that failed to parse

    NOTE:
        A common failure mode for JSON-LD is remote @context resolution.
        If rdflib cannot fetch a remote context, parsing may fail and no triples
        will be loaded.
    """
    if file is None:
        file = sys.stdout

    data_graph = Graph()
    loaded_count = 0
    failed_count = 0

    for i, rdf_file in enumerate(rdf_files, start=1):
        try:
            data_graph.parse(rdf_file, format=rdf_format)
            loaded_count += 1
            logging.debug("Loaded %s file: %s", rdf_format, rdf_file)
            print(f"✅ [{i}/{len(rdf_files)}] Loaded: {rdf_file}", file=file)
        except Exception as e:  # pragma: no cover - defensive
            failed_count += 1
            logging.error("Failed to load %s: %s", rdf_file, e)
            print(f"❌ [{i}/{len(rdf_files)}] Failed: {rdf_file} → {e}", file=file)

    return data_graph, loaded_count, failed_count


# ---------------------------------------------------------------------------
# Ontology & JSON-LD discovery
# ---------------------------------------------------------------------------


def build_dict_for_ontologies(
    root_dir: str,
    paths: List[str],
) -> Dict[str, Dict[str, object]]:
    """
    Build a dictionary keyed by relative folder names with second-level keys:
        - 'instance': List[str]
        - 'reference': List[str]
        - 'ontologies': List[str] (filled later with *relevant* schema files)
        - 'shacle_shapes': List[str] (filled later with *relevant* schema files)
        - 'prefixes': Dict[str, str] (JSON-LD + schema prefixes)
        - 'context_issues': Dict[file_path, dict]

    New semantics:

    - If 'paths' contains directories:
        we still collect *_instance.json and *_reference.json within them.

    - If 'paths' contains files:
        any *.json / *.jsonld file is accepted as an 'instance' file
        (unless it ends with '_reference.json', which is treated as 'reference').

    NOTE:
        Files are resolved relative to the current working directory. The 'root_dir'
        is used for grouping (relative folder keys) and for schema discovery.
    """
    ontology_dict: Dict[str, Dict[str, object]] = {}

    collected_files: List[str] = []

    for p in paths:
        # Interpret paths relative to current working directory, not root_dir.
        full_path = os.path.abspath(p)

        if os.path.isdir(full_path):
            # Legacy behaviour: directories with *_instance.json / *_reference.json.
            collected_files.extend(glob.glob(os.path.join(full_path, "*_instance.json")))
            collected_files.extend(glob.glob(os.path.join(full_path, "*_reference.json")))
        elif os.path.isfile(full_path) and (
            full_path.endswith(".json") or full_path.endswith(".jsonld")
        ):
            # Generic single JSON/JSON-LD file
            collected_files.append(full_path)
            # Old pattern: from an explicit *_instance.json we still auto-add
            # sibling *_reference.json files in the same directory.
            if full_path.endswith("_instance.json"):
                directory = os.path.dirname(full_path)
                collected_files.extend(glob.glob(os.path.join(directory, "*_reference.json")))

    if not collected_files:
        return {}

    # New: classify generic JSON files
    instance_files: List[str] = []
    reference_files: List[str] = []

    for f in collected_files:
        if f.endswith("_reference.json"):
            reference_files.append(f)
        else:
            # Any other JSON / JSON-LD file counts as "instance",
            # including *_instance.json and arbitrary names like
            # simpulseid-administrator-credential.json.
            instance_files.append(f)

    # Group JSON-LD by folder
    for key, files in (("instance", instance_files), ("reference", reference_files)):
        for file_path in files:
            rel_dir = os.path.relpath(os.path.dirname(file_path), root_dir)
            folder_name = rel_dir.replace(os.sep, "/")
            ensure_folder_entry(ontology_dict, folder_name)
            ontology_dict[folder_name][key].append(os.path.normpath(file_path))

    return ontology_dict


# ---------------------------------------------------------------------------
# Enrich dict with JSON-LD prefixes and context coverage
# ---------------------------------------------------------------------------


def add_jsonld_prefixes_and_context_info(
    ontology_dict: Dict[str, Dict[str, object]],
) -> None:
    """
    For each folder, extract prefixes from instance/reference JSON-LD files and
    store them under 'prefixes'. Also store context coverage issues per file
    under 'context_issues'.

    NOTE:
        Prefix extraction only considers inline @context dict entries. If the
        document relies on remote contexts, the dynamic prefix mapping may be
        incomplete unless those contexts are inlined in the JSON.
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
    For each folder, also extract prefixes from TTL-based ontology and
    SHACL files that are *actually used* (attached to the dict) and merge
    them into the folder's 'prefixes'.
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
    Merge all folder-level 'prefixes' into a single global mapping.
    """
    global_prefixes: Dict[str, str] = {}
    for folder_key, contents in ontology_dict.items():
        folder_prefixes = contents.get("prefixes", {})  # type: ignore[assignment]
        merge_prefix_mappings(global_prefixes, folder_prefixes, source=folder_key)
    logging.debug("Global dynamic prefixes: %s", global_prefixes)
    return global_prefixes


def print_prefix_mapping(prefixes: Dict[str, str], file=None) -> None:
    """Pretty-print the dynamic prefix mapping."""
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
    print(f"   {header_prefix}  → Namespace", file=file)
    print(f"   {'-' * max_len}  ─ {'-' * 60}", file=file)

    for prefix, ns in sorted(prefixes.items(), key=lambda x: (x[0] or "")):
        label = prefix if prefix else "(default)"
        print(f"   {label.ljust(max_len)}  → {ns}", file=file)
    print("", file=file)


# ---------------------------------------------------------------------------
# Helpers for instance/reference collection & data graph
# ---------------------------------------------------------------------------


def collect_instance_and_reference_files(
    ontology_dict: Dict[str, Dict[str, object]],
) -> Tuple[List[str], List[str]]:
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
) -> tuple[Graph, int, int]:

    def print_out(*args, **kwargs) -> None:
        print(*args, **kwargs, file=output_buffer)

    instance_files, reference_files = collect_instance_and_reference_files(
        ontology_dict
    )
    all_jsonld_files = instance_files + reference_files

    if not all_jsonld_files:
        print_out("Error code 100: No instance/reference JSON-LD files found.")
        return Graph(), 0, 0

    print_out("📌 Loading JSON-LD files into data graph...")
    # NOTE: This loads only the JSON(-LD) files discovered from the CLI args.
    return load_rdf_files(all_jsonld_files, rdf_format="json-ld", file=output_buffer)


# ---------------------------------------------------------------------------
# Ontology graph dependency helpers (ontology IRI based, with normalization)
# ---------------------------------------------------------------------------


def normalize_iri(iri: str) -> str:
    """Normalize IRIs/namespaces for comparison.

    We strip any trailing "#" or "/" characters so that ontology IRIs
    like ``.../owl``, ``.../owl/`` and ``.../owl#`` all collapse to the
    same canonical form. This improves matching between prefixes and
    ontology IRIs across different modelling styles.
    """
    while iri.endswith("#") or iri.endswith("/"):
        iri = iri[:-1]
    return iri


def _build_ontology_iri_index(root_dir: str) -> Dict[str, str]:
    """
    Map ontology IRI (the subject of rdf:type owl:Ontology)
    to the local *_ontology.ttl file that defines it.
    """
    iri_to_file: Dict[str, str] = {}
    ontology_files = glob.glob(f"{root_dir}/**/*_ontology.ttl", recursive=True)

    for onto in ontology_files:
        g = Graph()
        try:
            g.parse(onto, format="turtle")
        except Exception as e:  # defensive
            logging.warning("Failed to parse ontology %s for IRI index: %s", onto, e)
            continue

        for s in g.subjects(RDF.type, OWL.Ontology):
            iri_raw = str(s)
            iri = normalize_iri(iri_raw)
            # If there are multiple, we keep the first; log and continue
            if iri in iri_to_file and iri_to_file[iri] != onto:
                logging.warning(
                    "Ontology IRI %s defined by multiple files: %s, %s",
                    iri_raw,
                    iri_to_file[iri],
                    onto,
                )
            else:
                iri_to_file[iri] = onto

    logging.debug("Ontology IRI index: %s", iri_to_file)
    return iri_to_file


def _build_ontology_dependencies(
    root_dir: str,
    iri_to_file: Dict[str, str],
) -> Dict[str, Set[str]]:
    """
    For each *_ontology.ttl, determine which *other* ontologies it depends on,
    based on prefixes whose namespace matches a known ontology IRI.

    The edge direction is:
        current_ontology  --(uses namespace of)-->  depended_ontology
    """
    deps: Dict[str, Set[str]] = defaultdict(set)
    ontology_files = glob.glob(f"{root_dir}/**/*_ontology.ttl", recursive=True)

    for onto in ontology_files:
        g = Graph()
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
    Starting from 'initial_files', follow ontology dependencies transitively
    using the 'deps' graph.

    Only ontologies reachable along this graph will be returned.
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
# SHACL + ontology loading based on used rdf:type and ontology deps
# ---------------------------------------------------------------------------


def _select_relevant_shacl_files(
    root_dir: str,
    used_types: Set[str],
) -> Tuple[List[str], Graph]:
    """
    Identify and load SHACL files whose sh:targetClass matches any of the
    rdf:type values seen in the data graph.

    NOTE:
        This requires that the data graph actually contains rdf:type triples.
        If JSON-LD parsing fails (e.g., due to remote @context issues), used_types
        may be empty and no SHACL files will be selected.
    """
    shacl_graph = Graph()
    shacl_files = glob.glob(f"{root_dir}/**/*_shacl.ttl", recursive=True)

    SH = Namespace("http://www.w3.org/ns/shacl#")
    target_class_pred = SH["targetClass"]

    relevant_files: List[str] = []

    for shacl_file in shacl_files:
        tmp_graph = Graph()
        try:
            tmp_graph.parse(shacl_file, format="turtle")
        except Exception as e:  # defensive
            logging.warning("Failed to parse SHACL file %s: %s", shacl_file, e)
            continue

        is_relevant = False
        for _, _, rdf_type in tmp_graph.triples((None, target_class_pred, None)):
            if str(rdf_type) in used_types:
                is_relevant = True
                break

        if is_relevant:
            relevant_files.append(shacl_file)
            shacl_graph += tmp_graph

    return relevant_files, shacl_graph


def _select_relevant_ontologies(
    root_dir: str,
    used_types: Set[str],
) -> List[str]:
    """
    Find ontologies that define classes which appear in used_types,
    then expand them transitively via namespace-based ontology dependencies.
    """
    ontology_files = glob.glob(f"{root_dir}/**/*_ontology.ttl", recursive=True)

    # Step 1: ontologies that define at least one used class
    initially_relevant: List[str] = []
    for ontology_file in ontology_files:
        ontology_graph = Graph()
        try:
            ontology_graph.parse(ontology_file, format="turtle")
        except Exception as e:  # defensive
            logging.warning("Failed to parse ontology %s: %s", ontology_file, e)
            continue

        defined_classes = set(ontology_graph.subjects(RDF.type, OWL.Class)).union(
            ontology_graph.subjects(RDF.type, RDFS.Class)
        )
        defined_iris = {str(cls) for cls in defined_classes}
        matched_types = defined_iris.intersection(used_types)

        logging.debug("In %s, defined classes: %s", ontology_file, defined_iris)
        logging.debug("Matched types with data: %s", matched_types)

        if matched_types:
            initially_relevant.append(ontology_file)

    # Step 2: closure via ontology IRI / prefix graph
    iri_index = _build_ontology_iri_index(root_dir)
    deps = _build_ontology_dependencies(root_dir, iri_index)
    all_relevant = _expand_ontology_dependencies_from(
        initial_files=initially_relevant, deps=deps
    )

    return all_relevant


def load_shacl_and_ontologies(
    root_dir: str,
    used_types: Set[str],
    file=None,
) -> Tuple[Graph, Graph, List[str], List[str]]:
    if file is None:
        file = sys.stdout

    logging.debug("Starting to load SHACL and ontology files.")

    # 1) SHACL: data-driven via sh:targetClass
    relevant_shacl_files, shacl_graph = _select_relevant_shacl_files(
        root_dir, used_types
    )

    # 2) Ontologies: first those defining used classes, then dependency closure
    relevant_ontology_files = _select_relevant_ontologies(root_dir, used_types)

    # 2b) Always include core base ontologies (support vocabularies)
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

    support_paths: List[str] = []
    for rel in support_ontologies:
        full = os.path.normpath(os.path.join(root_dir, rel))
        if os.path.exists(full):
            support_paths.append(full)

    # Merge, keeping stable order and de-duplicating
    all_ontology_files = []
    seen = set()
    for path in list(relevant_ontology_files) + support_paths:
        if path not in seen:
            seen.add(path)
            all_ontology_files.append(path)
    relevant_ontology_files = all_ontology_files

    # Logging / human-readable summary
    if relevant_shacl_files:
        print("📌 Relevant SHACL files to load:", file=file)
        for path in sorted(relevant_shacl_files):
            print(f"   {path}", file=file)
    else:
        print(
            "📌 No relevant SHACL files found for the detected rdf:type values.",
            file=file,
        )

    if relevant_ontology_files:
        print("📌 Relevant ontology files to load:", file=file)
        for path in sorted(relevant_ontology_files):
            print(f"   {path}", file=file)
    else:
        print(
            "📌 No relevant ontology files found for the detected rdf:type values.",
            file=file,
        )

    # 3) Actually parse ontology files into a single graph
    ont_graph = Graph()
    for ontology_file in relevant_ontology_files:
        ontology_graph = Graph()
        try:
            ontology_graph.parse(ontology_file, format="turtle")
        except Exception as e:  # defensive
            logging.warning(
                "Failed to parse ontology %s when building ontology graph: %s",
                ontology_file,
                e,
            )
            continue
        ont_graph += ontology_graph
        print(
            f"✅ Loaded Ontology file into ontology graph: {ontology_file}", file=file
        )

    # 4) SHACL already parsed
    for shacl_file in sorted(relevant_shacl_files):
        print(f"✅ Loaded SHACL file into shacl graph: {shacl_file}", file=file)

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
) -> Tuple[int, str]:
    """
    Main validation pipeline using ontology_dict built beforehand.
    Returns (exit_code, output_text).

    Semantics:
    - Only the JSON(-LD) instance/reference files discovered from the CLI
      arguments are loaded into the data graph.
    - Based on the rdf:type values found there, only the *relevant*
      SHACL shapes and ontologies (plus their ontology dependencies)
      are loaded for validation.
    - Ontologies themselves are NOT self-validated against their SHACL
      shapes (focus is purely on instance data).

    IMPORTANT:
    - If no JSON-LD data could be loaded (e.g., remote context resolution fails),
      the script aborts validation to avoid false positives.
    """
    output_buffer = StringIO()

    def print_out(*args, **kwargs) -> None:
        print(*args, **kwargs, file=output_buffer)

    # Configure logging to write into the same buffer, so it ends
    # up in the returned message (and thus in --logfile or stdout).
    setup_logging(debug, stream=output_buffer)
    logger = logging.getLogger()
    if not debug:
        logger.disabled = True

    if PYSHACL_IMPORT_ERROR is not None:  # pragma: no cover - environment-only
        print_out(
            "Error: pyshacl is not installed. Validation cannot run. "
            f"Import error: {PYSHACL_IMPORT_ERROR}"
        )
        return 99, output_buffer.getvalue()

    if not ontology_dict:
        print_out("Error code 100: No valid files found in ontology_dict.")
        return 100, output_buffer.getvalue()

    if inference_mode not in {"none", "rdfs", "owlrl", "both"}:
        print_out(
            f"Error: Unsupported inference mode '{inference_mode}'. "
            "Use one of: none, rdfs, owlrl, both."
        )
        return 98, output_buffer.getvalue()

    # 1) JSON-LD prefixes + context coverage
    add_jsonld_prefixes_and_context_info(ontology_dict)

    # 2) Data graph (instance + reference) – ONLY those discovered from CLI args
    data_graph, loaded_count, failed_count = build_data_graph_from_dict(
        ontology_dict, output_buffer
    )

    # Abort if nothing could be loaded. Otherwise we get false positives.
    if loaded_count == 0:
        print_out(
            "Error code 101: No JSON-LD data could be loaded (all parses failed). "
            "Aborting validation to avoid false positives."
        )
        return 101, output_buffer.getvalue()

    # Abort if the graph is empty (edge case: files loaded but produce no triples)
    if len(data_graph) == 0:
        print_out(
            "Error code 102: Data graph is empty after loading JSON-LD. "
            "Aborting validation to avoid false positives."
        )
        return 102, output_buffer.getvalue()

    # 3) Extract RDF types from the data graph
    print_out("📌 Extracting RDF types from data graph...")
    # At this point we only have JSON-LD prefixes in the dict (schema prefixes are added later)
    jsonld_prefixes = build_global_prefix_mapping(ontology_dict)
    used_types = extract_used_types(
        data_graph, jsonld_prefixes, root_dir, file=output_buffer
    )

    # 4) Load only necessary SHACL & ontologies based on rdf:type usage
    print_out(
        "📌 Loading only necessary SHACL shapes and ontologies "
        "based on detected RDF types..."
    )
    shacl_graph, ont_graph, relevant_shacl_files, relevant_ontology_files = (
        load_shacl_and_ontologies(
            root_dir,
            used_types,
            file=output_buffer,
        )
    )

    # 5) Attach the relevant schema files back to the ontology_dict so we can
    #    derive a *schema-aware* prefix mapping (restricted to actually used files).
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

    # 6) Extend prefixes with those from the *relevant* schema files only
    extend_prefixes_with_schema_files(ontology_dict, root_dir)
    dynamic_prefixes = build_global_prefix_mapping(ontology_dict)
    if debug:
        print_prefix_mapping(dynamic_prefixes, file=output_buffer)

    # 7) Final validation
    instance_files, reference_files = collect_instance_and_reference_files(
        ontology_dict
    )
    print_out("🔍 Performing overall validation explicitly...")

    # Capture *all* stdout/stderr from pyshacl.validate into output_buffer,
    # so nothing leaks to the real console even if --logfile is set.
    with contextlib.redirect_stdout(output_buffer), contextlib.redirect_stderr(
        output_buffer
    ):
        conforms, _, v_text = validate(
            data_graph,
            shacl_graph=shacl_graph,
            ont_graph=ont_graph,
            abort_on_first=False,
            inference=inference_mode,
            validation_mode="strict",
            debug=debug,
            inplace=False,
        )

    if not conforms:
        print_validate_jsonld_against_shacl_result(
            False,
            instance_files + reference_files,
            v_text,
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
        "--debug",
        action="store_true",
        help="Enable debug logging",
    )
    parser.add_argument(
        "--logfile",
        type=str,
        help="Write full validator output to this file instead of stdout",
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
    root_dir = os.path.abspath(args.root_dir)

    # Redirect stdout/stderr to logfile if requested
    original_stdout = sys.stdout
    original_stderr = sys.stderr
    logfile_handle = None
    if args.logfile:
        logfile_handle = open(args.logfile, "w", encoding="utf-8")
        sys.stdout = logfile_handle
        sys.stderr = logfile_handle

    ontology_dict = build_dict_for_ontologies(root_dir, args.paths)
    if not ontology_dict:
        print(
            f"Error code 100: No valid files found in given paths {args.paths}.",
            file=sys.stderr,
        )
        if logfile_handle:
            logfile_handle.close()
            sys.stdout = original_stdout
            sys.stderr = original_stderr
        sys.exit(100)

    return_code, message = validate_jsonld_against_shacl(
        root_dir,
        ontology_dict,
        debug=args.debug,
        inference_mode=args.inference,
    )

    # Print the final message once (to stdout or logfile, depending on redirection)
    print(message)

    if logfile_handle:
        logfile_handle.close()
        sys.stdout = original_stdout
        sys.stderr = original_stderr

    sys.exit(return_code)


if __name__ == "__main__":
    main()
