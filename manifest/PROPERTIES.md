# Properties of SHACL Files in this folder

## Prefixes

- gx: <https://registry.lab.gaia-x.eu/development/api/trusted-shape-registry/v1/shapes/jsonld/trustframework#>
- manifest: <https://ontologies.envited-x.net/manifest/v5/ontology#>
- sh: <http://www.w3.org/ns/shacl#>
- skos: <http://www.w3.org/2004/02/skos/core#>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ManifestShape | manifest | hasManifestReference | 1 | 1 | Self-reference to the manifest.json providing the structure and list of contents for a domain specific asset. |  | manifest_shacl.ttl |
| ManifestShape | manifest | hasLicense | 1 | 1 | Defines the license valid for all content referenced in the manifest. Does not apply to linked data(sets) with explicit license terms. |  | manifest_shacl.ttl |
| ManifestShape | manifest | hasArtifacts | 1 |  | Defines the links to all relevant artifacts for a digital asset. This is extended by the domain specific ontology. |  | manifest_shacl.ttl |
| ManifestShape | manifest | hasReferencedArtifacts | 0 |  | Defines the links to all related referenced artifacts for a digital asset. This is extended by the domain specific ontology. |  | manifest_shacl.ttl |
| LicenseShape | gx | license | 1 | 1 | Reuses SPDX constraints from Gaia-X Trust Framework, with additional custom constraints. |  | manifest_shacl.ttl |
| LicenseShape | manifest | hasLink | 1 | 1 | Defines a link to the licensing terms. |  | manifest_shacl.ttl |
| LinkShape | manifest | iri | 0 | 1 | IRI required if the file is RDF/JSON-LD. | <http://www.w3.org/ns/shacl#IRI> | manifest_shacl.ttl |
| LinkShape | skos | note | 0 | 1 | Additional information about the manifest reference. | <http://www.w3.org/2001/XMLSchema#string> | manifest_shacl.ttl |
| LinkShape | sh | conformsTo | 0 |  | Specifies ontology conformance. | <http://www.w3.org/ns/shacl#IRI> | manifest_shacl.ttl |
| LinkShape | manifest | hasAccessRole | 1 | 1 |  |  | manifest_shacl.ttl |
| LinkShape | manifest | hasCategory | 1 | 1 | Specifies artifact category. |  | manifest_shacl.ttl |
| LinkShape | manifest | hasFileMetadata | 1 | 1 |  |  | manifest_shacl.ttl |
| FileMetadataShape | manifest | filePath | 1 | 1 | A local or remote path/URL from which the file can be retrieved (e.g. './manifest_reference.json', 'ipfs://...', 's3://...', 'https://...'). | <http://www.w3.org/2001/XMLSchema#anyURI> | manifest_shacl.ttl |
| FileMetadataShape | manifest | mimeType | 1 | 1 | Defines the MIME type of the file. | <http://www.w3.org/2001/XMLSchema#string> | manifest_shacl.ttl |
| FileMetadataShape | manifest | cid | 0 | 1 | Defines the IPFS CIDv1 identifier of the file. | <http://www.w3.org/2001/XMLSchema#string> | manifest_shacl.ttl |
| FileMetadataShape | manifest | fileSize | 0 | 1 | Specifies the file size in bytes. | <http://www.w3.org/2001/XMLSchema#integer> | manifest_shacl.ttl |
| FileMetadataShape | manifest | filename | 0 | 1 | Specifies the file name (excluding the path) along with its extension. | <http://www.w3.org/2001/XMLSchema#string> | manifest_shacl.ttl |
| FileMetadataShape | manifest | timestamp | 0 | 1 | Represents a date or time associated with the file, such as recording time or creation time. | <http://www.w3.org/2001/XMLSchema#dateTime> | manifest_shacl.ttl |
| FileMetadataShape | manifest | hasDimensions | 0 | 1 | Defines the dimensions for images and videos. |  | manifest_shacl.ttl |
| DimensionsShape | manifest | unit | 1 | 1 | Specifies the unit of measurement (e.g., metres, inches). |  | manifest_shacl.ttl |
| DimensionsShape | manifest | width | 1 | 1 | Specifies the width (x-axis) of the item in appropriate units. | <http://www.w3.org/2001/XMLSchema#float> | manifest_shacl.ttl |
| DimensionsShape | manifest | height | 1 | 1 | Specifies the height (y-axis) of the item in appropriate units. | <http://www.w3.org/2001/XMLSchema#float> | manifest_shacl.ttl |
| DimensionsShape | manifest | depth | 0 | 1 | Specifies the depth (z-axis) of the item in appropriate units. | <http://www.w3.org/2001/XMLSchema#float> | manifest_shacl.ttl |
