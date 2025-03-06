# Variables of SHACL Files in this folder

## Prefixes

- environment-model: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/environment-model/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EnvironmentModelShape | environment-model | general | 1 | 1 | General properties common for all simulation assets. |  | environment-model_shacl.ttl |
| EnvironmentModelShape | environment-model | quantity | 1 | 1 | Contains properties to describe the quantity (number of geometries, triangles, texture) of the environment-model asset. |  | environment-model_shacl.ttl |
| EnvironmentModelShape | environment-model | quality | 1 | 1 | Contains properties to describe the quality (detail level, features) of the environment-model asset. |  | environment-model_shacl.ttl |
| EnvironmentModelShape | environment-model | content | 1 | 1 | Contains properties to describe the content (elements, use cases) of the environment-model asset. |  | environment-model_shacl.ttl |
| EnvironmentModelShape | environment-model | project | 1 | 1 | Contains properties to describe the project information (software used for generation and visualisation) of the environment-model asset. |  | environment-model_shacl.ttl |
| EnvironmentModelShape | environment-model | format | 1 | 1 | Contains properties to describe the format of the environment-model asset. |  | environment-model_shacl.ttl |
| EnvironmentModelShape | environment-model | georeference | 1 | 1 | General properties for defining the location and projection of the environment-model asset. |  | environment-model_shacl.ttl |
| FormatShape | environment-model | formatType |  | 1 | Defines the data type of the environment-model asset. | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| FormatShape | environment-model | version |  | 1 | Defines the version of the environment-model asset's data type. | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| ContentShape | environment-model | elements |  | 1 | Provides a description of the visual elements contained in the environment-model asset. | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| ContentShape | environment-model | useCase |  | 1 | Defines the potential use case of the environment-model asset. | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| ProjectShape | environment-model | visualisationToolName |  | 1 | Defines the name of the visualisation tool for which the environment-model was created. | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| ProjectShape | environment-model | visualisationToolVendor |  | 1 | Defines the vendor name of the visualisation tool. | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| ProjectShape | environment-model | visualisationToolVersion |  | 1 | Defines the version of the visualisation tool. | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| ProjectShape | environment-model | creationToolName |  | 1 | Defines the name of the creation tool used to create the environment-model. | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| ProjectShape | environment-model | creationToolVendor |  | 1 | Defines the vendor name of the creation tool. | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| ProjectShape | environment-model | creationToolVersion |  | 1 | Defines the version of the creation tool. | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| QualityShape | environment-model | features | 0 | 1 | Describes the features that influence the quality of the environment-model. | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| QualityShape | environment-model | detailLevel |  | 1 | Defines the category of the level of detail. High: the highest level with additional object enrichment; Medium: derived directly from data sources with environmental context; Low: a simple topological representation. | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| QualityShape | environment-model | textureResolution | 0 | 1 | Specifies the maximum real texture resolution in metres. | <http://www.w3.org/2001/XMLSchema#float> | environment-model_shacl.ttl |
| QuantityShape | environment-model | geometryCount |  | 1 | Defines the total number of geometries (all triangles with a material assignment), counting each instance only once. | <http://www.w3.org/2001/XMLSchema#unsignedInt> | environment-model_shacl.ttl |
| QuantityShape | environment-model | triangleCount |  | 1 | Defines the total number of triangles, counting each instance only once. | <http://www.w3.org/2001/XMLSchema#unsignedInt> | environment-model_shacl.ttl |
| QuantityShape | environment-model | textureMaterialCount |  | 1 | Specifies the total number of textures used. | <http://www.w3.org/2001/XMLSchema#unsignedInt> | environment-model_shacl.ttl |
