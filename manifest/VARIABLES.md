# Variables of SHACL Files in this folder

## Prefixes

- manifest: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/manifest/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ManifestShape | manifest | data | 1 | 1 | Description of the content and file structure of the uploaded asset |  | manifest_shacl.ttl |
| ManifestShape | manifest | license | 1 | 1 | Description of the license of the uploaded asset |  | manifest_shacl.ttl |
| DataShape | manifest | assetData | 1 |  | Reference and description to asset data and other data not falling under content data |  | manifest_shacl.ttl |
| DataShape | manifest | contentData |  |  | Reference and description to content data |  | manifest_shacl.ttl |
| LicenseShape | manifest | spdxIdentifier | 1 | 1 | Any spdx identifier or LicenseRef-Custom-Commercial-Agreement or LicenseRef-Policy-Smart-Contract | <http://www.w3.org/2001/XMLSchema#string> | manifest_shacl.ttl |
| LicenseShape | manifest | licenseData | 1 | 1 | Reference and description to license data |  | manifest_shacl.ttl |
| LinkShape | manifest | accessRole | 1 | 1 | Access role which is related to the corresponding data | <http://www.w3.org/2001/XMLSchema#string> | manifest_shacl.ttl |
| LinkShape | manifest | type | 1 | 1 | Type of path which is related to the corresponding data | <http://www.w3.org/2001/XMLSchema#string> | manifest_shacl.ttl |
| LinkShape | manifest | fileMetaData | 1 | 1 | Metadata description of the uploaded file |  | manifest_shacl.ttl |
| FileMetaDataShape | manifest | uri | 1 | 1 | Enter path as url or did. | <http://www.w3.org/2001/XMLSchema#anyURI> | manifest_shacl.ttl |
| FileMetaDataShape | manifest | hash | 0 | 1 | Enter the IPFS CIDv1 identifier of the file. | <http://www.w3.org/2001/XMLSchema#string> | manifest_shacl.ttl |
| FileMetaDataShape | manifest | mimeType | 0 | 1 | Enter the MIME type of the file. | <http://www.w3.org/2001/XMLSchema#string> | manifest_shacl.ttl |
| FileMetaDataShape | manifest | dimensions | 0 | 1 | If you are describing an image or video, please fill out this shape |  | manifest_shacl.ttl |
| FileMetaDataShape | manifest | fileSize | 0 | 1 | Enter the file size in bytes. | <http://www.w3.org/2001/XMLSchema#integer> | manifest_shacl.ttl |
| FileMetaDataShape | manifest | filename | 0 | 1 | Enter the filename including its extension. | <http://www.w3.org/2001/XMLSchema#string> | manifest_shacl.ttl |
| DimensionsShape | manifest | unit | 1 | 1 | Specify the unit of measurement (e.g., meters, inches). | <http://www.w3.org/2001/XMLSchema#string> | manifest_shacl.ttl |
| DimensionsShape | manifest | width | 1 | 1 | Enter the width of the item in appropriate units. | <http://www.w3.org/2001/XMLSchema#decimal> | manifest_shacl.ttl |
| DimensionsShape | manifest | length | 1 | 1 | Enter the length of the item in appropriate units. | <http://www.w3.org/2001/XMLSchema#decimal> | manifest_shacl.ttl |
