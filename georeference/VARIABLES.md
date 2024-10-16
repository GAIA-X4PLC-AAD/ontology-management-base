# Variables of SHACL Files in this folder

## Prefixes

- georeference: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/georeference/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| GeoreferenceShape | georeference | projectLocation | 1 | 1 | projectLocation object with property for locations and description |  | georeference_shacl.ttl |
| GeoreferenceShape | georeference | geodeticReferenceSystem | 1 | 1 | geodeticReferenceSystem object with properties for projection informations |  | georeference_shacl.ttl |
| GeodeticReferenceSystemShape | georeference | origin | 1 | 1 | World coordinates of map origin |  | georeference_shacl.ttl |
| GeodeticReferenceSystemShape | georeference | coordinateSystem | 0 | 1 | EPSG code of the map | <http://www.w3.org/2001/XMLSchema#string> | georeference_shacl.ttl |
| GeodeticReferenceSystemShape | georeference | heightSystem |  | 1 | Ellipsodial height or orthometric height | <http://www.w3.org/2001/XMLSchema#string> | georeference_shacl.ttl |
| BoundingBoxShape | georeference | yMin |  | 1 |  | <http://www.w3.org/2001/XMLSchema#float> | georeference_shacl.ttl |
| BoundingBoxShape | georeference | yMax |  | 1 |  | <http://www.w3.org/2001/XMLSchema#float> | georeference_shacl.ttl |
| BoundingBoxShape | georeference | xMin |  | 1 |  | <http://www.w3.org/2001/XMLSchema#float> | georeference_shacl.ttl |
| BoundingBoxShape | georeference | xMax |  | 1 |  | <http://www.w3.org/2001/XMLSchema#float> | georeference_shacl.ttl |
| Coordinate2DShape | georeference | x |  | 1 |  | <http://www.w3.org/2001/XMLSchema#float> | georeference_shacl.ttl |
| Coordinate2DShape | georeference | y |  | 1 |  | <http://www.w3.org/2001/XMLSchema#float> | georeference_shacl.ttl |
| ProjectLocationShape | georeference | state |  | 1 | Code of federal state or province as ISO 3166-2 | <http://www.w3.org/2001/XMLSchema#string> | georeference_shacl.ttl |
| ProjectLocationShape | georeference | city |  | 1 | Main city of project area | <http://www.w3.org/2001/XMLSchema#string> | georeference_shacl.ttl |
| ProjectLocationShape | georeference | region |  | 1 | Region of project area | <http://www.w3.org/2001/XMLSchema#string> | georeference_shacl.ttl |
| ProjectLocationShape | georeference | country |  | 1 | Country code as ISO 3166-1, alpha-2 | <http://www.w3.org/2001/XMLSchema#string> | georeference_shacl.ttl |
| ProjectLocationShape | georeference | boundingBox | 1 | 1 | Bounding box with lat/lon values in WGS84 |  | georeference_shacl.ttl |
| ProjectLocationShape | georeference | relationOrArea |  | 1 | Description of the mapped area as relation for a certain road, or alternatively a region | <http://www.w3.org/2001/XMLSchema#string> | georeference_shacl.ttl |
