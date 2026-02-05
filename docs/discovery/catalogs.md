# Catalogs and Resolution

Validation tools resolve ontologies and shapes through XML catalogs.

## Catalogs

- `artifacts/catalog-v001.xml` maps domain IRIs to OWL, SHACL, and context files
- `imports/catalog-v001.xml` maps base vocabularies used for inference
- `tests/catalog-v001.xml` maps test data and fixtures

## Resolver Behavior

`RegistryResolver` loads these catalogs and provides:

- `get_ontology_path(domain)`
- `get_shacl_paths(domain)`
- `get_context_path(domain)`
- `get_base_ontology_paths_for_iris(used_iris)`

## Why It Matters

Catalogs allow offline validation, deterministic file resolution, and consistent tooling across CI and local development.

