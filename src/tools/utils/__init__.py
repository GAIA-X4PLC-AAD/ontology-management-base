"""
Shared utilities for ontology management tools.

This package provides reusable utilities that are not specific to any
particular validation or processing task.

Key utilities:
- RegistryResolver: Resolves ontology and SHACL paths from XML catalogs
- file_collector: File discovery utilities
- graph_loader: RDF graph loading utilities
- print_formatter: Output formatting utilities

The registry resolver is used by the SHACL validation pipeline (see
src.tools.validators.shacl) to discover required ontologies and SHACL
shapes based on RDF types in instance data.

Usage:
    from src.tools.utils import RegistryResolver

    resolver = RegistryResolver()
    owl_path = resolver.get_ontology_path("general")
    shacl_paths = resolver.get_shacl_paths("general")

See also:
    - src.tools.validators.shacl: Main consumer of RegistryResolver
    - artifacts/catalog-v001.xml
    - imports/catalog-v001.xml
    - tests/catalog-v001.xml
"""

from .file_collector import (
    collect_files_by_extension,
    collect_files_by_pattern,
    collect_jsonld_files,
    collect_ontology_bundles,
    collect_ontology_files,
    collect_test_files,
    collect_turtle_files,
)
from .graph_loader import (
    FAST_STORE,
    extract_external_iris,
    load_fixtures_for_iris,
    load_graph,
    load_graphs,
    load_jsonld_files,
    load_jsonld_with_context,
    load_turtle_files,
)
from .print_formatter import normalize_path_for_display
from .registry_resolver import RegistryResolver

__all__ = [
    # Registry
    "RegistryResolver",
    # File collection
    "collect_files_by_extension",
    "collect_files_by_pattern",
    "collect_jsonld_files",
    "collect_ontology_bundles",
    "collect_ontology_files",
    "collect_test_files",
    "collect_turtle_files",
    # Graph loading
    "FAST_STORE",
    "extract_external_iris",
    "load_fixtures_for_iris",
    "load_graph",
    "load_graphs",
    "load_jsonld_files",
    "load_jsonld_with_context",
    "load_turtle_files",
    # Print formatting
    "normalize_path_for_display",
]
