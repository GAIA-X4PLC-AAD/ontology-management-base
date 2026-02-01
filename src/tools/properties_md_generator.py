import os

import rdflib

# ENVIRONMENT PROPERTIES
# Define the directories for the new repository structure
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARTIFACTS_DIRECTORY = os.path.join(ROOT_DIR, "artifacts")


def main():
    """
    The main function controls the overall program flow.
    It reads SHACL .ttl files from artifacts/{domain}/, extracts properties,
    and writes PROPERTIES.md files to artifacts/{domain}/.
    """
    # Ensure artifacts directory exists
    if not os.path.isdir(ARTIFACTS_DIRECTORY):
        print(f"Artifacts directory not found: {ARTIFACTS_DIRECTORY}")
        return

    # Iterate through ontology directories
    ontology_dirs = [
        d
        for d in os.listdir(ARTIFACTS_DIRECTORY)
        if os.path.isdir(os.path.join(ARTIFACTS_DIRECTORY, d))
    ]

    for domain in sorted(ontology_dirs):
        domain_dir = os.path.join(ARTIFACTS_DIRECTORY, domain)
        shacl_file_name = f"{domain}.shacl.ttl"
        shacl_file_path = os.path.join(domain_dir, shacl_file_name)

        # Skip if SHACL file doesn't exist
        if not os.path.exists(shacl_file_path):
            continue

        properties_file = os.path.join(domain_dir, "PROPERTIES.md")

        # Extract SHACL properties
        file_path = shacl_file_path
        rdf_graph = extract_rdf_graph_from_ttl(file_path)
        shacl_properties = extract_shacl_properties(rdf_graph, shacl_file_name)

        # Extract relevant prefixes
        relevant_prefixes = set()
        for prop in shacl_properties:
            for prefix, namespace in rdf_graph.namespaces():
                if prop["path"].startswith(namespace):
                    relevant_prefixes.add((namespace, prefix))
                if prop["shape"].startswith(namespace):
                    relevant_prefixes.add((namespace, prefix))

        # Convert set of relevant prefixes to a dictionary
        extracted_prefixes = {
            namespace: prefix for namespace, prefix in relevant_prefixes
        }

        # Write extracted property details to PROPERTIES.md file
        if shacl_properties:
            with open(properties_file, "w") as file:
                # Write headline
                file.write(f"# Properties of SHACL Files for {domain}\n\n")

                # Write prefixes above the table
                if extracted_prefixes:
                    file.write("## Prefixes\n\n")
                    for namespace, prefix in sorted(
                        extracted_prefixes.items(), key=lambda x: x[1]
                    ):
                        file.write(f"- {prefix}: <{namespace}>\n")
                    file.write("\n")

                # Write table header
                file.write("## List of SHACL Properties\n\n")
                file.write(
                    "| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |\n"
                )
                file.write("| --- | --- | --- | --- | --- | --- | --- | --- |\n")

                for prop in shacl_properties:
                    # Replace IRIs with prefixes
                    for namespace, prefix in extracted_prefixes.items():
                        if prop["path"].startswith(namespace):
                            prop["path"] = prop["path"].replace(namespace, "")
                            prop["prefix"] = prefix
                        if prop["shape"].startswith(namespace):
                            prop["shape"] = prop["shape"].replace(namespace, "")

                    # Handling empty or None values explicitly
                    prefix_of_path = (
                        prop["prefix"]
                        if "prefix" in prop and prop["prefix"] is not None
                        else ""
                    )
                    min_count = prop["minCount"] if prop["minCount"] is not None else ""
                    max_count = prop["maxCount"] if prop["maxCount"] is not None else ""
                    description = (
                        prop["description"] if prop["description"] is not None else ""
                    )
                    if prop["datatype"] is not None:
                        datatype_or_nodekind = "<" + str(prop["datatype"]) + ">"
                    elif prop["nodeKind"] is not None:
                        datatype_or_nodekind = "<" + str(prop["nodeKind"]) + ">"
                    else:
                        datatype_or_nodekind = ""

                    file.write(
                        f"| {prop['shape']} | {prefix_of_path} | {prop['path']} | {min_count} | {max_count} | {description} | {datatype_or_nodekind} | {prop['filename']} "
                        f"|\n"
                    )

            print(f"Generated PROPERTIES.md for {domain} in {domain_dir}")


def extract_prefixes(rdf_graph):
    """
    Extracts prefixes used in the RDF graph.

    :param rdf_graph: An RDF graph.
    :return: A dictionary of prefixes.
    """
    prefixes = {}
    for prefix, namespace in rdf_graph.namespaces():
        prefixes[namespace] = prefix
    return prefixes


def replace_with_prefix(uri, prefixes):
    """
    Replaces the URI with its prefixed form using extracted prefixes.

    :param uri: URI to be replaced.
    :param prefixes: Dictionary of prefixes.
    :return: Prefixed form of the URI if a match is found, else the original URI.
    """
    for namespace, prefix in prefixes.items():
        if uri.startswith(namespace):
            return uri.replace(namespace, f"{prefix}:")
    return uri


def extract_shacl_properties(rdf_graph, insertion_filename=None) -> list[dict]:
    """
    Extracts properties including sh:path, sh:minCount, sh:maxcount, sh:description,
    sh:datatype, sh:nodekind, and sh:in from an RDF graph.

    :param rdf_graph: An RDF graph.
    :param insertion_filename The corresponding filename.
    :return: A list of dictionaries containing property details.
    """
    properties_list = []

    # SPARQL query to extract property details.
    query = """
    PREFIX sh: <http://www.w3.org/ns/shacl#>

    SELECT ?shape ?path ?minCount ?maxCount ?description ?datatype ?nodeKind ?in
    WHERE {
      ?shape a sh:NodeShape .
      ?shape sh:property ?property .
      ?property sh:path ?path .
      OPTIONAL { ?property sh:minCount ?minCount }
      OPTIONAL { ?property sh:maxCount ?maxCount }
      OPTIONAL { ?property sh:description ?description }
      OPTIONAL { ?property sh:datatype ?datatype }
      OPTIONAL { ?property sh:nodeKind ?nodeKind }
      OPTIONAL { ?property sh:in ?in }
    }
    """

    results = rdf_graph.query(query)

    for row in results:
        property_details = {
            "shape": row.shape,
            "path": row.path,
            "minCount": row.minCount,
            "maxCount": row.maxCount,
            "description": row.description,
            "datatype": row.datatype,
            "nodeKind": row.nodeKind,
            "in": getattr(row, "in", None),
        }
        if insertion_filename:
            property_details["filename"] = insertion_filename
        properties_list.append(property_details)

    return properties_list


def extract_rdf_graph_from_ttl(file_path) -> rdflib.Graph:
    """
    Extracts an RDF graph from a .ttl file.

    :param file_path: The path to the .ttl file.
    :return: An RDF graph.
    """
    rdf_graph = rdflib.Graph()
    rdf_graph.parse(file_path, format="ttl")
    return rdf_graph


if __name__ == "__main__":
    main()
