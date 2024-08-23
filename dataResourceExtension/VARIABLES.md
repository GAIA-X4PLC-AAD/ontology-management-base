# Variables of SHACL Files in this folder

## Prefixes

- dataResourceExtension: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/dataResourceExtension/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DataResourceExtensionShape | dataResourceExtension | links | 1 | 1 |  |  | dataResourceExtension_shacl.ttl |
| DataResourceExtensionShape | dataResourceExtension | bundleData | 1 | 1 |  |  | dataResourceExtension_shacl.ttl |
| BundleDataShape | dataResourceExtension | requiredData |  |  | Reference to required assets |  | dataResourceExtension_shacl.ttl |
| BundleDataShape | dataResourceExtension | relatedData |  |  | Reference to optional related assets |  | dataResourceExtension_shacl.ttl |
| LinksShape | dataResourceExtension | media |  |  | Reference to media data |  | dataResourceExtension_shacl.ttl |
| LinksShape | dataResourceExtension | data | 1 | 1 | Reference to the data asset as url/uri of the EDC |  | dataResourceExtension_shacl.ttl |
| UrlShape | dataResourceExtension | type | 1 | 1 | Choose type of link. | <http://www.w3.org/2001/XMLSchema#string> | dataResourceExtension_shacl.ttl |
| UrlShape | dataResourceExtension | url | 1 | 1 | Enter link as URL or DID. | <http://www.w3.org/2001/XMLSchema#anyURI> | dataResourceExtension_shacl.ttl |
| LinkShape | dataResourceExtension | type | 1 | 1 | Choose type of link. | <http://www.w3.org/2001/XMLSchema#string> | dataResourceExtension_shacl.ttl |
| LinkShape | dataResourceExtension | link | 1 | 1 | Enter the DID . | <http://www.w3.org/2001/XMLSchema#anyURI> | dataResourceExtension_shacl.ttl |
