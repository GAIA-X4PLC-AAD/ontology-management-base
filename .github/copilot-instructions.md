# Ontology Management Base - AI Assistant Instructions

This repository contains a validation suite for ontology artifacts (OWL, SHACL, JSON-LD).

## Quick Start Commands

```bash
# Run full validation suite
python3 -m src.tools.validators.validation_suite

# Validate specific domain
python3 -m src.tools.validators.validation_suite --domain manifest

# Validate arbitrary paths
python3 -m src.tools.validators.validation_suite --path ./my_data.json

# Run tests
pytest tests/

# Run with coverage
pytest tests/ --cov=src/tools --cov-report=html
```

## Instruction Files

Read these BEFORE making changes:

| Topic                           | File                                                                       |
| ------------------------------- | -------------------------------------------------------------------------- |
| Agent instructions              | [../AGENTS.md](../AGENTS.md)                                                |
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

## Before You Code

1. Check which catalog(s) are involved
2. Verify the module responsibilities match the architecture
3. Use centralized utilities (don't reinvent logging, IRI parsing, etc.)
4. Add tests for new functionality

## Common Mistakes to Avoid

- ❌ **Don't bypass catalogs** - Never scan the file system directly in validators
- ❌ **Don't use `file_collector.py` outside `registry_updater.py`**
- ❌ **Don't use `os.path`** - Use `pathlib.Path` instead
- ❌ **Don't silently return `None`** - Raise specific exceptions
- ❌ **Don't use `print()` for logging** - Use `logger` from `core/logging.py`

## Key Imports

```python
# Logging
from src.tools.core.logging import get_logger
logger = get_logger(__name__)

# Path resolution (READ from catalogs)
from src.tools.utils.registry_resolver import RegistryResolver

# Graph loading
from src.tools.utils.graph_loader import load_graph, load_jsonld_files

# Return codes
from src.tools.core.result import ReturnCodes, ValidationResult
```
