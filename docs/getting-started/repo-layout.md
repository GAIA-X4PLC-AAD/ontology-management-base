# Repository Layout

This repository uses a catalog-driven layout for ontologies, imports, and tests.

## Top-Level Structure

```
artifacts/                 Domain ontologies, shapes, and contexts
imports/                   Base vocabularies for inference and validation
tests/                     Test instances and fixtures
  catalog-v001.xml         Unified test catalog
src/tools/                 Validation and publishing tools
docs/                      Documentation and registry.json
```

## Key Files

- `artifacts/catalog-v001.xml` maps domain IRIs to local OWL, SHACL, and context files.
- `imports/catalog-v001.xml` maps base vocabularies for inference.
- `tests/catalog-v001.xml` lists test data and fixtures.
- `docs/registry.json` indexes ontologies and versions for discovery.

