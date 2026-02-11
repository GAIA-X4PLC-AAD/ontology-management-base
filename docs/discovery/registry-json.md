# registry.json Index

`docs/registry.json` is the canonical index of maintained ontology domains,
versions, and file paths (artifacts only). Base imports are resolved through
`imports/catalog-v001.xml`.

## Structure

Each domain entry provides:

- `namespace` for the owning namespace
- `latest` for the current version
- `iri` for the W3ID base IRI
- `versions` mapping to local files
- `versionInfo` and `versionIri` per version (from ontology metadata)

Example snippet:

```json
{
  "version": "2.1.0",
  "latestRelease": "v0.1.0",
  "ontologies": {
    "automotive-simulator": {
      "namespace": "gaia-x4plcaad",
      "iri": "https://w3id.org/gaia-x4plcaad/ontologies/automotive-simulator/v2",
      "latest": "v2",
      "versions": {
        "v2": {
          "releaseTag": "v0.1.0",
          "versionInfo": "v2",
          "versionIri": "https://w3id.org/gaia-x4plcaad/ontologies/automotive-simulator/v2",
          "files": {
            "ontology": "artifacts/automotive-simulator/automotive-simulator.owl.ttl",
            "shacl": [
              "artifacts/automotive-simulator/automotive-simulator.shacl.ttl"
            ],
            "properties": "artifacts/automotive-simulator/PROPERTIES.md",
            "instance": "tests/data/automotive-simulator/valid/automotive-simulator_instance.json"
          }
        }
      }
    }
  }
}
```

## Regeneration

```bash
python3 -m src.tools.utils.registry_updater
```
