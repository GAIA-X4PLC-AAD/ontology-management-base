#!/usr/bin/env python3
"""
Schema discovery based on RDF types.

This module provides functions for discovering required ontology and SHACL
files based on the RDF types found in instance data.
"""

from pathlib import Path
from typing import List, Optional, Set, Tuple

from rdflib import RDF, Graph, Literal

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


def extract_predicates(graph: Graph) -> Set[str]:
    """
    Extract all predicate IRIs from a graph.

    Args:
        graph: RDF graph to extract predicates from

    Returns:
        Set of predicate IRIs as strings
    """
    return {str(p) for p in graph.predicates()}


def extract_datatype_iris(graph: Graph) -> Set[str]:
    """
    Extract datatype IRIs used by literals in a graph.

    Args:
        graph: RDF graph to scan for datatypes

    Returns:
        Set of datatype IRIs as strings
    """
    datatypes = set()
    for _, _, o in graph:
        if isinstance(o, Literal) and o.datatype:
            datatypes.add(str(o.datatype))
    return datatypes


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


def get_base_ontology_paths(
    root_dir: Path, used_iris: Optional[Set[str]] = None
) -> List[str]:
    """
    Return paths to base ontologies required for RDFS inference.

    Base ontologies are discovered via the RegistryResolver, which reads
    imports/catalog-v001.xml to provide the vocabulary definitions
    (RDF, RDFS, OWL, SKOS, etc.) needed for inference and SHACL validation.

    Args:
        root_dir: Repository root directory

    Args:
        root_dir: Repository root directory
        used_iris: Optional set of IRIs referenced in the data graph; when
            provided, base ontologies are filtered to those namespaces.

    Returns:
        List of repository-relative paths to base ontology files
    """
    # Use RegistryResolver to get base ontologies from catalog
    resolver = RegistryResolver(root_dir)
    if used_iris is None:
        return resolver.get_base_ontology_paths()
    return resolver.get_base_ontology_paths_for_iris(used_iris)


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
