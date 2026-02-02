# SHACL Validation Tool

**Module:** `src.tools.validators.conformance_validator`

This tool validates JSON-LD instance files against SHACL shapes by dynamically resolving and loading required ontology dependencies.

## Features

- **Dynamic Schema Discovery** - Uses RDF types, predicates, and datatypes to select required schemas
- **Catalog-Based Resolution** - Resolves ontologies and shapes via XML catalogs
- **Base Ontology Filtering** - Loads only base vocabularies actually used in the data
- **Fixture Resolution** - Loads `did:web:` fixtures from the tests catalog
- **Optimized Performance** - Uses Oxigraph for fast parsing when available

## Usage

### Command Line

```bash
# Validate a single file (catalog-based)
python3 -m src.tools.validators.validation_suite \
  --run check-data-conformance \
  --path tests/data/hdmap/valid/hdmap_instance.json

# Validate a domain from the catalog
python3 -m src.tools.validators.validation_suite \
  --run check-data-conformance \
  --domain hdmap

# Direct module invocation (paths only)
python3 -m src.tools.validators.conformance_validator \
  tests/data/hdmap/valid/
```

### Options

| Option | Description |
|--------|-------------|
| `paths` | One or more JSON-LD files or directories to validate |
| `--root` | Root directory of the repository (default: `.`) |
| `--debug` | Enable debug logging |
| `--logfile FILE` | Write validation report to file |
| `--inference MODE` | Inference mode: `none`, `rdfs`, `owlrl`, `both` (default: `rdfs`) |

### Programmatic Use

```python
from pathlib import Path
from src.tools.validators.conformance_validator import (
    collect_jsonld_files,
    validate_data_conformance,
)

root = Path(".")
jsonld_files = collect_jsonld_files(["tests/data/hdmap/valid/"])

# Run validation
return_code, message = validate_data_conformance(
    jsonld_files,
    root,
    inference_mode="rdfs",
)

if return_code == 0:
    print("Validation passed!")
else:
    print(f"Validation failed: {message}")
```

## How It Works

### 1. Data Loading

JSON-LD files are parsed into a data graph. Any `did:web:` references are resolved via the tests catalog and loaded as fixtures.

### 2. Schema Discovery

The validator extracts RDF types, predicates, and datatypes, then resolves the required OWL and SHACL files via `artifacts/catalog-v001.xml`.
Base vocabularies from `imports/catalog-v001.xml` are filtered to only the namespaces actually used by the data.

### 3. Graph Construction

The validator builds three RDF graphs:
- **Data Graph** - Parsed from JSON-LD instances (plus fixtures)
- **Ontology Graph** - Loaded from OWL files discovered via the catalog
- **SHACL Graph** - Loaded from SHACL files discovered via the catalog

### 4. Inference

If inference is enabled (default: `rdfs`), inferred triples are materialized before validation.

### 5. Validation

PySHACL validates the data graph against the SHACL graph, with the ontology graph providing class definitions.

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Validation passed |
| 99 | PySHACL not installed |
| 100 | No valid files found |
| 101 | No files loaded |
| 102 | Empty data graph |
| 210 | SHACL validation failed |

## Troubleshooting

### "No valid files found"

Ensure the path contains `.json` or `.jsonld` files.

### "SHACL validation failed"

Check the validation report for specific constraint violations. Common issues:
- Missing required properties (MinCount)
- Invalid property values (Datatype)
- Wrong node types (NodeKind)

### Performance Issues

Install `oxrdflib` for faster parsing:

```bash
pip install oxrdflib
```
