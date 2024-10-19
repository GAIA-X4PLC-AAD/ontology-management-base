# Variables of SHACL Files in this folder

## Prefixes

- bundleData: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/bundleData/>
- marketplaceResource: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/marketplaceResource/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MarketplaceResourceShape | marketplaceResource | contentData | 1 |  |  |  | marketplaceResource_shacl.ttl |
| MarketplaceResourceShape | marketplaceResource | bundleData |  |  |  |  | marketplaceResource_shacl.ttl |
| ContentDataShape | marketplaceResource | dataType | 1 | 1 | Choose type of link. | <http://www.w3.org/2001/XMLSchema#string> | marketplaceResource_shacl.ttl |
| ContentDataShape | marketplaceResource | contentData | 1 | 1 | Reference to content data |  | marketplaceResource_shacl.ttl |
| DomainShape | marketplaceResource | domainType | 1 | 1 | Choose domain type. | <http://www.w3.org/2001/XMLSchema#string> | marketplaceResource_shacl.ttl |
| LinkShape | marketplaceResource | link | 1 | 1 | Enter a link or DID. | <http://www.w3.org/2001/XMLSchema#anyURI> | marketplaceResource_shacl.ttl |
| BundleDataShape | bundleData | requiredData | 1 |  |  |  | marketplaceResource_shacl.ttl |
| BundleDataShape | bundleData | relatedData |  |  |  |  | marketplaceResource_shacl.ttl |
| RequiredDataShape | bundleData | domain | 1 | 1 | Reference to required assets |  | marketplaceResource_shacl.ttl |
| RequiredDataShape | bundleData | requiredDataLink | 1 | 1 | Reference to required data |  | marketplaceResource_shacl.ttl |
| RelatedDataShape | bundleData | domain | 1 | 1 | Reference to related assets |  | marketplaceResource_shacl.ttl |
| RelatedDataShape | bundleData | relatedDataLink | 1 | 1 | Reference to related data |  | marketplaceResource_shacl.ttl |
