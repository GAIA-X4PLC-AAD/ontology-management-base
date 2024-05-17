# Variables of SHACL Files in this folder

## Prefixes

- environment-model: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/environment-model/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EnvironmentModelShape | environment-model | quantity | 1 | 1 |  |  | environment-model_shacl.ttl |
| EnvironmentModelShape | environment-model | quality | 1 | 1 |  |  | environment-model_shacl.ttl |
| EnvironmentModelShape | environment-model | project | 1 | 1 |  |  | environment-model_shacl.ttl |
| EnvironmentModelShape | environment-model | format | 1 | 1 |  |  | environment-model_shacl.ttl |
| EnvironmentModelShape | environment-model | georeference | 1 | 1 |  |  | environment-model_shacl.ttl |
| GeoreferenceShape | environment-model | projectLocation | 1 | 1 |  |  | environment-model_shacl.ttl |
| GeoreferenceShape | environment-model | geodeticReferenceSystem | 1 | 1 |  |  | environment-model_shacl.ttl |
| GeodeticReferenceSystemShape | environment-model | origin | 1 | 1 | World coordinates of map origin |  | environment-model_shacl.ttl |
| GeodeticReferenceSystemShape | environment-model | coordinateSystem |  | 1 | EPSG code of the map | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| GeodeticReferenceSystemShape | environment-model | heightSystem |  | 1 | Ellipsodial height or orthometric height | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| BoundingBoxShape | environment-model | yMin |  | 1 |  | <http://www.w3.org/2001/XMLSchema#float> | environment-model_shacl.ttl |
| BoundingBoxShape | environment-model | yMax |  | 1 |  | <http://www.w3.org/2001/XMLSchema#float> | environment-model_shacl.ttl |
| BoundingBoxShape | environment-model | xMin |  | 1 |  | <http://www.w3.org/2001/XMLSchema#float> | environment-model_shacl.ttl |
| BoundingBoxShape | environment-model | xMax |  | 1 |  | <http://www.w3.org/2001/XMLSchema#float> | environment-model_shacl.ttl |
| Coordinate2DShape | environment-model | x |  | 1 |  | <http://www.w3.org/2001/XMLSchema#float> | environment-model_shacl.ttl |
| Coordinate2DShape | environment-model | y |  | 1 |  | <http://www.w3.org/2001/XMLSchema#float> | environment-model_shacl.ttl |
| ProjectLocationShape | environment-model | state |  | 1 | State of project area | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| ProjectLocationShape | environment-model | city |  | 1 | nan | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| ProjectLocationShape | environment-model | region |  | 1 | Region of project area | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| ProjectLocationShape | environment-model | country |  | 1 | Country code as ISO 3166-1, alpha-2;  | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| ProjectLocationShape | environment-model | boundingBox | 1 | 1 | Bounding box with lat/lon values in WGS84 |  | environment-model_shacl.ttl |
| ProjectLocationShape | environment-model | relationOrArea |  | 1 | Description of the location, dependen if it is a more trajectory style data or area style data | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| FormatShape | environment-model | type |  | 1 | Format type definition | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| FormatShape | environment-model | version |  | 1 | Version of data format | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| ProjectShape | environment-model | creationVersion |  | 1 | Tool for the creation of the data | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| ProjectShape | environment-model | creationSource |  | 1 | Tool for the creation of the data | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| ProjectShape | environment-model | softwareName |  | 1 | Name of the visual system | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| ProjectShape | environment-model | softwareVendor |  | 1 | Name of software vendor | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| ProjectShape | environment-model | version |  | 1 | Version of visual system | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| QualityShape | environment-model | features | 0 | 1 | Description of quality features | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| QualityShape | environment-model | detailLevel |  | 1 | Category of the level of detail (High - highest level of detail with additional object enrichment, Med - directly from data sources, with environment, Low - topological representation). | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| QualityShape | environment-model | textureResolution | 0 | 1 | Real texture resolution in meter (max?) | <http://www.w3.org/2001/XMLSchema#float> | environment-model_shacl.ttl |
| QuantityShape | environment-model | geometryCount |  | 1 | Total number of all geoemtries, instances are considered only once | <http://www.w3.org/2001/XMLSchema#int> | environment-model_shacl.ttl |
| QuantityShape | environment-model | triangleCount |  | 1 | Total number of all triangles, instances are considered only once | <http://www.w3.org/2001/XMLSchema#int> | environment-model_shacl.ttl |
| QuantityShape | environment-model | textureMaterialCount |  | 1 | Number of textures | <http://www.w3.org/2001/XMLSchema#unsignedInt> | environment-model_shacl.ttl |
