# Properties of SHACL Files in this folder

## Prefixes

- manifest: <https://ontologies.envited-x.net/manifest/v5/ontology#>
- scenario: <https://ontologies.envited-x.net/scenario/v5/ontology#>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ScenarioShape | scenario | hasDataResource | 1 | 1 |  |  | scenario_shacl.ttl |
| ScenarioShape | scenario | hasDataResourceExtension | 1 | 1 |  |  | scenario_shacl.ttl |
| ScenarioShape | scenario | hasManifest | 1 | 1 |  |  | scenario_shacl.ttl |
| ScenarioManifestConstraints | manifest | hasReferencedArtifacts |  |  |  |  | scenario_shacl.ttl |
| DataResourceExtensionShape | scenario | hasContent | 1 | 1 |  |  | scenario_shacl.ttl |
| DataResourceExtensionShape | scenario | hasFormat | 1 | 1 |  |  | scenario_shacl.ttl |
| DataResourceExtensionShape | scenario | hasQuality | 1 | 1 |  |  | scenario_shacl.ttl |
| DataResourceExtensionShape | scenario | hasQuantity | 1 | 1 |  |  | scenario_shacl.ttl |
| DataResourceExtensionShape | scenario | hasDataSource | 1 | 1 |  |  | scenario_shacl.ttl |
| DataResourceExtensionShape | scenario | hasGeoreference | 1 | 1 |  |  | scenario_shacl.ttl |
| FormatShape | scenario | formatType | 1 |  |  | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| FormatShape | scenario | version | 1 |  |  | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| ContentShape | scenario | abstractionLevel |  |  |  |  | scenario_shacl.ttl |
| ContentShape | scenario | country |  |  |  | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| ContentShape | scenario | aim |  |  |  | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| ContentShape | scenario | movementDescription |  |  |  | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| ContentShape | scenario | customCommands |  |  |  | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| QuantityShape | scenario | numberTrafficObjects |  |  |  | <http://www.w3.org/2001/XMLSchema#unsignedInt> | scenario_shacl.ttl |
| QuantityShape | scenario | permanentTrafficObjects |  |  |  | <http://www.w3.org/2001/XMLSchema#unsignedInt> | scenario_shacl.ttl |
| QuantityShape | scenario | temporaryTrafficObjects |  |  |  | <http://www.w3.org/2001/XMLSchema#unsignedInt> | scenario_shacl.ttl |
| QuantityShape | scenario | controllers |  |  |  | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| QualityShape | scenario | accuracyObjects |  |  |  | <http://www.w3.org/2001/XMLSchema#float> | scenario_shacl.ttl |
| QualityShape | scenario | calibration |  |  |  | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| DataSourceShape | scenario | sourceType | 1 |  |  | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| DataSourceShape | scenario | sourceDescription |  |  |  | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
