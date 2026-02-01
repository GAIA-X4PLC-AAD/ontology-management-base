# Validation Tools Catalog

This section documents the validation tools available in the Ontology Management Base.

## Overview

The validation pipeline consists of several components that work together to ensure ontology quality:

```mermaid
graph LR
    A[JSON-LD Instance] --> B[Syntax Check]
    B --> C[SHACL Validation]
    C --> D[Target Class Check]
    D --> E[✓ Valid]
```

## Available Tools

### Core Validators

| Tool                                          | Purpose                                          | Documentation                            |
| --------------------------------------------- | ------------------------------------------------ | ---------------------------------------- |
| `check_jsonld_against_shacl_schema.py`        | Validates JSON-LD instances against SHACL shapes | [Details](check-jsonld-against-shacl.md) |
| `check_target_classes_against_owl_classes.py` | Verifies SHACL target classes exist in OWL       | [Details](check-target-classes.md)       |
| `run_all_checks_locally.py`                   | Orchestrates all validation checks               | [Details](run-all-checks.md)             |

### Documentation Tools

| Tool                         | Purpose                            | Documentation                  |
| ---------------------------- | ---------------------------------- | ------------------------------ |
| `properties_md_generator.py` | Generates PROPERTIES.md from SHACL | [Details](readme-generator.md) |

## Quick Reference

### Run All Checks

```bash
python3 -m src.tools.validators.run_all_checks_locally --check all
```

### Run Specific Check

```bash
# Syntax only
python3 -m src.tools.validators.run_all_checks_locally --check syntax

# SHACL only
python3 -m src.tools.validators.run_all_checks_locally --check shacl

# Target classes only
python3 -m src.tools.validators.run_all_checks_locally --check target-classes

# Failing tests only
python3 -m src.tools.validators.run_all_checks_locally --check failing-tests
```

### Run for Specific Domain

```bash
python3 -m src.tools.validators.run_all_checks_locally --check all --domain hdmap scenario
```

## Exit Codes

| Code    | Meaning                          |
| ------- | -------------------------------- |
| 0       | Success - all validations passed |
| 1       | General error                    |
| 100     | No files found                   |
| 101-102 | Data graph loading errors        |
| 200     | Target class validation failure  |
| 210     | SHACL validation failure         |

## CI Integration

The validation tools are integrated into the CI pipeline via GitHub Actions. See `.github/workflows/ci.yml` for the workflow definition.

### Workflow Jobs

1. **Standards & Syntax** - Runs linting and syntax checks
2. **SHACL Validation** - Validates instances against shapes
3. **OWL Classes** - Checks target class consistency
4. **Regression Tests** - Runs failing test cases
5. **Documentation** - Generates PROPERTIES.md files
