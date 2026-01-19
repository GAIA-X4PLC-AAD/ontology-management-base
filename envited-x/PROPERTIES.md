# Properties of SHACL Files in this folder

## Prefixes

- envited-x: <https://ontologies.envited-x.net/envited-x/v3/ontology#>
- gx: <https://w3id.org/gaia-x/development/>
- manifest: <https://ontologies.envited-x.net/manifest/v5/ontology#>
- rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SimulationAssetShape | envited-x | hasDataResource | 1 | 1 |  |  | envited-x_shacl.ttl |
| SimulationAssetShape | envited-x | hasDataResourceExtension | 0 |  |  |  | envited-x_shacl.ttl |
| SimulationAssetShape | envited-x | hasManifest | 1 | 1 |  |  | envited-x_shacl.ttl |
| ExtendedLinkShape | manifest | hasAccessRole |  |  |  |  | envited-x_shacl.ttl |
| ExtendedLinkShape | manifest | hasCategory |  |  |  |  | envited-x_shacl.ttl |
| ManifestLinkReferenceShape | manifest | hasCategory |  |  |  |  | envited-x_shacl.ttl |
| ManifestLinkReferenceShape | manifest | iri | 1 |  |  |  | envited-x_shacl.ttl |
| LicenseLinkReferenceShape | manifest | hasCategory |  |  |  |  | envited-x_shacl.ttl |
| LicenseLinkReferenceShape | manifest | iri | 1 |  |  |  | envited-x_shacl.ttl |
| ManifestShape | rdf | type |  |  |  |  | envited-x_shacl.ttl |
| ManifestShape | manifest | hasManifestReference |  |  |  |  | envited-x_shacl.ttl |
| ManifestShape | manifest | hasLicense | 1 | 1 |  |  | envited-x_shacl.ttl |
| ManifestShape | manifest | hasArtifacts |  |  |  |  | envited-x_shacl.ttl |
| ManifestShape | manifest | hasReferencedArtifacts |  |  |  |  | envited-x_shacl.ttl |
| ManifestShape | manifest | hasArtifacts |  |  |  |  | envited-x_shacl.ttl |
| ManifestShape | manifest | hasArtifacts |  |  |  |  | envited-x_shacl.ttl |
| ManifestShape | manifest | hasArtifacts |  |  |  |  | envited-x_shacl.ttl |
| ManifestShape | manifest | hasArtifacts |  |  |  |  | envited-x_shacl.ttl |
| DataResourceShape | gx | name | 1 | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | envited-x_shacl.ttl |
| DataResourceShape | gx | description | 1 | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | envited-x_shacl.ttl |
| DataResourceShape | gx | license |  | 1 | Allows custom commercial identifiers in addition to Gaia-X standard SPDX checks. |  | envited-x_shacl.ttl |
| DataResourceExtensionShape | envited-x | hasContent | 1 |  |  |  | envited-x_shacl.ttl |
| DataResourceExtensionShape | envited-x | hasFormat | 1 |  |  |  | envited-x_shacl.ttl |
| DataResourceExtensionShape | envited-x | hasDataSource | 0 |  |  |  | envited-x_shacl.ttl |
| DataResourceExtensionShape | envited-x | hasQuality | 0 |  |  |  | envited-x_shacl.ttl |
| DataResourceExtensionShape | envited-x | hasQuantity | 0 |  |  |  | envited-x_shacl.ttl |
