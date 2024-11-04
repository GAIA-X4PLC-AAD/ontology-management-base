# Variables of SHACL Files in this folder

## Prefixes

- manifest: <https://github.com/ASCS-eV/EVES/tree/onboarding/ontologyManifest/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ManifestShape | manifest | data | 1 | 1 | description of the content and filestructure of the uploaded asset |  | manifest_shacl.ttl |
| DataShape | manifest | assetData | 1 |  | reference and description to asset data and other data not falling under content data |  | manifest_shacl.ttl |
| DataShape | manifest | spdxIdentifier | 1 | 1 | any spdx identifier or LicenseRef-Custom-Commercial-Agreement or LicenseRef-Policy-Smart-ContractReference | <http://www.w3.org/2001/XMLSchema#string> | manifest_shacl.ttl |
| DataShape | manifest | licenseData | 1 | 1 | reference and description to license data |  | manifest_shacl.ttl |
| DataShape | manifest | contentData |  |  | reference and description to content data |  | manifest_shacl.ttl |
| LinkShape | manifest | accessRole | 1 | 1 | access role which is related to the corresponding data | <http://www.w3.org/2001/XMLSchema#string> | manifest_shacl.ttl |
| LinkShape | manifest | type | 1 | 1 | type of patch which is related to the corresponding data | <http://www.w3.org/2001/XMLSchema#string> | manifest_shacl.ttl |
| LinkShape | manifest | format | 1 | 1 | format of the file from the corresponding path | <http://www.w3.org/2001/XMLSchema#string> | manifest_shacl.ttl |
| LinkShape | manifest | path | 1 | 1 | Enter path as URL or DID. | <http://www.w3.org/2001/XMLSchema#anyURI> | manifest_shacl.ttl |
