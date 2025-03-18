import glob
import logging
import os
import sys
import textwrap
from collections import defaultdict
from urllib.parse import urlparse

from pyshacl import validate
from rdflib import RDF, Graph, Namespace

# Global standard prefixes
STANDARD_PREFIXES = {
    "owl": "http://www.w3.org/2002/07/owl#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "dcterms": "http://purl.org/dc/terms/",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "org": "http://www.w3.org/ns/org#",
    "prov": "http://www.w3.org/ns/prov#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "sh": "http://www.w3.org/ns/shacl#",  # ✅ Add this line
    # Force redirect gx: to the local repo
    "gx": "https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/gx/",
}


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

    # Define breakpoints for logical sectioning
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

    # Ensure each important section starts on a new line
    for bp in breakpoints:
        v_text = v_text.replace(bp, f"\n{bp}")

    # Process line-by-line
    indent_level = 0
    last_line_was_blank = False
    for line in v_text.splitlines():
        stripped_line = line.strip()

        # Ensure empty lines start and end with "="
        if not stripped_line:
            if last_line_was_blank:
                continue  # Prevent multiple blank lines in a row
            last_line_was_blank = True
            formatted_lines.append(f"= {' ' * (width - 4)} =")
            continue
        else:
            last_line_was_blank = False

        # Detect section headers and adjust indentation levels
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

        # Apply indentation and wrap lines
        indent_space = " " * (indent_level * indent_size)
        wrapped_lines = textwrap.fill(
            stripped_line, width=width - 4 - len(indent_space)
        )

        # Apply left-padding and format each line
        for wrapped_line in wrapped_lines.split("\n"):
            formatted_lines.append(
                f"= {indent_space}{wrapped_line.ljust(width - 4 - len(indent_space))} ="
            )

    return f"{border_line}\n" + "\n".join(formatted_lines) + f"\n{border_line}"


def format_filenames(filenames: list, width: int = 150) -> list:
    """
    Splits the filenames list at ", '" ensuring filenames remain intact.
    Ensures each filename starts on a new line properly formatted.
    """
    formatted_lines = []
    current_line = "["

    for i, file in enumerate(filenames):
        if i > 0:
            current_line += ", "  # Properly format the separator

        if (
            len(current_line) + len(file) + 2 >= width - 4
        ):  # Check if adding this file exceeds width
            formatted_lines.append(f"{current_line}")
            current_line = (
                "  " + file
            )  # Indent next line slightly for better readability
        else:
            current_line += f"'{file}'"

    formatted_lines.append(f"{current_line}]")  # Close the list correctly
    return formatted_lines


def print_validation_result(
    success: bool, onto_files: list = None, v_text: str = "", exit_code: int = None
):
    width = 150
    border_line = "=" * width
    header_text_files = [""]

    # Construct a flexible, center-aligned header
    if success:
        header_text = ["✅ SHACL validation passed for:"]
    else:
        header_text = ["❌ SHACL validation failed for:"]

    # Center-align the header and handle line breaks properly
    centered_header_lines = [f"= {line.center(width - 5)} =" for line in header_text]

    if onto_files:
        formatted_filenames = format_filenames(onto_files, width)
        header_text_files.extend(formatted_filenames)
        centered_header_file_lines = [
            f"= {line.center(width - 4)} =" for line in header_text_files
        ]

    # Print the header
    print(border_line)
    print("\n".join(centered_header_lines))
    print("\n".join(centered_header_file_lines))
    print(border_line)

    if not success:
        # Use `format_validation_report()` without overriding it again
        formatted_v_text = format_validation_report(v_text, width)
        print(formatted_v_text, file=sys.stderr)

    # Exit only if an exit_code is provided
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


def load_shacl_and_ontologies(root_dir, used_types):
    """Loads SHACL and ontology files relevant to the detected RDF types."""
    shacl_graph = Graph()
    loaded_files = set()

    # Bind standard prefixes
    for prefix, namespace in STANDARD_PREFIXES.items():
        shacl_graph.bind(prefix, Namespace(namespace))

    # Load GX trust framework SHACL explicitly (as before)
    namespace_gx = {"gx": os.path.join(root_dir, "gx", "gx_shacl.ttl")}
    for prefix, file_path in namespace_gx.items():
        print(f"✅ Loading mapped SHACL file for {prefix}: {file_path}")
        shacl_graph.parse(file_path, format="turtle")
        loaded_files.add(file_path)

    # Gather SHACL files
    shacl_files = glob.glob(f"{root_dir}/**/*_shacl.ttl", recursive=True)
    ontology_files = glob.glob(f"{root_dir}/**/*_ontology.ttl", recursive=True)

    # Function to load relevant files based on used_types
    def is_relevant(graph, used_types):
        SH = Namespace(STANDARD_PREFIXES["sh"])
        for _, _, rdf_type in graph.triples((None, SH.targetClass, None)):
            if str(rdf_type) in used_types:
                return True
        return False

    # Load relevant SHACL files
    for shacl_file in shacl_files:
        tmp_graph = Graph()
        tmp_graph.parse(shacl_file, format="turtle")
        if is_relevant(tmp_graph, used_types):
            shacl_graph += tmp_graph
            loaded_files.add(shacl_file)
            print(f"✅ Loaded SHACL file: {shacl_file}")

    # Load relevant Ontology files (robust and verified solution)
    OWL = Namespace(STANDARD_PREFIXES["owl"])
    RDFS = Namespace(STANDARD_PREFIXES["rdfs"])

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


def resolve_prefixed_type(json_type, context):
    """Resolves prefixed RDF types to full IRIs using global prefixes."""
    full_context = context.copy() if context else {}
    for prefix, namespace in STANDARD_PREFIXES.items():
        full_context.setdefault(prefix, namespace)  # Add only if missing

    if ":" in json_type:
        prefix, suffix = json_type.split(":", 1)
        base_iri = full_context.get(prefix)
        if base_iri:
            return f"{base_iri}{suffix}"
    return json_type


def extract_used_types(data_graph):
    """Extracts all unique RDF types used in the JSON-LD data graph, grouped by namespace for better readability."""
    used_types = defaultdict(set)  # Use a set to store unique values per namespace

    for _, _, rdf_type in data_graph.triples((None, RDF.type, None)):
        rdf_type_str = str(rdf_type)
        namespace = (
            urlparse(rdf_type_str).scheme + "://" + urlparse(rdf_type_str).netloc
        )  # Extract domain
        used_types[namespace].add(rdf_type_str)  # Store unique values only

    # Format output for better readability with newlines
    formatted_output = []
    for namespace, types in used_types.items():
        formatted_types = "\n    ".join(sorted(types))  # Sort for consistent order
        formatted_output.append(f"  - {namespace}:\n    {formatted_types}")

    print(
        f"✅ Extracted {sum(len(types) for types in used_types.values())} unique RDF types:\n{''.join(formatted_output)}"
    )

    return {rdf_type for types in used_types.values() for rdf_type in types}


def load_jsonld_files(jsonld_files):
    """Loads JSON-LD files into an RDF graph and prints each file with its number."""
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


def main():
    debug = "--debug" in sys.argv

    if len(sys.argv) < 2:
        v_text = "Usage: python validate_jsonld_shacl.py [--debug] <directory or file> [additional files...]"
        print_validation_result(False, None, v_text, exit_code=100)

    paths = [arg for arg in sys.argv[1:] if arg != "--debug"]

    setup_logging(debug)

    logging.info(f"Debug mode {'enabled' if debug else 'disabled'}.")

    # Step 1: Collect all *ontology.ttl files
    ontology_files = []
    for path in paths:
        if os.path.isdir(path):
            ontology_files.extend(glob.glob(os.path.join(path, "*_ontology.ttl")))
        elif os.path.isfile(path) and path.endswith("_ontology.ttl"):
            ontology_files.append(path)

    # Step 2: Load corresponding SHACL files
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

    # Step 3: Validate each ontology.ttl against its SHACL graph
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
            print_validation_result(False, onto_file, v_text, exit_code=200)
        else:
            print(f"✅ Ontology file {onto_file} passed SHACL validation.\n")

    # Step 4: Load JSON-LD Instance and Reference Files
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

    # ✅ Step 5: Load JSON-LD files FIRST
    print("📌 Loading JSON-LD files into data graph...")
    data_graph = load_jsonld_files(instance_files + reference_files)

    # ✅ Step 6: Now Extract RDF Types From the Loaded Data Graph
    print("📌 Extracting RDF types from data graph...")
    used_types = extract_used_types(data_graph)

    # ✅ Step 7: Load only necessary SHACL shapes based on detected RDF types
    print("📌 Loading only necessary SHACL shapes based on detected RDF types...")
    shacl_graph = load_shacl_and_ontologies(".", used_types)

    # ✅ Step 8: Perform Final Validation
    print("🔍 Performing overall validation explicitly...")
    conforms, _, v_text = validate(
        data_graph, shacl_graph=shacl_graph, inference="rdfs", debug=debug
    )

    # ✅ Step 9: Print Validation Report
    if not conforms:
        print_validation_result(False, instance_files, v_text, exit_code=210)
    else:
        print_validation_result(True, instance_files, v_text, exit_code=None)


if __name__ == "__main__":
    main()
