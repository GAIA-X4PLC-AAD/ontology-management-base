# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Central repository for **Gaia-X 25.11 compliant ontologies** for the ENVITED-X Ecosystem. Provides OWL ontology definitions, SHACL validation shapes, JSON-LD context files, and a Python validation suite.

**Key URLs:**
- Documentation: https://gaia-x4plc-aad.github.io/ontology-management-base/
- Repository: https://github.com/gaia-x4plc-aad/ontology-management-base

## Essential Commands

```bash
# Install (dev mode with pre-commit hooks)
pip install -e ".[dev]" && pre-commit install

# Run full validation suite
python3 -m src.tools.validators.validation_suite

# Validate specific domain(s)
python3 -m src.tools.validators.validation_suite --domain manifest hdmap

# Validate arbitrary files (for pre-commit)
python3 -m src.tools.validators.validation_suite --path ./my_data.json

# Run tests with coverage
pytest tests/ --cov=src/tools --cov-report=html

# Lint and format
make lint       # pre-commit on all files
make format     # black + isort on src/

# Local docs server
DOCS_SITE_URL=http://127.0.0.1:8000/ontology-management-base mkdocs serve

# Update catalogs after artifact changes
python3 -m src.tools.utils.registry_updater
```

## Architecture

### Module Hierarchy

```
src/tools/
├── core/           # Foundation (no internal deps) - constants, logging, result codes, IRI utils
├── utils/          # Catalog I/O + graph loading - depends on core/
└── validators/     # Validation CLI - depends on core/ + utils/
```

**Dependency rule:** Never import upward (utils cannot import from validators).

### Catalog-Driven Design

All file discovery goes through XML catalogs. Validators never scan the filesystem directly.

| Module | Responsibility |
|--------|----------------|
| `registry_updater.py` | WRITES catalogs, uses `file_collector.py` for discovery |
| `registry_resolver.py` | READS catalogs, resolves IRIs to paths |
| `file_collector.py` | Shared file discovery utilities (used by updater + validators) |

### Catalog Locations

- `artifacts/catalog-v001.xml` - Ontology IRIs → local OWL/SHACL/context files
- `imports/catalog-v001.xml` - Base ontologies (RDF, RDFS, OWL, SKOS)
- `tests/catalog-v001.xml` - Test data files + fixtures (mock external refs)

### Validation Pipeline

Four checks in sequence:
1. **check-syntax** - JSON/Turtle well-formedness
2. **check-artifact-coherence** - SHACL targets exist in OWL (domain mode only)
3. **check-data-conformance** - SHACL validation of instance data
4. **check-failing-tests** - Invalid data fails as expected (domain mode only)

## Key Imports

```python
from src.tools.core.logging import get_logger
from src.tools.core.result import ReturnCodes, ValidationResult
from src.tools.utils.registry_resolver import RegistryResolver
from src.tools.utils.graph_loader import load_graph, load_jsonld_files

logger = get_logger(__name__)
```

## File Types

| Extension | Purpose |
|-----------|---------|
| `.owl.ttl` | OWL ontology definitions |
| `.shacl.ttl` | SHACL validation shapes |
| `.context.jsonld` | JSON-LD context files |
| `.expected` | Expected output for invalid test data |

## Coding Conventions

- **Python 3.12+** with type hints on public APIs
- **pathlib.Path** (never `os.path`)
- **Centralized logging** via `get_logger(__name__)`; reserve `print()` for final user output
- **Fail fast** - raise specific exceptions, no silent `None` returns
- **Test naming** - `test_{function}_{scenario}_{expected}`
- **Import order** - stdlib, third-party, local core, local utils

## Instruction Files

Read these before making changes:

| Topic | File |
|-------|------|
| Module structure | `.github/instructions/architecture.md` |
| Code style | `.github/instructions/coding-standards.md` |
| Validation pipeline | `.github/instructions/validation-workflow.md` |
| Testing requirements | `.github/instructions/testing.md` |
| Domain terminology | `.github/instructions/glossary.md` |

## Change Documentation

When making changes to the codebase, always update these two files in `.playground/` (gitignored):

| File | Purpose |
|------|---------|
| `.playground/change-summary.md` | Detailed markdown summary of all changes grouped by severity/category, including file paths, problem descriptions, and fixes applied |
| `.playground/commit-message.md` | Conventional commit message with bullet points, ready for copy-paste into `git commit` |

Update both files **before** presenting the final result to the user. If a session involves multiple rounds of changes, keep these files in sync with the cumulative state.

## Common Mistakes to Avoid

- Bypassing catalogs with direct filesystem scanning in validators
- Using `os.path` instead of `pathlib.Path`
- Silent `None` returns instead of raising exceptions
- Using `print()` for internal progress (use `logger`)
