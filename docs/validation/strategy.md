# Validation Strategy

Validation is catalog-driven and deterministic. It prioritizes correctness and reproducibility over heuristic discovery.

## Pipeline Overview

1. Syntax validation for JSON-LD and Turtle
2. Coherence checks between SHACL target classes and OWL classes
3. SHACL conformance checks for JSON-LD instances
4. Regression checks for invalid test cases

## Catalog-Based Discovery

- Required OWL and SHACL files are resolved via XML catalogs.
- Base ontologies from `imports/` are filtered by actual usage in data.
- Fixtures are resolved via `tests/catalog-v001.xml`.

## Inference

The validation pipeline applies RDFS inference to ensure shape targeting works across subclass hierarchies.

