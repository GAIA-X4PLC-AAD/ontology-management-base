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

# List of folder names allowed to fail validation
EXPECTED_TARGETCLASS_FAILURES = set()


def get_local_name(uri: str) -> str:
    """
    Extract the local name from a given URI by taking the part after `#` or the last `/`.
    Converts to lowercase for case-insensitive comparison.
    """
    if "#" in uri:
        return uri.rsplit("#", 1)[1].lower()
    else:
        return uri.rsplit("/", 1)[-1].lower()


def extract_classes_from_graph(graph: Graph) -> set:
    """
    Extract local names of all classes (OWL and RDFS) from a graph.
    """
    classes = {get_local_name(str(cls)) for cls in graph.subjects(RDF.type, OWL.Class)}
    classes.update(
        {get_local_name(str(cls)) for cls in graph.subjects(RDF.type, RDFS.Class)}
    )
    return classes


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

    ontology_classes = extract_classes_from_graph(ontology_graph)

    label_to_class = {}
    for cls, label in ontology_graph.subject_objects(RDFS.label):
        class_local_name = get_local_name(str(cls))
        label_str = str(label).strip().lower()
        if label_str and class_local_name:
            label_to_class[label_str] = class_local_name

    return ontology_classes, label_to_class


def get_base_ontology_classes(base_dir: str) -> set:
    """
    Recursively load classes from all .ttl files in the base-ontologies directory.
    This provides context for external classes (e.g. schema.org) that are locally mirrored.
    """
    base_classes = set()
    if not os.path.isdir(base_dir):
        return base_classes

    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".ttl"):
                try:
                    g = Graph()
                    g.parse(os.path.join(root, file), format="turtle")
                    base_classes.update(extract_classes_from_graph(g))
                except Exception:
                    # Silently ignore parsing errors in base ontologies to keep validation focused
                    pass
    return base_classes


def validate_target_classes_against_owl_classes(directory: str) -> tuple[int, str]:
    """
    Validate if all target classes in the SHACL shapes are present in the ontology files
    (either locally or in the base-ontologies).
    """
    ontology_files = glob.glob(os.path.join(directory, "*ontology.ttl"))
    if not ontology_files:
        message = f"⚠️  No ontology files found in {directory}. Skipping target class validation."
        return 100, message

    # Locate base-ontologies (assuming sibling structure)
    abs_dir = os.path.abspath(directory)
    root_dir = os.path.dirname(abs_dir)
    base_ontologies_dir = os.path.join(root_dir, "base-ontologies")
    base_classes = get_base_ontology_classes(base_ontologies_dir)

    full_message = []
    for ontology_file in ontology_files:
        ontology_classes, label_to_class = extract_ontology_classes(ontology_file)

        # Combine local classes with base classes
        valid_classes = ontology_classes.union(base_classes)

        shacl_classes = extract_shacl_classes(directory)

        # Convert all to lowercase for case-insensitive matching
        valid_classes_lower = {cls.lower() for cls in valid_classes}
        shacl_classes_lower = {cls.lower() for cls in shacl_classes}

        matches = valid_classes_lower & shacl_classes_lower
        missing_classes = shacl_classes_lower - valid_classes_lower

        # Check against pure local classes for "extra" reporting (optional, keeps output clean)
        local_classes_lower = {cls.lower() for cls in ontology_classes}
        extra_classes = local_classes_lower - shacl_classes_lower

        # Try to recover missing classes using labels (only for local labels)
        recovered_classes = set()
        for missing in list(missing_classes):
            if missing in label_to_class:
                recovered_classes.add(missing)
        missing_classes -= recovered_classes

        summary = format_validate_target_classes_against_owl_classes_result(
            ontology_file,
            len(valid_classes),
            len(shacl_classes),
            matches,
            missing_classes,
            recovered_classes,
            extra_classes,
        )
        full_message.append(summary)

        if missing_classes:
            return 200, "\n".join(full_message)

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

    # Perform validation
    return_code, message = validate_target_classes_against_owl_classes(directory)

    folder_name = os.path.basename(directory)

    if return_code != 0:
        if folder_name in EXPECTED_TARGETCLASS_FAILURES:
            print(
                f"⚠️ Expected target class failure for '{folder_name}' (ignored).",
                flush=True,
            )
            print(message, flush=True)
            sys.exit(0)
        else:
            print(message, file=sys.stderr)
            sys.exit(return_code)
    else:
        print(message)
        sys.exit(0)


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")
    main()
