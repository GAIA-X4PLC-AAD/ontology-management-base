import glob
import json
import logging
import os
import sys
import textwrap
from collections import defaultdict
from urllib.parse import urlparse

from pyshacl import validate
from rdflib import RDF, Graph, Namespace

# --- Dynamic Prefix Extraction Functions ---


def extract_prefixes_from_ttl(file_path: str) -> dict:
    """
    Parses a Turtle file and returns a dictionary mapping prefixes to namespaces.
    """
    g = Graph()
    g.parse(file_path, format="turtle")
    # g.namespaces() yields (prefix, namespace) pairs.
    return {prefix: str(namespace) for prefix, namespace in g.namespaces()}


def extract_prefixes_from_jsonld(file_path: str) -> dict:
    """
    Loads a JSON-LD file, extracts the @context (if a dictionary), and returns prefix mappings.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    context = data.get("@context", {})
    prefix_mapping = {}
    if isinstance(context, dict):
        for key, value in context.items():
            # Only consider string values as prefix mappings.
            if isinstance(value, str):
                prefix_mapping[key] = value
    return prefix_mapping


def load_dynamic_prefixes(files: list) -> dict:
    """
    Given a list of file paths (Turtle and/or JSON-LD),
    extracts and aggregates prefix mappings into a single dictionary.
    """
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
            print(f"⚠️ Warning: Failed to extract prefixes from {file}: {e}")
    return dynamic_prefixes


# --- Resolver Functions ---


def resolve_manifest_local_path(name: str, file_type: str, root_dir: str = ".") -> str:
    """
    Given a manifest name and the file type ("ontology" or "shacl"),
    returns the corresponding local file path.
    For example, if name is "NAME" and file_type is "ontology",
    the file path will be: "<root_dir>/NAME/NAME_ontology.ttl"
    """
    filename = f"{name}_{file_type}.ttl"
    return os.path.join(root_dir, name, filename)


def resolve_prefixed_type(
    json_type: str,
    context: dict = None,
    root_dir: str = ".",
    dynamic_mapping: dict = None,
) -> str:
    """
    Resolves a prefixed RDF type to a full IRI using a dynamic prefix mapping.
    The dynamic_mapping (if provided) is merged with any supplied context.
    If the resolved IRI matches the manifest pattern, it is converted to a local file path.
    """
    full_context = {}
    if dynamic_mapping:
        full_context.update(dynamic_mapping)
    if context:
        full_context.update(context)

    if ":" in json_type:
        prefix, suffix = json_type.split(":", 1)
        base_iri = full_context.get(prefix)
        if base_iri:
            resolved = f"{base_iri}{suffix}"
            # If the resolved IRI is a manifest URL that needs redirecting.
            if resolved.startswith("https://ontologies.envited-x.net/"):
                parsed = urlparse(resolved)
                # Expecting path like /NAME/v4/ontology...
                path_parts = parsed.path.strip("/").split("/")
                if len(path_parts) >= 3:
                    name = path_parts[0]
                    local_ontology = resolve_manifest_local_path(
                        name, "ontology", root_dir
                    )
                    return local_ontology
            return resolved
    return json_type


# --- Formatting and Printing Functions ---


def format_validation_report(
    v_text: str, width: int = 150, indent_size: int = 4
) -> str:
    """
    Parses and formats the SHACL validation report while:
    - Ensuring consistent indentation for nested properties.
    - Removing unnecessary blank lines.
    - Center-aligning section headers.
    - Keeping empty lines enclosed with '='.
    """
    border_line = "=" * width
    formatted_lines = []
    breakpoints = [
        "Validation Report",
        "Conforms:",
        "Results (",
        "Constraint Violation in",
        "Severity:",
        "Source Shape:",
        "Focus Node:",
        "Value Node:",
        "Message:",
        "Result Path:",
    ]
    for bp in breakpoints:
        v_text = v_text.replace(bp, f"\n{bp}")
    indent_level = 0
    last_line_was_blank = False
    for line in v_text.splitlines():
        stripped_line = line.strip()
        if not stripped_line:
            if last_line_was_blank:
                continue
            last_line_was_blank = True
            formatted_lines.append(f"= {' ' * (width - 4)} =")
            continue
        else:
            last_line_was_blank = False
        if stripped_line in breakpoints or stripped_line.endswith(":"):
            indent_level = 0
        elif stripped_line.startswith("sh:") or stripped_line.startswith("skos:"):
            indent_level = 1
        elif stripped_line.startswith("[") or stripped_line.startswith("]"):
            indent_level = 2
        elif stripped_line.startswith("<") and stripped_line.endswith(">"):
            indent_level = 2
        elif stripped_line.startswith("Literal("):
            indent_level = 3
        elif stripped_line.startswith("datatype="):
            indent_level = 4
        indent_space = " " * (indent_level * indent_size)
        wrapped_lines = textwrap.fill(
            stripped_line, width=width - 4 - len(indent_space)
        )
        for wrapped_line in wrapped_lines.split("\n"):
            formatted_lines.append(
                f"= {indent_space}{wrapped_line.ljust(width - 4 - len(indent_space))} ="
            )
    return f"{border_line}\n" + "\n".join(formatted_lines) + f"\n{border_line}"


def format_filenames(filenames: list, width: int = 150) -> list:
    """
    Splits the filenames list ensuring filenames remain intact.
    Ensures each filename starts on a new line properly formatted.
    """
    formatted_lines = []
    current_line = "["
    for i, file in enumerate(filenames):
        if i > 0:
            current_line += ", "
        if len(current_line) + len(file) + 2 >= width - 4:
            formatted_lines.append(f"{current_line}")
            current_line = "  " + file
        else:
            current_line += f"'{file}'"
    formatted_lines.append(f"{current_line}]")
    return formatted_lines


def print_validation_result(
    success: bool, onto_files: list = None, v_text: str = "", exit_code: int = None
):
    width = 150
    border_line = "=" * width
    header_text_files = [""]
    if success:
        header_text = ["✅ SHACL validation passed for:"]
    else:
        header_text = ["❌ SHACL validation failed for:"]
    centered_header_lines = [f"= {line.center(width - 5)} =" for line in header_text]
    if onto_files:
        formatted_filenames = format_filenames(onto_files, width)
        header_text_files.extend(formatted_filenames)
        centered_header_file_lines = [
            f"= {line.center(width - 4)} =" for line in header_text_files
        ]
    print(border_line)
    print("\n".join(centered_header_lines))
    if onto_files:
        print("\n".join(centered_header_file_lines))
    print(border_line)
    if not success:
        formatted_v_text = format_validation_report(v_text, width)
        print(formatted_v_text, file=sys.stderr)
    if exit_code is not None:
        sys.exit(exit_code)


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


# --- Loading SHACL and Ontology Files ---


def load_shacl_and_ontologies(root_dir, used_types, dynamic_mapping: dict):
    """
    Loads SHACL and ontology files relevant to the detected RDF types.
    The dynamic mapping is used to bind prefixes.
    """
    shacl_graph = Graph()
    loaded_files = set()
    # Bind prefixes from the dynamic mapping.
    if dynamic_mapping:
        for prefix, namespace in dynamic_mapping.items():
            shacl_graph.bind(prefix, Namespace(namespace))
    # Load GX trust framework SHACL explicitly.
    namespace_gx = {"gx": os.path.join(root_dir, "gx", "gx_shacl.ttl")}
    for prefix, file_path in namespace_gx.items():
        print(f"✅ Loading mapped SHACL file for {prefix}: {file_path}")
        shacl_graph.parse(file_path, format="turtle")
        loaded_files.add(file_path)
    shacl_files = glob.glob(f"{root_dir}/**/*_shacl.ttl", recursive=True)
    ontology_files = glob.glob(f"{root_dir}/**/*_ontology.ttl", recursive=True)

    def is_relevant(graph, used_types):
        # Use the 'sh' prefix from dynamic mapping.
        sh_ns = dynamic_mapping.get("sh")
        if sh_ns:
            SH = Namespace(sh_ns)
        else:
            # If not defined, return False (or raise an error as appropriate)
            return False
        for _, _, rdf_type in graph.triples((None, SH.targetClass, None)):
            if str(rdf_type) in used_types:
                return True
        return False

    for shacl_file in shacl_files:
        tmp_graph = Graph()
        tmp_graph.parse(shacl_file, format="turtle")
        if is_relevant(tmp_graph, used_types):
            shacl_graph += tmp_graph
            loaded_files.add(shacl_file)
            print(f"✅ Loaded SHACL file: {shacl_file}")

    from rdflib.namespace import OWL, RDFS

    for ontology_file in ontology_files:
        ontology_graph = Graph()
        ontology_graph.parse(ontology_file, format="turtle")
        defined_classes = set(ontology_graph.subjects(RDF.type, OWL.Class)).union(
            ontology_graph.subjects(RDF.type, RDFS.Class)
        )
        expanded_defined_classes = {str(cls) for cls in defined_classes}
        matched_types = expanded_defined_classes.intersection(used_types)
        if matched_types:
            shacl_graph += ontology_graph
            loaded_files.add(ontology_file)
            print(f"✅ Loaded ontology file: '{ontology_file}'")
    return shacl_graph


# --- Namespace Extraction and Used Types ---


def extract_namespace(rdf_type_str):
    if "://" not in rdf_type_str:
        prefix = rdf_type_str.split(":", 1)[0]
        return f"{prefix}:"
    else:
        parsed = urlparse(rdf_type_str)
        return f"{parsed.scheme}://{parsed.netloc}"


def extract_used_types(data_graph):
    used_types = defaultdict(set)
    for _, _, rdf_type in data_graph.triples((None, RDF.type, None)):
        rdf_type_str = str(rdf_type)
        namespace = extract_namespace(rdf_type_str)
        used_types[namespace].add(rdf_type_str)
    formatted_output = []
    for namespace, types in used_types.items():
        formatted_types = "\n    ".join(sorted(types))
        formatted_output.append(f"  - {namespace}:\n    {formatted_types}")
    print(
        f"✅ Extracted {sum(len(types) for types in used_types.values())} unique RDF types:\n"
        + "\n".join(formatted_output)
    )
    return {rdf_type for types in used_types.values() for rdf_type in types}


def load_jsonld_files(jsonld_files):
    """
    Loads JSON-LD files into an RDF graph and prints each file with its number.
    """
    data_graph = Graph()
    failed_files = 0
    for i, jsonld_file in enumerate(jsonld_files, start=1):
        try:
            data_graph.parse(jsonld_file, format="json-ld")
            print(f"✅ [{i}/{len(jsonld_files)}] Loaded: {jsonld_file}")
        except Exception as e:
            print(f"❌ [{i}/{len(jsonld_files)}] Failed: {jsonld_file} → {e}")
            failed_files += 1
    print(
        f"\n✅ Successfully loaded {len(jsonld_files) - failed_files}/{len(jsonld_files)} JSON-LD files."
    )
    return data_graph


def print_validation_result_wrapper(
    success: bool, onto_files: list = None, v_text: str = "", exit_code: int = None
):
    print_validation_result(success, onto_files, v_text, exit_code)


# --- Main Function ---


def main():
    debug = "--debug" in sys.argv
    if len(sys.argv) < 2:
        v_text = "Usage: python validate_jsonld_shacl.py [--debug] <directory or file> [additional files...]"
        print_validation_result_wrapper(False, None, v_text, exit_code=100)
    paths = [arg for arg in sys.argv[1:] if arg != "--debug"]
    setup_logging(debug)
    logging.info(f"Debug mode {'enabled' if debug else 'disabled'}.")

    # --- Dynamic Prefix Mapping ---
    # Use all ontology and JSON-LD files from the provided paths to build the mapping.
    files_for_prefixes = []
    for path in paths:
        if os.path.isdir(path):
            files_for_prefixes.extend(glob.glob(os.path.join(path, "*_ontology.ttl")))
            files_for_prefixes.extend(glob.glob(os.path.join(path, "*_instance.json")))
            files_for_prefixes.extend(glob.glob(os.path.join(path, "*_reference.json")))
        elif os.path.isfile(path):
            files_for_prefixes.append(path)
    dynamic_prefixes = load_dynamic_prefixes(files_for_prefixes)

    # Display the resolved dynamic prefixes
    print("\n✅ Resolved Dynamic Prefix Mapping:")
    for prefix, ns in sorted(dynamic_prefixes.items()):
        print(f"   {prefix}: {ns}")
    print()

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
            print(f"✅ Loading SHACL file for ontology: {shacl_file}")
            shacl_graph_onto.parse(shacl_file, format="turtle")
        else:
            print(
                f"⚠️ Warning: No SHACL file found for {onto_file}, skipping validation."
            )

    # --- Step 3: Validate each ontology.ttl against its SHACL graph ---
    for onto_file in ontology_files:
        print(f"🔍 Validating ontology {onto_file} against the SHACL shapes...")
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
            print_validation_result_wrapper(False, [onto_file], v_text, exit_code=200)
        else:
            print(f"✅ Ontology file {onto_file} passed SHACL validation.\n")

    # --- Step 4: Load JSON-LD Instance and Reference Files ---
    data_graph = Graph()
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

    # --- Step 5: Load JSON-LD files into data graph ---
    print("📌 Loading JSON-LD files into data graph...")
    data_graph = load_jsonld_files(instance_files + reference_files)

    # --- Step 6: Extract RDF Types from the Data Graph ---
    print("📌 Extracting RDF types from data graph...")
    used_types = extract_used_types(data_graph)

    # --- Step 7: Load only necessary SHACL shapes based on detected RDF types ---
    print("📌 Loading only necessary SHACL shapes based on detected RDF types...")
    shacl_graph = load_shacl_and_ontologies(".", used_types, dynamic_prefixes)

    # --- Step 8: Perform Final Validation ---
    print("🔍 Performing overall validation explicitly...")
    conforms, _, v_text = validate(
        data_graph, shacl_graph=shacl_graph, inference="rdfs", debug=debug
    )

    # --- Step 9: Print Validation Report ---
    if not conforms:
        print_validation_result_wrapper(False, instance_files, v_text, exit_code=210)
    else:
        print_validation_result_wrapper(True, instance_files, v_text, exit_code=None)


if __name__ == "__main__":
    main()
