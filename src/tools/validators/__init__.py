"""
Validation tools for ontology artifacts and instance data.

This package provides validators for:

1. Artifact Coherence (validate_artifact_coherence.py):
   - Validates SHACL target classes match OWL class definitions
   - Ensures consistency between ontology and shapes files

2. Data Conformance (shacl/ subpackage):
   - Validates JSON-LD instance data against SHACL shapes
   - Uses registry-based discovery to find required ontologies
   - Applies RDFS inference before validation

3. Validation Suite (validation_suite.py):
   - Aggregates all validators (syntax + coherence + conformance)
   - Command-line entry point for running all checks

Organization:
    validators/
    ├── validate_artifact_coherence.py  (standalone validator)
    ├── validate_data_conformance.py    (entry point to shacl/)
    ├── validation_suite.py              (aggregator)
    └── shacl/                           (modular SHACL subsystem)
        ├── validator.py
        ├── graph_loader.py
        ├── schema_discovery.py
        └── inference.py

Key dependencies:
    - src.tools.utils.registry_resolver: Registry-based path resolution
    - docs/registry.json: Registry configuration file

Usage:
    # Run all validators
    python -m src.tools.validators.validation_suite --check all --domain general

    # Run specific validator
    from src.tools.validators.shacl import validate_data_conformance
    result = validate_data_conformance("data.jsonld", domains=["general"])
"""
