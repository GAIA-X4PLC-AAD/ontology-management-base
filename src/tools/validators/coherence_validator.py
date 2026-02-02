#!/usr/bin/env python3
"""
Coherence Validator - SHACL Target Class vs OWL Class Validation

FEATURE SET:
============
1. validate_artifact_coherence - Validate SHACL targets match OWL definitions
2. extract_ontology_classes - Extract class definitions from OWL files
3. extract_shacl_classes - Extract target classes from SHACL files
4. get_base_ontology_classes - Load classes from base/imported ontologies
5. get_local_name - Extract local name from URI (case-insensitive)

USAGE:
======
    from src.tools.validators.coherence_validator import (
        validate_artifact_coherence,
        extract_ontology_classes,
    )

    # Validate single domain
    code, msg = validate_artifact_coherence("manifest")

    # Extract classes from ontology
    classes, labels = extract_ontology_classes("artifacts/manifest/manifest.owl.ttl")

STANDALONE TESTING:
==================
    python3 -m src.tools.validators.coherence_validator [--test] domain [owl_dir] [imports_dir]

DEPENDENCIES:
=============
- rdflib: For RDF graph handling

NOTES:
======
- Case-insensitive class matching (local names converted to lowercase)
- Missing classes can be recovered via rdfs:label matching
- Base ontologies from imports/ are included in valid class set
"""

import argparse
import io
import sys
from pathlib import Path
from typing import Dict, Set, Tuple

from rdflib import OWL, RDF, RDFS, Graph, Namespace

from src.tools.core.result import ReturnCodes
from src.tools.utils.file_collector import collect_files_by_pattern
from src.tools.utils.print_formatter import (
    format_artifact_coherence_result,
    normalize_path_for_display,
)
from src.tools.utils.registry_resolver import RegistryResolver

# Define SHACL namespace
SH = Namespace("http://www.w3.org/ns/shacl#")

# List of folder names allowed to fail validation (configurable)
EXPECTED_TARGETCLASS_FAILURES: Set[str] = set()


def get_local_name(uri: str) -> str:
    """
    Extract the local name from a given URI.

    Takes the part after `#` or the last `/` and converts to lowercase
    for case-insensitive comparison.

    Args:
        uri: Full URI string

    Returns:
        Local name in lowercase
    """
    if "#" in uri:
        return uri.rsplit("#", 1)[1].lower()
    else:
        return uri.rsplit("/", 1)[-1].lower()


def extract_classes_from_graph(graph: Graph) -> Set[str]:
    """
    Extract local names of all classes (OWL and RDFS) from a graph.

    Args:
        graph: RDF graph to scan

    Returns:
        Set of lowercase class local names
    """
    classes = {get_local_name(str(cls)) for cls in graph.subjects(RDF.type, OWL.Class)}
    classes.update(
        {get_local_name(str(cls)) for cls in graph.subjects(RDF.type, RDFS.Class)}
    )
    return classes


def extract_shacl_classes_from_file(shacl_file: str) -> Set[str]:
    """
    Extract SHACL target classes from a single SHACL file.

    Args:
        shacl_file: Path to SHACL file

    Returns:
        Set of lowercase target class local names
    """
    shacl_classes = set()
    shacl_graph = Graph()
    shacl_graph.parse(shacl_file, format="turtle")

    for cls in shacl_graph.objects(None, SH.targetClass):
        local_name = get_local_name(str(cls))
        shacl_classes.add(local_name)

    return shacl_classes


def extract_shacl_classes(directory: str) -> Set[str]:
    """
    Extract SHACL target classes from all SHACL files in a directory.

    Args:
        directory: Path to directory containing SHACL files

    Returns:
        Set of lowercase target class local names
    """
    shacl_classes = set()
    shacl_files = collect_files_by_pattern([directory], "*shacl.ttl")

    for shacl_file in shacl_files:
        shacl_classes.update(extract_shacl_classes_from_file(shacl_file))

    return shacl_classes


def extract_ontology_classes(ontology_file: str) -> Tuple[Set[str], Dict[str, str]]:
    """
    Extract class definitions from an ontology file.

    Args:
        ontology_file: Path to OWL ontology file

    Returns:
        Tuple of (classes, label_to_class) where:
        - classes: Set of lowercase class local names
        - label_to_class: Dict mapping lowercase rdfs:label to class name
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


def get_base_ontology_classes(resolver: RegistryResolver, root_dir: Path) -> Set[str]:
    """
    Load classes from base ontologies listed in imports/catalog-v001.xml.

    Args:
        resolver: RegistryResolver instance
        root_dir: Repository root directory

    Returns:
        Set of lowercase class local names from base ontologies
    """
    base_classes = set()
    for rel_path in resolver.get_base_ontology_paths():
        abs_path = resolver.to_absolute(rel_path)
        if not abs_path.exists():
            continue
        try:
            g = Graph()
            g.parse(str(abs_path), format="turtle")
            base_classes.update(extract_classes_from_graph(g))
        except Exception:
            # Silently ignore parsing errors in base ontologies
            pass
    return base_classes


def validate_artifact_coherence(
    domain: str,
    owl_dir: str = None,
    shacl_dir: str = None,
    imports_dir: str = None,
    root_dir: Path = None,
) -> Tuple[int, str]:
    """
    Validate that all target classes in SHACL shapes are defined in ontology.

    Args:
        domain: Ontology domain name (e.g., "hdmap", "manifest")
        owl_dir: Deprecated (catalogs are used for resolution)
        shacl_dir: Deprecated (catalogs are used for resolution)
        imports_dir: Deprecated (catalogs are used for resolution)
        root_dir: Repository root directory for path normalization

    Returns:
        Tuple of (return_code, message) where return_code is 0 for success
    """
    root_dir = root_dir or Path.cwd()
    resolver = RegistryResolver(root_dir)

    ontology_rel = resolver.get_ontology_path(domain)
    shacl_rels = resolver.get_shacl_paths(domain)

    if not ontology_rel:
        message = (
            f"No ontology file found for '{domain}'. "
            "Target class validation cannot proceed."
        )
        return ReturnCodes.COHERENCE_ERROR, message

    if not shacl_rels:
        message = (
            f"No SHACL file found for '{domain}'. "
            "Target class validation cannot proceed."
        )
        return ReturnCodes.COHERENCE_ERROR, message

    ontology_file = resolver.to_absolute(ontology_rel)
    shacl_files = [resolver.to_absolute(p) for p in shacl_rels]

    if not ontology_file.exists():
        # Normalize paths for display
        ont_display = normalize_path_for_display(ontology_file, root_dir)
        message = (
            f"No ontology file found: {ont_display}. "
            "Target class validation cannot proceed."
        )
        return ReturnCodes.COHERENCE_ERROR, message

    missing_shacl = [p for p in shacl_files if not p.exists()]
    if missing_shacl:
        # Normalize paths for display
        missing_display = ", ".join(
            normalize_path_for_display(p, root_dir) for p in missing_shacl
        )
        message = (
            f"No SHACL file found: {missing_display}. "
            "Target class validation cannot proceed."
        )
        return ReturnCodes.COHERENCE_ERROR, message

    # Normalize paths for display (used in summary output)
    ont_display = normalize_path_for_display(ontology_file, root_dir)

    # Load base classes from imports catalog
    base_classes = get_base_ontology_classes(resolver, root_dir)

    # Extract classes from ontology
    ontology_classes, label_to_class = extract_ontology_classes(str(ontology_file))

    # Combine local classes with base classes
    valid_classes = ontology_classes.union(base_classes)

    # Extract SHACL target classes
    shacl_classes = set()
    for shacl_file in shacl_files:
        shacl_classes.update(extract_shacl_classes_from_file(str(shacl_file)))

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

    summary = format_artifact_coherence_result(
        ont_display,
        len(valid_classes),
        len(shacl_classes),
        matches,
        missing_classes,
        recovered_classes,
        extra_classes,
    )

    if missing_classes:
        return ReturnCodes.COHERENCE_ERROR, summary

    return ReturnCodes.SUCCESS, summary


def _run_tests() -> bool:
    """Run self-tests for the module."""
    import tempfile

    print("Running coherence_validator self-tests...")
    all_passed = True

    # Test 1: get_local_name with hash
    result = get_local_name("http://example.org/ontology#MyClass")
    if result != "myclass":
        print(f"FAIL: get_local_name hash - expected 'myclass', got '{result}'")
        all_passed = False
    else:
        print("PASS: get_local_name with hash")

    # Test 2: get_local_name with slash
    result = get_local_name("http://example.org/ontology/MyClass")
    if result != "myclass":
        print(f"FAIL: get_local_name slash - expected 'myclass', got '{result}'")
        all_passed = False
    else:
        print("PASS: get_local_name with slash")

    # Test 3: Extract classes from graph
    with tempfile.TemporaryDirectory() as tmpdir:
        tmppath = Path(tmpdir)

        owl_file = tmppath / "test.owl.ttl"
        owl_file.write_text(
            """@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix : <http://example.org/> .

:MyClass a owl:Class ;
    rdfs:label "My Class" .

:OtherClass a owl:Class .
"""
        )

        classes, labels = extract_ontology_classes(str(owl_file))
        if "myclass" not in classes or "otherclass" not in classes:
            print(f"FAIL: extract_ontology_classes - got {classes}")
            all_passed = False
        else:
            print("PASS: extract_ontology_classes")

        if "my class" not in labels:
            print(f"FAIL: label extraction - got {labels}")
            all_passed = False
        else:
            print("PASS: label extraction")

        # Test 4: Extract SHACL classes
        shacl_file = tmppath / "test.shacl.ttl"
        shacl_file.write_text(
            """@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix : <http://example.org/> .

:MyClassShape a sh:NodeShape ;
    sh:targetClass :MyClass .
"""
        )

        shacl_classes = extract_shacl_classes_from_file(str(shacl_file))
        if "myclass" not in shacl_classes:
            print(f"FAIL: extract_shacl_classes - got {shacl_classes}")
            all_passed = False
        else:
            print("PASS: extract_shacl_classes")

    if all_passed:
        print("\nAll tests passed!")
    else:
        print("\nSome tests failed!")

    return all_passed


def main():
    """CLI entry point for coherence_validator."""
    parser = argparse.ArgumentParser(
        description="Validate SHACL target classes match OWL class definitions."
    )
    parser.add_argument("domain", nargs="?", help="Ontology domain name")
    parser.add_argument(
        "owl_dir",
        nargs="?",
        default="artifacts",
        help="Directory containing ontology directories (default: artifacts)",
    )
    parser.add_argument(
        "imports_dir",
        nargs="?",
        default="imports",
        help="Directory containing base ontologies (default: imports)",
    )
    parser.add_argument("--test", action="store_true", help="Run self-tests")

    args = parser.parse_args()

    if args.test:
        success = _run_tests()
        sys.exit(0 if success else 1)

    if not args.domain:
        parser.print_help()
        sys.exit(1)

    # Use current working directory as root for path normalization
    root_dir = Path.cwd()

    return_code, message = validate_artifact_coherence(
        args.domain, args.owl_dir, None, args.imports_dir, root_dir
    )

    if return_code != 0:
        if args.domain in EXPECTED_TARGETCLASS_FAILURES:
            print(
                f"Expected target class failure for '{args.domain}' (ignored).",
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
