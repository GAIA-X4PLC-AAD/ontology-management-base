import sys
import glob
import os
import json
from rdflib import Graph, URIRef
from pyshacl import validate

# Explicit mapping of reference JSON files to SHACL shape URIs
SHAPE_URI_MAPPING = {
    'manifest_reference.json': "https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/general/ExtendedManifestShape",
    'hdmap_reference.json': "https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/hdmap/HDMapExtendedShape",
    # Add further mappings explicitly as needed
}

def load_shacl_files(root_dir):
    shacl_graph = Graph()
    shacl_files = glob.glob(f'{root_dir}/**/*_shacl.ttl', recursive=True)
    for shacl_file in shacl_files:
        print(f'Loading SHACL file: {shacl_file}')
        shacl_graph.parse(shacl_file, format='turtle')
    return shacl_graph

def load_jsonld_files(jsonld_files):
    data_graph = Graph()
    for jsonld_file in jsonld_files:
        print(f'Adding JSON-LD file to data graph: {jsonld_file}')
        data_graph.parse(jsonld_file, format='json-ld')
    return data_graph

def explicitly_validate_references(data_graph, shacl_graph, reference_files):
    for ref_file in reference_files:
        filename = os.path.basename(ref_file)
        shape_uri_str = SHAPE_URI_MAPPING.get(filename)

        if not shape_uri_str:
            print(f'No explicit SHACL shape mapping found for {filename}, skipping validation.')
            continue

        with open(ref_file, 'r') as f:
            json_data = json.load(f)
            manifest_id = json_data.get('@id')

        if not manifest_id:
            print(f'No explicit "@id" found in {ref_file}, skipping validation.')
            continue

        focus_node = URIRef(manifest_id)
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

        print(f'Validation result explicitly for {filename}: Conforms={conforms}')
        if not conforms:
            print(v_text)

def main():
    if len(sys.argv) != 2:
        print('Usage explicitly: python validate_jsonld_shacl.py <directory>')
        sys.exit(1)

    directory = sys.argv[1]

    print('Loading SHACL shapes explicitly...')
    shacl_graph = load_shacl_files('.')

    print('Loading JSON-LD files explicitly...')
    instance_files = glob.glob(f'{directory}/*_instance.json')
    reference_files = glob.glob(f'{directory}/*_reference.json')
    data_graph = load_jsonld_files(instance_files + reference_files)

    if reference_files:
        explicitly_validate_references(data_graph, shacl_graph, reference_files)

    print('Performing overall validation explicitly...')
    conforms, _, v_text = validate(
        data_graph,
        shacl_graph=shacl_graph,
        inference='rdfs',
        debug=False
    )

    print(f'Overall validation explicitly: Conforms={conforms}')
    if not conforms:
        print(v_text)

if __name__ == "__main__":
    main()
