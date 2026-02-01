# SHACL Validation Tool

**Module:** `src.tools.validators.check_jsonld_against_shacl_schema`

This tool validates JSON-LD instance files against SHACL shapes by dynamically resolving and loading required ontology dependencies.

## Features

- **Dynamic Dependency Resolution** - Analyzes JSON-LD `@context` and `rdf:type` to identify required namespaces
- **Offline Context Resolution** - Maps remote context IRIs to local files
- **Optimized Performance** - Uses Oxigraph for fast parsing when available
- **Hybrid Inference** - Custom SPARQL-based RDFS inference

## Usage

### Command Line

```bash
# Validate a single file
python3 -m src.tools.validators.check_jsonld_against_shacl_schema \
  tests/data/hdmap/valid/hdmap_instance.json

# Validate a directory
python3 -m src.tools.validators.check_jsonld_against_shacl_schema \
  tests/data/hdmap/valid/

# With debug output
python3 -m src.tools.validators.check_jsonld_against_shacl_schema \
  tests/data/hdmap/valid/ --debug --logfile validation.log
```

### Options

| Option | Description |
|--------|-------------|
| `paths` | One or more JSON-LD files or directories to validate |
| `--root` | Root directory of the repository (default: `.`) |
| `--debug` | Enable debug logging |
| `--logfile FILE` | Write validation report to file |
| `--inference MODE` | Inference mode: `none`, `rdfs`, `owlrl`, `both` (default: `rdfs`) |
| `--force-load` | Force load all ontologies, bypassing discovery |

### Programmatic Use

```python
from src.tools.validators.check_jsonld_against_shacl_schema import (
    build_dict_for_ontologies,
    validate_jsonld_against_shacl,
)
from pathlib import Path

# Build ontology dictionary
root = Path(".")
ontology_dict = build_dict_for_ontologies(root, ["tests/data/hdmap/valid/"])

# Run validation
return_code, message = validate_jsonld_against_shacl(
    root,
    ontology_dict,
    debug=False,
    inference_mode="rdfs"
)

if return_code == 0:
    print("Validation passed!")
else:
    print(f"Validation failed: {message}")
```

## How It Works

### 1. Context Resolution

The validator scans JSON-LD files for `@context` declarations and resolves remote contexts to local files in `imports/` or domain directories.

### 2. Dependency Discovery

From the resolved contexts and `rdf:type` declarations, the validator identifies:
- Required ontology files (`*_ontology.ttl`)
- Required SHACL shapes (`*_shacl.ttl`)
- Transitive dependencies via `owl:imports`

### 3. Graph Construction

The validator builds three RDF graphs:
- **Data Graph** - Parsed from JSON-LD instances
- **Ontology Graph** - Loaded from OWL files
- **SHACL Graph** - Loaded from SHACL files

### 4. Inference

If inference is enabled (default: `rdfs`), the validator materializes inferred triples:
- Class hierarchy (`rdfs:subClassOf`)
- Property hierarchy (`rdfs:subPropertyOf`)

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

Ensure the path contains `*_instance.json` or `*_reference.json` files.

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
