# Validation Tools

This section documents the tools available for validating ontologies and data conformance in this repository.

## Quick Navigation

**I want to...**

- **Understand available tools** → Start with [Tools Comparison](#tools-comparison) below
- **Validate my data** → See [Getting Started with Validation](../4-getting-started/03-first-validation.md)
- **Troubleshoot validation issues** → Go to [Troubleshooting](01-troubleshooting.md)
- **Deep dive into a specific tool** → See [Tools Reference](#tools-reference) below

## Overview

This repository includes Python-based validation tools that work with OWL ontologies and SHACL shapes to:

- ✅ Validate that data conforms to ontology constraints
- ✅ Check ontology consistency and correctness
- ✅ Generate HTML documentation from ontologies
- ✅ Discover and catalog ontologies
- ✅ Optimize SHACL validation performance

All tools are located in `src/tools/` and can be run from the command line or imported as Python modules.

## Tools Comparison

| Tool                               | Purpose                                    | Input              | Output                       |
| ---------------------------------- | ------------------------------------------ | ------------------ | ---------------------------- |
| **check-artifact-coherence** | Verify SHACL target classes exist in OWL   | OWL, SHACL         | CSV report                   |
| **check-jsonld-against-shacl**     | Validate JSON-LD data against SHACL shapes | JSON-LD, SHACL     | Pass/Fail + violations       |
| **readme-generator**               | Auto-generate documentation from SHACL     | SHACL shapes       | Markdown (PROPERTIES.md)     |
| **ontology-discovery**             | Find and catalog all ontologies            | Artifact directory | JSON registry                |
| **run-all-checks**                 | Execute all validation tools               | All                | Combined report              |
| **optimize-shacl**                 | Improve SHACL validation performance       | SHACL shapes       | Optimization recommendations |

## Tools Reference

### 1. Check Target Classes Against OWL Classes

**Purpose:** Verify that all SHACL target classes are actually defined in the OWL ontology

**When to use:**

- After adding new SHACL shapes
- When validating shape consistency
- Before deploying shapes to production

**Learn more:** [check-target-classes.md](tools/check-target-classes.md)

**Quick usage:**

```bash
python3 -m src.tools.validators.validation_suite \
  --run check-artifact-coherence \
  --domain scenario
```

---

### 2. Check JSON-LD Against SHACL Schema

**Purpose:** Validate JSON-LD data instances against SHACL validation rules

**When to use:**

- Validating data before ingestion
- Quality assurance on exported datasets
- Integration testing

**Learn more:** [check-jsonld-against-shacl.md](tools/check-jsonld-against-shacl.md)

**Quick usage:**

```bash
python3 -m src.tools.validators.validation_suite \
  --run check-data-conformance \
  --domain scenario
```

---

### 3. README Generator

**Purpose:** Auto-generate human-readable documentation (PROPERTIES.md) from SHACL shapes

**When to use:**

- Creating ontology documentation
- Publishing ontologies to w3id.org
- Updating documentation after changes

**Learn more:** [readme-generator.md](tools/readme-generator.md)

**Quick usage:**

```bash
python src/tools/utils/properties_updater.py \
  --ontology artifacts/scenario/scenario.owl.ttl \
  --shacl artifacts/scenario/scenario.shacl.ttl \
  --output artifacts/scenario/PROPERTIES.md
```

---

### 4. Ontology and Shape Discovery

**Purpose:** Automatically discover and catalog all ontologies and shapes in the repository

**When to use:**

- Generating the ontology registry
- Finding ontologies by name or domain
- Understanding repository structure

**Learn more:** [ontology_and_shape_discovery.md](tools/ontology_and_shape_discovery.md)

**Quick usage:**

```bash
python -m src.tools.utils.registry_updater
```

---

### 5. Run All Checks

**Purpose:** Execute all validation tools in a single command

**When to use:**

- CI/CD pipelines
- Pre-commit hooks
- Comprehensive validation before releases

**Learn more:** [run-all-checks.md](tools/run-all-checks.md)

**Quick usage:**

```bash
python3 -m src.tools.validators.validation_suite --run all
```

---

### 6. Optimize SHACL Validation

**Purpose:** Analyze and recommend optimizations for SHACL shape performance

**When to use:**

- Validating large datasets (>100K instances)
- Performance tuning
- Understanding SHACL execution patterns

**Learn more:** [optimizing_shacl_validation_import_strategy.md](tools/optimizing_shacl_validation_import_strategy.md)

**Quick usage:**

See the optimization guide:
[optimizing_shacl_validation_import_strategy.md](tools/optimizing_shacl_validation_import_strategy.md)

---

## Common Workflows

### Workflow 1: Validate Data Quality

When you have JSON-LD data and want to check it against ontology rules:

```bash
# Validate against cataloged shapes for a domain
python3 -m src.tools.validators.validation_suite \
  --run check-data-conformance \
  --domain scenario

# Or validate specific files (temporary catalog domain)
python3 -m src.tools.validators.validation_suite \
  --run check-data-conformance \
  --path path/to/my-scenarios.jsonld
```

### Workflow 2: Generate Documentation

When you've updated an ontology and want fresh documentation:

```bash
# Generate PROPERTIES.md from SHACL shapes
python src/tools/utils/properties_updater.py \
  --ontology artifacts/scenario/scenario.owl.ttl \
  --shacl artifacts/scenario/scenario.shacl.ttl \
  --output artifacts/scenario/PROPERTIES.md

# Update the registry
python -m src.tools.utils/registry_updater
```

### Workflow 3: Pre-release Checklist

Before publishing a new ontology version:

```bash
# 1. Check shape consistency
python3 -m src.tools.validators.validation_suite \
  --run check-artifact-coherence \
  --domain my-ontology

# 2. Validate against sample data
python3 -m src.tools.validators.validation_suite \
  --run check-data-conformance \
  --domain my-ontology

# 3. Generate documentation
python src/tools/utils/properties_updater.py \
  --ontology artifacts/my-ontology/my-ontology.owl.ttl \
  --shacl artifacts/my-ontology/my-ontology.shacl.ttl \
  --output artifacts/my-ontology/PROPERTIES.md

# 4. Run full validation suite
python3 -m src.tools.validators.validation_suite \
  --run all \
  --domain my-ontology
```

### Workflow 4: CI/CD Integration

In your CI/CD pipeline (GitHub Actions, GitLab CI, etc.):

```bash
# Install dependencies
pip install -r requirements-validation.txt

# Run all checks
python3 -m src.tools.validators.validation_suite --run all

# Publish report as artifact
```

## Troubleshooting

For common validation issues and solutions, see [Troubleshooting](01-troubleshooting.md).

## Python API

All tools can be imported and used programmatically:

```python
from pathlib import Path
from src.tools.validators.conformance_validator import (
    collect_jsonld_files,
    validate_data_conformance,
)

root = Path(".")
jsonld_files = collect_jsonld_files(["tests/data/hdmap/valid/"])
return_code, message = validate_data_conformance(jsonld_files, root)

if return_code == 0:
    print("Data is valid!")
else:
    print(f"Validation failed:\n{message}")
```

## Performance Considerations

For large-scale validation:

- **Single large file**: Use built-in Python tools (fast)
- **Many small files**: Parallelize with `multiprocessing`
- **Very large datasets (>1GB)**: Consider streaming validation
- **Real-time validation**: Pre-compile shapes for faster checking

See [optimizing_shacl_validation_import_strategy.md](tools/optimizing_shacl_validation_import_strategy.md) for details.

## Contributing Tools

To add a new validation tool:

1. Create Python module in `src/tools/`
2. Implement validation logic
3. Add documentation in this section
4. Update `validation_suite.py` to include new tool
5. Submit pull request with examples

See [Building & Contributing](../5-building-contributing/01-contributing.md) for detailed guidelines.

## Related Documentation

- [First Validation](../4-getting-started/03-first-validation.md) - Hands-on tutorial
- [RDF, OWL, and SHACL](../1-foundations/02-rdf-owl-shacl.md) - Technology background
- [Troubleshooting](01-troubleshooting.md) - Common issues and solutions
- [Building & Contributing](../5-building-contributing/) - How to extend tools
