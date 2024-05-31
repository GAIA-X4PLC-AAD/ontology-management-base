# Variables of SHACL Files in this folder

## Prefixes

- environmentmodel: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/environmentmodel/>
- georeference: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/georeference/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| environmentModelShape | environmentmodel | quantity | 1 | 1 |  |  | environment-model_shacl.ttl |
| environmentModelShape | environmentmodel | quality | 1 | 1 |  |  | environment-model_shacl.ttl |
| environmentModelShape | environmentmodel | project | 1 | 1 |  |  | environment-model_shacl.ttl |
| environmentModelShape | environmentmodel | format | 1 | 1 |  |  | environment-model_shacl.ttl |
| environmentModelShape | georeference | georeference | 0 | 1 |  |  | environment-model_shacl.ttl |
| FormatShape | environmentmodel | type |  | 1 | Format type definition | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| FormatShape | environmentmodel | version |  | 1 | Version of data format | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| ProjectShape | environmentmodel | creationVersion |  | 1 | Tool for the creation of the data | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| ProjectShape | environmentmodel | creationSource |  | 1 | Tool for the creation of the data | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| ProjectShape | environmentmodel | softwareName |  | 1 | Name of the visual system | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| ProjectShape | environmentmodel | softwareVendor |  | 1 | Name of software vendor | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| ProjectShape | environmentmodel | version |  | 1 | Version of visual system | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| QualityShape | environmentmodel | features | 0 | 1 | Description of quality features | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| QualityShape | environmentmodel | detailLevel |  | 1 | Category of the level of detail (High - highest level of detail with additional object enrichment, Med - directly from data sources, with environment, Low - topological representation). | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| QualityShape | environmentmodel | textureResolution | 0 | 1 | Real texture resolution in meter (max?) | <http://www.w3.org/2001/XMLSchema#float> | environment-model_shacl.ttl |
| QuantityShape | environmentmodel | geometryCount |  | 1 | Total number of all geoemtries, instances are considered only once | <http://www.w3.org/2001/XMLSchema#int> | environment-model_shacl.ttl |
| QuantityShape | environmentmodel | triangleCount |  | 1 | Total number of all triangles, instances are considered only once | <http://www.w3.org/2001/XMLSchema#int> | environment-model_shacl.ttl |
| QuantityShape | environmentmodel | textureMaterialCount |  | 1 | Number of textures | <http://www.w3.org/2001/XMLSchema#unsignedInt> | environment-model_shacl.ttl |
