# Python
import glob
import os
import sys

from rdflib import Graph

# Import the functions from fc_upload_with_update.py
from fc_upload_with_update import find_corresponding_shapes_from_filesystem


def validate_target_classes_against_owl_classes(directory: str):
    """
    Validate if all target classes in the SHACL shapes are present in the ontology file as OWL classes.
    """
    ontology_files = glob.glob(os.path.join(directory, "*ontology.ttl"))
    for ontology_file in ontology_files:
        # Load the ontology graph
        ontology_graph = Graph()
        ontology_graph.parse(ontology_file, format="turtle")

        # Find corresponding shapes from the filesystem
        corresponding_shapes, ontology_name = find_corresponding_shapes_from_filesystem(
            directory, ontology_graph, True
        )
        if not corresponding_shapes:
            print(
                f"Error for {ontology_name}\n"
                f"Please check the log and correct your SHACL shapes to have all target classes are present in "
                f"the ontology."
            )
            sys.exit(300)
        else:
            print(
                f"Validated that all target classes in SHACL are existent in ontology {ontology_file}."
            )


def main():
    if len(sys.argv) != 2:
        print("Usage: python check_target_classes_against_owl_classes <directory>")
        sys.exit(100)

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"The directory {directory} does not exist. Abort.")
        sys.exit(200)

    validate_target_classes_against_owl_classes(directory)


if __name__ == "__main__":
    main()
