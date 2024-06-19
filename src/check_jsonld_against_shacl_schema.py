# Python
import json
import sys
import glob
import os
from pyshacl import validate
from rdflib import Graph


def load_shacl_files(root_dir):
    shacl_graph = Graph()
    shacl_files = glob.glob(f'{root_dir}/**/*_shacl.ttl', recursive=True)
    for shacl_file in shacl_files:
        shacl_graph.parse(shacl_file, format='turtle')
    return shacl_graph


def load_jsonld_file(jsonld_file):
    data_graph = Graph()
    with open(jsonld_file) as f:
        data = json.load(f)
    data_graph.parse(data=data, format='json-ld')
    return data_graph


def validate_jsonld_against_shacl(data_graph, shacl_graph):
    conforms, v_graph, v_text = validate(data_graph, shacl_graph=shacl_graph, data_graph_format='json-ld', inference='rdfs', debug=False)
    print(f'Conforms: {conforms}')
    if not conforms:
        print('Validation errors:')
        print(v_text)
        print('Validation graph:')
        print(v_graph.serialize(format='turtle'))
        sys.exit(3)


def main():
    if len(sys.argv) != 2:
        print("Usage: python check_jsonld_against_shacl_schema.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"The directory {directory} does not exist. Abort.")
        sys.exit(2)

    jsonld_files = glob.glob(f'{directory}/*_instance.json')
    if not jsonld_files:
        print(f"No *_instance.json files found in directory: {directory}. Abort.")
        sys.exit(2)

    shacl_graph = load_shacl_files('.')

    for jsonld_file in jsonld_files:
        data_graph = load_jsonld_file(jsonld_file)
        validate_jsonld_against_shacl(data_graph, shacl_graph)


if __name__ == "__main__":
    main()
