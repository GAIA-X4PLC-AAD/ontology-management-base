# Properties of SHACL Files in this folder

## Prefixes

- manifest: <https://ontologies.envited-x.net/manifest/v5/ontology#>
- rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
- scenario: <https://ontologies.envited-x.net/scenario/v5/ontology#>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ScenarioShape | scenario | hasDataResource | 1 | 1 |  |  | scenario_shacl.ttl |
| ScenarioShape | scenario | hasDataResourceExtension | 1 | 1 |  |  | scenario_shacl.ttl |
| ScenarioShape | scenario | hasManifest | 1 | 1 |  |  | scenario_shacl.ttl |
| ManifestShape | rdf | type |  |  |  |  | scenario_shacl.ttl |
| ManifestShape | manifest | hasLicense | 1 | 1 |  |  | scenario_shacl.ttl |
| ManifestShape | manifest | hasManifestReference |  |  |  |  | scenario_shacl.ttl |
| ManifestShape | manifest | hasArtifacts |  |  |  |  | scenario_shacl.ttl |
| ManifestShape | manifest | hasReferencedArtifacts |  |  |  |  | scenario_shacl.ttl |
| ManifestShape | manifest | hasArtifacts |  |  |  |  | scenario_shacl.ttl |
| ManifestShape | manifest | hasReferencedArtifacts |  |  |  |  | scenario_shacl.ttl |
| ManifestShape | manifest | hasReferencedArtifacts |  |  | Each scenario:Manifest must reference at least one HD Map. |  | scenario_shacl.ttl |
| ManifestShape | manifest | hasReferencedArtifacts |  |  | Each scenario:Manifest must reference at least one Environment Model. |  | scenario_shacl.ttl |
| ManifestShape | manifest | hasArtifacts |  |  | Each scenario:Manifest must reference at least one catalog via a manifest:Link. |  | scenario_shacl.ttl |
| DataResourceExtensionShape | scenario | hasContent | 1 | 1 |  |  | scenario_shacl.ttl |
| DataResourceExtensionShape | scenario | hasFormat | 1 | 1 |  |  | scenario_shacl.ttl |
| DataResourceExtensionShape | scenario | hasQuality | 1 | 1 |  |  | scenario_shacl.ttl |
| DataResourceExtensionShape | scenario | hasQuantity | 1 | 1 |  |  | scenario_shacl.ttl |
| DataResourceExtensionShape | scenario | hasDataSource | 1 | 1 |  |  | scenario_shacl.ttl |
| DataResourceExtensionShape | scenario | hasGeoreference | 1 | 1 |  |  | scenario_shacl.ttl |
