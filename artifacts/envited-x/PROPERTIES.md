# Properties of SHACL Files for envited-x

## Prefixes

- envited-x: <https://w3id.org/ascs-ev/envited-x/envited-x/v3/>
- gx: <https://w3id.org/gaia-x/development/>
- manifest: <https://w3id.org/ascs-ev/envited-x/manifest/v5/>
- rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SimulationAssetShape | envited-x | hasDataResource | 1 | 1 |  |  | envited-x.shacl.ttl |
| SimulationAssetShape | envited-x | hasDataResourceExtension | 0 |  |  |  | envited-x.shacl.ttl |
| SimulationAssetShape | envited-x | hasManifest | 1 | 1 |  |  | envited-x.shacl.ttl |
| ExtendedLinkShape | manifest | hasAccessRole |  |  |  |  | envited-x.shacl.ttl |
| ExtendedLinkShape | manifest | hasCategory |  |  |  |  | envited-x.shacl.ttl |
| ManifestLinkReferenceShape | manifest | hasCategory |  |  |  |  | envited-x.shacl.ttl |
| ManifestLinkReferenceShape | manifest | iri | 1 |  |  |  | envited-x.shacl.ttl |
| LicenseLinkReferenceShape | manifest | hasCategory |  |  |  |  | envited-x.shacl.ttl |
| LicenseLinkReferenceShape | manifest | iri | 1 |  |  |  | envited-x.shacl.ttl |
| ManifestShape | rdf | type |  |  |  |  | envited-x.shacl.ttl |
| ManifestShape | manifest | hasManifestReference |  |  |  |  | envited-x.shacl.ttl |
| ManifestShape | manifest | hasLicense | 1 | 1 |  |  | envited-x.shacl.ttl |
| ManifestShape | manifest | hasArtifacts |  |  |  |  | envited-x.shacl.ttl |
| ManifestShape | manifest | hasReferencedArtifacts |  |  |  |  | envited-x.shacl.ttl |
| ManifestShape | manifest | hasArtifacts |  |  |  |  | envited-x.shacl.ttl |
| ManifestShape | manifest | hasArtifacts |  |  |  |  | envited-x.shacl.ttl |
| ManifestShape | manifest | hasArtifacts |  |  |  |  | envited-x.shacl.ttl |
| ManifestShape | manifest | hasArtifacts |  |  |  |  | envited-x.shacl.ttl |
| DataResourceShape | gx | name | 1 | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | envited-x.shacl.ttl |
| DataResourceShape | gx | description | 1 | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | envited-x.shacl.ttl |
| DataResourceShape | gx | license |  | 1 | Allows custom commercial identifiers in addition to Gaia-X standard SPDX checks. |  | envited-x.shacl.ttl |
| DataResourceExtensionShape | envited-x | hasContent | 1 |  |  |  | envited-x.shacl.ttl |
| DataResourceExtensionShape | envited-x | hasFormat | 1 |  |  |  | envited-x.shacl.ttl |
| DataResourceExtensionShape | envited-x | hasDataSource | 0 |  |  |  | envited-x.shacl.ttl |
| DataResourceExtensionShape | envited-x | hasQuality | 0 |  |  |  | envited-x.shacl.ttl |
| DataResourceExtensionShape | envited-x | hasQuantity | 0 |  |  |  | envited-x.shacl.ttl |
