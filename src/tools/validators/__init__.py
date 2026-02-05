"""
Validation tools for ontology artifacts and instance data.

This package provides validators for:

1. Artifact Coherence (coherence_validator.py):
   - Validates SHACL target classes match OWL class definitions
   - Ensures consistency between ontology and shapes files

2. Data Conformance (shacl/ subpackage):
   - Validates JSON-LD instance data against SHACL shapes
   - Uses catalog-based discovery to find required ontologies
   - Applies RDFS inference before validation

3. Validation Suite (validation_suite.py):
   - Aggregates all validators (syntax + coherence + conformance)
   - Command-line entry point for running all checks

Organization:
    validators/
    ├── coherence_validator.py          (standalone validator)
    ├── conformance_validator.py        (entry point to shacl/)
    ├── validation_suite.py              (aggregator)
    └── shacl/                           (modular SHACL subsystem)
        ├── validator.py
        ├── schema_discovery.py
        └── inference.py

Key dependencies:
    - src.tools.utils.registry_resolver: Catalog-based path resolution
    - artifacts/catalog-v001.xml
    - imports/catalog-v001.xml
    - tests/catalog-v001.xml

Usage:
    # Run all validators
    python -m src.tools.validators.validation_suite --run all --domain general

    # Run specific validator
    from src.tools.validators.conformance_validator import validate_data_conformance
    result = validate_data_conformance(["data.jsonld"], root_dir=".")
"""
