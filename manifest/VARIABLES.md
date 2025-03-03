# Variables of SHACL Files in this folder

## Prefixes

- manifest: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/manifest/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ManifestShape | manifest | data | 1 | 1 | Defines the data components of the simulation asset. |  | manifest_shacl.ttl |
| ManifestShape | manifest | license | 1 | 1 | Defines the license of the simulation asset. |  | manifest_shacl.ttl |
| DataShape | manifest | assetData | 1 |  | Defines links to the asset and to other data that is not classified as content data. |  | manifest_shacl.ttl |
| DataShape | manifest | contentData |  |  | Defines links to content data. |  | manifest_shacl.ttl |
| LicenseShape | manifest | spdxIdentifier | 1 | 1 | Define a SPDX identifier, such as LicenseRef-Custom-Commercial-Agreement or LicenseRef-Policy-Smart-Contract. | <http://www.w3.org/2001/XMLSchema#string> | manifest_shacl.ttl |
| LicenseShape | manifest | licenseData | 1 | 1 | Defines a link to license data. |  | manifest_shacl.ttl |
| LinkShape | manifest | accessRole | 1 | 1 | Specifies the access role associated with the corresponding file. | <http://www.w3.org/2001/XMLSchema#string> | manifest_shacl.ttl |
| LinkShape | manifest | type | 1 | 1 | Specifies the data type of the corresponding file. | <http://www.w3.org/2001/XMLSchema#string> | manifest_shacl.ttl |
| LinkShape | manifest | fileMetaData | 1 | 1 | Defines a general class for a data file that is referenced via a link. |  | manifest_shacl.ttl |
| FileMetaDataShape | manifest | uri | 1 | 1 | Defines a path as url or did. | <http://www.w3.org/2001/XMLSchema#anyURI> | manifest_shacl.ttl |
| FileMetaDataShape | manifest | hash | 0 | 1 | Defines the IPFS CIDv1 identifier of the file. | <http://www.w3.org/2001/XMLSchema#string> | manifest_shacl.ttl |
| FileMetaDataShape | manifest | mimeType | 0 | 1 | Defines the MIME type of the file. | <http://www.w3.org/2001/XMLSchema#string> | manifest_shacl.ttl |
| FileMetaDataShape | manifest | dimensions | 0 | 1 | Define the dimensional information for images and videos. |  | manifest_shacl.ttl |
| FileMetaDataShape | manifest | fileSize | 0 | 1 | Specify the file size in bytes. | <http://www.w3.org/2001/XMLSchema#integer> | manifest_shacl.ttl |
| FileMetaDataShape | manifest | filename | 0 | 1 | Specifies the file name (excluding the path) along with its extension. | <http://www.w3.org/2001/XMLSchema#string> | manifest_shacl.ttl |
| DimensionsShape | manifest | unit | 1 | 1 | Specifies the unit of measurement (e.g., meters, inches). | <http://www.w3.org/2001/XMLSchema#string> | manifest_shacl.ttl |
| DimensionsShape | manifest | width | 1 | 1 | Specifies the width (x-axis) of the item in appropriate units. | <http://www.w3.org/2001/XMLSchema#decimal> | manifest_shacl.ttl |
| DimensionsShape | manifest | length | 1 | 1 | Specifies the length (y-axis) of the item in appropriate units. | <http://www.w3.org/2001/XMLSchema#decimal> | manifest_shacl.ttl |
