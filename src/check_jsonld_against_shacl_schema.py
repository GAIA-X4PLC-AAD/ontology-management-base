import glob
import logging
import os
import sys
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
    # Force redirect gx: to the local repo
    "gx": "https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/gx/",
}


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


def load_shacl_files(root_dir, used_types):
    """Loads only SHACL files relevant to the detected RDF types."""
    shacl_graph = Graph()
    loaded_shacl_files = set()

    # Bind standard prefixes
    for prefix, namespace in STANDARD_PREFIXES.items():
        shacl_graph.bind(prefix, Namespace(namespace))

    # Always load mapped SHACL files (e.g., gx)
    namespace_mapping = {"gx": os.path.join(root_dir, "gx/gx_shacl.ttl")}
    for prefix, local_path in namespace_mapping.items():
        if os.path.exists(local_path):
            print(f"✅ Loading mapped SHACL file for {prefix}: {local_path}")
            shacl_graph.parse(local_path, format="turtle")

    # Load only SHACL files relevant to used RDF types
    shacl_files = glob.glob(f"{root_dir}/**/*_shacl.ttl", recursive=True)

    for shacl_file in shacl_files:
        if shacl_file in namespace_mapping.values():
            continue  # Already loaded manually

        temp_graph = Graph()
        temp_graph.parse(shacl_file, format="turtle")

        SH = Namespace("http://www.w3.org/ns/shacl#")
        file_is_relevant = False

        for _, _, rdf_type in temp_graph.triples((None, SH.targetClass, None)):
            rdf_type_str = str(rdf_type)
            if rdf_type_str in used_types:
                file_is_relevant = True
                break  # No need to continue if at least one match is found

        # ✅ Load the SHACL file only if it constrains at least one used RDF type
        if file_is_relevant:
            shacl_graph += temp_graph
            loaded_shacl_files.add(shacl_file)
            print(f"✅ Loaded SHACL file: {os.path.basename(shacl_file)}")

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
        print(
            "Usage: python validate_jsonld_shacl.py [--debug] <directory or file> [additional files...]"
        )
        sys.exit(1)

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
            onto_graph, shacl_graph=shacl_graph_onto, inference="owlrl", debug=debug
        )
        if not conforms:
            print(f"❌ Failed SHACL validation for {onto_file}!")
            print(v_text)
            sys.exit(2)
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
    shacl_graph = load_shacl_files(".", used_types)

    # ✅ Step 8: Perform Final Validation
    print("🔍 Performing overall validation explicitly...")
    conforms, _, v_text = validate(
        data_graph, shacl_graph=shacl_graph, inference="rdfs", debug=debug
    )

    # ✅ Step 9: Print Validation Report
    print("========== VALIDATION REPORTS ==========")
    if not conforms:
        print(v_text)
    else:
        print("=              No failures             =")
    print("========================================")


if __name__ == "__main__":
    main()
