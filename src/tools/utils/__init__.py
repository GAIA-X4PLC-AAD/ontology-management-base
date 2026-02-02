"""
Shared utilities for ontology management tools.

This package provides reusable utilities that are not specific to any
particular validation or processing task.

Key utilities:
- RegistryResolver: Resolves ontology and SHACL paths from registry.json
- verify_json_syntax: Validates JSON-LD syntax
- verify_turtle_syntax: Validates Turtle/RDF syntax
- print_formatting: Output formatting utilities

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
    - docs/registry.json: Registry configuration file
"""

from .file_collector import (
    collect_files_by_extension,
    collect_jsonld_files,
    collect_turtle_files,
)
from .registry_resolver import RegistryResolver

__all__ = [
    "RegistryResolver",
    "collect_files_by_extension",
    "collect_jsonld_files",
    "collect_turtle_files",
]
