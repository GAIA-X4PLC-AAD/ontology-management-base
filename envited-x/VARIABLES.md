# Variables of SHACL Files in this folder

## Prefixes

- envited-x: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/envited-x/>
- gx: <https://registry.lab.gaia-x.eu/development/api/trusted-shape-registry/v1/shapes/jsonld/trustframework#>
- manifest: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/manifest/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SimulationAssetShape | envited-x | hasDataResource | 1 | 1 |  |  | envited-x_shacl.ttl |
| SimulationAssetShape | envited-x | hasManifest | 1 | 1 |  |  | envited-x_shacl.ttl |
| DataResourceShape | gx | name | 1 | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | envited-x_shacl.ttl |
| DataResourceShape | gx | description | 1 | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | envited-x_shacl.ttl |
| ManifestShape | manifest | content | 4 |  |  |  | envited-x_shacl.ttl |
