"""
SHACL-based data conformance validation.

This module validates JSON-LD instance data against SHACL shapes using
catalog-based discovery. The validation pipeline:

1. Loads JSON-LD instance data (utils.graph_loader)
2. Discovers required ontologies/SHACL shapes based on RDF types (schema_discovery.py)
3. Applies RDFS inference to complete the data graph (inference.py)
4. Validates against SHACL shapes using pyshacl (validator.py)

The registry resolver (from src.tools.utils) is used throughout this
pipeline to map RDF types to domain ontologies and SHACL shapes. This
allows the validator to automatically discover which ontologies and
shapes are needed based on the types present in the instance data.

Components:
    - utils.graph_loader: JSON-LD and Turtle graph loading
    - inference: RDFS inference engine
    - schema_discovery: Type-to-schema mapping using RegistryResolver
    - validator: Main validation orchestrator

Entry point:
    from src.tools.validators.shacl.validator import ShaclValidator

    validator = ShaclValidator(domains=["general"])
    result = validator.validate("data.jsonld")

    if not result.conforms:
        print(result.report_text)

See also:
    - src.tools.utils.registry_resolver: Catalog-based path resolution
    - artifacts/catalog-v001.xml
    - imports/catalog-v001.xml
    - tests/catalog-v001.xml
"""

from src.tools.utils.graph_loader import (
    load_fixtures_for_iris,
    load_jsonld_files,
    load_turtle_files,
)

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
