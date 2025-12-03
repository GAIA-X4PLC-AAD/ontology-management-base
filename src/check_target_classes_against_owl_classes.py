import glob
import io
import os
import sys

from rdflib import OWL, RDF, RDFS, Graph, Namespace

from utils.print_formatting import (
    format_validate_target_classes_against_owl_classes_result,
)

# Define SHACL namespace
SH = Namespace("http://www.w3.org/ns/shacl#")


def get_local_name(uri: str) -> str:
    """
    Extract the local name from a given URI by taking the part after `#` or the last `/`.
    Converts to lowercase for case-insensitive comparison.
    """
    if "#" in uri:
        return uri.rsplit("#", 1)[1].lower()
    else:
        return uri.rsplit("/", 1)[-1].lower()


def extract_shacl_classes(directory: str) -> set:
    """
    Extract SHACL target classes from all SHACL `.ttl` files in the given directory.
    Returns a set of local names of target classes (case-insensitive).
    """
    shacl_classes = set()
    shacl_files = glob.glob(os.path.join(directory, "*shacl.ttl"))

    for shacl_file in shacl_files:
        shacl_graph = Graph()
        shacl_graph.parse(shacl_file, format="turtle")

        for cls in shacl_graph.objects(None, SH.targetClass):
            local_name = get_local_name(str(cls))
            shacl_classes.add(local_name)

    return shacl_classes


def extract_ontology_classes(ontology_file: str) -> tuple:
    """
    Extracts class definitions from an ontology file.
    - Returns a set of class local names (case-insensitive).
    - Returns a dictionary mapping lowercase rdfs:label values to class names.
    """
    ontology_graph = Graph()
    ontology_graph.parse(ontology_file, format="turtle")

    ontology_classes = {
        get_local_name(str(cls)) for cls in ontology_graph.subjects(RDF.type, OWL.Class)
    }

    label_to_class = {}
    for cls, label in ontology_graph.subject_objects(RDFS.label):
        class_local_name = get_local_name(str(cls))
        label_str = str(label).strip().lower()
        if label_str and class_local_name:
            label_to_class[label_str] = class_local_name

    return ontology_classes, label_to_class


def validate_target_classes_against_owl_classes(directory: str) -> tuple[int, str]:
    """
    Validate if all target classes in the SHACL shapes are present in the ontology file as OWL classes.
    - Passes if ontology_classes ⊇ shacl_classes (matching by local name, case-insensitive)
    - Warns if ontology_classes has more classes than shacl_classes
    - Fails if shacl_classes contains classes not found in ontology_classes

    Returns:
        (return_code, message) where return_code=0 means success,
        200 means missing classes found (failure),
        100 means no ontology files found (warning),
        other codes can be defined as needed.
    """
    ontology_files = glob.glob(os.path.join(directory, "*ontology.ttl"))
    if not ontology_files:
        message = f"⚠️  No ontology files found in {directory}. Skipping target class validation."
        # Return a non-zero code to indicate a warning or special condition
        return 100, message

    full_message = []
    for ontology_file in ontology_files:
        ontology_classes, label_to_class = extract_ontology_classes(ontology_file)
        shacl_classes = extract_shacl_classes(directory)

        # Convert all to lowercase for case-insensitive matching
        ontology_classes_lower = {cls.lower() for cls in ontology_classes}
        shacl_classes_lower = {cls.lower() for cls in shacl_classes}

        matches = ontology_classes_lower & shacl_classes_lower
        missing_classes = shacl_classes_lower - ontology_classes_lower
        extra_classes = ontology_classes_lower - shacl_classes_lower

        recovered_classes = set()
        for missing in list(missing_classes):
            if missing in label_to_class:
                recovered_classes.add(missing)
        missing_classes -= recovered_classes

        summary = format_validate_target_classes_against_owl_classes_result(
            ontology_file,
            len(ontology_classes),
            len(shacl_classes),
            matches,
            missing_classes,
            recovered_classes,
            extra_classes,
        )
        full_message.append(summary)

        if missing_classes:
            # Failure: missing classes found
            return 200, "\n".join(full_message)

    # If no missing classes found, success
    return 0, "\n".join(full_message)


def main():
    if len(sys.argv) != 2:
        print(
            "Usage: python check_target_classes_against_owl_classes.py <directory>",
            file=sys.stderr,
        )
        sys.exit(100)

    directory = os.path.normpath(sys.argv[1])
    if not os.path.isdir(directory):
        print(f"The directory {directory} does not exist. Abort.", file=sys.stderr)
        sys.exit(110)

    return_code, message = validate_target_classes_against_owl_classes(directory)
    if return_code != 0:
        print(message, file=sys.stderr)
        sys.exit(return_code)
    else:
        print(message)
        sys.exit(0)


if __name__ == "__main__":
    # Set the encoding for stdout to UTF-8
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")
    main()
