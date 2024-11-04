# Variables of SHACL Files in this folder

## Prefixes

- hdmap: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/hdmap/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| HdMapShape | hdmap | general | 1 | 1 | general object with properties for descriptions, data, links, bundle |  | hdmap_shacl.ttl |
| HdMapShape | hdmap | format | 1 | 1 | format object with properties for format informations |  | hdmap_shacl.ttl |
| HdMapShape | hdmap | content | 1 | 1 | content object with properties for road types, lane type, object type and traffic direction |  | hdmap_shacl.ttl |
| HdMapShape | hdmap | quantity | 1 | 1 | quantity object with properties for quantity informations |  | hdmap_shacl.ttl |
| HdMapShape | hdmap | quality | 1 | 1 | quality object with properties for quality informations |  | hdmap_shacl.ttl |
| HdMapShape | hdmap | dataSource | 1 | 1 | dataSource object with properties for data sources |  | hdmap_shacl.ttl |
| HdMapShape | hdmap | georeference | 1 | 1 | georeference object with properties for georeference informations |  | hdmap_shacl.ttl |
| ContentShape | hdmap | roadTypes |  |  | Covered/used road types, defined over ODR element t_road_type, see ODR spec section 8.3 | <http://www.w3.org/2001/XMLSchema#string> | hdmap_shacl.ttl |
| ContentShape | hdmap | laneTypes |  |  | Covered lane types, see ODR spec section 9.5.3. | <http://www.w3.org/2001/XMLSchema#string> | hdmap_shacl.ttl |
| ContentShape | hdmap | levelOfDetail |  |  | Covered object classes, see ODR spec section 11 | <http://www.w3.org/2001/XMLSchema#string> | hdmap_shacl.ttl |
| ContentShape | hdmap | trafficDirection |  | 1 | Traffic direction, i.e. right-hand or left-hand traffic | <http://www.w3.org/2001/XMLSchema#string> | hdmap_shacl.ttl |
| DataSourceShape | hdmap | measurementSystem |  | 1 | Main acquisition device | <http://www.w3.org/2001/XMLSchema#string> | hdmap_shacl.ttl |
| DataSourceShape | hdmap | usedDataSources |  |  | Basic data for the creation of the map | <http://www.w3.org/2001/XMLSchema#string> | hdmap_shacl.ttl |
| FormatShape | hdmap | version |  | 1 | Version of data format | <http://www.w3.org/2001/XMLSchema#string> | hdmap_shacl.ttl |
| FormatShape | hdmap | formatType |  | 1 | Format type definition | <http://www.w3.org/2001/XMLSchema#string> | hdmap_shacl.ttl |
| QualityShape | hdmap | accuracySignals | 0 | 1 | Accuracy of traffic relevant objects, signs and signals | <http://www.w3.org/2001/XMLSchema#float> | hdmap_shacl.ttl |
| QualityShape | hdmap | accuracyObjects | 0 | 1 | Accuracy of objects in the traffic space, which do not directly affect the traffic | <http://www.w3.org/2001/XMLSchema#float> | hdmap_shacl.ttl |
| QualityShape | hdmap | accuracyLaneModelHeight | 0 | 1 | Accuracy lane modell height | <http://www.w3.org/2001/XMLSchema#float> | hdmap_shacl.ttl |
| QualityShape | hdmap | precision | 0 | 1 | Precision of measured road network (relative accuracy) | <http://www.w3.org/2001/XMLSchema#float> | hdmap_shacl.ttl |
| QualityShape | hdmap | accuracyLaneModel2d | 0 | 1 | Accuracy of lane modell 2d | <http://www.w3.org/2001/XMLSchema#float> | hdmap_shacl.ttl |
| QuantityShape | hdmap | numberIntersections |  | 1 | Sum of all junctions defined in the map,  see ODR spec section 10 | <http://www.w3.org/2001/XMLSchema#unsignedInt> | hdmap_shacl.ttl |
| QuantityShape | hdmap | numberTrafficLights |  | 1 | Sum of all traffic lights defined in the map,  see ODR spec section 12 | <http://www.w3.org/2001/XMLSchema#unsignedInt> | hdmap_shacl.ttl |
| QuantityShape | hdmap | rangeOfModeling | 0 | 1 | How wide is the area beyond the traffic space modeled | <http://www.w3.org/2001/XMLSchema#float> | hdmap_shacl.ttl |
| QuantityShape | hdmap | numberOutlines |  | 1 | Sum of all objects outlines in the map,  see ODR spec section 11.2 | <http://www.w3.org/2001/XMLSchema#unsignedInt> | hdmap_shacl.ttl |
| QuantityShape | hdmap | speedLimit |  | 1 | Range of speed limits defined in the map, see ODR spec section 9.5.5.  |  | hdmap_shacl.ttl |
| QuantityShape | hdmap | length |  | 1 | Road network length in km, sum over road length; see ODR spec section 8 | <http://www.w3.org/2001/XMLSchema#float> | hdmap_shacl.ttl |
| QuantityShape | hdmap | elevationRange |  | 1 | Difference of max and mit elevation, extraction from openDrive Element t_road_elevationprofile_elevation, see section 8.4 | <http://www.w3.org/2001/XMLSchema#float> | hdmap_shacl.ttl |
| QuantityShape | hdmap | numberObjects |  | 1 | Sum of all objects in the map,  see ODR spec section 11 | <http://www.w3.org/2001/XMLSchema#unsignedInt> | hdmap_shacl.ttl |
| QuantityShape | hdmap | numberTrafficSigns |  | 1 | Sum of all traffic signs in the map,  see ODR spec section 12 | <http://www.w3.org/2001/XMLSchema#unsignedInt> | hdmap_shacl.ttl |
