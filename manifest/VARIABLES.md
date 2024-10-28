# Variables of SHACL Files in this folder

## Prefixes

- manifest: <https://github.com/ASCS-eV/EVES/tree/onboarding/ontologyManifest/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ManifestShape | manifest | data | 1 | 1 | Description of the content and filestructure of the uploaded asset.zip |  | manifest_shacl.ttl |
| DataShape | manifest | assetData | 1 |  | Reference to valuable data/asset as relativePath or link |  | manifest_shacl.ttl |
| DataShape | manifest | licenseType | 1 | 1 |  |  | manifest_shacl.ttl |
| DataShape | manifest | licenseData | 1 | 1 | link to licenseData as relativePath |  | manifest_shacl.ttl |
| DataShape | manifest | contentData |  |  | Reference to content data as relativePath |  | manifest_shacl.ttl |
| LinkShape | manifest | accessRole | 1 | 1 | Choose an accessRole. | <http://www.w3.org/2001/XMLSchema#string> | manifest_shacl.ttl |
| LinkShape | manifest | type | 1 | 1 | Choose type of link. | <http://www.w3.org/2001/XMLSchema#string> | manifest_shacl.ttl |
| LinkShape | manifest | format | 1 | 1 | Choose an format. | <http://www.w3.org/2001/XMLSchema#string> | manifest_shacl.ttl |
| LinkShape | manifest | relativePath | 1 | 1 | Enter link as URL or DID. | <http://www.w3.org/2001/XMLSchema#anyURI> | manifest_shacl.ttl |
