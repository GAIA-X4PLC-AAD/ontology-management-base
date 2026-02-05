# Search and Discovery

Ontology discovery is catalog-driven and supported by `docs/registry.json`.

## Discovery Sources

- `docs/registry.json` indexes domains, versions, and file paths
- XML catalogs resolve IRIs to local files for validation
- The documentation site search indexes the catalog table

## Quick Searches

Search by domain name:

```bash
jq -r '.ontologies | keys[]' docs/registry.json
```

Search by IRI substring:

```bash
jq -r '.ontologies | to_entries[] | select(.value.iri | contains("hdmap")) | .key' docs/registry.json
```

## Programmatic Access

Use `src.tools.utils.registry_resolver.RegistryResolver` to resolve domains to paths inside tools and scripts.

