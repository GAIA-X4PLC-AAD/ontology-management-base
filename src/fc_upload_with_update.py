import os
import requests
import rdflib
import sys
from typing import List, Optional
from urllib.parse import quote_plus
import authhelper.keycloakhandling

# ENVIRONMENT VARIABLES
ROOT_DIRECTORY = os.getcwd()
FOLDER_TO_UPLOAD = os.environ.get("FOLDER_TO_UPLOAD")
FEDERATED_CATALOGUE_URL = os.environ.get("FEDERATED_CATALOGUE_URL", default="https://fc-server.gxfs.gx4fm.org")
SCHEMA_ENDPOINT = f"{FEDERATED_CATALOGUE_URL}/schemas"


# FUNCTIONS
def main():
    """
    Main function to upload or update .ttl files by checking all existing schemas.
    """
    try:
        # Step 1: Get the auth header
        auth_header = authhelper.keycloakhandling.get_auth_header()

        # Step 2: Get all schemas (both ontologies and SHACL shapes)
        existing_schemas = get_all_schemas(auth_header)

        # Step 3: Process each ontology.ttl file
        for directory in next(os.walk(ROOT_DIRECTORY))[1]:
            if directory == FOLDER_TO_UPLOAD:
                full_directory_path = os.path.join(ROOT_DIRECTORY, directory)
                process_files(auth_header, existing_schemas, full_directory_path)

        print("All files processed successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")
        sys.exit(100)


def process_files(auth_header, existing_schemas, full_directory_path):
    """
    Process a single ontology Turtle file, determining if it should be created or updated.
    """
    execution = False
    for filename in os.listdir(full_directory_path):
        if filename.endswith("ontology.ttl"):
            full_filepath = os.path.join(full_directory_path, filename)
            with open(full_filepath, "r") as ontology_file:
                ontology_file_content = ontology_file.read()
                try:
                    process_ontology_file(auth_header, ontology_file_content, existing_schemas, full_directory_path)
                    execution = True
                except Exception as e:
                    print(f"Error at processing {filename}: {e}")
                    raise

    if not execution:
        raise RuntimeError("No files processed.")


def process_ontology_file(auth_header: dict, ontology_file_content: str, existing_schemas: dict, directory_path: str):
    """
    Process a single ontology Turtle file, determining if it should be created or updated.
    """
    ontology_graph_filesystem = rdflib.Graph()
    ontology_graph_filesystem.parse(data=ontology_file_content, format="turtle")

    # Extract the ontology name
    ontology_name = extract_ontology_name(ontology_graph_filesystem)
    if not ontology_name:
        raise ValueError(f"Ontology name not found in the file {directory_path}")

    # Check if the ontology exists in the catalogue
    ontology_graph_catalogue = find_existing_schema_graph(auth_header, ontology_name, existing_schemas)
    if ontology_graph_catalogue:
        print(f"Updating ontology: {ontology_name}")
        put_to_catalogue(auth_header, f"{SCHEMA_ENDPOINT}/{quote_plus(ontology_name)}", ontology_file_content)
        update_existing_shape(auth_header, ontology_name, ontology_graph_filesystem, ontology_graph_catalogue,
                              existing_schemas, directory_path)
    else:
        print(f"Creating new ontology: {ontology_name}")
        post_to_catalogue(auth_header, SCHEMA_ENDPOINT, ontology_file_content)
        add_shape(auth_header, ontology_name, ontology_graph_filesystem, directory_path)


def get_all_schemas(auth_header: dict):
    """
    Get all schemas (ontologies and SHACL shapes) from the catalogue.
    """
    response = requests.get(SCHEMA_ENDPOINT, headers=auth_header)
    if response.status_code != 200:
        raise requests.exceptions.RequestException(f"Failed to fetch schemas. Status code: {response.status_code}")
    return response.json()


def extract_ontology_name(graph: rdflib.Graph) -> Optional[str]:
    """
    Extract the ontology name from the RDF graph if it exists.
    Returns the ontology name or None.
    """
    query = """
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    SELECT ?ontology WHERE {
        ?ontology a owl:Ontology .
    }
    """
    results = graph.query(query)
    for row in results:
        return str(row.ontology)  # Return the ontology name as the ID
    return None


def extract_shape_target_classes(graph: rdflib.Graph) -> List[str]:
    """
    Extract all target classes from the top-level (!) SHACL shapes (shapes that are not used as sh:node).
    Returns a list of class URIs.
    """
    query = """
    PREFIX sh: <http://www.w3.org/ns/shacl#>
    SELECT ?targetClass WHERE {
        ?shape a sh:NodeShape ;
               sh:targetClass ?targetClass .
    }
    """
    results = graph.query(query)
    target_classes = [str(row.targetClass) for row in results]
    return target_classes


def find_existing_schema_graph(auth_header: dict, schema_id: str, existing_schemas: dict) -> Optional[rdflib.Graph]:
    """
   Find if a schema exists in the list of existing schemas by its ID.
   If it exists, fetch the schema details from catalogue. If not, return None.
   """
    if schema_id in existing_schemas.get("ontologies", []):
        response = get_schema_details(auth_header, schema_id)
        graph = rdflib.Graph()
        graph.parse(data=response, format="turtle")
        return graph
    return None


def find_corresponding_shapes_from_catalogue(auth_header: dict, ontology_graph: rdflib.Graph, existing_schemas: dict) \
        -> dict:
    """
    Find SHACL shapes that correspond to the given ontology.
    Returns a map of schema_id and shape_data.
    Raises an exception if more than one corresponding shape is found.
    """
    corresponding_shapes = {}
    ontology_name = extract_ontology_name(ontology_graph)
    for schema_id in existing_schemas.get("shapes", []):
        shape_data = get_schema_details(auth_header, schema_id)
        graph = rdflib.Graph()
        graph.parse(data=shape_data, format="turtle")
        shape_target_classes = extract_shape_target_classes(graph)

        if all_classes_exist_in_ontology(ontology_graph, shape_target_classes):
            corresponding_shapes[schema_id] = shape_data
            print(f"Found corresponding SHACL shape in catalogue: {schema_id} for ontology: {ontology_name}")
            print(f"SHACL shape content: {shape_data}")

    if not corresponding_shapes:
        raise ValueError("No corresponding shapes found in catalogue for {ontology_name}. Please update manually.")

    if len(corresponding_shapes) > 1:
        raise ValueError(f"Multiple corresponding shapes found in catalogue for {ontology_name}. "
                         f"IDs are {list(corresponding_shapes.keys())}. Please upload manually.")
    return corresponding_shapes


def find_corresponding_shapes_from_filesystem(ontology_graph: rdflib.Graph, directory_path: str) -> dict:
    """
    Find SHACL shapes that correspond to the given ontology from the filesystem.
    Returns a map of filename and shape_data.
    """
    corresponding_shapes = {}
    ontology_name = extract_ontology_name(ontology_graph)
    for filename in os.listdir(directory_path):
        if filename.endswith("shacl.ttl"):
            full_filepath = os.path.join(directory_path, filename)
            with open(full_filepath, "r") as shape_file:
                shape_data = shape_file.read()
                shape_graph = rdflib.Graph()
                shape_graph.parse(data=shape_data, format="turtle")
                shape_target_classes = extract_shape_target_classes(shape_graph)

                if all_classes_exist_in_ontology(ontology_graph, shape_target_classes):
                    corresponding_shapes[filename] = shape_data
                    print(f"Found corresponding local SHACL shape: {filename} for ontology: {ontology_name}")

    if not corresponding_shapes:
        raise ValueError("No corresponding shapes found in catalogue for {ontology_name}. Please check your SHACL "
                         "shapes or update manually.")

    if len(corresponding_shapes) > 1:
        raise ValueError(f"Multiple corresponding shapes found in filesystem for {ontology_name}. "
                         f"files are {list(corresponding_shapes.keys())}. Please upload manually.")
    return corresponding_shapes


def all_classes_exist_in_ontology(ontology_graph: rdflib.Graph, target_classes: List[str]) -> bool:
    """
    Check if all target classes exist in the ontology.
    """
    query = """
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    SELECT ?cls WHERE {
        ?cls a owl:Class .
    }
    """
    results = ontology_graph.query(query)
    ontology_classes = {str(row.cls) for row in results}

    return all(target_class in ontology_classes for target_class in target_classes)


def get_schema_details(auth_header: dict, schema_id: str) -> str:
    """
    Fetch the details of a schema by its ID.
    """
    response = requests.get(f"{SCHEMA_ENDPOINT}/{quote_plus(schema_id)}", headers=auth_header)
    if response.status_code != 200:
        raise requests.exceptions.RequestException(f"Failed to fetch schema details for ID: {schema_id}")
    return response.text  # Assuming Turtle format in the response


def add_shape(auth_header: dict, ontology_name: str, ontology_graph: rdflib.Graph, directory_path: str):
    """
    Add new SHACL shapes to the catalogue that correspond to the given ontology.
    """
    corresponding_shapes = find_corresponding_shapes_from_filesystem(ontology_graph, directory_path)
    for filename, shape_data in corresponding_shapes.items():
        post_to_catalogue(auth_header, SCHEMA_ENDPOINT, shape_data)
        print(f"Added new SHACL shape: {filename} for ontology: {ontology_name}")


def update_existing_shape(auth_header: dict, ontology_name: str, ontology_graph_filesystem: rdflib.Graph,
                          ontology_graph_catalogue: rdflib.Graph, existing_schemas: dict, directory_path: str):
    """
    Update existing SHACL shapes in the catalogue that correspond to the given ontology.
    """
    corresponding_shapes_from_catalogue = find_corresponding_shapes_from_catalogue(auth_header,
                                                                                   ontology_graph_catalogue,
                                                                                   existing_schemas)
    for shape_id, shape_data_catalogue in corresponding_shapes_from_catalogue.items():
        corresponding_shapes_from_filesystem = find_corresponding_shapes_from_filesystem(ontology_graph_filesystem,
                                                                                         directory_path)
        for filename, shape_data_filesystem in corresponding_shapes_from_filesystem.items():
            put_to_catalogue(auth_header, f"{SCHEMA_ENDPOINT}/{quote_plus(shape_id)}", shape_data_filesystem)
            print(f"Updated SHACL shape: {shape_id} for ontology: {ontology_name}")


def post_to_catalogue(auth_header: dict, endpoint: str, request_body: str) -> requests.Response:
    """Perform a HTTP-POST request on the Federated Catalogue"""
    print(f"Would have posted to {endpoint}: {request_body}")
    # auth_header["Content-Type"] = "text/turtle"
    # response = requests.post(endpoint, headers=auth_header, data=request_body)
    # if response.status_code not in [200, 201]:
    #     raise requests.exceptions.RequestException(f"Failed to POST data to {endpoint}. Status code: {response.status_code}")
    # print(f"Successfully posted to {endpoint}: {response.status_code}")
    # return response


def put_to_catalogue(auth_header: dict, endpoint: str, request_body: str) -> requests.Response:
    """Perform a HTTP-PUT request to update an existing schema in the Federated Catalogue"""
    print(f"Would have updated {endpoint}: {request_body}")
    # auth_header["Content-Type"] = "text/turtle"
    # response = requests.put(endpoint, headers=auth_header, data=request_body)
    # if response.status_code not in [200, 201]:
    #     raise requests.exceptions.RequestException(f"Failed to PUT data to {endpoint}. Status code: {response.status_code}")
    # print(f"Successfully updated {endpoint}: {response.status_code}")
    # return response


if __name__ == '__main__':
    main()
