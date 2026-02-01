import glob
import io
import os
import sys

from rdflib import OWL, RDF, RDFS, Graph, Namespace

from src.tools.utils.print_formatting import (
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


def extract_shacl_classes_from_file(shacl_file: str) -> set:
    """
    Extract SHACL target classes from a single SHACL file.
    Returns a set of local names of target classes (case-insensitive).
    """
    shacl_classes = set()
    shacl_graph = Graph()
    shacl_graph.parse(shacl_file, format="turtle")

    for cls in shacl_graph.objects(None, SH.targetClass):
        local_name = get_local_name(str(cls))
        shacl_classes.add(local_name)

    return shacl_classes


def extract_shacl_classes(directory: str) -> set:
    """
    Extract SHACL target classes from all SHACL `.ttl` files in the given directory.
    Returns a set of local names of target classes (case-insensitive).
    """
    shacl_classes = set()
    shacl_files = glob.glob(os.path.join(directory, "*shacl.ttl"))

    for shacl_file in shacl_files:
        shacl_classes.update(extract_shacl_classes_from_file(shacl_file))

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
    Recursively load classes from all .ttl files in the imports directory.
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


def validate_target_classes_against_owl_classes(
    domain: str,
    owl_dir: str = None,
    shacl_dir: str = None,
    imports_dir: str = None,
) -> tuple[int, str]:
    """
    Validate if all target classes in the SHACL shapes are present in the ontology files.

    Args:
        domain: ontology domain name (e.g., "hdmap")
        owl_dir: directory containing ontology directories (default: artifacts)
        shacl_dir: not used (kept for backward compatibility)
        imports_dir: directory containing base ontologies (default: imports)

    Returns:
        Tuple of (return_code, message) where return_code is 0 for success
    """
    # New structure mode
    if owl_dir is None:
        owl_dir = "artifacts"
    if imports_dir is None:
        imports_dir = "imports"

    ontology_file = os.path.join(owl_dir, domain, f"{domain}.owl.ttl")
    shacl_file = os.path.join(owl_dir, domain, f"{domain}.shacl.ttl")

    if not os.path.exists(ontology_file):
        message = f"⚠️  No ontology file found: {ontology_file}. Skipping target class validation."
        return 100, message

    if not os.path.exists(shacl_file):
        message = (
            f"⚠️  No SHACL file found: {shacl_file}. Skipping target class validation."
        )
        return 100, message

    # Load base classes from imports
    base_classes = get_base_ontology_classes(imports_dir)

    # Extract classes from ontology
    ontology_classes, label_to_class = extract_ontology_classes(ontology_file)

    # Combine local classes with base classes
    valid_classes = ontology_classes.union(base_classes)

    # Extract SHACL target classes
    shacl_classes = extract_shacl_classes_from_file(shacl_file)

    # Convert all to lowercase for case-insensitive matching
    valid_classes_lower = {cls.lower() for cls in valid_classes}
    shacl_classes_lower = {cls.lower() for cls in shacl_classes}

    matches = valid_classes_lower & shacl_classes_lower
    missing_classes = shacl_classes_lower - valid_classes_lower

    # Check against pure local classes for "extra" reporting
    local_classes_lower = {cls.lower() for cls in ontology_classes}
    extra_classes = local_classes_lower - shacl_classes_lower

    # Try to recover missing classes using labels
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

    if missing_classes:
        return 200, summary

    return 0, summary


def main():
    if len(sys.argv) < 2:
        print(
            "Usage: python check_target_classes_against_owl_classes.py <domain> [owl_dir] [imports_dir]",
            file=sys.stderr,
        )
        sys.exit(100)

    domain = sys.argv[1]
    owl_dir = sys.argv[2] if len(sys.argv) > 2 else "artifacts"
    imports_dir = sys.argv[3] if len(sys.argv) > 3 else "imports"

    return_code, message = validate_target_classes_against_owl_classes(
        domain, owl_dir, None, imports_dir
    )

    if return_code != 0:
        if domain in EXPECTED_TARGETCLASS_FAILURES:
            print(
                f"Expected target class failure for '{domain}' (ignored).",
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
