# Properties of SHACL Files in this folder

## Prefixes

- ex: <https://openlabel.asam.net/V1-0-0/ontologies/>
- schema: <https://schema.org/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TagShape | ex | AdminTag | 0 |  |  |  | openlabel_shacl.ttl |
| TagShape | ex | Behaviour | 0 |  |  |  | openlabel_shacl.ttl |
| TagShape | ex | Odd | 0 |  |  |  | openlabel_shacl.ttl |
| TagShape | ex | RoadUser | 0 |  |  |  | openlabel_shacl.ttl |
| AdminTagShape | ex | LiscenceURI |  |  | The type of license which governs usage of the scenario | <http://www.w3.org/2000/01/rdf-schema#Literal> | openlabel_shacl.ttl |
| AdminTagShape | ex | ownerEmail |  |  | Scenario owner email | <http://www.w3.org/2000/01/rdf-schema#Literal> | openlabel_shacl.ttl |
| AdminTagShape | ex | ownerName |  |  | Scenario owner name | <http://www.w3.org/2000/01/rdf-schema#Literal> | openlabel_shacl.ttl |
| AdminTagShape | ex | ownerURL |  |  | Scenario owner URL | <http://www.w3.org/2000/01/rdf-schema#Literal> | openlabel_shacl.ttl |
| AdminTagShape | ex | scenarioCreatedDate |  |  | Scenario created date | <http://www.w3.org/2000/01/rdf-schema#Literal> | openlabel_shacl.ttl |
| AdminTagShape | ex | scenarioDefinition |  |  | Scenario definition SDL | <http://www.w3.org/2000/01/rdf-schema#Literal> | openlabel_shacl.ttl |
| AdminTagShape | ex | scenarioDefinitionLanguageURI |  |  | Scenario definition type | <http://www.w3.org/2000/01/rdf-schema#Literal> | openlabel_shacl.ttl |
| AdminTagShape | ex | scenarioDescription |  |  | Scenario description | <http://www.w3.org/2000/01/rdf-schema#Literal> | openlabel_shacl.ttl |
| AdminTagShape | ex | scenarioName |  |  | Scenario name | <http://www.w3.org/2000/01/rdf-schema#Literal> | openlabel_shacl.ttl |
| AdminTagShape | ex | scenarioParentReference |  |  | Scenario parent reference | <http://www.w3.org/2000/01/rdf-schema#Literal> | openlabel_shacl.ttl |
| AdminTagShape | ex | scenarioUniqueReference |  |  | Scenario unique reference | <http://www.w3.org/2000/01/rdf-schema#Literal> | openlabel_shacl.ttl |
| AdminTagShape | ex | scenarioVersion |  |  | Scenario version | <http://www.w3.org/2000/01/rdf-schema#Literal> | openlabel_shacl.ttl |
| AdminTagShape | ex | scenarioVisualisationURL |  |  | Scenario visualization | <http://www.w3.org/2000/01/rdf-schema#Literal> | openlabel_shacl.ttl |
| RoadUserShape | ex | motionDriveValue |  |  | Speed (km/h) . | <http://www.w3.org/2001/XMLSchema#decimal> | openlabel_shacl.ttl |
| RoadUserShape | ex | RoadUserVehicle |  |  | Validation class for RoadUserVehicle | <http://www.w3.org/2001/XMLSchema#string> | openlabel_shacl.ttl |
| RoadUserShape | ex | RoadUserHuman |  |  | Validation class for RoadUserHuman  | <http://www.w3.org/2001/XMLSchema#string> | openlabel_shacl.ttl |
| RoadUserShape | ex | RoadUserAnimal |  |  | Validation class for RoadUserAnimal  | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| BehaviourShape | ex | BehaviourCommunication |  |  | Validation class for BehaviourCommunication | <http://www.w3.org/2001/XMLSchema#string> | openlabel_shacl.ttl |
| BehaviourShape | ex | MotionAway |  |  | Validation class for MotionAway | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| BehaviourShape | ex | MotionCross |  |  | Validation class for MotionCross | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| BehaviourShape | ex | MotionCutIn |  |  | Validation class for MotionCutIn | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| BehaviourShape | ex | MotionCutOut |  |  | Validation class for MotionCutOut | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| BehaviourShape | ex | MotionLaneChangeLeft |  |  | Validation class for MotionLaneChangeLeft | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| BehaviourShape | ex | MotionLaneChangeRight |  |  | Validation class for MotionLaneChangeRight | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| BehaviourShape | ex | MotionOvertake |  |  | Validation class for MotionOvertake | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| BehaviourShape | ex | MotionReverse |  |  | Validation class for MotionReverse | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| BehaviourShape | ex | MotionRun |  |  | Validation class for MotionRun | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| BehaviourShape | ex | MotionSlide |  |  | Validation class for MotionSlide | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| BehaviourShape | ex | MotionStop |  |  | Validation class for MotionStop | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| BehaviourShape | ex | MotionTowards |  |  | Validation class for MotionTowards | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| BehaviourShape | ex | MotionTurn |  |  | Validation class for MotionTurn | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| BehaviourShape | ex | MotionTurnLeft |  |  | Validation class for MotionTurnLeft | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| BehaviourShape | ex | MotionTurnRight |  |  | Validation class for MotionTurnRight | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| BehaviourShape | ex | MotionUTurn |  |  | Validation class for MotionUTurn | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| BehaviourShape | ex | MotionWalk |  |  | Validation class for MotionWalk | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| BehaviourShape | ex | MotionAccelerate |  |  | Validation class for motionAccelerate | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| BehaviourShape | ex | MotionDecelerate |  |  | Validation class for motionDecelerate | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| BehaviourShape | ex | MotionDrive |  |  | Validation class for motionDrive | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| BehaviourShape | ex | motionAccelerateValue |  |  | Rate of acceleration (ms-2) . |  | openlabel_shacl.ttl |
| BehaviourShape | ex | motionDecelerateValue |  |  | MotionDecelerateVale can be a single decimal or a range (ms-2) . |  | openlabel_shacl.ttl |
| BehaviourShape | ex | motionDriveValue |  |  | Motion drive value can be a single decimal or a range Speed (km/h) . |  | openlabel_shacl.ttl |
| OddShape | ex | DrivableAreaEdge |  |  | Validation class for DrivableAreaEdge | <http://www.w3.org/2001/XMLSchema#string> | openlabel_shacl.ttl |
| OddShape | ex | GeometryTransverse |  |  | Validation class for GeometryTransverse | <http://www.w3.org/2001/XMLSchema#string> | openlabel_shacl.ttl |
| OddShape | ex | LaneSpecificationTravelDirection |  |  | Validation class for LaneSpecificationTravelDirection | <http://www.w3.org/2001/XMLSchema#string> | openlabel_shacl.ttl |
| OddShape | ex | LaneSpecificationType |  |  | Validation class for LaneSpecificationType | <http://www.w3.org/2001/XMLSchema#string> | openlabel_shacl.ttl |
| OddShape | ex | SignsInformation |  |  | Validation class for SignsInformation | <http://www.w3.org/2001/XMLSchema#string> | openlabel_shacl.ttl |
| OddShape | ex | SignsRegulatory |  |  | Validation class for SignsRegulatory | <http://www.w3.org/2001/XMLSchema#string> | openlabel_shacl.ttl |
| OddShape | ex | SignsWarning |  |  | Validation class for SignsWarning | <http://www.w3.org/2001/XMLSchema#string> | openlabel_shacl.ttl |
| OddShape | ex | DrivableAreaSurfaceCondition |  |  | Validation class for DrivableAreaSurfaceCondition | <http://www.w3.org/2001/XMLSchema#string> | openlabel_shacl.ttl |
| OddShape | ex | DrivableAreaSurfaceFeature |  |  | Validation class for DrivableAreaSurfaceFeature | <http://www.w3.org/2001/XMLSchema#string> | openlabel_shacl.ttl |
| OddShape | ex | DrivableAreaSurfaceType |  |  | Validation class for DrivableAreaSurfaceType | <http://www.w3.org/2001/XMLSchema#string> | openlabel_shacl.ttl |
| OddShape | ex | DrivableAreaType |  |  | Validation class for DrivableAreaType | <http://www.w3.org/2001/XMLSchema#string> | openlabel_shacl.ttl |
| OddShape | ex | SceneryFixedStructure |  |  | Validation class for SceneryFixedStructure | <http://www.w3.org/2001/XMLSchema#string> | openlabel_shacl.ttl |
| OddShape | ex | JunctionIntersection |  |  | Validation class for JunctionIntersection | <http://www.w3.org/2001/XMLSchema#string> | openlabel_shacl.ttl |
| OddShape | ex | JunctionRoundabout |  |  | Validation class for JunctionRoundabout | <http://www.w3.org/2001/XMLSchema#string> | openlabel_shacl.ttl |
| OddShape | ex | ScenerySpecialStructure |  |  | Validation class for ScenerySpecialStructure | <http://www.w3.org/2001/XMLSchema#string> | openlabel_shacl.ttl |
| OddShape | ex | SceneryTemporaryStructure |  |  | Validation class for SceneryTemporaryStructure | <http://www.w3.org/2001/XMLSchema#string> | openlabel_shacl.ttl |
| OddShape | ex | SceneryZone |  |  | Validation class for SceneryZone | <http://www.w3.org/2001/XMLSchema#string> | openlabel_shacl.ttl |
| OddShape | ex | ConnectivityCommunication |  |  | Validation class for ConnectivityCommunication | <http://www.w3.org/2001/XMLSchema#string> | openlabel_shacl.ttl |
| OddShape | ex | ConnectivityPositioning |  |  | Validation class for ConnectivityPositioning | <http://www.w3.org/2001/XMLSchema#string> | openlabel_shacl.ttl |
| OddShape | ex | IlluminationArtificial |  |  | Validation class for IlluminationArtificial | <http://www.w3.org/2001/XMLSchema#string> | openlabel_shacl.ttl |
| OddShape | ex | IlluminationLowLight |  |  | Validation class for IlluminationLowLight | <http://www.w3.org/2001/XMLSchema#string> | openlabel_shacl.ttl |
| OddShape | ex | RainType |  |  | Validation class for RainType | <http://www.w3.org/2001/XMLSchema#string> | openlabel_shacl.ttl |
| OddShape | ex | EnvironmentParticulates |  |  | Validation class for EnvironmentParticulates | <http://www.w3.org/2001/XMLSchema#string> | openlabel_shacl.ttl |
| OddShape | ex | RainType |  |  | Validation class for RainType | <http://www.w3.org/2001/XMLSchema#string> | openlabel_shacl.ttl |
| OddShape | ex | LaneSpecificationMarking |  |  | Validation class for LaneSpecificationMarking | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| OddShape | ex | HorizontalStraights |  |  | Validation class for HorizontalStraights | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| OddShape | ex | LongitudinalLevelPlane |  |  | Validation class for LongitudinalLevelPlane | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| OddShape | ex | DaySunPosition |  |  | Validation class for DaySunPosition | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| OddShape | ex | ParticulatesDust |  |  | Validation class for ParticulatesDust | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| OddShape | ex | ParticulatesMarine |  |  | Validation class for ParticulatesMarine | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| OddShape | ex | ParticulatesPollution |  |  | Validation class for ParticulatesPollution | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| OddShape | ex | ParticulatesVolcanic |  |  | Validation class for ParticulatesVolcanic | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| OddShape | ex | TrafficSpecialVehicle |  |  | Validation class for TrafficSpecialVehicle | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| OddShape | ex | SubjectVehicleSpeed |  |  | Validation class for subjectVehicleSpeed | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| OddShape | ex | subjectVehicleSpeedValue |  |  | Speed (km/h) (Refer to BSI PAS-1883 Section 5.4.b) . |  | openlabel_shacl.ttl |
| OddShape | ex | WeatherRain |  |  | Validation class for weatherRain | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| OddShape | ex | weatherRainValue |  |  | Rainfall Intensity (mm/h) (Refer to BSI PAS-1883 Section 5.3.1.2) . | <http://www.w3.org/2001/XMLSchema#decimal> | openlabel_shacl.ttl |
| OddShape | ex | WeatherSnow |  |  | Validation class for weatherSnow | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| OddShape | ex | weatherSnowValue |  |  | Visibility (km) (Refer to BSI PAS-1883 Section 5.3.1.3) . | <http://www.w3.org/2001/XMLSchema#decimal> | openlabel_shacl.ttl |
| OddShape | ex | WeatherWind |  |  | Validation class for weatherWind | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| OddShape | ex | weatherWindValue |  |  | Wind Speed (m/s) (Refer to BSI PAS-1883 Section 5.3.1.1) . | <http://www.w3.org/2001/XMLSchema#decimal> | openlabel_shacl.ttl |
| OddShape | ex | IlluminationCloudiness |  |  | Validation class for illuminationCloudiness | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| OddShape | ex | illuminationCloudinessValue |  |  | Cloud cover (okta) (Refer to BSI PAS-1883 Section 5.3.3.c) . | <http://www.w3.org/2001/XMLSchema#decimal> | openlabel_shacl.ttl |
| OddShape | ex | DaySunElevation |  |  | Validation class for daySunElevation | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| OddShape | ex | daySunElevationValue |  |  | Sun Elevation (degrees) (Refer to BSI PAS-1883 Section 5.3.3.a.1) . | <http://www.w3.org/2001/XMLSchema#decimal> | openlabel_shacl.ttl |
| OddShape | ex | TrafficAgentDensity |  |  | Validation class for trafficAgentDensity | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| OddShape | ex | trafficAgentDensityValue |  |  | Density (vehicles/km) (Refer to BSI PAS-1883 Section 5.4.a.1) . | <http://www.w3.org/2001/XMLSchema#nonNegativeInteger> | openlabel_shacl.ttl |
| OddShape | ex | TrafficFlowRate |  |  | Validation class for trafficFlowRate | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| OddShape | ex | trafficFlowRateValue |  |  | Rate (vehicles/h) (Refer to BSI PAS-1883 Section 5.4.a.3) . | <http://www.w3.org/2001/XMLSchema#nonNegativeInteger> | openlabel_shacl.ttl |
| OddShape | ex | TrafficVolume |  |  | Validation class for trafficVolume | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| OddShape | ex | trafficVolumeValue |  |  | Volume (vehicle km) (Refer to BSI PAS-1883 Section 5.4.a.2) . | <http://www.w3.org/2001/XMLSchema#nonNegativeInteger> | openlabel_shacl.ttl |
| OddShape | ex | LaneSpecificationDimensions |  |  | Validation class for laneSpecificationDimensions | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| OddShape | ex | laneSpecificationDimensionsValue |  |  | Lane width (m) (Refer to BSI PAS-1883 Section 5.2.3.4.a) . |  | openlabel_shacl.ttl |
| OddShape | ex | LaneSpecificationLaneCount |  |  | Validation class for laneSpecificationLaneCount | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| OddShape | ex | laneSpecificationLaneCountValue |  |  | Number of lanes (Unit) (Refer to BSI PAS-1883 Section 5.2.3.4.d) . |  | openlabel_shacl.ttl |
| OddShape | ex | HorizontalCurves |  |  | Validation class for horizontalCurves | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| OddShape | ex | horizontalCurvesValue |  |  | Curve Radius (m) (Refer to BSI PAS-1883 Section 5.2.3.3) . | <http://www.w3.org/2001/XMLSchema#decimal> | openlabel_shacl.ttl |
| OddShape | ex | LongitudinalDownSlope |  |  | Validation class for longitudinalDownSlope | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel_shacl.ttl |
| OddShape | ex | longitudinalDownSlopeValue |  |  | Gradient (%) (Refer to BSI PAS-1883 Section 5.2.3.3.ii) . | <http://www.w3.org/2001/XMLSchema#decimal> | openlabel_shacl.ttl |
| QuantitativeValueShape | schema | minValue | 1 |  |  |  | openlabel_shacl.ttl |
| QuantitativeValueShape | schema | maxValue | 1 |  |  |  | openlabel_shacl.ttl |
