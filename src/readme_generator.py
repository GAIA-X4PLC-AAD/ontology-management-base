import os
import rdflib

### ENVIRONMENT VARIABLES
# Define the directory from which to crawl directories for.ttl files (os.getcwd() for the current directory).
SHACL_DIRECTORY = os.getcwd()

### FUNCTIONS

def main():
    """
    The main function controls the overall program flow.
    It reads .ttl files, extracts RDF graphs, sh:path attributes, and appends them to VARIABLES.md files.
    """
    # Iterate through the first level of all directories in the current directory except for "src".
    for directory in next(os.walk(SHACL_DIRECTORY))[1]:
        if directory == "src":
            continue

        # Initialize the needed variables.
        full_directory_path = os.path.join(SHACL_DIRECTORY, directory)
        variables_file = os.path.join(full_directory_path, "VARIABLES.md")
        shacl_paths = []  

        # Extract SHACL Properties (paths) from all .ttl files in the directory and store them in shacl_paths 
        for filename in os.listdir(full_directory_path):
            if filename.endswith(".ttl"):
                file_path = os.path.join(full_directory_path, filename)
                rdf_graph = extract_rdf_graph_from_ttl(file_path)
                shacl_paths.extend(extract_shacl_paths(rdf_graph))

        # Sort SHACL paths alphabetically and create the VARIABLES.md file.
        if shacl_paths:
            sorted_uris = sorted(shacl_paths)
            with open(variables_file, "w") as file:
                file.write("# List of IRIs:\n")
                for uri in sorted_uris:
                    file.write(f"- {uri}\n")
            print(f"Appended to VARIABLES.md in {full_directory_path}")

def extract_shacl_paths(rdf_graph):
    """
    Extracts sh:path attributes from an RDF graph.

    :param rdf_graph: An RDF graph.
    :return: A list of sh:path values.
    """
    path_list = []

    # SPARQL query to extract sh:path values.
    query = """
    PREFIX sh: <http://www.w3.org/ns/shacl#>
    
    SELECT ?path
    WHERE {
      ?shape a sh:NodeShape .
      ?shape sh:property ?property .
      ?property sh:path ?path .
    }
    """

    results = rdf_graph.query(query)

    for row in results:
        path_list.append(row.path)

    return path_list

def extract_rdf_graph_from_ttl(file_path) -> rdflib.Graph:
    """
    Extracts an RDF graph from a .ttl file.

    :param file_path: The path to the .ttl file.
    :return: An RDF graph.
    """
    rdf_graph = rdflib.Graph()
    rdf_graph.parse(file_path, format='ttl')
    return rdf_graph

if __name__ == '__main__':
    main()
