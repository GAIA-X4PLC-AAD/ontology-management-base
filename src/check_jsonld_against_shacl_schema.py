import sys
import glob
import os
import json
from rdflib import Graph, URIRef, Namespace
from pyshacl import validate


def resolve_prefixed_type(json_type, context):
    """Converts a prefixed type like 'manifest:Manifest' to a full IRI."""
    if ":" in json_type:
        prefix, suffix = json_type.split(":", 1)
        base_iri = context.get(prefix)
        if base_iri:
            return f"{base_iri}{suffix}"
    return json_type  # Return as-is if it's already a full IRI


def load_shacl_files(root_dir):
    """Loads all SHACL files and extracts shape mappings based on sh:targetClass."""
    shacl_graph = Graph()
    shape_mappings = {}

    shacl_files = glob.glob(f'{root_dir}/**/*_shacl.ttl', recursive=True)
    for shacl_file in shacl_files:
        shacl_graph.parse(shacl_file, format='turtle')

    SH = Namespace("http://www.w3.org/ns/shacl#")
    for s, p, o in shacl_graph.triples((None, SH.targetClass, None)):
        if str(o) not in shape_mappings:
            shape_mappings[str(o)] = []  # Initialize as list
        shape_mappings[str(o)].append(str(s))  # Append to list

    return shacl_graph, shape_mappings


def load_jsonld_files(jsonld_files):
    data_graph = Graph()
    for jsonld_file in jsonld_files:
        print(f'Adding JSON-LD file to data graph: {jsonld_file}')
        data_graph.parse(jsonld_file, format='json-ld')
    return data_graph


def explicitly_validate_references(data_graph, shacl_graph, reference_files, shape_mappings):
    failed_validations = []

    for ref_file in reference_files:
        filename = os.path.basename(ref_file)

        with open(ref_file, 'r') as f:
            json_data = json.load(f)
            manifest_id = json_data.get('@id')
            json_type = json_data.get("@type", "")

        if not manifest_id:
            print(f'No explicit "@id" found in {ref_file}, skipping validation.')
            continue

        context = json_data.get("@context", {})
        full_type = resolve_prefixed_type(json_type, context)

        shape_uris = shape_mappings.get(full_type, [])  # Get all matching shapes
        if not shape_uris:
            print(f'No SHACL shape found for {filename} (Type: {json_type} resolved as {full_type}), skipping validation.')
            continue

        focus_node = URIRef(manifest_id)

        for shape_uri_str in shape_uris:
            target_shape_uri = URIRef(shape_uri_str)

            print(f'Explicitly validating {filename} against shape {target_shape_uri}')
            conforms, _, v_text = validate(
                data_graph,
                shacl_graph=shacl_graph,
                inference='rdfs',
                debug=False,
                focus=focus_node,
                target_shape=target_shape_uri
            )
            if not conforms:
                failed_validations.append((conforms, filename, v_text))

    return failed_validations


def main():
    if len(sys.argv) < 2:
        print('Usage: python validate_jsonld_shacl.py <directory or file> [additional files...]')
        sys.exit(1)

    paths = sys.argv[1:]  # Accept multiple file paths

    print('Loading all SHACL shapes into shacle graph and create shape mappings...')
    shacl_graph, shape_mappings = load_shacl_files('.')

    data_graph = Graph()
    instance_files = []
    reference_files = []
    skip_overall = False

    # Process multiple files
    for path in paths:
        if os.path.isdir(path):
            print(f'Loading JSON-LD files from directory: {path}')
            instance_files.extend(glob.glob(f'{path}/*_instance.json'))
            reference_files.extend(glob.glob(f'{path}/*_reference.json'))
        elif os.path.isfile(path):
            print(f'Loading single JSON-LD file: {path}')
            if path.endswith("_instance.json"):
                instance_files.append(path)
            elif path.endswith("_reference.json"):
                reference_files.append(path)
        else:
            print(f'Error: {path} is neither a file nor a directory.')
            sys.exit(1)

    if instance_files or reference_files:
        data_graph = load_jsonld_files(instance_files + reference_files)

    failed_validations = []

    if reference_files:
        failed_validations = explicitly_validate_references(data_graph, shacl_graph, reference_files, shape_mappings)

        # Stop execution if explicit validation already failed
        for conforms, _, v_text in failed_validations:
            if not conforms:
                print("$$_$$")
                print(v_text)
                skip_overall = True

    if not skip_overall:
        print('Performing overall validation explicitly...')
        conforms, _, v_text = validate(
            data_graph,
            shacl_graph=shacl_graph,
            inference='rdfs',
            debug=False
        )

        if not conforms:
            print("$$_$$")
            print(v_text)

if __name__ == "__main__":
    main()
