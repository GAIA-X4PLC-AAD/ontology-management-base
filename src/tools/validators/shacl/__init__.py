"""
SHACL Validation Module.

This module provides modular components for SHACL validation:
  - graph_loader: JSON-LD and Turtle graph loading
  - inference: RDFS inference engine
  - schema_discovery: Type-to-schema mapping
  - validator: Main validation orchestrator
"""

from .graph_loader import load_fixtures_for_iris, load_jsonld_files, load_turtle_files
from .inference import apply_rdfs_inference
from .schema_discovery import discover_required_schemas, get_base_ontology_paths
from .validator import ShaclValidator, ValidationResult

__all__ = [
    "load_jsonld_files",
    "load_turtle_files",
    "load_fixtures_for_iris",
    "apply_rdfs_inference",
    "discover_required_schemas",
    "get_base_ontology_paths",
    "ShaclValidator",
    "ValidationResult",
]
