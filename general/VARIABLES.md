# Variables of SHACL Files in this folder

## Prefixes

- general: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/general/>
- gx: <https://registry.lab.gaia-x.eu/development/api/trusted-shape-registry/v1/shapes/jsonld/trustframework#>
- manifest: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/manifest/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SimulationAssetShape | general | hasMetadata | 1 | 1 |  |  | general_shacl.ttl |
| SimulationAssetShape | general | hasManifest | 1 | 1 |  |  | general_shacl.ttl |
| MetadataShape | gx | name | 1 | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | general_shacl.ttl |
| MetadataShape | gx | description | 1 | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | general_shacl.ttl |
| ExtendedManifestShape | manifest | content | 4 |  |  |  | general_shacl.ttl |
