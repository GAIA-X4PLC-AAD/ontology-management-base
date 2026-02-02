#!/usr/bin/env python3
"""
Graph loading utilities with path normalization.

This module provides functions for loading JSON-LD and Turtle files into
RDF graphs, with consistent path normalization for console output.
"""

import json
import logging
from pathlib import Path
from typing import Dict, List, Set, Tuple

import rdflib
from rdflib import Graph

from src.tools.utils.print_formatter import normalize_path_for_display
from src.tools.utils.registry_resolver import RegistryResolver

# Try to import performance optimization
try:
    import oxrdflib  # noqa: F401

    FAST_STORE = "oxigraph"
except ImportError:
    FAST_STORE = "default"


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


def load_fixtures_for_iris(
    iris: Set[str],
    resolver: RegistryResolver,
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
