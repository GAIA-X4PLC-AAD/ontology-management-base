import os
import requests
import rdflib
import sys
from typing import List
from typing import Optional
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

    # Step 1: Get the auth header
    auth_header = authhelper.keycloakhandling.get_auth_header()

    # Step 2: Get all schemas (both ontologies and SHACL shapes)
    existing_schemas = get_all_schemas(auth_header)

    execution = False

    # Step 3: Process each .ttl file
    for directory in next(os.walk(ROOT_DIRECTORY))[1]:
        if directory == FOLDER_TO_UPLOAD:
            full_directory_path = os.path.join(ROOT_DIRECTORY, directory)
            for filename in os.listdir(full_directory_path):
                full_filepath = os.path.join(full_directory_path, filename)
                if filename.endswith(".ttl"):
                    with open(full_filepath, "r") as new_turtle_file:
                        new_turtle_file_text = new_turtle_file.read()
                        try:
                            process_turtle_file(auth_header, new_turtle_file_text, existing_schemas)
                            execution = True
                        except Exception as e:
                            print(f"Error processing {filename}: {e}")
                            sys.exit(100)

    if execution:
        print("All files processed successfully.")
    else:
        print("No files processed.")
        sys.exit(101)


def get_all_schemas(auth_header: dict):
    """
    Get all schemas (ontologies and SHACL shapes) from the catalogue.
    """
    response = requests.get(SCHEMA_ENDPOINT, headers=auth_header)

    if response.status_code != 200:
        raise requests.exceptions.RequestException(f"Failed to fetch schemas. Status code: {response.status_code}")

    return response.json()


def process_turtle_file(auth_header: dict, turtle_data: str, existing_schemas: dict):
    """
    Process a single Turtle file, determining if it should be created or updated.
    """
    graph = rdflib.Graph()
    graph.parse(data=turtle_data, format="turtle")

    # Determine if it's an ontology or SHACL shape
    ontology_name = extract_ontology_name(graph)
    shape_target_classes = extract_shape_target_classes(graph)

    if ontology_name:
        # This is an ontology
        handle_ontology(auth_header, ontology_name, turtle_data, existing_schemas)
    elif shape_target_classes:
        # This is a SHACL shape
        handle_shape(auth_header, shape_target_classes, turtle_data, existing_schemas)
    else:
        raise ValueError("Unknown schema type - neither ontology nor SHACL shape.")


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
        FILTER NOT EXISTS {
            ?parentShape sh:property ?property .
            ?property (sh:node|sh:path) ?shape .
        }
    }
    """
    results = graph.query(query)
    target_classes = [str(row.targetClass) for row in results]
    return target_classes


def handle_ontology(auth_header: dict, ontology_name: str, turtle_data: str, existing_schemas: dict):
    """
    Handle the upload or update of an ontology.
    """
    schema_id = find_existing_schema(ontology_name, existing_schemas)

    if schema_id:
        print(f"Updating ontology: {ontology_name}")
        put_to_catalogue(auth_header, f"{SCHEMA_ENDPOINT}/{schema_id}", turtle_data)
    else:
        print(f"Creating new ontology: {ontology_name}")
        post_to_catalogue(auth_header, SCHEMA_ENDPOINT, turtle_data)


def handle_shape(auth_header: dict, target_classes: List[str], turtle_data: str, existing_schemas: dict):
    """
    Handle the upload or update of a SHACL shape.
    """
    # Step 1: Find the ontology the SHACL shape refers to
    ontology_name = find_corresponding_ontology(auth_header, target_classes, existing_schemas)

    if not ontology_name:
        raise ValueError(f"No matching ontology found for target classes: {target_classes}")

    # Step 2: Verify that the SHACL shape exists
    shape_id = find_existing_schema_by_target_classes(auth_header, target_classes, existing_schemas)

    if shape_id:
        print(f"Updating SHACL shape for target classes: {target_classes}")
        put_to_catalogue(auth_header, f"{SCHEMA_ENDPOINT}/{shape_id}", turtle_data)
    else:
        print(f"Creating new SHACL shape for target classes: {target_classes}")
        post_to_catalogue(auth_header, SCHEMA_ENDPOINT, turtle_data)


def find_corresponding_ontology(auth_header: dict, target_classes: List[str], existing_schemas: dict) -> Optional[str]:
    """
    Find the ontology that corresponds to the SHACL shape's targetClass.
    Returns the ontology name or None.
    """
    for schema in existing_schemas.get("ontologies", []):
        ontology_data = get_schema_details(auth_header, schema)
        graph = rdflib.Graph()
        graph.parse(data=ontology_data, format="turtle")

        # Check if the target class exists in the ontology
        if check_if_classes_in_ontology(target_classes, graph):
            return schema

    return None


def check_if_classes_in_ontology(target_classes: List[str], ontology_graph: rdflib.Graph) -> bool:
    """
        Check if all classes in target_classes exist in the ontology.
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


def find_existing_schema(schema_id: str, existing_schemas: dict) -> str:
    """
    Find if a schema exists in the list of existing schemas by its ID.
    """
    return schema_id if schema_id in existing_schemas.get("ontologies", []) else None


def find_existing_schema_by_target_classes(auth_header: dict, target_classes: List[str], existing_schemas: dict) -> Optional[str]:
    """
    Find if a SHACL shape exists based on its targetClasses.
    """
    for schema in existing_schemas.get("shapes", []):
        shape_data = get_schema_details(auth_header, schema)
        graph = rdflib.Graph()
        graph.parse(data=shape_data, format="turtle")
        extracted_target_classes = extract_shape_target_classes(graph)
        if set(extracted_target_classes) == set(target_classes):
            return schema
    return None


def get_schema_details(auth_header: dict, schema_id: str) -> str:
    """
    Fetch the details of a schema by its ID.
    """
    response = requests.get(f"{SCHEMA_ENDPOINT}/{schema_id}", headers=auth_header)

    if response.status_code != 200:
        raise requests.exceptions.RequestException(f"Failed to fetch schema details for ID: {schema_id}")

    return response.text  # Assuming Turtle format in the response


def post_to_catalogue(auth_header: dict, endpoint: str, request_body: str) -> requests.Response:
    """Perform a HTTP-POST request on the Federated Catalogue"""

    print(f"Would have posted to {endpoint}: {request_body}")

#    auth_header["Content-Type"] = "text/turtle"

#    response = requests.post(endpoint, headers=auth_header, data=request_body)

#    if response.status_code not in [200, 201]:
#        raise requests.exceptions.RequestException(f"Failed to POST data to {endpoint}. Status code: {response.status_code}")

#    print(f"Successfully posted to {endpoint}: {response.status_code}")
#    return response


def put_to_catalogue(auth_header: dict, endpoint: str, request_body: str) -> requests.Response:
    """Perform a HTTP-PUT request to update an existing schema in the Federated Catalogue"""

    print(f"Would have updated {endpoint}: {request_body}")

#    auth_header["Content-Type"] = "text/turtle"

#    response = requests.put(endpoint, headers=auth_header, data=request_body)

#    if response.status_code not in [200, 201]:
#        raise requests.exceptions.RequestException(f"Failed to PUT data to {endpoint}. Status code: {response.status_code}")

#    print(f"Successfully updated {endpoint}: {response.status_code}")
#    return response


if __name__ == '__main__':
    main()
