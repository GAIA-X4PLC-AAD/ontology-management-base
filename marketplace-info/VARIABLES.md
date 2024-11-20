# Variables of SHACL Files in this folder

## Prefixes

- marketplace-info: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/marketplace-info/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MarketplaceInfoShape | marketplace-info | domain | 1 | 1 | Marketplace compatible domain types |  | marketplace-info_shacl.ttl |
| MarketplaceInfoShape | marketplace-info | contentData | 1 |  | ContentData with direct links to the storage |  | marketplace-info_shacl.ttl |
| MarketplaceInfoShape | marketplace-info | contract | 1 | 1 | contract object with property for, id |  | marketplace-info_shacl.ttl |
| MarketplaceInfoShape | marketplace-info | bundleData |  |  | bundle object with links to required and / or related data |  | marketplace-info_shacl.ttl |
| DomainShape | marketplace-info | domain | 1 | 1 | Choose domain type. | <http://www.w3.org/2001/XMLSchema#string> | marketplace-info_shacl.ttl |
| ContentDataShape | marketplace-info | dataType | 1 | 1 | Choose type of link. | <http://www.w3.org/2001/XMLSchema#string> | marketplace-info_shacl.ttl |
| ContentDataShape | marketplace-info | contentData | 1 | 1 | Reference to content data |  | marketplace-info_shacl.ttl |
| ContractShape | marketplace-info | contractId | 1 | 1 | Contract information in regards to the data exchange component. | <http://www.w3.org/2001/XMLSchema#string> | marketplace-info_shacl.ttl |
| LinkShape | marketplace-info | link | 1 | 1 | Enter a link or DID. | <http://www.w3.org/2001/XMLSchema#anyURI> | marketplace-info_shacl.ttl |
| BundleDataShape | marketplace-info | requiredData | 0 |  | links to required data |  | marketplace-info_shacl.ttl |
| BundleDataShape | marketplace-info | relatedData | 0 |  | links to related data |  | marketplace-info_shacl.ttl |
| RequiredDataShape | marketplace-info | domain | 1 | 1 | Reference to required assets |  | marketplace-info_shacl.ttl |
| RequiredDataShape | marketplace-info | requiredDataLink | 1 | 1 | Reference to required data |  | marketplace-info_shacl.ttl |
| RelatedDataShape | marketplace-info | domain | 1 | 1 | Reference to related assets |  | marketplace-info_shacl.ttl |
| RelatedDataShape | marketplace-info | relatedDataLink | 1 | 1 | Reference to related data |  | marketplace-info_shacl.ttl |
