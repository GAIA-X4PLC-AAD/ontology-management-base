# Ontology Management Base - AI Assistant Instructions

This repository contains a validation suite for ontology artifacts (OWL, SHACL, JSON-LD).

## Quick Reference

Before making changes, read the relevant instruction files:

| Topic                           | File                                                                       |
| ------------------------------- | -------------------------------------------------------------------------- |
| Module structure & dependencies | [instructions/architecture.md](instructions/architecture.md)               |
| Code style & patterns           | [instructions/coding-standards.md](instructions/coding-standards.md)       |
| Validation pipeline             | [instructions/validation-workflow.md](instructions/validation-workflow.md) |
| Testing requirements            | [instructions/testing.md](instructions/testing.md)                         |
| Domain terminology              | [instructions/glossary.md](instructions/glossary.md)                       |

## Core Principles

1. **Catalog-Driven Architecture**: All file discovery goes through XML catalogs. No fallbacks to file system scanning.

2. **Single Responsibility**:
   - `registry_updater.py` → WRITES catalogs
   - `registry_resolver.py` → READS catalogs
   - `file_collector.py` → INTERNAL use by registry_updater only
   - Validators → NEVER discover files directly

3. **Fail Fast**: If a resource is not in a catalog, raise an error. No silent fallbacks.

4. **Centralized Utilities**:
   - Logging → `core/logging.py`
   - IRI string operations → `core/iri_utils.py`
   - Graph operations → `utils/graph_loader.py`
   - Path resolution → `utils/registry_resolver.py`

## Key Commands

```bash
# Run full validation suite
python3 -m src.tools.validators.validation_suite

# Validate specific domain
python3 -m src.tools.validators.validation_suite --domain manifest

# Validate arbitrary paths (creates temp catalog first)
python3 -m src.tools.validators.validation_suite --path ./my_data.json

# Run tests
pytest tests/
```

## Before You Code

1. Check which catalog(s) are involved
2. Verify the module responsibilities match the architecture
3. Use centralized utilities (don't reinvent logging, IRI parsing, etc.)
4. Add tests for new functionality
