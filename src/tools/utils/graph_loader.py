#!/usr/bin/env python3
"""
Graph Loader - RDF Graph Loading Utilities

FEATURE SET:
============
1. load_graph - Load single file into graph with auto-format detection
2. load_graphs - Load multiple files into combined graph
3. load_jsonld_files - Load JSON-LD files with prefix extraction
4. load_turtle_files - Load Turtle files into graph
5. load_jsonld_with_context - Load JSON-LD with prefix extraction
6. load_fixtures_for_iris - Resolve and load fixture files for external IRIs
7. extract_external_iris - Find did:web: style references in graph

USAGE:
======
    from src.tools.utils.graph_loader import (
        load_graph,
        load_jsonld_files,
        load_turtle_files,
    )

    # Load single file
    graph = load_graph(Path("data/instance.json"))

    # Load multiple JSON-LD files
    graph, prefixes = load_jsonld_files(json_files, root_dir)

    # Load Turtle files
    graph = load_turtle_files(ttl_files, root_dir)

STANDALONE TESTING:
==================
    python3 -m src.tools.utils.graph_loader [--test] [--verbose] [files...]

DEPENDENCIES:
=============
- rdflib: For RDF graph handling
- oxrdflib (optional): For Oxigraph performance optimization

NOTES:
======
- FAST_STORE is imported from core.constants
- This module consolidates all graph loading logic
- All other modules should delegate graph loading here
"""

import argparse
import json
import logging
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple

import rdflib
from rdflib import Graph

from src.tools.core.constants import FAST_STORE
from src.tools.utils.print_formatter import normalize_path_for_display

# Re-export FAST_STORE for backwards compatibility
__all__ = [
    "FAST_STORE",
    "load_graph",
    "load_graphs",
    "load_jsonld_files",
    "load_turtle_files",
    "load_jsonld_with_context",
    "load_fixtures_for_iris",
    "extract_external_iris",
]


def load_graph(
    file_path: Path,
    format: str = "auto",
    store: str = None,
) -> Graph:
    """
    Load single file into graph with auto-format detection.

    Args:
        file_path: Path to the file to load
        format: RDF format ("auto", "json-ld", "turtle", etc.)
        store: RDF store to use (default: auto-detect oxigraph)

    Returns:
        Graph containing the loaded triples
    """
    if store is None:
        store = FAST_STORE

    graph = Graph(store=store)
    path = Path(file_path)

    # Auto-detect format from extension
    if format == "auto":
        suffix = path.suffix.lower()
        if suffix in (".json", ".jsonld"):
            format = "json-ld"
        elif suffix == ".ttl":
            format = "turtle"
        elif suffix in (".rdf", ".xml"):
            format = "xml"
        elif suffix == ".nt":
            format = "nt"
        else:
            format = "turtle"  # Default fallback

    graph.parse(str(path), format=format)
    return graph


def load_graphs(
    file_paths: List[Path],
    format: str = "auto",
    store: str = None,
) -> Graph:
    """
    Load multiple files into a combined graph.

    Args:
        file_paths: List of file paths to load
        format: RDF format ("auto" for auto-detection)
        store: RDF store to use

    Returns:
        Graph containing all loaded triples
    """
    if store is None:
        store = FAST_STORE

    combined = Graph(store=store)

    for path in file_paths:
        try:
            temp_graph = load_graph(path, format=format, store="default")
            combined += temp_graph
        except Exception as e:
            logging.warning(f"Could not load {path}: {e}")

    return combined


def load_jsonld_files(
    files: List[Path],
    root_dir: Path,
    store: str = None,
) -> Tuple[Graph, Dict[str, str]]:
    """
    Load JSON-LD files into a graph with prefix extraction.

    Args:
        files: List of JSON-LD file paths to load
        root_dir: Repository root directory for path normalization
        store: RDF store to use (default: auto-detect oxigraph)

    Returns:
        Tuple of (graph, prefixes) where prefixes is a dict of prefix->namespace
    """
    if store is None:
        store = FAST_STORE

    graph = Graph(store=store)
    prefixes: Dict[str, str] = {}

    for json_file in files:
        rel_path = normalize_path_for_display(json_file, root_dir)

        # Extract prefixes from @context
        try:
            file_prefixes = _extract_prefixes_from_jsonld(json_file)
            prefixes.update(file_prefixes)
        except Exception as e:
            logging.debug(f"Could not extract prefixes from {rel_path}: {e}")

        # Parse into graph
        try:
            graph.parse(str(json_file), format="json-ld")
        except Exception as e:
            logging.error(f"Failed to load {rel_path}: {e}")
            raise

    return graph, prefixes


def load_turtle_files(
    files: List[Path],
    root_dir: Path,
    store: str = None,
) -> Graph:
    """
    Load Turtle files into a graph.

    Args:
        files: List of Turtle file paths to load
        root_dir: Repository root directory for path normalization
        store: RDF store to use (default: auto-detect oxigraph)

    Returns:
        Graph containing all loaded triples
    """
    if store is None:
        store = FAST_STORE

    graph = Graph(store=store)

    for ttl_file in files:
        rel_path = normalize_path_for_display(ttl_file, root_dir)

        try:
            graph.parse(str(ttl_file), format="turtle")
        except Exception as e:
            logging.warning(f"Could not load {rel_path}: {e}")

    return graph


def load_jsonld_with_context(file_path: Path) -> Tuple[Graph, Dict[str, str]]:
    """
    Load JSON-LD file with prefix extraction.

    Args:
        file_path: Path to JSON-LD file

    Returns:
        Tuple of (graph, prefixes) where prefixes is dict of prefix->namespace
    """
    graph = Graph(store=FAST_STORE)
    graph.parse(str(file_path), format="json-ld")

    prefixes = _extract_prefixes_from_jsonld(file_path)

    return graph, prefixes


def load_fixtures_for_iris(
    iris: Set[str],
    resolver: "RegistryResolver",  # noqa: F821 - forward reference
    graph: Graph,
    root_dir: Path,
) -> int:
    """
    Load fixture files for external IRI references.

    This resolves did:web: style IRIs to local fixture files and loads
    them into the provided graph.

    Args:
        iris: Set of IRIs to resolve
        resolver: RegistryResolver instance
        graph: Graph to load fixtures into
        root_dir: Repository root directory

    Returns:
        Number of fixtures loaded
    """
    fixtures_loaded = 0
    existing_subjects = {str(s) for s in graph.subjects()}

    for iri in iris:
        # Skip if already in graph
        if iri in existing_subjects:
            continue

        # Try to resolve fixture
        fixture_path = resolver.resolve_fixture_iri(iri)
        if not fixture_path:
            continue

        abs_path = resolver.to_absolute(fixture_path)
        if not abs_path.exists():
            continue

        try:
            graph.parse(str(abs_path), format="json-ld")
            rel_path = normalize_path_for_display(abs_path, root_dir)
            logging.debug(f"Loaded fixture: {rel_path} for {iri}")
            fixtures_loaded += 1
        except Exception as e:
            logging.warning(f"Could not load fixture for {iri}: {e}")

    return fixtures_loaded


def _extract_prefixes_from_jsonld(file_path: Path) -> Dict[str, str]:
    """
    Extract prefix mappings from a JSON-LD @context.

    Args:
        file_path: Path to JSON-LD file

    Returns:
        Dictionary of prefix -> namespace URI mappings
    """
    with file_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    context = data.get("@context", {})
    prefixes = {}

    if isinstance(context, dict):
        for key, value in context.items():
            if isinstance(value, str) and (value.endswith("#") or value.endswith("/")):
                prefixes[key] = value
    elif isinstance(context, list):
        for ctx in context:
            if isinstance(ctx, dict):
                for key, value in ctx.items():
                    if isinstance(value, str) and (
                        value.endswith("#") or value.endswith("/")
                    ):
                        prefixes[key] = value

    return prefixes


def extract_external_iris(graph: Graph) -> Set[str]:
    """
    Extract external IRI references (did:web: style) from a graph.

    Args:
        graph: RDF graph to scan

    Returns:
        Set of external IRIs
    """
    external_iris = set()

    for s, p, o in graph:
        if isinstance(s, rdflib.URIRef) and str(s).startswith("did:web:"):
            external_iris.add(str(s))
        if isinstance(o, rdflib.URIRef) and str(o).startswith("did:web:"):
            external_iris.add(str(o))

    return external_iris


def _run_tests() -> bool:
    """Run self-tests for the module."""
    import tempfile

    print("Running graph_loader self-tests...")
    all_passed = True

    # Test 1: FAST_STORE is defined
    if FAST_STORE not in ("oxigraph", "default"):
        print(f"FAIL: Invalid FAST_STORE value: {FAST_STORE}")
        all_passed = False
    else:
        print(f"PASS: FAST_STORE is '{FAST_STORE}'")

    # Test 2: Create and load JSON-LD file
    with tempfile.TemporaryDirectory() as tmpdir:
        tmppath = Path(tmpdir)

        # Create test JSON-LD file
        jsonld_file = tmppath / "test.json"
        jsonld_content = {
            "@context": {"@vocab": "http://example.org/"},
            "@id": "http://example.org/test",
            "@type": "Thing",
        }
        jsonld_file.write_text(json.dumps(jsonld_content))

        # Test load_graph
        try:
            graph = load_graph(jsonld_file)
            if len(graph) < 1:
                print("FAIL: Graph should have at least 1 triple")
                all_passed = False
            else:
                print("PASS: load_graph JSON-LD")
        except Exception as e:
            print(f"FAIL: load_graph raised exception: {e}")
            all_passed = False

        # Test load_jsonld_files
        try:
            graph, prefixes = load_jsonld_files([jsonld_file], tmppath)
            if len(graph) < 1:
                print("FAIL: load_jsonld_files should have triples")
                all_passed = False
            else:
                print("PASS: load_jsonld_files")
        except Exception as e:
            print(f"FAIL: load_jsonld_files raised exception: {e}")
            all_passed = False

        # Create test Turtle file
        ttl_file = tmppath / "test.ttl"
        ttl_content = """@prefix ex: <http://example.org/> .
ex:subject a ex:Thing .
"""
        ttl_file.write_text(ttl_content)

        # Test load_turtle_files
        try:
            graph = load_turtle_files([ttl_file], tmppath)
            if len(graph) < 1:
                print("FAIL: load_turtle_files should have triples")
                all_passed = False
            else:
                print("PASS: load_turtle_files")
        except Exception as e:
            print(f"FAIL: load_turtle_files raised exception: {e}")
            all_passed = False

        # Test extract_external_iris
        external_graph = Graph()
        external_graph.parse(
            data="""
            @prefix ex: <http://example.org/> .
            <did:web:test.example:subject> a ex:Thing .
            ex:other ex:ref <did:web:test.example:ref> .
            """,
            format="turtle",
        )
        iris = extract_external_iris(external_graph)
        if len(iris) != 2:
            print(f"FAIL: Expected 2 external IRIs, got {len(iris)}")
            all_passed = False
        else:
            print("PASS: extract_external_iris")

    if all_passed:
        print("\nAll tests passed!")
    else:
        print("\nSome tests failed!")

    return all_passed


def main():
    """CLI entry point for graph_loader."""
    parser = argparse.ArgumentParser(description="Load and inspect RDF graphs")
    parser.add_argument(
        "files",
        nargs="*",
        help="Files to load",
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="Run self-tests",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Verbose output",
    )
    parser.add_argument(
        "--format",
        "-f",
        default="auto",
        help="RDF format (auto, json-ld, turtle, etc.)",
    )

    args = parser.parse_args()

    if args.test:
        success = _run_tests()
        sys.exit(0 if success else 1)

    if not args.files:
        parser.print_help()
        sys.exit(1)

    # Load and report
    root_dir = Path.cwd()
    total_triples = 0

    for file_path in args.files:
        path = Path(file_path)
        try:
            graph = load_graph(path, format=args.format)
            triple_count = len(graph)
            total_triples += triple_count

            rel_path = normalize_path_for_display(path, root_dir)
            print(f"{rel_path}: {triple_count} triples")

            if args.verbose:
                for s, p, o in list(graph)[:5]:
                    print(f"  {s} {p} {o}")
                if len(graph) > 5:
                    print(f"  ... and {len(graph) - 5} more")

        except Exception as e:
            print(f"Error loading {file_path}: {e}", file=sys.stderr)

    print(f"\nTotal: {total_triples} triples from {len(args.files)} file(s)")


if __name__ == "__main__":
    main()
