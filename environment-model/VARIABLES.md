# Variables of SHACL Files in this folder

## Prefixes

- environmentmodel: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/environmentmodel/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| environmentModelShape | environmentmodel | Quantity | 1 | 1 |  |  | environment-model_shacl.ttl |
| environmentModelShape | environmentmodel | Quality | 1 | 1 |  |  | environment-model_shacl.ttl |
| environmentModelShape | environmentmodel | Project | 1 | 1 |  |  | environment-model_shacl.ttl |
| environmentModelShape | environmentmodel | Format | 1 | 1 |  |  | environment-model_shacl.ttl |
| environmentModelShape | environmentmodel | Georeference | 1 | 1 |  |  | environment-model_shacl.ttl |
| GeoreferenceShape | environmentmodel | ProjectLocation | 1 | 1 |  |  | environment-model_shacl.ttl |
| GeoreferenceShape | environmentmodel | GeodeticReferenceSystem | 1 | 1 |  |  | environment-model_shacl.ttl |
| GeodeticReferenceSystemShape | environmentmodel | origin | 1 | 1 | World coordinates of map origin |  | environment-model_shacl.ttl |
| GeodeticReferenceSystemShape | environmentmodel | coordinateSystem |  | 1 | EPSG code of the map | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| GeodeticReferenceSystemShape | environmentmodel | heightSystem |  | 1 | Ellipsodial height or orthometric height | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| BoundingBoxShape | environmentmodel | yMin |  | 1 |  | <http://www.w3.org/2001/XMLSchema#float> | environment-model_shacl.ttl |
| BoundingBoxShape | environmentmodel | yMax |  | 1 |  | <http://www.w3.org/2001/XMLSchema#float> | environment-model_shacl.ttl |
| BoundingBoxShape | environmentmodel | xMin |  | 1 |  | <http://www.w3.org/2001/XMLSchema#float> | environment-model_shacl.ttl |
| BoundingBoxShape | environmentmodel | xMax |  | 1 |  | <http://www.w3.org/2001/XMLSchema#float> | environment-model_shacl.ttl |
| Coordinate2DShape | environmentmodel | x |  | 1 |  | <http://www.w3.org/2001/XMLSchema#float> | environment-model_shacl.ttl |
| Coordinate2DShape | environmentmodel | y |  | 1 |  | <http://www.w3.org/2001/XMLSchema#float> | environment-model_shacl.ttl |
| ProjectLocationShape | environmentmodel | state |  | 1 | State of project area | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| ProjectLocationShape | environmentmodel | city |  | 1 | nan | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| ProjectLocationShape | environmentmodel | region |  | 1 | Region of project area | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| ProjectLocationShape | environmentmodel | country |  | 1 | Country code as ISO 3166-1, alpha-2;  | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| ProjectLocationShape | environmentmodel | boundingBox | 1 | 1 | Bounding box with lat/lon values in WGS84 |  | environment-model_shacl.ttl |
| ProjectLocationShape | environmentmodel | relationOrArea |  | 1 | Description of the location, dependen if it is a more trajectory style data or area style data | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
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
