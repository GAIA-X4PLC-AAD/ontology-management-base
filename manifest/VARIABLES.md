# Variables of SHACL Files in this folder

## Prefixes

- manifest: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/manifest/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ManifestShape | manifest | data | 1 | 1 | Description of the content and filestructure of the uploaded asset |  | manifest_shacl.ttl |
| ManifestShape | manifest | license | 1 | 1 | Description of the license of the uploaded asset |  | manifest_shacl.ttl |
| DataShape | manifest | assetData | 1 |  | Reference and description to asset data and other data not falling under content data |  | manifest_shacl.ttl |
| DataShape | manifest | contentData |  |  | Reference and description to content data |  | manifest_shacl.ttl |
| LicenseShape | manifest | spdxIdentifier | 1 | 1 | Any spdx identifier or LicenseRef-Custom-Commercial-Agreement or LicenseRef-Policy-Smart-Contract | <http://www.w3.org/2001/XMLSchema#string> | manifest_shacl.ttl |
| LicenseShape | manifest | licenseData | 1 | 1 | Reference and description to license data |  | manifest_shacl.ttl |
| LinkShape | manifest | accessRole | 1 | 1 | Access role which is related to the corresponding data | <http://www.w3.org/2001/XMLSchema#string> | manifest_shacl.ttl |
| LinkShape | manifest | type | 1 | 1 | Type of patch which is related to the corresponding data | <http://www.w3.org/2001/XMLSchema#string> | manifest_shacl.ttl |
| LinkShape | manifest | format | 1 | 1 | Format of the file from the corresponding path | <http://www.w3.org/2001/XMLSchema#string> | manifest_shacl.ttl |
| LinkShape | manifest | path | 1 | 1 | Enter path as url or did. | <http://www.w3.org/2001/XMLSchema#anyURI> | manifest_shacl.ttl |
