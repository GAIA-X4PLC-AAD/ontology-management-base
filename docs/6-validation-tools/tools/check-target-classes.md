# Target Class Validation Tool

**Module:** `src.tools.validators.coherence_validator`

This tool verifies that all SHACL target classes (`sh:targetClass`) are defined as OWL classes in the ontology.

## Purpose

SHACL shapes declare target classes that instances should be validated against. This tool ensures consistency by checking that every target class exists in the OWL ontology.

## Usage

### Command Line

```bash
# Validate by domain name (catalog-based)
python3 -m src.tools.validators.validation_suite \
  --run check-artifact-coherence \
  --domain hdmap

# Direct module invocation
python3 -m src.tools.validators.coherence_validator hdmap
```

### Programmatic Use

```python
from pathlib import Path
from src.tools.validators.coherence_validator import validate_artifact_coherence

return_code, message = validate_artifact_coherence(
    "hdmap",
    root_dir=Path("."),
)

if return_code == 0:
    print("All target classes are defined!")
else:
    print(f"Missing classes: {message}")
```

## How It Works

### 1. Extract OWL Classes

The tool parses the ontology file and extracts all class definitions:

- `owl:Class` declarations
- `rdfs:Class` declarations

### 2. Load Base Classes

External classes from `imports/` are also loaded to support references to standard ontologies (e.g., `schema:Thing`).

### 3. Extract SHACL Target Classes

From the SHACL file, the tool extracts all `sh:targetClass` values from node shapes.

### 4. Compare

The tool performs case-insensitive comparison of class local names:

- **Matches** - Target classes found in ontology
- **Missing** - Target classes not defined anywhere
- **Recovered** - Classes matched via `rdfs:label`

## Output

### Success

```
✅ Target classes are correctly defined for hdmap.
   OWL Classes: 15
   SHACL Target Classes: 12
   Matched: 12
   Missing: 0
```

### Failure

```
❌ Missing SHACL target classes:
   - unknownclass
   - anotherundefinedclass
```

## Exit Codes

| Code | Meaning                         |
| ---- | ------------------------------- |
| 0    | All target classes are defined |
| 200  | Coherence error (missing files or classes) |

## Troubleshooting

### "No ontology file found"

Ensure the file exists at the expected path:

- Check that the domain exists in `artifacts/catalog-v001.xml`
- Ensure the ontology and SHACL files referenced in the catalog exist

### Missing Class Errors

If a target class is reported missing:

1. **Check spelling** - Class names are case-insensitive but must otherwise match
2. **Check imports** - If the class is from an external ontology, ensure it's in `imports/`
3. **Add to ontology** - Define the class in the domain's ontology file
