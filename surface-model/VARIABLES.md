# Variables of SHACL Files in this folder

## Prefixes

- surface-model: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/surface-model/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| surfaceModelShape | surface-model | Format | 1 | 1 |  |  | surface-model_shacl.ttl |
| surfaceModelShape | surface-model | Data | 1 | 1 |  |  | surface-model_shacl.ttl |
| surfaceModelShape | surface-model | Quality | 1 | 1 |  |  | surface-model_shacl.ttl |
| surfaceModelShape | surface-model | Quantity | 1 | 1 |  |  | surface-model_shacl.ttl |
| surfaceModelShape | surface-model | Georeference | 1 | 1 |  |  | surface-model_shacl.ttl |
| GeoreferenceShape | surface-model | ProjectLocation | 1 | 1 |  |  | surface-model_shacl.ttl |
| GeoreferenceShape | surface-model | GeodeticReferenceSystem | 1 | 1 |  |  | surface-model_shacl.ttl |
| GeodeticReferenceSystemShape | surface-model | origin | 1 | 1 | World coordinates of map origin |  | surface-model_shacl.ttl |
| GeodeticReferenceSystemShape | surface-model | coordinateSystem |  | 1 | EPSG code of the map | <http://www.w3.org/2001/XMLSchema#string> | surface-model_shacl.ttl |
| GeodeticReferenceSystemShape | surface-model | heightSystem |  | 1 | Ellipsodial height or orthometric height | <http://www.w3.org/2001/XMLSchema#string> | surface-model_shacl.ttl |
| BoundingBoxShape | surface-model | yMin |  | 1 |  | <http://www.w3.org/2001/XMLSchema#float> | surface-model_shacl.ttl |
| BoundingBoxShape | surface-model | yMax |  | 1 |  | <http://www.w3.org/2001/XMLSchema#float> | surface-model_shacl.ttl |
| BoundingBoxShape | surface-model | xMin |  | 1 |  | <http://www.w3.org/2001/XMLSchema#float> | surface-model_shacl.ttl |
| BoundingBoxShape | surface-model | xMax |  | 1 |  | <http://www.w3.org/2001/XMLSchema#float> | surface-model_shacl.ttl |
| Coordinate2DShape | surface-model | x |  | 1 |  | <http://www.w3.org/2001/XMLSchema#float> | surface-model_shacl.ttl |
| Coordinate2DShape | surface-model | y |  | 1 |  | <http://www.w3.org/2001/XMLSchema#float> | surface-model_shacl.ttl |
| ProjectLocationShape | surface-model | state |  | 1 | State of project area | <http://www.w3.org/2001/XMLSchema#string> | surface-model_shacl.ttl |
| ProjectLocationShape | surface-model | city |  | 1 | nan | <http://www.w3.org/2001/XMLSchema#string> | surface-model_shacl.ttl |
| ProjectLocationShape | surface-model | region |  | 1 | Region of project area | <http://www.w3.org/2001/XMLSchema#string> | surface-model_shacl.ttl |
| ProjectLocationShape | surface-model | country |  | 1 | Country code as ISO 3166-1, alpha-2;  | <http://www.w3.org/2001/XMLSchema#string> | surface-model_shacl.ttl |
| ProjectLocationShape | surface-model | boundingBox | 1 | 1 | Bounding box with lat/lon values in WGS84 |  | surface-model_shacl.ttl |
| ProjectLocationShape | surface-model | relationOrArea |  | 1 | Description of the location, dependen if it is a more trajectory style data or area style data | <http://www.w3.org/2001/XMLSchema#string> | surface-model_shacl.ttl |
| DataShape | surface-model | dataType |  | 1 | Height, friction values, grey values | <http://www.w3.org/2001/XMLSchema#string> | surface-model_shacl.ttl |
| FormatShape | surface-model | formatType |  | 1 | Format type definition | <http://www.w3.org/2001/XMLSchema#string> | surface-model_shacl.ttl |
| FormatShape | surface-model | version |  | 1 | Version of data format | <http://www.w3.org/2001/XMLSchema#string> | surface-model_shacl.ttl |
| QualityShape | surface-model | resolutionLongitudinal |  | 1 | Longitudinal resolution  | <http://www.w3.org/2001/XMLSchema#float> | surface-model_shacl.ttl |
| QualityShape | surface-model | orientation |  | 1 | Heading at starting position | <http://www.w3.org/2001/XMLSchema#float> | surface-model_shacl.ttl |
| QualityShape | surface-model | platformExists |  | 1 | Existence of horizontal starting platform | <http://www.w3.org/2001/XMLSchema#boolean> | surface-model_shacl.ttl |
| QualityShape | surface-model | resolutionLateral |  | 1 | Lateral resolutions | <http://www.w3.org/2001/XMLSchema#float> | surface-model_shacl.ttl |
| QualityShape | surface-model | rampExists |  | 1 | Existence of smooth ramp from platform to road | <http://www.w3.org/2001/XMLSchema#boolean> | surface-model_shacl.ttl |
| QuantityShape | surface-model | mapDataField |  | 1 | Is projection system provided within the dataset | <http://www.w3.org/2001/XMLSchema#boolean> | surface-model_shacl.ttl |
| QuantityShape | surface-model | elevationRange | 0 | 1 | Range of elevation values | <http://www.w3.org/2001/XMLSchema#float> | surface-model_shacl.ttl |
| QuantityShape | surface-model | length |  | 1 | Road network length in km | <http://www.w3.org/2001/XMLSchema#float> | surface-model_shacl.ttl |
