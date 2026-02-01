# Properties of SHACL Files for openlabel

## Prefixes

- openlabel: <https://openlabel.asam.net/V1-0-0/ontologies/>
- schema: <https://schema.org/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TagShape | openlabel | AdminTag | 0 |  |  |  | openlabel.shacl.ttl |
| TagShape | openlabel | Behaviour | 0 |  |  |  | openlabel.shacl.ttl |
| TagShape | openlabel | Odd | 0 |  |  |  | openlabel.shacl.ttl |
| TagShape | openlabel | RoadUser | 0 |  |  |  | openlabel.shacl.ttl |
| AdminTagShape | openlabel | licenseURI |  |  | The type of license which governs usage of the scenario | <http://www.w3.org/2000/01/rdf-schema#Literal> | openlabel.shacl.ttl |
| AdminTagShape | openlabel | ownerEmail |  |  | Scenario owner email | <http://www.w3.org/2000/01/rdf-schema#Literal> | openlabel.shacl.ttl |
| AdminTagShape | openlabel | ownerName |  |  | Scenario owner name | <http://www.w3.org/2000/01/rdf-schema#Literal> | openlabel.shacl.ttl |
| AdminTagShape | openlabel | ownerURL |  |  | Scenario owner URL | <http://www.w3.org/2000/01/rdf-schema#Literal> | openlabel.shacl.ttl |
| AdminTagShape | openlabel | scenarioCreatedDate |  |  | Scenario created date | <http://www.w3.org/2000/01/rdf-schema#Literal> | openlabel.shacl.ttl |
| AdminTagShape | openlabel | scenarioDefinition |  |  | Scenario definition SDL | <http://www.w3.org/2000/01/rdf-schema#Literal> | openlabel.shacl.ttl |
| AdminTagShape | openlabel | scenarioDefinitionLanguageURI |  |  | Scenario definition type | <http://www.w3.org/2000/01/rdf-schema#Literal> | openlabel.shacl.ttl |
| AdminTagShape | openlabel | scenarioDescription |  |  | Scenario description | <http://www.w3.org/2000/01/rdf-schema#Literal> | openlabel.shacl.ttl |
| AdminTagShape | openlabel | scenarioName |  |  | Scenario name | <http://www.w3.org/2000/01/rdf-schema#Literal> | openlabel.shacl.ttl |
| AdminTagShape | openlabel | scenarioParentReference |  |  | Scenario parent reference | <http://www.w3.org/2000/01/rdf-schema#Literal> | openlabel.shacl.ttl |
| AdminTagShape | openlabel | scenarioUniqueReference |  |  | Scenario unique reference | <http://www.w3.org/2000/01/rdf-schema#Literal> | openlabel.shacl.ttl |
| AdminTagShape | openlabel | scenarioVersion |  |  | Scenario version | <http://www.w3.org/2000/01/rdf-schema#Literal> | openlabel.shacl.ttl |
| AdminTagShape | openlabel | scenarioVisualisationURL |  |  | Scenario visualization | <http://www.w3.org/2000/01/rdf-schema#Literal> | openlabel.shacl.ttl |
| RoadUserShape | openlabel | motionDriveValue |  |  | Speed (km/h). | <http://www.w3.org/2001/XMLSchema#decimal> | openlabel.shacl.ttl |
| RoadUserShape | openlabel | RoadUserVehicle |  |  | Validation class for RoadUserVehicle |  | openlabel.shacl.ttl |
| RoadUserShape | openlabel | RoadUserHuman |  |  | Validation class for RoadUserHuman | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| RoadUserShape | openlabel | RoadUserAnimal |  |  | Validation class for RoadUserAnimal | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| BehaviourShape | openlabel | BehaviourCommunication |  |  | Validation class for BehaviourCommunication |  | openlabel.shacl.ttl |
| BehaviourShape | openlabel | MotionAway |  |  | Validation class for MotionAway | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| BehaviourShape | openlabel | MotionCross |  |  | Validation class for MotionCross | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| BehaviourShape | openlabel | MotionCutIn |  |  | Validation class for MotionCutIn | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| BehaviourShape | openlabel | MotionCutOut |  |  | Validation class for MotionCutOut | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| BehaviourShape | openlabel | MotionLaneChangeLeft |  |  | Validation class for MotionLaneChangeLeft | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| BehaviourShape | openlabel | MotionLaneChangeRight |  |  | Validation class for MotionLaneChangeRight | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| BehaviourShape | openlabel | MotionOvertake |  |  | Validation class for MotionOvertake | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| BehaviourShape | openlabel | MotionReverse |  |  | Validation class for MotionReverse | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| BehaviourShape | openlabel | MotionRun |  |  | Validation class for MotionRun | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| BehaviourShape | openlabel | MotionSlide |  |  | Validation class for MotionSlide | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| BehaviourShape | openlabel | MotionStop |  |  | Validation class for MotionStop | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| BehaviourShape | openlabel | MotionTowards |  |  | Validation class for MotionTowards | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| BehaviourShape | openlabel | MotionTurn |  |  | Validation class for MotionTurn | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| BehaviourShape | openlabel | MotionTurnLeft |  |  | Validation class for MotionTurnLeft | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| BehaviourShape | openlabel | MotionTurnRight |  |  | Validation class for MotionTurnRight | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| BehaviourShape | openlabel | MotionUTurn |  |  | Validation class for MotionUTurn | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| BehaviourShape | openlabel | MotionWalk |  |  | Validation class for MotionWalk | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| BehaviourShape | openlabel | MotionAccelerate |  |  | Validation class for motionAccelerate | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| BehaviourShape | openlabel | MotionDecelerate |  |  | Validation class for motionDecelerate | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| BehaviourShape | openlabel | MotionDrive |  |  | Validation class for motionDrive | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| BehaviourShape | openlabel | motionAccelerateValue |  |  | Rate of acceleration (ms-2). |  | openlabel.shacl.ttl |
| BehaviourShape | openlabel | motionDecelerateValue |  |  | MotionDecelerateValue can be a single decimal or a range (ms-2). |  | openlabel.shacl.ttl |
| BehaviourShape | openlabel | motionDriveValue |  |  | Motion drive value can be a single decimal or a range Speed (km/h). |  | openlabel.shacl.ttl |
| OddShape | openlabel | DrivableAreaEdge |  |  | Validation class for DrivableAreaEdge |  | openlabel.shacl.ttl |
| OddShape | openlabel | GeometryTransverse |  |  | Validation class for GeometryTransverse |  | openlabel.shacl.ttl |
| OddShape | openlabel | LaneSpecificationTravelDirection |  |  | Validation class for LaneSpecificationTravelDirection |  | openlabel.shacl.ttl |
| OddShape | openlabel | LaneSpecificationType |  |  | Validation class for LaneSpecificationType |  | openlabel.shacl.ttl |
| OddShape | openlabel | SignsInformation |  |  | Validation class for SignsInformation |  | openlabel.shacl.ttl |
| OddShape | openlabel | SignsRegulatory |  |  | Validation class for SignsRegulatory |  | openlabel.shacl.ttl |
| OddShape | openlabel | SignsWarning |  |  | Validation class for SignsWarning |  | openlabel.shacl.ttl |
| OddShape | openlabel | DrivableAreaSurfaceCondition |  |  | Validation class for DrivableAreaSurfaceCondition |  | openlabel.shacl.ttl |
| OddShape | openlabel | DrivableAreaSurfaceFeature |  |  | Validation class for DrivableAreaSurfaceFeature |  | openlabel.shacl.ttl |
| OddShape | openlabel | DrivableAreaSurfaceType |  |  | Validation class for DrivableAreaSurfaceType |  | openlabel.shacl.ttl |
| OddShape | openlabel | DrivableAreaType |  |  | Validation class for DrivableAreaType |  | openlabel.shacl.ttl |
| OddShape | openlabel | SceneryFixedStructure |  |  | Validation class for SceneryFixedStructure |  | openlabel.shacl.ttl |
| OddShape | openlabel | JunctionIntersection |  |  | Validation class for JunctionIntersection |  | openlabel.shacl.ttl |
| OddShape | openlabel | JunctionRoundabout |  |  | Validation class for JunctionRoundabout |  | openlabel.shacl.ttl |
| OddShape | openlabel | ScenerySpecialStructure |  |  | Validation class for ScenerySpecialStructure |  | openlabel.shacl.ttl |
| OddShape | openlabel | SceneryTemporaryStructure |  |  | Validation class for SceneryTemporaryStructure |  | openlabel.shacl.ttl |
| OddShape | openlabel | SceneryZone |  |  | Validation class for SceneryZone |  | openlabel.shacl.ttl |
| OddShape | openlabel | ConnectivityCommunication |  |  | Validation class for ConnectivityCommunication |  | openlabel.shacl.ttl |
| OddShape | openlabel | ConnectivityPositioning |  |  | Validation class for ConnectivityPositioning |  | openlabel.shacl.ttl |
| OddShape | openlabel | IlluminationArtificial |  |  | Validation class for IlluminationArtificial |  | openlabel.shacl.ttl |
| OddShape | openlabel | IlluminationLowLight |  |  | Validation class for IlluminationLowLight |  | openlabel.shacl.ttl |
| OddShape | openlabel | RainType |  |  | Validation class for RainType |  | openlabel.shacl.ttl |
| OddShape | openlabel | EnvironmentParticulates |  |  | Validation class for EnvironmentParticulates |  | openlabel.shacl.ttl |
| OddShape | openlabel | LaneSpecificationMarking |  |  | Validation class for LaneSpecificationMarking | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| OddShape | openlabel | HorizontalStraights |  |  | Validation class for HorizontalStraights | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| OddShape | openlabel | LongitudinalLevelPlane |  |  | Validation class for LongitudinalLevelPlane | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| OddShape | openlabel | DaySunPosition |  |  | Validation class for DaySunPosition | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| OddShape | openlabel | ParticulatesDust |  |  | Validation class for ParticulatesDust | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| OddShape | openlabel | ParticulatesMarine |  |  | Validation class for ParticulatesMarine | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| OddShape | openlabel | ParticulatesPollution |  |  | Validation class for ParticulatesPollution | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| OddShape | openlabel | ParticulatesVolcanic |  |  | Validation class for ParticulatesVolcanic | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| OddShape | openlabel | TrafficSpecialVehicle |  |  | Validation class for TrafficSpecialVehicle | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| OddShape | openlabel | SubjectVehicleSpeed |  |  | Validation class for subjectVehicleSpeed | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| OddShape | openlabel | subjectVehicleSpeedValue |  |  | Speed (km/h) (Refer to BSI PAS-1883 Section 5.4.b). |  | openlabel.shacl.ttl |
| OddShape | openlabel | WeatherRain |  |  | Validation class for weatherRain | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| OddShape | openlabel | weatherRainValue |  |  | Rainfall Intensity (mm/h) (Refer to BSI PAS-1883 Section 5.3.1.2). | <http://www.w3.org/2001/XMLSchema#decimal> | openlabel.shacl.ttl |
| OddShape | openlabel | WeatherSnow |  |  | Validation class for weatherSnow | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| OddShape | openlabel | weatherSnowValue |  |  | Visibility (km) (Refer to BSI PAS-1883 Section 5.3.1.3). | <http://www.w3.org/2001/XMLSchema#decimal> | openlabel.shacl.ttl |
| OddShape | openlabel | WeatherWind |  |  | Validation class for weatherWind | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| OddShape | openlabel | weatherWindValue |  |  | Wind Speed (m/s) (Refer to BSI PAS-1883 Section 5.3.1.1). | <http://www.w3.org/2001/XMLSchema#decimal> | openlabel.shacl.ttl |
| OddShape | openlabel | IlluminationCloudiness |  |  | Validation class for illuminationCloudiness | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| OddShape | openlabel | illuminationCloudinessValue |  |  | Cloud cover (okta) (Refer to BSI PAS-1883 Section 5.3.3.c). | <http://www.w3.org/2001/XMLSchema#decimal> | openlabel.shacl.ttl |
| OddShape | openlabel | DaySunElevation |  |  | Validation class for daySunElevation | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| OddShape | openlabel | daySunElevationValue |  |  | Sun Elevation (degrees) (Refer to BSI PAS-1883 Section 5.3.3.a.1). | <http://www.w3.org/2001/XMLSchema#decimal> | openlabel.shacl.ttl |
| OddShape | openlabel | TrafficAgentDensity |  |  | Validation class for trafficAgentDensity | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| OddShape | openlabel | trafficAgentDensityValue |  |  | Density (vehicles/km) (Refer to BSI PAS-1883 Section 5.4.a.1). | <http://www.w3.org/2001/XMLSchema#integer> | openlabel.shacl.ttl |
| OddShape | openlabel | TrafficFlowRate |  |  | Validation class for trafficFlowRate | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| OddShape | openlabel | trafficFlowRateValue |  |  | Rate (vehicles/h) (Refer to BSI PAS-1883 Section 5.4.a.3). | <http://www.w3.org/2001/XMLSchema#integer> | openlabel.shacl.ttl |
| OddShape | openlabel | TrafficVolume |  |  | Validation class for trafficVolume | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| OddShape | openlabel | trafficVolumeValue |  |  | Volume (vehicle km) (Refer to BSI PAS-1883 Section 5.4.a.2). | <http://www.w3.org/2001/XMLSchema#integer> | openlabel.shacl.ttl |
| OddShape | openlabel | LaneSpecificationDimensions |  |  | Validation class for laneSpecificationDimensions | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| OddShape | openlabel | laneSpecificationDimensionsValue |  |  | Lane width (m) (Refer to BSI PAS-1883 Section 5.2.3.4.a). |  | openlabel.shacl.ttl |
| OddShape | openlabel | LaneSpecificationLaneCount |  |  | Validation class for laneSpecificationLaneCount | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| OddShape | openlabel | laneSpecificationLaneCountValue |  |  | Number of lanes (Unit) (Refer to BSI PAS-1883 Section 5.2.3.4.d). |  | openlabel.shacl.ttl |
| OddShape | openlabel | HorizontalCurves |  |  | Validation class for horizontalCurves | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| OddShape | openlabel | horizontalCurvesValue |  |  | Curve Radius (m) (Refer to BSI PAS-1883 Section 5.2.3.3). | <http://www.w3.org/2001/XMLSchema#decimal> | openlabel.shacl.ttl |
| OddShape | openlabel | LongitudinalDownSlope |  |  | Validation class for longitudinalDownSlope | <http://www.w3.org/2001/XMLSchema#boolean> | openlabel.shacl.ttl |
| OddShape | openlabel | longitudinalDownSlopeValue |  |  | Gradient (%) (Refer to BSI PAS-1883 Section 5.2.3.3.ii). | <http://www.w3.org/2001/XMLSchema#decimal> | openlabel.shacl.ttl |
| QuantitativeValueShape | schema | minValue | 1 |  |  |  | openlabel.shacl.ttl |
| QuantitativeValueShape | schema | maxValue | 1 |  |  |  | openlabel.shacl.ttl |
