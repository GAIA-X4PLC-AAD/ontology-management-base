# Variables of SHACL Files in this folder

## Prefixes

- bundleData: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/bundleData/>
- marketplaceResource: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/marketplaceResource/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BundleDataResourceShape | bundleData | requiredData | 1 |  |  |  | bundleDataResource_shacl.ttl |
| BundleDataResourceShape | bundleData | relatedData |  |  |  |  | bundleDataResource_shacl.ttl |
| RequiredDataShape | bundleData | domain | 1 | 1 | Reference to required assets |  | bundleDataResource_shacl.ttl |
| RequiredDataShape | bundleData | requiredDataLink | 1 | 1 | Reference to required data |  | bundleDataResource_shacl.ttl |
| RelatedDataShape | bundleData | domain | 1 | 1 | Reference to related assets |  | bundleDataResource_shacl.ttl |
| RelatedDataShape | bundleData | relatedDataLink | 1 | 1 | Reference to related data |  | bundleDataResource_shacl.ttl |
| DomainShape | marketplaceResource | domainType | 1 | 1 | Choose domain type. | <http://www.w3.org/2001/XMLSchema#string> | bundleDataResource_shacl.ttl |
| LinkShape | marketplaceResource | link | 1 | 1 | Enter a link or DID. | <http://www.w3.org/2001/XMLSchema#anyURI> | bundleDataResource_shacl.ttl |
