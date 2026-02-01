# Properties of SHACL Files for georeference

## Prefixes

- georeference: <https://w3id.org/ascs-ev/envited-x/georeference/v5/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| GeoreferenceShape | georeference | hasProjectLocation | 1 | 1 | Contains properties (state, city, region, country, bounding) to describe the location of the simulation asset. |  | georeference.shacl.ttl |
| GeoreferenceShape | georeference | hasGeodeticReferenceSystem | 1 | 1 | This ontology includes properties for positions (e.g., origin and viewpoint), projection type, and an ellipsoidal height system, which together define a geodetic reference system. |  | georeference.shacl.ttl |
| GeodeticReferenceSystemShape | georeference | hasOrigin | 1 | 1 | Defines the center position of the asset in world coordinates. |  | georeference.shacl.ttl |
| GeodeticReferenceSystemShape | georeference | hasViewPoint |  | 1 | Defines the imported viewpoint position of the asset in world coordinates. |  | georeference.shacl.ttl |
| GeodeticReferenceSystemShape | georeference | codeEPSG |  | 1 | Defines the projection EPSG code for the asset. | <http://www.w3.org/2001/XMLSchema#integer> | georeference.shacl.ttl |
| GeodeticReferenceSystemShape | georeference | coordinateSystemName |  | 1 | Describes the coordinate system name of the asset as an alternative to the EPSG code. | <http://www.w3.org/2001/XMLSchema#string> | georeference.shacl.ttl |
| GeodeticReferenceSystemShape | georeference | heightSystem |  | 1 | Defines the height system type of the asset. |  | georeference.shacl.ttl |
| BoundingBoxShape | georeference | xMin | 1 | 1 | Defines the minimum bounding box value along the x-axis. | <http://www.w3.org/2001/XMLSchema#float> | georeference.shacl.ttl |
| BoundingBoxShape | georeference | yMin | 1 | 1 | Defines the minimum bounding box value along the y-axis. | <http://www.w3.org/2001/XMLSchema#float> | georeference.shacl.ttl |
| BoundingBoxShape | georeference | xMax | 1 | 1 | Defines the maximum bounding box value along the x-axis. | <http://www.w3.org/2001/XMLSchema#float> | georeference.shacl.ttl |
| BoundingBoxShape | georeference | yMax | 1 | 1 | Defines the maximum bounding box value along the y-axis. | <http://www.w3.org/2001/XMLSchema#float> | georeference.shacl.ttl |
| LatLonCoordinateShape | georeference | lat | 1 | 1 | Defines a world latitude value (on the y-axis) in degrees. | <http://www.w3.org/2001/XMLSchema#float> | georeference.shacl.ttl |
| LatLonCoordinateShape | georeference | lon | 1 | 1 | Defines a world longitude value (on the x-axis) in degrees. | <http://www.w3.org/2001/XMLSchema#float> | georeference.shacl.ttl |
| ProjectLocationShape | georeference | state |  | 1 | Defines an ISO 3166-2 code for the state or province in which the asset centre is located. | <http://www.w3.org/2001/XMLSchema#string> | georeference.shacl.ttl |
| ProjectLocationShape | georeference | city |  | 1 | Specifies the name of the city in which the asset's centre is located. | <http://www.w3.org/2001/XMLSchema#string> | georeference.shacl.ttl |
| ProjectLocationShape | georeference | region |  | 1 | Specifies the name of the region in which the asset's centre is located. | <http://www.w3.org/2001/XMLSchema#string> | georeference.shacl.ttl |
| ProjectLocationShape | georeference | country |  | 1 | Defines an ISO 3166-1, alpha-2 code for the country in which the asset centre is located. | <http://www.w3.org/2001/XMLSchema#string> | georeference.shacl.ttl |
| ProjectLocationShape | georeference | hasBoundingBox | 1 | 1 | Defines the bounding box in world coordinates of the asset. |  | georeference.shacl.ttl |
| ProjectLocationShape | georeference | relationOrArea |  | 1 | Describes the area in which the asset is located, such as the name of the main street or the landscape region. | <http://www.w3.org/2001/XMLSchema#string> | georeference.shacl.ttl |
