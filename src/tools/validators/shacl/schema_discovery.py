#!/usr/bin/env python3
"""
Schema discovery based on RDF types.

This module provides functions for discovering required ontology and SHACL
files based on the RDF types found in instance data.
"""

from pathlib import Path
from typing import List, Set, Tuple

from rdflib import RDF, Graph

from src.tools.utils.registry_resolver import RegistryResolver


def extract_rdf_types(graph: Graph) -> Set[str]:
    """
    Extract all rdf:type values from a graph.

    Args:
        graph: RDF graph to extract types from

    Returns:
        Set of type IRIs as strings
    """
    types = set()
    for s, p, o in graph.triples((None, RDF.type, None)):
        types.add(str(o))
    return types


def discover_required_schemas(
    rdf_types: Set[str],
    resolver: RegistryResolver,
) -> Tuple[List[str], List[str]]:
    """
    Map RDF types to required ontology and SHACL files.

    Uses the registry resolver to find the ontology domains that define
    the given RDF types, then returns paths to their ontology and SHACL files.

    Args:
        rdf_types: Set of rdf:type IRIs found in the data
        resolver: RegistryResolver instance

    Returns:
        Tuple of (ontology_paths, shacl_paths) as repository-relative strings
    """
    ontology_paths = []
    shacl_paths = []
    domains_found = set()

    for rdf_type in rdf_types:
        domain = resolver.resolve_type_to_domain(rdf_type)
        if domain and domain not in domains_found:
            domains_found.add(domain)

            ont_path = resolver.get_ontology_path(domain)
            if ont_path:
                ontology_paths.append(ont_path)

            shacl_paths.extend(resolver.get_shacl_paths(domain))

    return sorted(set(ontology_paths)), sorted(set(shacl_paths))


def get_base_ontology_paths(root_dir: Path) -> List[str]:
    """
    Return paths to base ontologies required for RDFS inference.

    These ontologies (RDF, RDFS, OWL, SKOS) provide the vocabulary
    definitions needed for inference and SHACL validation.

    Args:
        root_dir: Repository root directory

    Returns:
        List of repository-relative paths to base ontology files
    """
    base_files = [
        "imports/rdf/rdf.owl.ttl",
        "imports/rdfs/rdfs.owl.ttl",
        "imports/owl/owl.owl.ttl",
        "imports/skos/skos.owl.ttl",
    ]

    # Filter to only existing files
    return [f for f in base_files if (root_dir / f).exists()]


def get_domains_for_types(rdf_types: Set[str], resolver: RegistryResolver) -> Set[str]:
    """
    Get the set of domains that define the given RDF types.

    Args:
        rdf_types: Set of rdf:type IRIs
        resolver: RegistryResolver instance

    Returns:
        Set of domain names
    """
    domains = set()
    for rdf_type in rdf_types:
        domain = resolver.resolve_type_to_domain(rdf_type)
        if domain:
            domains.add(domain)
    return domains
