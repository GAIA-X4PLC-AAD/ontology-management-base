import glob
import io
import json
import logging
import os
import sys
from collections import defaultdict
from io import StringIO
from typing import Dict, List
from urllib.parse import urlparse

from pyshacl import validate
from rdflib import OWL, RDF, RDFS, Graph, Namespace

from utils.print_formatting import print_validate_jsonld_against_shacl_result

ROOT_DIRECTORY = "."

# Set the encoding for stdout and stderr to UTF-8 only when run as main
if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")


def setup_logging(debug=False):
    handlers = [logging.StreamHandler(sys.stdout)]
    if debug:
        handlers.append(logging.FileHandler("output.log", mode="w"))
    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO,
        handlers=handlers,
        format="%(asctime)s [%(levelname)s] %(message)s",
        force=True,
    )


# --- Dynamic Prefix Extraction Functions ---
def extract_prefixes_from_ttl(file_path: str) -> dict:
    g = Graph()
    g.parse(file_path, format="turtle")
    prefixes = {prefix: str(namespace) for prefix, namespace in g.namespaces()}
    logging.debug(f"Extracted prefixes from TTL {file_path}: {prefixes}")
    return prefixes


def extract_prefixes_from_jsonld(file_path: str) -> dict:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    context = data.get("@context", {})
    prefix_mapping = {}
    if isinstance(context, dict):
        for key, value in context.items():
            if isinstance(value, str):
                prefix_mapping[key] = value
    logging.debug(f"Extracted prefixes from JSON-LD {file_path}: {prefix_mapping}")
    return prefix_mapping


def load_dynamic_prefixes(files: list) -> dict:
    dynamic_prefixes = {}
    for file in files:
        try:
            if file.endswith(".ttl"):
                mapping = extract_prefixes_from_ttl(file)
            elif file.endswith(".json") or file.endswith(".jsonld"):
                mapping = extract_prefixes_from_jsonld(file)
            else:
                continue
            dynamic_prefixes.update(mapping)
        except Exception as e:
            logging.warning(f"Failed to extract prefixes from {file}: {e}")
    logging.debug(f"Aggregated dynamic prefixes: {dynamic_prefixes}")
    return dynamic_prefixes


def resolve_manifest_local_path(
    name: str, file_type: str, root_dir: str = ROOT_DIRECTORY
) -> str:
    filename = f"{name}_{file_type}.ttl"
    local_path = os.path.join(root_dir, name, filename)
    print(f"Resolved manifest local path for {name} ({file_type}): {local_path}")
    return local_path


def resolve_prefixed_type(
    json_type: str,
    context: dict = None,
    root_dir: str = ROOT_DIRECTORY,
    dynamic_mapping: dict = None,
) -> str:
    full_context = {}
    if dynamic_mapping:
        for prefix, iri in dynamic_mapping.items():
            if not iri.endswith("#") and not iri.endswith("/"):
                full_context[prefix] = iri + "#"
            else:
                full_context[prefix] = iri
    if context:
        full_context.update(context)
    logging.info(f"Resolving type '{json_type}' using context: {full_context}")

    if ":" in json_type:
        prefix, suffix = json_type.split(":", 1)
        base_iri = full_context.get(prefix)
        if base_iri:
            resolved = f"{base_iri}{suffix}"
            logging.debug(f"Resolved '{json_type}' to '{resolved}'")
            if resolved.startswith("https://ontologies.envited-x.net/"):
                parsed = urlparse(resolved)
                path_parts = parsed.path.strip("/").split("/")
                if len(path_parts) >= 3:
                    name = path_parts[0]
                    local_ontology = resolve_manifest_local_path(
                        name, "ontology", root_dir
                    )
                    logging.debug(
                        f"Redirecting '{resolved}' to local ontology: '{local_ontology}'"
                    )
                    return local_ontology
            return resolved
    return json_type


def load_shacl_and_ontologies(
    root_dir,
    used_types,
    dynamic_prefixes: dict,
    file=None,
):
    logging.debug("Starting to load SHACL and ontology files.")
    shacl_graph = Graph()
    ont_graph = Graph()
    if dynamic_prefixes:
        for prefix, namespace in dynamic_prefixes.items():
            shacl_graph.bind(prefix, Namespace(namespace))
            logging.debug(f"Bound prefix {prefix} -> {namespace}")
    shacl_files = glob.glob(f"{root_dir}/**/*_shacl.ttl", recursive=True)
    ontology_files = glob.glob(f"{root_dir}/**/*_ontology.ttl", recursive=True)
    logging.debug(f"Found SHACL files: {shacl_files}")
    logging.debug(f"Found Ontology files: {ontology_files}")

    def is_relevant(graph, used_types):
        sh_ns = dynamic_prefixes.get("sh")
        if sh_ns:
            SH = Namespace(sh_ns)
        else:
            logging.error("No 'sh' prefix found in dynamic mapping.")
            return False
        for subj, pred, rdf_type in graph.triples((None, SH.targetClass, None)):
            logging.debug(f"Found targetClass triple: {subj} {pred} {rdf_type}")
            if str(rdf_type) in used_types:
                logging.debug(f"Match found for target {rdf_type}")
                return True
        return False

    for shacl_file in shacl_files:
        tmp_graph = Graph()
        tmp_graph.parse(shacl_file, format="turtle")
        if is_relevant(tmp_graph, used_types):
            shacl_graph += tmp_graph
            print(f"✅ Loaded SHACL file into shacle graph: {shacl_file}", file=file)

    for ontology_file in ontology_files:
        ontology_graph = Graph()
        ontology_graph.parse(ontology_file, format="turtle")
        defined_classes = set(ontology_graph.subjects(RDF.type, OWL.Class)).union(
            ontology_graph.subjects(RDF.type, RDFS.Class)
        )
        expanded_defined_classes = {str(cls) for cls in defined_classes}
        matched_types = expanded_defined_classes.intersection(used_types)
        logging.debug(
            f"In {ontology_file}, defined classes: {expanded_defined_classes}"
        )
        logging.debug(f"Matched types: {matched_types}")
        if matched_types:
            ont_graph += ontology_graph
            print(
                f"✅ Loaded Ontology file into shacle graph: {ontology_file}", file=file
            )
    logging.debug("Completed loading SHACL and ontology files.")
    return shacl_graph, ont_graph


# --- Namespace Extraction and Used Types ---


def extract_namespace(rdf_type_str):
    if "://" not in rdf_type_str:
        prefix = rdf_type_str.split(":", 1)[0]
        return f"{prefix}:"
    else:
        parsed = urlparse(rdf_type_str)
        return f"{parsed.scheme}://{parsed.netloc}"


def extract_used_types(
    data_graph, dynamic_prefixes=None, root_dir=ROOT_DIRECTORY, file=None
):
    used_types = defaultdict(set)
    for _, _, rdf_type in data_graph.triples((None, RDF.type, None)):
        rdf_type_str = str(rdf_type)
        # Resolve prefixed type if dynamic prefixes are available
        if dynamic_prefixes:
            rdf_type_str = resolve_prefixed_type(
                rdf_type_str, dynamic_mapping=dynamic_prefixes, root_dir=root_dir
            )
        namespace = extract_namespace(rdf_type_str)
        used_types[namespace].add(rdf_type_str)
    formatted_output = []
    for namespace, types in used_types.items():
        formatted_types = "\n    ".join(sorted(types))
        formatted_output.append(f"  - {namespace}:\n    {formatted_types}")
    logging.debug("Extracted RDF types:\n" + "\n".join(formatted_output))
    print(
        f"✅ Extracted {sum(len(types) for types in used_types.values())} unique RDF types:\n"
        + "\n".join(formatted_output),
        file=file,
    )
    return {rdf_type for types in used_types.values() for rdf_type in types}


def load_rdf_files(rdf_files, rdf_format, file=None):
    """
    Loads RDF files of a given format into an RDF graph and prints each file with its number.

    Args:
        rdf_files (list): List of file paths or URLs to RDF files.
        rdf_format (str): Format of the RDF files (e.g., "json-ld", "turtle").
        file: Optional file-like object to print output messages (default is None, which prints to stdout).

    Returns:
        rdflib.Graph: The RDF graph with all loaded data.
    """
    data_graph = Graph()
    failed_files = 0

    for i, rdf_file in enumerate(rdf_files, start=1):
        try:
            data_graph.parse(rdf_file, format=rdf_format)
            logging.debug(f"Loaded {rdf_format} file: {rdf_file}")
            print(f"✅ [{i}/{len(rdf_files)}] Loaded: {rdf_file}", file=file)
        except Exception as e:
            logging.error(f"Failed to load {rdf_file}: {e}")
            print(f"❌ [{i}/{len(rdf_files)}] Failed: {rdf_file} → {e}", file=file)
            failed_files += 1

    return data_graph


# --- Main Function ---


def validate_jsonld_against_shacl(paths: list, debug: bool = False) -> tuple[int, str]:
    """
    Main validation logic extracted from CLI main.
    Args:
        paths: List of file or directory paths to validate.
        debug: Enable debug logging.
    Returns:
        (return_code, message)
    """

    output_buffer = StringIO()

    setup_logging(debug)

    logger = logging.getLogger()
    if not debug:
        logger.disabled = True

    def print_out(*args, **kwargs):
        print(*args, **kwargs, file=output_buffer)

    # --- Dynamic Prefix Mapping ---
    files_for_prefixes = []
    for path in paths:
        if os.path.isdir(path):
            files_for_prefixes.extend(glob.glob(os.path.join(path, "*_instance.json")))
            files_for_prefixes.extend(glob.glob(os.path.join(path, "*_reference.json")))
        elif os.path.isfile(path) and path.endswith(".json"):
            files_for_prefixes.append(path)

    if not files_for_prefixes:
        print_out("\nError code 100: No valid files found.")
        return 100, output_buffer.getvalue()

    dynamic_prefixes = load_dynamic_prefixes(files_for_prefixes)
    print_out("\n✅ Resolved Dynamic Prefix Mapping:")
    for prefix, ns in sorted(dynamic_prefixes.items()):
        print_out(f"   {prefix}: {ns}")
    print_out()

    # --- Step 1: Collect all *ontology.ttl files ---
    ontology_files = []
    for path in paths:
        if os.path.isdir(path):
            ontology_files.extend(glob.glob(os.path.join(path, "*_ontology.ttl")))
        elif os.path.isfile(path) and path.endswith("_ontology.ttl"):
            ontology_files.append(path)

    # --- Step 2: Load corresponding SHACL files ---
    shacl_graph_onto = Graph()
    for onto_file in ontology_files:
        shacl_file = onto_file.replace("_ontology.ttl", "_shacl.ttl")
        if os.path.exists(shacl_file):
            print_out(
                f"📌 Testing ontology against corresponding shacle: \n   Loading SHACL: {shacl_file}\n   Loading ontology: {onto_file}"
            )
            shacl_graph_onto.parse(shacl_file, format="turtle")
        else:
            print_out(
                f"⚠️ Warning: No SHACL file found for {onto_file}, skipping validation."
            )

    # --- Step 3: Validate each ontology.ttl against its SHACL graph ---
    for onto_file in ontology_files:
        onto_graph = Graph()
        onto_graph.parse(onto_file, format="turtle")
        conforms, _, v_text = validate(
            onto_graph,
            shacl_graph=shacl_graph_onto,
            inference="owlrl",
            validation_mode="strict",
            debug=debug,
        )
        if not conforms:
            print_validate_jsonld_against_shacl_result(
                False, [onto_file], v_text, exit_code=None
            )
            print_out(f"❌ Ontology file {onto_file} failed SHACL validation.\n")
            return 200, output_buffer.getvalue()
        else:
            print_out(f"✅ Ontology file {onto_file} passed SHACL validation.\n")

    # --- Step 4: Load JSON-LD Instance and Reference Files ---
    instance_files = []
    reference_files = []
    for path in paths:
        if os.path.isdir(path):
            instance_files.extend(glob.glob(f"{path}/*_instance.json"))
            reference_files.extend(glob.glob(f"{path}/*_reference.json"))
        elif os.path.isfile(path):
            if path.endswith("_instance.json"):
                instance_files.append(path)
            elif path.endswith("_reference.json"):
                reference_files.append(path)
    print_out("📌 Loading JSON-LD files into data graph...")
    data_graph = load_rdf_files(
        instance_files + reference_files, rdf_format="json-ld", file=output_buffer
    )

    # --- Step 6: Extract RDF Types from the Data Graph ---
    print_out("📌 Extracting RDF types from data graph...")
    used_types = extract_used_types(
        data_graph, dynamic_prefixes, ".", file=output_buffer
    )

    # --- Step 7: Load only necessary SHACL shapes based on detected RDF types ---
    print_out("📌 Loading only necessary SHACL shapes based on detected RDF types...")
    script_path = os.path.abspath(__file__)
    script_directory = os.path.dirname(script_path)
    parent_directory = os.path.relpath(os.path.dirname(script_directory))
    logging.debug(f"Parent dir...: {parent_directory}")
    shacl_graph, ont_graph = load_shacl_and_ontologies(
        parent_directory,
        used_types,
        dynamic_prefixes,
        file=output_buffer,
    )

    # --- Step 8: Perform Final Validation ---
    print_out("🔍 Performing overall validation explicitly...")
    conforms, _, v_text = validate(
        data_graph,
        shacl_graph=shacl_graph,
        ont_graph=ont_graph,
        abort_on_first=True,
        inference="owlrl",
        validation_mode="strict",
        debug=debug,
    )
    logging.debug(f"Final overall validation: Conforms = {conforms}")

    # --- Step 9: Print Validation Report ---
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


def build_dict_for_ontologies(
    root_dir: str, paths: List[str]
) -> Dict[str, Dict[str, List[str]]]:
    """
    Build a dictionary keyed by relative folder names with second-level keys:
    'instance', 'reference', 'ontologies', 'shacle_shapes' each containing lists
    of full file paths. The entry 'prefixes' will contain the dict ['prefix', 'full_uri'].

    Args:
        root_dir (str): Root directory of the project.
        paths (List[str]): List of folder paths, JSON files, or other strings.

    Returns:
        Dict[str, Dict[str, List[str]]]: Nested dictionary as described.
    """
    data_dict: Dict[str, Dict[str, List[str]]] = {}

    def init_dict_entry(folder_name: str):
        if folder_name not in data_dict:
            data_dict[folder_name] = {
                "instance": [],
                "reference": [],
                "ontologies": [],
                "shacle_shapes": [],
                "prefixes": [],
            }

    collected_files = []

    # Collect files from input paths
    for p in paths:
        full_path = os.path.join(root_dir, p)
        if os.path.isdir(full_path):
            # Add all *_instance.json and *_reference.json files in directory (non-recursive)
            collected_files.extend(
                glob.glob(os.path.join(full_path, "*_instance.json"))
            )
            collected_files.extend(
                glob.glob(os.path.join(full_path, "*_reference.json"))
            )
        elif os.path.isfile(full_path) and full_path.endswith(".json"):
            collected_files.append(full_path)
            if full_path.endswith("_instance.json"):
                directory = os.path.dirname(full_path)
                collected_files.extend(
                    glob.glob(os.path.join(directory, "*_reference.json"))
                )
        else:
            # Ignore invalid or non-existent paths
            pass

    if not collected_files:
        # No valid files found; return empty dict
        return {}

    # Separate instance and reference files explicitly provided or found so far
    instance_files = [f for f in collected_files if f.endswith("_instance.json")]
    reference_files = [f for f in collected_files if f.endswith("_reference.json")]

    # Combine all instance and reference files for folder-based grouping
    all_files = {"instance": instance_files, "reference": reference_files}

    # Group files by relative folder and add to the dictionary under correct keys
    for key in ["instance", "reference"]:
        for file_path in all_files[key]:
            # Determine folder relative to root_dir
            rel_dir = os.path.relpath(os.path.dirname(file_path), root_dir)
            folder_name = rel_dir.replace(os.sep, "/")  # normalize for consistent keys
            init_dict_entry(folder_name)
            full_path = os.path.normpath(file_path)
            data_dict[folder_name][key].append(full_path)

    # ontologies and shacle_shapes remain empty lists for now

    return data_dict


def add_prefixes_to_ontologies(ontology_dict: Dict[str, Dict[str, List[str]]]) -> None:
    """
    For each top-level ontology (e.g. 'envited-x', 'scenario'), extract unique prefixes
    from all files listed under 'instance' and 'reference', and add a 'prefixes' dict
    under each ontology containing these prefixes.

    This function modifies the input dictionary in place.

    Args:
        ontology_dict (Dict[str, Dict[str, List[str]]]): Dictionary with ontology data,
            expected to have keys like 'instance' and 'reference' with lists of file paths.
    """
    for ontology_key, contents in ontology_dict.items():
        files_to_process = []
        # Collect all instance and reference files for this ontology
        for key in ["instance", "reference"]:
            file_list = contents.get(key, [])
            if file_list:
                files_to_process.extend(file_list)

        # Extract prefixes from these files using your existing function
        prefixes = load_dynamic_prefixes(files_to_process) if files_to_process else {}

        # Add or update the 'prefixes' key with the aggregated prefixes dictionary
        contents["prefixes"] = prefixes

        logging.debug(f"Added prefixes for ontology '{ontology_key}': {prefixes}")


def main():
    debug = "--debug" in sys.argv
    if len(sys.argv) < 2:
        print(
            "Usage: python validate_jsonld_shacl.py [--debug] <directory or file> [additional files...]",
            file=sys.stderr,
        )
        sys.exit(100)
    paths = [os.path.normpath(arg) for arg in sys.argv[1:] if arg != "--debug"]

    data_dict_4 = build_dict_for_ontologies(ROOT_DIRECTORY, paths)
    add_prefixes_to_ontologies(data_dict_4)

    return_code, message = validate_jsonld_against_shacl(paths, debug)
    if return_code != 0:
        print(message, file=sys.stderr)
        sys.exit(return_code)
    else:
        print(message)
        sys.exit(0)


if __name__ == "__main__":
    main()
