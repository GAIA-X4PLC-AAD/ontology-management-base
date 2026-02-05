# Tooling Index

This repository provides a small set of focused tools.

## Validators

- `validation_suite.py` orchestrates all checks
- `conformance_validator.py` runs SHACL validation
- `coherence_validator.py` checks SHACL target classes against OWL
- `syntax_validator.py` validates JSON-LD and Turtle syntax

## Registry and Catalog Tools

- `registry_updater.py` regenerates `docs/registry.json` and XML catalogs
- `registry_resolver.py` resolves domains and IRIs to file paths
- `readme_updater.py` updates README catalog tables
- `properties_updater.py` generates `PROPERTIES.md` from SHACL

## Publishing Tools

- `fc_upload_with_update.py` uploads OWL and SHACL files to the Gaia-X federated catalog

