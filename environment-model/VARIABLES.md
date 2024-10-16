# Variables of SHACL Files in this folder

## Prefixes

- environment-model: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/environment-model/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EnvironmentModelShape | environment-model | general | 1 | 1 | general object with properties for description, data, links, bundles |  | environment-model_shacl.ttl |
| EnvironmentModelShape | environment-model | quantity | 1 | 1 | quantity object with properties for quatity values |  | environment-model_shacl.ttl |
| EnvironmentModelShape | environment-model | quality | 1 | 1 | quality object with properties for quality values |  | environment-model_shacl.ttl |
| EnvironmentModelShape | environment-model | project | 1 | 1 | project object with properties for project informations |  | environment-model_shacl.ttl |
| EnvironmentModelShape | environment-model | format | 1 | 1 | format object with properties for format informations |  | environment-model_shacl.ttl |
| EnvironmentModelShape | environment-model | georeference | 0 | 1 | georeference object with properties for georeference informations |  | environment-model_shacl.ttl |
| FormatShape | environment-model | formatType |  | 1 | Data type definition | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| FormatShape | environment-model | version |  | 1 | Version of data format | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| ProjectShape | environment-model | creationVersion |  | 1 | Tool for the creation of the data | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| ProjectShape | environment-model | creationSource |  | 1 | Tool for the creation of the data | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| ProjectShape | environment-model | softwareName |  | 1 | Name of the graphics engine | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| ProjectShape | environment-model | softwareVendor |  | 1 | Name of software vendor | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| ProjectShape | environment-model | softwareVersion |  | 1 | Version of graphics engine | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| QualityShape | environment-model | features | 0 | 1 | Description of quality features | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| QualityShape | environment-model | detailLevel |  | 1 | Category of the level of detail (High - highest level of detail with additional object enrichment, Medium - directly from data sources, with environment, Low - topological representation). | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| QualityShape | environment-model | textureResolution | 0 | 1 | Real texture resolution in meter (max?) | <http://www.w3.org/2001/XMLSchema#float> | environment-model_shacl.ttl |
| QuantityShape | environment-model | geometryCount |  | 1 | Total number of all geoemtries(all triangles with a material assignment), instances are considered only once | <http://www.w3.org/2001/XMLSchema#int> | environment-model_shacl.ttl |
| QuantityShape | environment-model | triangleCount |  | 1 | Total number of all triangles, instances are considered only once | <http://www.w3.org/2001/XMLSchema#int> | environment-model_shacl.ttl |
| QuantityShape | environment-model | textureMaterialCount |  | 1 | Number of textures | <http://www.w3.org/2001/XMLSchema#unsignedInt> | environment-model_shacl.ttl |
