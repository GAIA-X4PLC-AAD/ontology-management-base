# Contribute

This guide describes how to add or update ontologies, shapes, and test data.

## Workflow

1. Add or update ontology artifacts under `artifacts/{domain}/`.
2. Add or update JSON-LD contexts in the same folder.
3. Add test instances under `tests/data/{domain}/`.
4. Update catalogs and registry.
5. Run validation.

## Catalog and Registry Updates

Run the updater to regenerate `docs/registry.json` and the XML catalogs:

```bash
python3 -m src.tools.utils.registry_updater
```

This updates:

- `docs/registry.json`
- `artifacts/catalog-v001.xml`
- `imports/catalog-v001.xml`
- `tests/catalog-v001.xml`

## Validation

```bash
python3 -m src.tools.validators.validation_suite --run all --domain {domain}
```

## Documentation

Generate SHACL-derived documentation:

```bash
python3 -m src.tools.utils.properties_updater
```

## Review Checklist

- Ontology IRI and version are consistent
- SHACL shapes import the ontology
- Context points to the correct W3ID namespace
- Tests cover both valid and invalid cases
- Catalogs and registry are up to date
