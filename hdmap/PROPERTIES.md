# Properties of SHACL Files in this folder

## Prefixes

- hdmap: <https://ontologies.envited-x.net/hdmap/v4/ontology#>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| HdMapShape | hdmap | hasDataResource | 1 | 1 |  |  | hdmap_shacl.ttl |
| HdMapShape | hdmap | hasDataResourceExtension | 1 | 1 |  |  | hdmap_shacl.ttl |
| HdMapShape | hdmap | hasManifest | 1 | 1 |  |  | hdmap_shacl.ttl |
| DataResourceShapeExtension | hdmap | hasFormat | 1 | 1 | Contains properties to describe the format of the HD map asset. |  | hdmap_shacl.ttl |
| DataResourceShapeExtension | hdmap | hasContent | 1 | 1 | Defines the content (road types, lane types, object types, traffic direction) of the HD map asset. |  | hdmap_shacl.ttl |
| DataResourceShapeExtension | hdmap | hasQuantity | 1 | 1 | Contains properties to describe the quantity (e.g. number of intersections, traffic lights, signs, length, range of speed limits/elevations) of the HD map asset. |  | hdmap_shacl.ttl |
| DataResourceShapeExtension | hdmap | hasQuality | 1 | 1 | Contains properties to describe the accuracy of the HD map asset. |  | hdmap_shacl.ttl |
| DataResourceShapeExtension | hdmap | hasDataSource | 1 | 1 | Defines which data resources or measurement systems were used to create the HD map asset. |  | hdmap_shacl.ttl |
| DataResourceShapeExtension | hdmap | hasGeoreference | 1 | 1 |  |  | hdmap_shacl.ttl |
| ContentShape | hdmap | roadTypes |  |  | Lists the road types used in the HD map asset. See ASAM OpenDRIVE 1.8.1 Chapter 10.4 (https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/10_roads/10_04_road_type.html) | <http://www.w3.org/2001/XMLSchema#string> | hdmap_shacl.ttl |
| ContentShape | hdmap | laneTypes |  |  | Lists the lanes types used in the HD map asset. See ASAM OpenDRIVE 1.8.1 Chapter 11.7.1 (https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/11_lanes/11_07_lane_properties.html). | <http://www.w3.org/2001/XMLSchema#string> | hdmap_shacl.ttl |
| ContentShape | hdmap | levelOfDetail |  |  | Lists the object types used in the HD map asset. See ASAM OpenDRIVE 1.8.1 Annex A.4.5 (https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/16_annexes/enumerations/map_uml_enumerations.html#top-EAID_C47587D0_7173_42df_8BB7_36B2C598D95F) | <http://www.w3.org/2001/XMLSchema#string> | hdmap_shacl.ttl |
| ContentShape | hdmap | trafficDirection |  | 1 | Indicates whether the HD map is designed for left or right-hand traffic. | <http://www.w3.org/2001/XMLSchema#string> | hdmap_shacl.ttl |
| DataSourceShape | hdmap | measurementSystem |  | 1 | Specifies the name of the primary acquisition device. | <http://www.w3.org/2001/XMLSchema#string> | hdmap_shacl.ttl |
| DataSourceShape | hdmap | usedDataSources |  |  | Indicates the source data used to create the HD map. | <http://www.w3.org/2001/XMLSchema#string> | hdmap_shacl.ttl |
| FormatShape | hdmap | version |  | 1 | Defines the version of the data format used for the HD map asset. | <http://www.w3.org/2001/XMLSchema#string> | hdmap_shacl.ttl |
| FormatShape | hdmap | formatType |  | 1 | Defines the type of data format used for the HD map asset. | <http://www.w3.org/2001/XMLSchema#string> | hdmap_shacl.ttl |
| QualityShape | hdmap | accuracySignals | 0 | 1 | Specifies the accuracy of traffic-relevant signals, signs and objects in metres. | <http://www.w3.org/2001/XMLSchema#float> | hdmap_shacl.ttl |
| QualityShape | hdmap | accuracyObjects | 0 | 1 | Specifies the accuracy, in metres, of objects within the traffic area that do not directly affect traffic. | <http://www.w3.org/2001/XMLSchema#float> | hdmap_shacl.ttl |
| QualityShape | hdmap | accuracyLaneModelHeight | 0 | 1 | Specifies the accuracy of the lane model's height in metres. | <http://www.w3.org/2001/XMLSchema#float> | hdmap_shacl.ttl |
| QualityShape | hdmap | precision | 0 | 1 | Specifies the relative precision of the measured road network in metres. | <http://www.w3.org/2001/XMLSchema#float> | hdmap_shacl.ttl |
| QualityShape | hdmap | accuracyLaneModel2d | 0 | 1 | Specifies the accuracy of the lane model in the 2D plane in metres. | <http://www.w3.org/2001/XMLSchema#float> | hdmap_shacl.ttl |
| QuantityShape | hdmap | numberIntersections |  | 1 | Specifies the total number of intersections defined in the HD map. See ASAM OpenDRIVE 1.8.1 Chapter 12.1 (https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/12_junctions/12_01_introduction.html) | <http://www.w3.org/2001/XMLSchema#unsignedInt> | hdmap_shacl.ttl |
| QuantityShape | hdmap | numberTrafficLights |  | 1 | Specifies the number of all traffic lights defined in the HD map. | <http://www.w3.org/2001/XMLSchema#unsignedInt> | hdmap_shacl.ttl |
| QuantityShape | hdmap | rangeOfModeling | 0 | 1 | Indicates the distance (in metres) to which the area beyond the traffic area has been modeled. | <http://www.w3.org/2001/XMLSchema#float> | hdmap_shacl.ttl |
| QuantityShape | hdmap | numberOutlines |  | 1 | Specifies the number of all outline objects defined in the HD map. See ASAM OpenDRIVE 1.8.1 Chapter 13.3 (https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/13_objects/13_03_object_outline.html) | <http://www.w3.org/2001/XMLSchema#unsignedInt> | hdmap_shacl.ttl |
| QuantityShape | hdmap | speedLimit |  | 1 | Specifies the range of speed limits defined in the HD map, using the unit specified in the HD map. See ASAM OpenDRIVE 1.8.1 Annex A.1.4 (https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/16_annexes/enumerations/map_uml_enumerations.html#top-EAID_491DC05E_01C6_49b3_83BE_A06DD81F9C35) |  | hdmap_shacl.ttl |
| QuantityShape | hdmap | length |  | 1 | Defines the total length (sum of road lengths) of the road network in kilometres. | <http://www.w3.org/2001/XMLSchema#float> | hdmap_shacl.ttl |
| QuantityShape | hdmap | elevationRange |  | 1 | Specifies the difference between the maximum and minimum height of the road elevation profiles in metres. See ASAM OpenDRIVE 1.8.1 Chapter 10.5 (https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/10_roads/10_05_elevation.html) | <http://www.w3.org/2001/XMLSchema#float> | hdmap_shacl.ttl |
| QuantityShape | hdmap | numberObjects |  | 1 | Specifies the number of all objects in the HD map. See ASAM OpenDRIVE 1.8.1 Chapter 13.1 (https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/13_objects/13_01_introduction.html) | <http://www.w3.org/2001/XMLSchema#unsignedInt> | hdmap_shacl.ttl |
| QuantityShape | hdmap | numberTrafficSigns |  | 1 | Specifies the number of all traffic signs (signals) in the HD map. See ASAM OpenDRIVE 1.8.1 Chapter 14.1 (https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/14_signals/14_01_introduction.html) | <http://www.w3.org/2001/XMLSchema#unsignedInt> | hdmap_shacl.ttl |
| Range2DShape | hdmap | max |  |  | The maximum value of the range. | <http://www.w3.org/2001/XMLSchema#float> | hdmap_shacl.ttl |
| Range2DShape | hdmap | min |  |  | The minimum value of the range. | <http://www.w3.org/2001/XMLSchema#float> | hdmap_shacl.ttl |
