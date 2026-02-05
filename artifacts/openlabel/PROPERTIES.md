## openlabel Properties

### Class Diagram

_Class diagram omitted for size (243 classes). See class hierarchy and definitions below._

### Class Hierarchy

- Base Tag (https://openlabel.asam.net/V1-0-0/ontologies/Tag)
  - Base Administration Tag (https://openlabel.asam.net/V1-0-0/ontologies/AdminTag)
  - Behaviour (https://openlabel.asam.net/V1-0-0/ontologies/Behaviour)
    - Communication (https://openlabel.asam.net/V1-0-0/ontologies/BehaviourCommunication)
      - Flash headlight (https://openlabel.asam.net/V1-0-0/ontologies/CommunicationHeadlightFlash)
      - Signal emergency (https://openlabel.asam.net/V1-0-0/ontologies/CommunicationSignalEmergency)
      - Signal hazard (https://openlabel.asam.net/V1-0-0/ontologies/CommunicationSignalHazard)
      - Signal left (https://openlabel.asam.net/V1-0-0/ontologies/CommunicationSignalLeft)
      - Signal right (https://openlabel.asam.net/V1-0-0/ontologies/CommunicationSignalRight)
      - Signal slowing (https://openlabel.asam.net/V1-0-0/ontologies/CommunicationSignalSlowing)
      - Sound horn (https://openlabel.asam.net/V1-0-0/ontologies/CommunicationHorn)
      - Wave (https://openlabel.asam.net/V1-0-0/ontologies/CommunicationWave)
    - Motion (https://openlabel.asam.net/V1-0-0/ontologies/BehaviourMotion)
      - Accelerate (https://openlabel.asam.net/V1-0-0/ontologies/MotionAccelerate)
      - Cross (https://openlabel.asam.net/V1-0-0/ontologies/MotionCross)
      - Cut-in (https://openlabel.asam.net/V1-0-0/ontologies/MotionCutIn)
      - Cut-out (https://openlabel.asam.net/V1-0-0/ontologies/MotionCutOut)
      - Decelerate (https://openlabel.asam.net/V1-0-0/ontologies/MotionDecelerate)
      - Drive (https://openlabel.asam.net/V1-0-0/ontologies/MotionDrive)
      - Lane change left (https://openlabel.asam.net/V1-0-0/ontologies/MotionLaneChangeLeft)
      - Lane change right (https://openlabel.asam.net/V1-0-0/ontologies/MotionLaneChangeRight)
      - Move away (https://openlabel.asam.net/V1-0-0/ontologies/MotionAway)
      - Move towards (https://openlabel.asam.net/V1-0-0/ontologies/MotionTowards)
      - Overtake (https://openlabel.asam.net/V1-0-0/ontologies/MotionOvertake)
      - Reverse (https://openlabel.asam.net/V1-0-0/ontologies/MotionReverse)
      - Run (https://openlabel.asam.net/V1-0-0/ontologies/MotionRun)
      - Slide (https://openlabel.asam.net/V1-0-0/ontologies/MotionSlide)
      - Stop (https://openlabel.asam.net/V1-0-0/ontologies/MotionStop)
      - Turn (https://openlabel.asam.net/V1-0-0/ontologies/MotionTurn)
      - Turn left (https://openlabel.asam.net/V1-0-0/ontologies/MotionTurnLeft)
      - Turn right (https://openlabel.asam.net/V1-0-0/ontologies/MotionTurnRight)
      - U-turn (https://openlabel.asam.net/V1-0-0/ontologies/MotionUTurn)
      - Walk (https://openlabel.asam.net/V1-0-0/ontologies/MotionWalk)
  - ODD (https://openlabel.asam.net/V1-0-0/ontologies/Odd)
    - Dynamic elements (https://openlabel.asam.net/V1-0-0/ontologies/OddDynamicElements)
      - Subject vehicle (https://openlabel.asam.net/V1-0-0/ontologies/DynamicElementsSubjectVehicle)
        - Speed (https://openlabel.asam.net/V1-0-0/ontologies/SubjectVehicleSpeed)
      - Traffic (https://openlabel.asam.net/V1-0-0/ontologies/DynamicElementsTraffic)
        - Agent type (https://openlabel.asam.net/V1-0-0/ontologies/TrafficAgentType)
        - Density of agents (https://openlabel.asam.net/V1-0-0/ontologies/TrafficAgentDensity)
        - Flow rate (https://openlabel.asam.net/V1-0-0/ontologies/TrafficFlowRate)
        - Presence of special vehicles (e.g. ambulances or police vehicles). (https://openlabel.asam.net/V1-0-0/ontologies/TrafficSpecialVehicle)
        - Volume of traffic (https://openlabel.asam.net/V1-0-0/ontologies/TrafficVolume)
    - Environmental Conditions (https://openlabel.asam.net/V1-0-0/ontologies/OddEnvironment)
      - Connectivity (https://openlabel.asam.net/V1-0-0/ontologies/EnvironmentConnectivity)
        - Communication (https://openlabel.asam.net/V1-0-0/ontologies/ConnectivityCommunication)
          - Vehicle to infrastructure communication (V2I) (https://openlabel.asam.net/V1-0-0/ontologies/CommunicationV2i)
            - 802.11p-based WiFi (https://openlabel.asam.net/V1-0-0/ontologies/V2iWifi)
            - Cellular (https://openlabel.asam.net/V1-0-0/ontologies/V2iCellular)
            - Satellite (https://openlabel.asam.net/V1-0-0/ontologies/V2iSatellite)
          - Vehicle to vehicle communication (V2V) (https://openlabel.asam.net/V1-0-0/ontologies/CommunicationV2v)
            - 802.11p-based WiFi (https://openlabel.asam.net/V1-0-0/ontologies/V2vWifi)
            - Cellular (https://openlabel.asam.net/V1-0-0/ontologies/V2vCellular)
            - Satellite (https://openlabel.asam.net/V1-0-0/ontologies/V2vSatellite)
        - Positioning (https://openlabel.asam.net/V1-0-0/ontologies/ConnectivityPositioning)
          - Galileo (https://openlabel.asam.net/V1-0-0/ontologies/PositioningGalileo)
          - GLObal NAvigation Satellite System (GLONASS) (https://openlabel.asam.net/V1-0-0/ontologies/PositioningGlonass)
          - Global Positioning System (GPS) (https://openlabel.asam.net/V1-0-0/ontologies/PositioningGps)
      - Illumination (https://openlabel.asam.net/V1-0-0/ontologies/EnvironmentIllumination)
        - Artificial illumination (https://openlabel.asam.net/V1-0-0/ontologies/IlluminationArtificial)
          - Oncoming vehicle lights (https://openlabel.asam.net/V1-0-0/ontologies/ArtificialVehicleLighting)
          - Streetlights (https://openlabel.asam.net/V1-0-0/ontologies/ArtificialStreetLighting)
        - Cloudiness (https://openlabel.asam.net/V1-0-0/ontologies/IlluminationCloudiness)
        - Day (https://openlabel.asam.net/V1-0-0/ontologies/IlluminationDay)
          - Elevation of the sun above the horizon (https://openlabel.asam.net/V1-0-0/ontologies/DaySunElevation)
          - Position of the sun (https://openlabel.asam.net/V1-0-0/ontologies/DaySunPosition)
            - Behind (https://openlabel.asam.net/V1-0-0/ontologies/SunPositionBehind)
            - Front (https://openlabel.asam.net/V1-0-0/ontologies/SunPositionFront)
            - Left (https://openlabel.asam.net/V1-0-0/ontologies/SunPositionLeft)
            - Right (https://openlabel.asam.net/V1-0-0/ontologies/SunPositionRight)
        - Night or lowAmbient lighting condition (https://openlabel.asam.net/V1-0-0/ontologies/IlluminationLowLight)
          - LowAmbient lighting (https://openlabel.asam.net/V1-0-0/ontologies/LowLightAmbient)
          - Night (https://openlabel.asam.net/V1-0-0/ontologies/LowLightNight)
      - Particulates (obscuration by nonPrecipitating water droplets and other particulates) (https://openlabel.asam.net/V1-0-0/ontologies/EnvironmentParticulates)
        - Marine (coastal areas only) (https://openlabel.asam.net/V1-0-0/ontologies/ParticulatesMarine)
        - Non-precipitating water droplets or ice crystals (i.e. mist/fog) (https://openlabel.asam.net/V1-0-0/ontologies/ParticulatesWater)
        - Sand and dust (https://openlabel.asam.net/V1-0-0/ontologies/ParticulatesDust)
        - Smoke and pollution (https://openlabel.asam.net/V1-0-0/ontologies/ParticulatesPollution)
        - Volcanic ash (https://openlabel.asam.net/V1-0-0/ontologies/ParticulatesVolcanic)
      - Weather (https://openlabel.asam.net/V1-0-0/ontologies/EnvironmentWeather)
        - Rainfall (https://openlabel.asam.net/V1-0-0/ontologies/WeatherRain)
          - Rainfall type (https://openlabel.asam.net/V1-0-0/ontologies/RainType)
            - Convective (https://openlabel.asam.net/V1-0-0/ontologies/RainTypeConvective)
            - Dynamic (https://openlabel.asam.net/V1-0-0/ontologies/RainTypeDynamic)
            - Orographic (https://openlabel.asam.net/V1-0-0/ontologies/RainTypeOrographic)
        - Snowfall (https://openlabel.asam.net/V1-0-0/ontologies/WeatherSnow)
        - Wind (https://openlabel.asam.net/V1-0-0/ontologies/WeatherWind)
    - Scenery (https://openlabel.asam.net/V1-0-0/ontologies/OddScenery)
      - Drivable area (https://openlabel.asam.net/V1-0-0/ontologies/SceneryDrivableArea)
        - Drivable area edge (https://openlabel.asam.net/V1-0-0/ontologies/DrivableAreaEdge)
          - Line markers (https://openlabel.asam.net/V1-0-0/ontologies/EdgeLineMarkers)
          - None (https://openlabel.asam.net/V1-0-0/ontologies/EdgeNone)
          - Shoulder (grass) (https://openlabel.asam.net/V1-0-0/ontologies/EdgeShoulderGrass)
          - Shoulder (paved or gravel) (https://openlabel.asam.net/V1-0-0/ontologies/EdgeShoulderPavedOrGravel)
          - Solid barriers (e.g. grating, rails, curb, cones) (https://openlabel.asam.net/V1-0-0/ontologies/EdgeSolidBarriers)
          - Temporary line markers (https://openlabel.asam.net/V1-0-0/ontologies/EdgeTemporaryLineMarkers)
        - Drivable area geometry (https://openlabel.asam.net/V1-0-0/ontologies/DrivableAreaGeometry)
          - Horizontal plane (https://openlabel.asam.net/V1-0-0/ontologies/GeometryHorizontal)
            - Curves (https://openlabel.asam.net/V1-0-0/ontologies/HorizontalCurves)
            - Straight lines (https://openlabel.asam.net/V1-0-0/ontologies/HorizontalStraights)
          - Longitudinal plane (https://openlabel.asam.net/V1-0-0/ontologies/GeometryLongitudinal)
            - Dow-slope (negativeGradient) (https://openlabel.asam.net/V1-0-0/ontologies/LongitudinalDownSlope)
            - Level plane (https://openlabel.asam.net/V1-0-0/ontologies/LongitudinalLevelPlane)
            - Up-slope (positive gradient) (https://openlabel.asam.net/V1-0-0/ontologies/LongitudinalUpSlope)
          - Transverse plane (https://openlabel.asam.net/V1-0-0/ontologies/GeometryTransverse)
            - Barriers on edges (https://openlabel.asam.net/V1-0-0/ontologies/TransverseBarriers)
            - Divided (https://openlabel.asam.net/V1-0-0/ontologies/TransverseDivided)
            - Pavements (https://openlabel.asam.net/V1-0-0/ontologies/TransversePavements)
            - Types of lanes together (https://openlabel.asam.net/V1-0-0/ontologies/TransverseLanesTogether)
            - Undivided (https://openlabel.asam.net/V1-0-0/ontologies/TransverseUndivided)
        - Drivable area lane specification (https://openlabel.asam.net/V1-0-0/ontologies/DrivableAreaLaneSpecification)
          - Direction of travel (https://openlabel.asam.net/V1-0-0/ontologies/LaneSpecificationTravelDirection)
            - Left (https://openlabel.asam.net/V1-0-0/ontologies/TravelDirectionLeft)
            - Right (https://openlabel.asam.net/V1-0-0/ontologies/TravelDirectionRight)
          - Lane dimensions (https://openlabel.asam.net/V1-0-0/ontologies/LaneSpecificationDimensions)
          - Lane marking (https://openlabel.asam.net/V1-0-0/ontologies/LaneSpecificationMarking)
          - Lane type (https://openlabel.asam.net/V1-0-0/ontologies/LaneSpecificationType)
            - Bus lane (https://openlabel.asam.net/V1-0-0/ontologies/LaneTypeBus)
            - Cycle lane (https://openlabel.asam.net/V1-0-0/ontologies/LaneTypeCycle)
            - Emergency lane (https://openlabel.asam.net/V1-0-0/ontologies/LaneTypeEmergency)
            - Special purpose lane (https://openlabel.asam.net/V1-0-0/ontologies/LaneTypeSpecial)
            - Traffic lane (https://openlabel.asam.net/V1-0-0/ontologies/LaneTypeTraffic)
            - Tram lane (https://openlabel.asam.net/V1-0-0/ontologies/LaneTypeTram)
          - Number of lanes (https://openlabel.asam.net/V1-0-0/ontologies/LaneSpecificationLaneCount)
        - Drivable area signs (https://openlabel.asam.net/V1-0-0/ontologies/DrivableAreaSigns)
          - Information signs (https://openlabel.asam.net/V1-0-0/ontologies/SignsInformation)
            - Uniform (https://openlabel.asam.net/V1-0-0/ontologies/InformationSignsUniform)
              - FullTime (https://openlabel.asam.net/V1-0-0/ontologies/InformationSignsUniformFullTime)
              - Temporary (https://openlabel.asam.net/V1-0-0/ontologies/InformationSignsUniformTemporary)
            - Variable (https://openlabel.asam.net/V1-0-0/ontologies/InformationSignsVariable)
              - FullTime (https://openlabel.asam.net/V1-0-0/ontologies/InformationSignsVariableFullTime)
              - Temporary (https://openlabel.asam.net/V1-0-0/ontologies/InformationSignsVariableTemporary)
          - Regulatory signs (https://openlabel.asam.net/V1-0-0/ontologies/SignsRegulatory)
            - Uniform (https://openlabel.asam.net/V1-0-0/ontologies/RegulatorySignsUniform)
              - FullTime (https://openlabel.asam.net/V1-0-0/ontologies/RegulatorySignsUniformFullTime)
              - Temporary (https://openlabel.asam.net/V1-0-0/ontologies/RegulatorySignsUniformTemporary)
            - Variable (https://openlabel.asam.net/V1-0-0/ontologies/RegulatorySignsVariable)
              - FullTime (https://openlabel.asam.net/V1-0-0/ontologies/RegulatorySignsVariableFullTime)
              - Temporary (https://openlabel.asam.net/V1-0-0/ontologies/RegulatorySignsVariableTemporary)
          - Warning signs (https://openlabel.asam.net/V1-0-0/ontologies/SignsWarning)
            - Uniform (https://openlabel.asam.net/V1-0-0/ontologies/WarningSignsUniform)
              - FullTime (https://openlabel.asam.net/V1-0-0/ontologies/WarningSignsUniformFullTime)
              - Temporary (https://openlabel.asam.net/V1-0-0/ontologies/WarningSignsUniformTemporary)
            - Variable (https://openlabel.asam.net/V1-0-0/ontologies/WarningSignsVariable)
              - FullTime (https://openlabel.asam.net/V1-0-0/ontologies/WarningSignsVariableFullTime)
              - Temporary (https://openlabel.asam.net/V1-0-0/ontologies/WarningSignsVariableTemporary)
        - Drivable area surface (https://openlabel.asam.net/V1-0-0/ontologies/DrivableAreaSurface)
          - Drivable area induced road surface conditions (https://openlabel.asam.net/V1-0-0/ontologies/DrivableAreaSurfaceCondition)
            - Flooded roadways (https://openlabel.asam.net/V1-0-0/ontologies/SurfaceConditionFlooded)
            - Icy (https://openlabel.asam.net/V1-0-0/ontologies/SurfaceConditionIcy)
            - Mirage (https://openlabel.asam.net/V1-0-0/ontologies/SurfaceConditionMirage)
            - Snow on drivable area (https://openlabel.asam.net/V1-0-0/ontologies/SurfaceConditionSnow)
            - Standing water (https://openlabel.asam.net/V1-0-0/ontologies/SurfaceConditionStandingWater)
            - Surface contamination (https://openlabel.asam.net/V1-0-0/ontologies/SurfaceConditionContamination)
            - Wet road (https://openlabel.asam.net/V1-0-0/ontologies/SurfaceConditionWet)
          - Drivable area surface features (https://openlabel.asam.net/V1-0-0/ontologies/DrivableAreaSurfaceFeature)
            - Cracks (https://openlabel.asam.net/V1-0-0/ontologies/SurfaceFeatureCrack)
            - Potholes (https://openlabel.asam.net/V1-0-0/ontologies/SurfaceFeaturePothole)
            - Ruts (https://openlabel.asam.net/V1-0-0/ontologies/SurfaceFeatureRut)
            - Swells (https://openlabel.asam.net/V1-0-0/ontologies/SurfaceFeatureSwell)
          - Drivable area surface type (https://openlabel.asam.net/V1-0-0/ontologies/DrivableAreaSurfaceType)
            - Loose (e.g. gravel, earth, sand) (https://openlabel.asam.net/V1-0-0/ontologies/SurfaceTypeLoose)
            - Segmented (e.g. concrete slabs, granite setts, cobblestones) (https://openlabel.asam.net/V1-0-0/ontologies/SurfaceTypeSegmented)
            - Uniform (e.g. asphalt) (https://openlabel.asam.net/V1-0-0/ontologies/SurfaceTypeUniform)
        - Drivable area type (https://openlabel.asam.net/V1-0-0/ontologies/DrivableAreaType)
          - Distributor roads (https://openlabel.asam.net/V1-0-0/ontologies/RoadTypeDistributor)
          - Minor roads (https://openlabel.asam.net/V1-0-0/ontologies/RoadTypeMinor)
          - Motorways (https://openlabel.asam.net/V1-0-0/ontologies/RoadTypeMotorway)
            - With active traffic management (smart motorways) (https://openlabel.asam.net/V1-0-0/ontologies/MotorwayManaged)
            - Without active traffic management (https://openlabel.asam.net/V1-0-0/ontologies/MotorwayUnmanaged)
          - Parking (https://openlabel.asam.net/V1-0-0/ontologies/RoadTypeParking)
          - Radial roads (https://openlabel.asam.net/V1-0-0/ontologies/RoadTypeRadial)
          - Shared space (https://openlabel.asam.net/V1-0-0/ontologies/RoadTypeShared)
          - Slip roads (https://openlabel.asam.net/V1-0-0/ontologies/RoadTypeSlip)
      - Fixed road structures (https://openlabel.asam.net/V1-0-0/ontologies/SceneryFixedStructure)
        - Buildings (https://openlabel.asam.net/V1-0-0/ontologies/FixedStructureBuilding)
        - Street furniture (e.g. bollards) (https://openlabel.asam.net/V1-0-0/ontologies/FixedStructureStreetFurniture)
        - Street lights (https://openlabel.asam.net/V1-0-0/ontologies/FixedStructureStreetlight)
        - Vegetation (https://openlabel.asam.net/V1-0-0/ontologies/FixedStructureVegetation)
      - Junctions (https://openlabel.asam.net/V1-0-0/ontologies/SceneryJunction)
        - Intersections (https://openlabel.asam.net/V1-0-0/ontologies/JunctionIntersection)
          - Crossroads (https://openlabel.asam.net/V1-0-0/ontologies/IntersectionCrossroad)
          - Grade separated (https://openlabel.asam.net/V1-0-0/ontologies/IntersectionGradeSeperated)
          - Staggered (https://openlabel.asam.net/V1-0-0/ontologies/IntersectionStaggered)
          - TJunctions (https://openlabel.asam.net/V1-0-0/ontologies/IntersectionTJunction)
          - YJunction (https://openlabel.asam.net/V1-0-0/ontologies/IntersectionYJunction)
        - Roundabouts (https://openlabel.asam.net/V1-0-0/ontologies/JunctionRoundabout)
          - Compact (https://openlabel.asam.net/V1-0-0/ontologies/RoundaboutCompact)
            - NonSignalised (https://openlabel.asam.net/V1-0-0/ontologies/RoundaboutCompactSignal)
            - Signalised (https://openlabel.asam.net/V1-0-0/ontologies/RoundaboutCompactNosignal)
          - Double (https://openlabel.asam.net/V1-0-0/ontologies/RoundaboutDouble)
            - NonSignalised (https://openlabel.asam.net/V1-0-0/ontologies/RoundaboutDoubleSignal)
            - Signalised (https://openlabel.asam.net/V1-0-0/ontologies/RoundaboutDoubleNosignal)
          - Large (https://openlabel.asam.net/V1-0-0/ontologies/RoundaboutLarge)
            - NonSignalised (https://openlabel.asam.net/V1-0-0/ontologies/RoundaboutLargeSignal)
            - Signalised (https://openlabel.asam.net/V1-0-0/ontologies/RoundaboutLargeNosignal)
          - Mini (https://openlabel.asam.net/V1-0-0/ontologies/RoundaboutMini)
            - NonSignalised (https://openlabel.asam.net/V1-0-0/ontologies/RoundaboutMiniSignal)
            - Signalised (https://openlabel.asam.net/V1-0-0/ontologies/RoundaboutMiniNosignal)
          - Normal (https://openlabel.asam.net/V1-0-0/ontologies/RoundaboutNormal)
            - NonSignalised (https://openlabel.asam.net/V1-0-0/ontologies/RoundaboutNormalSignal)
            - Signalised (https://openlabel.asam.net/V1-0-0/ontologies/RoundaboutNormalNosignal)
      - Special structures (https://openlabel.asam.net/V1-0-0/ontologies/ScenerySpecialStructure)
        - Automatic access control (https://openlabel.asam.net/V1-0-0/ontologies/SpecialStructureAutoAccess)
        - Bridges (https://openlabel.asam.net/V1-0-0/ontologies/SpecialStructureBridge)
        - Pedestrian crossings (https://openlabel.asam.net/V1-0-0/ontologies/SpecialStructurePedestrianCrossing)
        - Rail crossings (https://openlabel.asam.net/V1-0-0/ontologies/SpecialStructureRailCrossing)
        - Toll plaza (https://openlabel.asam.net/V1-0-0/ontologies/SpecialStructureTollPlaza)
        - Tunnels (https://openlabel.asam.net/V1-0-0/ontologies/SpecialStructureTunnel)
      - Temporary road structures (https://openlabel.asam.net/V1-0-0/ontologies/SceneryTemporaryStructure)
        - Construction site detours (https://openlabel.asam.net/V1-0-0/ontologies/TemporaryStructureConstructionDetour)
        - Refuse collection (https://openlabel.asam.net/V1-0-0/ontologies/TemporaryStructureRefuseCollection)
        - Road signage (https://openlabel.asam.net/V1-0-0/ontologies/TemporaryStructureRoadSignage)
        - Road works (https://openlabel.asam.net/V1-0-0/ontologies/TemporaryStructureRoadWorks)
      - Zones (https://openlabel.asam.net/V1-0-0/ontologies/SceneryZone)
        - GeoFenced areas (https://openlabel.asam.net/V1-0-0/ontologies/ZoneGeoFenced)
        - Interference zones (https://openlabel.asam.net/V1-0-0/ontologies/ZoneInterference)
        - Regions or states (https://openlabel.asam.net/V1-0-0/ontologies/ZoneRegion)
        - School zones (https://openlabel.asam.net/V1-0-0/ontologies/ZoneSchool)
        - Traffic management zones (https://openlabel.asam.net/V1-0-0/ontologies/ZoneTrafficManagement)
  - Road user (https://openlabel.asam.net/V1-0-0/ontologies/RoadUser)
    - Animal (https://openlabel.asam.net/V1-0-0/ontologies/RoadUserAnimal)
    - Human (https://openlabel.asam.net/V1-0-0/ontologies/RoadUserHuman)
      - Animal rider (https://openlabel.asam.net/V1-0-0/ontologies/HumanAnimalRider)
      - Cyclist (https://openlabel.asam.net/V1-0-0/ontologies/HumanCyclist)
      - Driver (https://openlabel.asam.net/V1-0-0/ontologies/HumanDriver)
      - Motorcyclist (https://openlabel.asam.net/V1-0-0/ontologies/HumanMotorcyclist)
      - Passenger (https://openlabel.asam.net/V1-0-0/ontologies/HumanPassenger)
      - Pedestrian (https://openlabel.asam.net/V1-0-0/ontologies/HumanPedestrian)
      - Wheelchair user (https://openlabel.asam.net/V1-0-0/ontologies/HumanWheelchairUser)
    - Vehicle (https://openlabel.asam.net/V1-0-0/ontologies/RoadUserVehicle)
      - Agricultural vehicle (https://openlabel.asam.net/V1-0-0/ontologies/VehicleAgricultural)
      - Bus (https://openlabel.asam.net/V1-0-0/ontologies/VehicleBus)
      - Car (https://openlabel.asam.net/V1-0-0/ontologies/VehicleCar)
      - Construction vehicle (https://openlabel.asam.net/V1-0-0/ontologies/VehicleConstruction)
      - Cycle (https://openlabel.asam.net/V1-0-0/ontologies/VehicleCycle)
      - Emergency vehicle (https://openlabel.asam.net/V1-0-0/ontologies/VehicleEmergency)
      - Motorcycle (https://openlabel.asam.net/V1-0-0/ontologies/VehicleMotorcycle)
      - Trailer (https://openlabel.asam.net/V1-0-0/ontologies/VehicleTrailer)
      - Truck (https://openlabel.asam.net/V1-0-0/ontologies/VehicleTruck)
      - Van (https://openlabel.asam.net/V1-0-0/ontologies/VehicleVan)
      - Wheelchair (https://openlabel.asam.net/V1-0-0/ontologies/VehicleWheelchair)
- Scenario (https://openlabel.asam.net/V1-0-0/ontologies/Scenario)

### Class Definitions

|Class|IRI|Description|Parents|
|---|---|---|---|
|802.11p-based WiFi|https://openlabel.asam.net/V1-0-0/ontologies/V2iWifi|Refer to BSI PAS-1883 Section 5.3.4.a.2.iii|CommunicationV2i|
|802.11p-based WiFi|https://openlabel.asam.net/V1-0-0/ontologies/V2vWifi|Refer to BSI PAS-1883 Section 5.3.4.a.1.iii|CommunicationV2v|
|Accelerate|https://openlabel.asam.net/V1-0-0/ontologies/MotionAccelerate|An activity where the road user increases their velocity|BehaviourMotion|
|Agent type|https://openlabel.asam.net/V1-0-0/ontologies/TrafficAgentType|Refer to BSI PAS-1883 Section 5.4.a.4|DynamicElementsTraffic|
|Agricultural vehicle|https://openlabel.asam.net/V1-0-0/ontologies/VehicleAgricultural|A motor vehicle designed for the purpose of farming, such as tractors, harvesters|RoadUserVehicle|
|Animal|https://openlabel.asam.net/V1-0-0/ontologies/RoadUserAnimal|A non-human living organism that feeds on organic matter, typically having specialized sense organs and nervous system and able to respond rapidly to stimuli|RoadUser|
|Animal rider|https://openlabel.asam.net/V1-0-0/ontologies/HumanAnimalRider|A person who is riding an animal|RoadUserHuman|
|Artificial illumination|https://openlabel.asam.net/V1-0-0/ontologies/IlluminationArtificial|Refer to BSI PAS-1883 Section 5.3.3.d|EnvironmentIllumination|
|Automatic access control|https://openlabel.asam.net/V1-0-0/ontologies/SpecialStructureAutoAccess|Refer to BSI PAS-1883 Section 5.2.5.a|ScenerySpecialStructure|
|Barriers on edges|https://openlabel.asam.net/V1-0-0/ontologies/TransverseBarriers|Refer to BSI PAS-1883 Section 5.2.3.3.4|GeometryTransverse|
|Base Administration Tag|https://openlabel.asam.net/V1-0-0/ontologies/AdminTag|The base tag to use when extending the Administration tags with new classes.|Tag|
|Base Tag|https://openlabel.asam.net/V1-0-0/ontologies/Tag|The base tag|Class|
|Behaviour|https://openlabel.asam.net/V1-0-0/ontologies/Behaviour|An activity performed by a road user|Tag|
|Behind|https://openlabel.asam.net/V1-0-0/ontologies/SunPositionBehind|Refer to BSI PAS-1883 Section 5.3.3.a.2|DaySunPosition|
|Bridges|https://openlabel.asam.net/V1-0-0/ontologies/SpecialStructureBridge|Refer to BSI PAS-1883 Section 5.2.5.b|ScenerySpecialStructure|
|Buildings|https://openlabel.asam.net/V1-0-0/ontologies/FixedStructureBuilding|Refer to BSI PAS-1883 Section 5.2.6.a|SceneryFixedStructure|
|Bus|https://openlabel.asam.net/V1-0-0/ontologies/VehicleBus|A motor vehicle designed to carry many passengers, contracted from omnibus, with variants multibus, motorbus, autobus|RoadUserVehicle|
|Bus lane|https://openlabel.asam.net/V1-0-0/ontologies/LaneTypeBus|Refer to BSI PAS-1883 Section 5.2.3.4|LaneSpecificationType|
|Car|https://openlabel.asam.net/V1-0-0/ontologies/VehicleCar|A motor vehicle used primarily for the transportation of a small number of people where the occupants are protected by a safety frame|RoadUserVehicle|
|Cellular|https://openlabel.asam.net/V1-0-0/ontologies/V2iCellular|Refer to BSI PAS-1883 Section 5.3.4.a.2.i|CommunicationV2i|
|Cellular|https://openlabel.asam.net/V1-0-0/ontologies/V2vCellular|Refer to BSI PAS-1883 Section 5.3.4.a.1.i|CommunicationV2v|
|Cloudiness|https://openlabel.asam.net/V1-0-0/ontologies/IlluminationCloudiness|Refer to BSI PAS-1883 Section 5.3.3.c|EnvironmentIllumination|
|Communication|https://openlabel.asam.net/V1-0-0/ontologies/BehaviourCommunication|An activity in which the road user issues a communication|Behaviour|
|Communication|https://openlabel.asam.net/V1-0-0/ontologies/ConnectivityCommunication|Refer to BSI PAS-1883 Section 5.3.4.a|EnvironmentConnectivity|
|Compact|https://openlabel.asam.net/V1-0-0/ontologies/RoundaboutCompact|Refer to BSI PAS-1883 Section 5.2.4.b|JunctionRoundabout|
|Connectivity|https://openlabel.asam.net/V1-0-0/ontologies/EnvironmentConnectivity|Refer to BSI PAS-1883 Section 5.3.4|OddEnvironment|
|Construction site detours|https://openlabel.asam.net/V1-0-0/ontologies/TemporaryStructureConstructionDetour|Refer to BSI PAS-1883 Section 5.2.7.a|SceneryTemporaryStructure|
|Construction vehicle|https://openlabel.asam.net/V1-0-0/ontologies/VehicleConstruction|A motor vehicle designed for the purpose of construction, such as cranes, bulldozer|RoadUserVehicle|
|Convective|https://openlabel.asam.net/V1-0-0/ontologies/RainTypeConvective|Refer to BSI PAS-1883 Section 5.3.1.2.2|RainType|
|Cracks|https://openlabel.asam.net/V1-0-0/ontologies/SurfaceFeatureCrack|Refer to BSI PAS-1883 Section 5.2.3.7|DrivableAreaSurfaceFeature|
|Cross|https://openlabel.asam.net/V1-0-0/ontologies/MotionCross|An activity where the trajectory of the road user crosses the trajectory of the object|BehaviourMotion|
|Crossroads|https://openlabel.asam.net/V1-0-0/ontologies/IntersectionCrossroad|Refer to BSI PAS-1883 Section 5.2.4.iv|JunctionIntersection|
|Curves|https://openlabel.asam.net/V1-0-0/ontologies/HorizontalCurves|Refer to BSI PAS-1883 Section 5.2.3.3|GeometryHorizontal|
|Cut-in|https://openlabel.asam.net/V1-0-0/ontologies/MotionCutIn|An activity where the subject vehicle ends up directly in front of the object vehicle in such a manner as to (potentially) affect the behavior of the object vehicle|BehaviourMotion|
|Cut-out|https://openlabel.asam.net/V1-0-0/ontologies/MotionCutOut|A two participant moving activity where the subject and object vehicles start in the same lane and then the object participant suddenly moves out of the lane|BehaviourMotion|
|Cycle|https://openlabel.asam.net/V1-0-0/ontologies/VehicleCycle|A cycle, is a human-powered or motor-assisted, pedal-driven, wheeled vehicle|RoadUserVehicle|
|Cycle lane|https://openlabel.asam.net/V1-0-0/ontologies/LaneTypeCycle|Refer to BSI PAS-1883 Section 5.2.3.4|LaneSpecificationType|
|Cyclist|https://openlabel.asam.net/V1-0-0/ontologies/HumanCyclist|A person who is riding a cycle|RoadUserHuman|
|Day|https://openlabel.asam.net/V1-0-0/ontologies/IlluminationDay|Refer to BSI PAS-1883 Section 5.3.3.a|EnvironmentIllumination|
|Decelerate|https://openlabel.asam.net/V1-0-0/ontologies/MotionDecelerate|An activity where the road user decreases their velocity|BehaviourMotion|
|Density of agents|https://openlabel.asam.net/V1-0-0/ontologies/TrafficAgentDensity|Refer to BSI PAS-1883 Section 5.4.a.1|DynamicElementsTraffic|
|Direction of travel|https://openlabel.asam.net/V1-0-0/ontologies/LaneSpecificationTravelDirection|Refer to BSI PAS-1883 Section 5.2.3.4.e|DrivableAreaLaneSpecification|
|Distributor roads|https://openlabel.asam.net/V1-0-0/ontologies/RoadTypeDistributor|Refer to BSI PAS-1883 Section 5.2.3.2.c|DrivableAreaType|
|Divided|https://openlabel.asam.net/V1-0-0/ontologies/TransverseDivided|Refer to BSI PAS-1883 Section 5.2.3.3.1|GeometryTransverse|
|Double|https://openlabel.asam.net/V1-0-0/ontologies/RoundaboutDouble|Refer to BSI PAS-1883 Section 5.2.4.c|JunctionRoundabout|
|Dow-slope (negativeGradient)|https://openlabel.asam.net/V1-0-0/ontologies/LongitudinalDownSlope|Refer to BSI PAS-1883 Section 5.2.3.3.ii|GeometryLongitudinal|
|Drivable area|https://openlabel.asam.net/V1-0-0/ontologies/SceneryDrivableArea|Refer to BSI PAS-1883 Section 5.2.1.b|OddScenery|
|Drivable area edge|https://openlabel.asam.net/V1-0-0/ontologies/DrivableAreaEdge|Refer to BSI PAS-1883 Section 5.2.3.1.e|SceneryDrivableArea|
|Drivable area geometry|https://openlabel.asam.net/V1-0-0/ontologies/DrivableAreaGeometry|Refer to BSI PAS-1883 Section 5.2.3.3|SceneryDrivableArea|
|Drivable area induced road surface conditions|https://openlabel.asam.net/V1-0-0/ontologies/DrivableAreaSurfaceCondition|Refer to BSI PAS-1883 Section 5.2.3.7.c|DrivableAreaSurface|
|Drivable area lane specification|https://openlabel.asam.net/V1-0-0/ontologies/DrivableAreaLaneSpecification|Refer to BSI PAS-1883 Section 5.2.3.1.c|SceneryDrivableArea|
|Drivable area signs|https://openlabel.asam.net/V1-0-0/ontologies/DrivableAreaSigns|Refer to BSI PAS-1883 Section 5.2.3.1.d|SceneryDrivableArea|
|Drivable area surface|https://openlabel.asam.net/V1-0-0/ontologies/DrivableAreaSurface|Refer to BSI PAS-1883 Section 5.2.3.1.f|SceneryDrivableArea|
|Drivable area surface features|https://openlabel.asam.net/V1-0-0/ontologies/DrivableAreaSurfaceFeature|Refer to BSI PAS-1883 Section 5.2.3.7.b|DrivableAreaSurface|
|Drivable area surface type|https://openlabel.asam.net/V1-0-0/ontologies/DrivableAreaSurfaceType|Refer to BSI PAS-1883 Section 5.2.3.7.a|DrivableAreaSurface|
|Drivable area type|https://openlabel.asam.net/V1-0-0/ontologies/DrivableAreaType|Refer to BSI PAS-1883 Section 5.2.3.2|SceneryDrivableArea|
|Drive|https://openlabel.asam.net/V1-0-0/ontologies/MotionDrive|An activity where the subject vehicle is moving in the direction in which it is facing|BehaviourMotion|
|Driver|https://openlabel.asam.net/V1-0-0/ontologies/HumanDriver|A person who is operating a motorised vehicle, excluding motorcycles|RoadUserHuman|
|Dynamic|https://openlabel.asam.net/V1-0-0/ontologies/RainTypeDynamic|Refer to BSI PAS-1883 Section 5.3.1.2.1|RainType|
|Dynamic elements|https://openlabel.asam.net/V1-0-0/ontologies/OddDynamicElements|Refer to BSI PAS-1883 Section 5.1.c|Odd|
|Elevation of the sun above the horizon|https://openlabel.asam.net/V1-0-0/ontologies/DaySunElevation|Refer to BSI PAS-1883 Section 5.3.3.a.1|IlluminationDay|
|Emergency lane|https://openlabel.asam.net/V1-0-0/ontologies/LaneTypeEmergency|Refer to BSI PAS-1883 Section 5.2.3.4|LaneSpecificationType|
|Emergency vehicle|https://openlabel.asam.net/V1-0-0/ontologies/VehicleEmergency|A vehicle that is used by emergency services to respond to an incident|RoadUserVehicle|
|Environmental Conditions|https://openlabel.asam.net/V1-0-0/ontologies/OddEnvironment|Refer to BSI PAS-1883 Section 5.1.b|Odd|
|Fixed road structures|https://openlabel.asam.net/V1-0-0/ontologies/SceneryFixedStructure|Refer to BSI PAS-1883 Section 5.2.1.e|OddScenery|
|Flash headlight|https://openlabel.asam.net/V1-0-0/ontologies/CommunicationHeadlightFlash|Headlight flashing is the act of either briefly switching on the headlights of a vehicle, or of momentarily switching between a headlight's high beams and low beams, in an effort to communicate with other road users|BehaviourCommunication|
|Flooded roadways|https://openlabel.asam.net/V1-0-0/ontologies/SurfaceConditionFlooded|Refer to BSI PAS-1883 Section 5.2.3.7.ii|DrivableAreaSurfaceCondition|
|Flow rate|https://openlabel.asam.net/V1-0-0/ontologies/TrafficFlowRate|Refer to BSI PAS-1883 Section 5.4.a.3|DynamicElementsTraffic|
|Front|https://openlabel.asam.net/V1-0-0/ontologies/SunPositionFront|Refer to BSI PAS-1883 Section 5.3.3.a.2|DaySunPosition|
|FullTime|https://openlabel.asam.net/V1-0-0/ontologies/InformationSignsUniformFullTime|Refer to BSI PAS-1883 Section 5.2.3.5.1|InformationSignsUniform|
|FullTime|https://openlabel.asam.net/V1-0-0/ontologies/InformationSignsVariableFullTime|Refer to BSI PAS-1883 Section 5.2.3.5.1|InformationSignsVariable|
|FullTime|https://openlabel.asam.net/V1-0-0/ontologies/RegulatorySignsUniformFullTime|Refer to BSI PAS-1883 Section 5.2.3.5.1|RegulatorySignsUniform|
|FullTime|https://openlabel.asam.net/V1-0-0/ontologies/RegulatorySignsVariableFullTime|Refer to BSI PAS-1883 Section 5.2.3.5.1|RegulatorySignsVariable|
|FullTime|https://openlabel.asam.net/V1-0-0/ontologies/WarningSignsUniformFullTime|Refer to BSI PAS-1883 Section 5.2.3.5.1|WarningSignsUniform|
|FullTime|https://openlabel.asam.net/V1-0-0/ontologies/WarningSignsVariableFullTime|Refer to BSI PAS-1883 Section 5.2.3.5.1|WarningSignsVariable|
|Galileo|https://openlabel.asam.net/V1-0-0/ontologies/PositioningGalileo|Refer to BSI PAS-1883 Section 5.3.4.b.1|ConnectivityPositioning|
|GeoFenced areas|https://openlabel.asam.net/V1-0-0/ontologies/ZoneGeoFenced|Refer to BSI PAS-1883 Section 5.2.2.a|SceneryZone|
|GLObal NAvigation Satellite System (GLONASS)|https://openlabel.asam.net/V1-0-0/ontologies/PositioningGlonass|Refer to BSI PAS-1883 Section 5.3.4.b.2|ConnectivityPositioning|
|Global Positioning System (GPS)|https://openlabel.asam.net/V1-0-0/ontologies/PositioningGps|Refer to BSI PAS-1883 Section 5.3.4.b.3|ConnectivityPositioning|
|Grade separated|https://openlabel.asam.net/V1-0-0/ontologies/IntersectionGradeSeperated|Refer to BSI PAS-1883 Section 5.2.4.v|JunctionIntersection|
|Horizontal plane|https://openlabel.asam.net/V1-0-0/ontologies/GeometryHorizontal|Refer to BSI PAS-1883 Section 5.2.3.3.a|DrivableAreaGeometry|
|Human|https://openlabel.asam.net/V1-0-0/ontologies/RoadUserHuman|A person|RoadUser|
|Icy|https://openlabel.asam.net/V1-0-0/ontologies/SurfaceConditionIcy|Refer to BSI PAS-1883 Section 5.2.3.7.i|DrivableAreaSurfaceCondition|
|Illumination|https://openlabel.asam.net/V1-0-0/ontologies/EnvironmentIllumination|Refer to BSI PAS-1883 Section 5.3.3|OddEnvironment|
|Information signs|https://openlabel.asam.net/V1-0-0/ontologies/SignsInformation|Refer to BSI PAS-1883 Section 5.2.3.5.a|DrivableAreaSigns|
|Interference zones|https://openlabel.asam.net/V1-0-0/ontologies/ZoneInterference|Refer to BSI PAS-1883 Section 5.2.2.e|SceneryZone|
|Intersections|https://openlabel.asam.net/V1-0-0/ontologies/JunctionIntersection|Refer to BSI PAS-1883 Section 5.2.4|SceneryJunction|
|Junctions|https://openlabel.asam.net/V1-0-0/ontologies/SceneryJunction|Refer to BSI PAS-1883 Section 5.2.1.c|OddScenery|
|Lane change left|https://openlabel.asam.net/V1-0-0/ontologies/MotionLaneChangeLeft|An activity where the subject vehicle is in a lane left of the original lane at the end of the activity|BehaviourMotion|
|Lane change right|https://openlabel.asam.net/V1-0-0/ontologies/MotionLaneChangeRight|An activity where the subject vehicle is in a lane right of the original lane at the end of the activity|BehaviourMotion|
|Lane dimensions|https://openlabel.asam.net/V1-0-0/ontologies/LaneSpecificationDimensions|Refer to BSI PAS-1883 Section 5.2.3.4.a|DrivableAreaLaneSpecification|
|Lane marking|https://openlabel.asam.net/V1-0-0/ontologies/LaneSpecificationMarking|Refer to BSI PAS-1883 Section 5.2.3.4.b|DrivableAreaLaneSpecification|
|Lane type|https://openlabel.asam.net/V1-0-0/ontologies/LaneSpecificationType|Refer to BSI PAS-1883 Section 5.2.3.4.c|DrivableAreaLaneSpecification|
|Large|https://openlabel.asam.net/V1-0-0/ontologies/RoundaboutLarge|Refer to BSI PAS-1883 Section 5.2.4.d|JunctionRoundabout|
|Left|https://openlabel.asam.net/V1-0-0/ontologies/SunPositionLeft|Refer to BSI PAS-1883 Section 5.3.3.a.2|DaySunPosition|
|Left|https://openlabel.asam.net/V1-0-0/ontologies/TravelDirectionLeft|Refer to BSI PAS-1883 Section 5.2.3.4.e|LaneSpecificationTravelDirection|
|Level plane|https://openlabel.asam.net/V1-0-0/ontologies/LongitudinalLevelPlane|Refer to BSI PAS-1883 Section 5.2.3.3.iii|GeometryLongitudinal|
|Line markers|https://openlabel.asam.net/V1-0-0/ontologies/EdgeLineMarkers|Refer to BSI PAS-1883 Section 5.2.3.6.a|DrivableAreaEdge|
|Longitudinal plane|https://openlabel.asam.net/V1-0-0/ontologies/GeometryLongitudinal|Refer to BSI PAS-1883 Section 5.2.3.3.c|DrivableAreaGeometry|
|Loose (e.g. gravel, earth, sand)|https://openlabel.asam.net/V1-0-0/ontologies/SurfaceTypeLoose|Refer to BSI PAS-1883 Section 5.2.3.7.1|DrivableAreaSurfaceType|
|LowAmbient lighting|https://openlabel.asam.net/V1-0-0/ontologies/LowLightAmbient|Refer to BSI PAS-1883 Section 5.3.3.b.2|IlluminationLowLight|
|Marine (coastal areas only)|https://openlabel.asam.net/V1-0-0/ontologies/ParticulatesMarine|Refer to BSI PAS-1883 Section 5.3.2.a|EnvironmentParticulates|
|Mini|https://openlabel.asam.net/V1-0-0/ontologies/RoundaboutMini|Refer to BSI PAS-1883 Section 5.2.4.e|JunctionRoundabout|
|Minor roads|https://openlabel.asam.net/V1-0-0/ontologies/RoadTypeMinor|Refer to BSI PAS-1883 Section 5.2.3.2.d|DrivableAreaType|
|Mirage|https://openlabel.asam.net/V1-0-0/ontologies/SurfaceConditionMirage|Refer to BSI PAS-1883 Section 5.2.3.7.iii|DrivableAreaSurfaceCondition|
|Motion|https://openlabel.asam.net/V1-0-0/ontologies/BehaviourMotion|An activity in which the road user changes position, velocity or direction|Behaviour|
|Motorcycle|https://openlabel.asam.net/V1-0-0/ontologies/VehicleMotorcycle|A motorcycle, often called a motorbike, is a two- or three-wheeled motor vehicle, where the riders are not enclosed in a protective frame|RoadUserVehicle|
|Motorcyclist|https://openlabel.asam.net/V1-0-0/ontologies/HumanMotorcyclist|A person who is riding a motorcycle|RoadUserHuman|
|Motorways|https://openlabel.asam.net/V1-0-0/ontologies/RoadTypeMotorway|Refer to BSI PAS-1883 Section 5.2.3.2.a|DrivableAreaType|
|Move away|https://openlabel.asam.net/V1-0-0/ontologies/MotionAway|An activity where the rod user is further away from the object by the end of the activity|BehaviourMotion|
|Move towards|https://openlabel.asam.net/V1-0-0/ontologies/MotionTowards|An activity where the road user is closer to the object by the end of the activity|BehaviourMotion|
|Night|https://openlabel.asam.net/V1-0-0/ontologies/LowLightNight|Refer to BSI PAS-1883 Section 5.3.3.b.1|IlluminationLowLight|
|Night or lowAmbient lighting condition|https://openlabel.asam.net/V1-0-0/ontologies/IlluminationLowLight|Refer to BSI PAS-1883 Section 5.3.3.b|EnvironmentIllumination|
|Non-precipitating water droplets or ice crystals (i.e. mist/fog)|https://openlabel.asam.net/V1-0-0/ontologies/ParticulatesWater|Refer to BSI PAS-1883 Section 5.3.2.b|EnvironmentParticulates|
|None|https://openlabel.asam.net/V1-0-0/ontologies/EdgeNone|Refer to BSI PAS-1883 Section 5.2.3.6.f|DrivableAreaEdge|
|NonSignalised|https://openlabel.asam.net/V1-0-0/ontologies/RoundaboutCompactSignal|Refer to BSI PAS-1883 Section 5.2.4.b.2|RoundaboutCompact|
|NonSignalised|https://openlabel.asam.net/V1-0-0/ontologies/RoundaboutDoubleSignal|Refer to BSI PAS-1883 Section 5.2.4.c.2|RoundaboutDouble|
|NonSignalised|https://openlabel.asam.net/V1-0-0/ontologies/RoundaboutLargeSignal|Refer to BSI PAS-1883 Section 5.2.4.d.2|RoundaboutLarge|
|NonSignalised|https://openlabel.asam.net/V1-0-0/ontologies/RoundaboutMiniSignal|Refer to BSI PAS-1883 Section 5.2.4.e.2|RoundaboutMini|
|NonSignalised|https://openlabel.asam.net/V1-0-0/ontologies/RoundaboutNormalSignal|Refer to BSI PAS-1883 Section 5.2.4.a.2|RoundaboutNormal|
|Normal|https://openlabel.asam.net/V1-0-0/ontologies/RoundaboutNormal|Refer to BSI PAS-1883 Section 5.2.4.a|JunctionRoundabout|
|Number of lanes|https://openlabel.asam.net/V1-0-0/ontologies/LaneSpecificationLaneCount|Refer to BSI PAS-1883 Section 5.2.3.4.d|DrivableAreaLaneSpecification|
|ODD|https://openlabel.asam.net/V1-0-0/ontologies/Odd|Refer to BSI PAS-1883 Section 5|Tag|
|Oncoming vehicle lights|https://openlabel.asam.net/V1-0-0/ontologies/ArtificialVehicleLighting|Refer to BSI PAS-1883 Section 5.3.2.d.2|IlluminationArtificial|
|Orographic|https://openlabel.asam.net/V1-0-0/ontologies/RainTypeOrographic|Refer to BSI PAS-1883 Section 5.3.1.2.3|RainType|
|Overtake|https://openlabel.asam.net/V1-0-0/ontologies/MotionOvertake|An activity where the subject starts behind the object and then ends up in front of the object by changing lanes twice|BehaviourMotion|
|Parking|https://openlabel.asam.net/V1-0-0/ontologies/RoadTypeParking|Refer to BSI PAS-1883 Section 5.2.3.2.f|DrivableAreaType|
|Particulates (obscuration by nonPrecipitating water droplets and other particulates)|https://openlabel.asam.net/V1-0-0/ontologies/EnvironmentParticulates|Refer to BSI PAS-1883 Section 5.3.2|OddEnvironment|
|Passenger|https://openlabel.asam.net/V1-0-0/ontologies/HumanPassenger|A person who is using a vehicle to travel but who is not operating the vehicle|RoadUserHuman|
|Pavements|https://openlabel.asam.net/V1-0-0/ontologies/TransversePavements|Refer to BSI PAS-1883 Section 5.2.3.3.3|GeometryTransverse|
|Pedestrian|https://openlabel.asam.net/V1-0-0/ontologies/HumanPedestrian|A person who is using a road without the use of a vehicle|RoadUserHuman|
|Pedestrian crossings|https://openlabel.asam.net/V1-0-0/ontologies/SpecialStructurePedestrianCrossing|Refer to BSI PAS-1883 Section 5.2.5.c|ScenerySpecialStructure|
|Position of the sun|https://openlabel.asam.net/V1-0-0/ontologies/DaySunPosition|Refer to BSI PAS-1883 Section 5.3.3.a.2|IlluminationDay|
|Positioning|https://openlabel.asam.net/V1-0-0/ontologies/ConnectivityPositioning|Refer to BSI PAS-1883 Section 5.3.4.b|EnvironmentConnectivity|
|Potholes|https://openlabel.asam.net/V1-0-0/ontologies/SurfaceFeaturePothole|Refer to BSI PAS-1883 Section 5.2.3.7|DrivableAreaSurfaceFeature|
|Presence of special vehicles (e.g. ambulances or police vehicles).|https://openlabel.asam.net/V1-0-0/ontologies/TrafficSpecialVehicle|Refer to BSI PAS-1883 Section 5.4.a.5|DynamicElementsTraffic|
|Radial roads|https://openlabel.asam.net/V1-0-0/ontologies/RoadTypeRadial|Refer to BSI PAS-1883 Section 5.2.3.2.b|DrivableAreaType|
|Rail crossings|https://openlabel.asam.net/V1-0-0/ontologies/SpecialStructureRailCrossing|Refer to BSI PAS-1883 Section 5.2.5.d|ScenerySpecialStructure|
|Rainfall|https://openlabel.asam.net/V1-0-0/ontologies/WeatherRain|Refer to BSI PAS-1883 Section 5.3.1.2|EnvironmentWeather|
|Rainfall type|https://openlabel.asam.net/V1-0-0/ontologies/RainType|Refer to BSI PAS-1883 Section 5.3.1.2|WeatherRain|
|Refuse collection|https://openlabel.asam.net/V1-0-0/ontologies/TemporaryStructureRefuseCollection|Refer to BSI PAS-1883 Section 5.2.7.b|SceneryTemporaryStructure|
|Regions or states|https://openlabel.asam.net/V1-0-0/ontologies/ZoneRegion|Refer to BSI PAS-1883 Section 5.2.2.d|SceneryZone|
|Regulatory signs|https://openlabel.asam.net/V1-0-0/ontologies/SignsRegulatory|Refer to BSI PAS-1883 Section 5.2.3.5.b|DrivableAreaSigns|
|Reverse|https://openlabel.asam.net/V1-0-0/ontologies/MotionReverse|An activity where the subject vehicle is moving in the opposite direction to which it is facing|BehaviourMotion|
|Right|https://openlabel.asam.net/V1-0-0/ontologies/SunPositionRight|Refer to BSI PAS-1883 Section 5.3.3.a.2|DaySunPosition|
|Right|https://openlabel.asam.net/V1-0-0/ontologies/TravelDirectionRight|Refer to BSI PAS-1883 Section 5.2.3.4.e|LaneSpecificationTravelDirection|
|Road signage|https://openlabel.asam.net/V1-0-0/ontologies/TemporaryStructureRoadSignage|Refer to BSI PAS-1883 Section 5.2.7.d|SceneryTemporaryStructure|
|Road user|https://openlabel.asam.net/V1-0-0/ontologies/RoadUser|Something which uses a road to travel|Tag|
|Road works|https://openlabel.asam.net/V1-0-0/ontologies/TemporaryStructureRoadWorks|Refer to BSI PAS-1883 Section 5.2.7.c|SceneryTemporaryStructure|
|Roundabouts|https://openlabel.asam.net/V1-0-0/ontologies/JunctionRoundabout|Refer to BSI PAS-1883 Section 5.2.4|SceneryJunction|
|Run|https://openlabel.asam.net/V1-0-0/ontologies/MotionRun|Locomotion mode of humans (and animals) in which at a specific point in time no foot touches the ground|BehaviourMotion|
|Ruts|https://openlabel.asam.net/V1-0-0/ontologies/SurfaceFeatureRut|Refer to BSI PAS-1883 Section 5.2.3.7|DrivableAreaSurfaceFeature|
|Sand and dust|https://openlabel.asam.net/V1-0-0/ontologies/ParticulatesDust|Refer to BSI PAS-1883 Section 5.3.2.c|EnvironmentParticulates|
|Satellite|https://openlabel.asam.net/V1-0-0/ontologies/V2iSatellite|Refer to BSI PAS-1883 Section 5.3.4.a.2.ii|CommunicationV2i|
|Satellite|https://openlabel.asam.net/V1-0-0/ontologies/V2vSatellite|Refer to BSI PAS-1883 Section 5.3.4.a.1.ii|CommunicationV2v|
|Scenario|https://openlabel.asam.net/V1-0-0/ontologies/Scenario||Class|
|Scenery|https://openlabel.asam.net/V1-0-0/ontologies/OddScenery|Refer to BSI PAS-1883 Section 5.1.a|Odd|
|School zones|https://openlabel.asam.net/V1-0-0/ontologies/ZoneSchool|Refer to BSI PAS-1883 Section 5.2.2.c|SceneryZone|
|Segmented (e.g. concrete slabs, granite setts, cobblestones)|https://openlabel.asam.net/V1-0-0/ontologies/SurfaceTypeSegmented|Refer to BSI PAS-1883 Section 5.2.3.7.2|DrivableAreaSurfaceType|
|Shared space|https://openlabel.asam.net/V1-0-0/ontologies/RoadTypeShared|Refer to BSI PAS-1883 Section 5.2.3.2.g|DrivableAreaType|
|Shoulder (grass)|https://openlabel.asam.net/V1-0-0/ontologies/EdgeShoulderGrass|Refer to BSI PAS-1883 Section 5.2.3.6.c|DrivableAreaEdge|
|Shoulder (paved or gravel)|https://openlabel.asam.net/V1-0-0/ontologies/EdgeShoulderPavedOrGravel|Refer to BSI PAS-1883 Section 5.2.3.6.b|DrivableAreaEdge|
|Signal emergency|https://openlabel.asam.net/V1-0-0/ontologies/CommunicationSignalEmergency|Signals made by an emergency vehicle when responding to an emergency, i.e. flashing blue lights|BehaviourCommunication|
|Signal hazard|https://openlabel.asam.net/V1-0-0/ontologies/CommunicationSignalHazard|A signal made by a road user to warn other road users of a hazardous situation, such as when a vehicle is causing an obstruction|BehaviourCommunication|
|Signal left|https://openlabel.asam.net/V1-0-0/ontologies/CommunicationSignalLeft|A signal made by a road user to indicate an intention to move or turn left|BehaviourCommunication|
|Signal right|https://openlabel.asam.net/V1-0-0/ontologies/CommunicationSignalRight|A signal made by a road user to indicate an intention to move or turn right|BehaviourCommunication|
|Signal slowing|https://openlabel.asam.net/V1-0-0/ontologies/CommunicationSignalSlowing|A signal made by a road user to indicate an intention to slow down or stop|BehaviourCommunication|
|Signalised|https://openlabel.asam.net/V1-0-0/ontologies/RoundaboutCompactNosignal|Refer to BSI PAS-1883 Section 5.2.4.b.1|RoundaboutCompact|
|Signalised|https://openlabel.asam.net/V1-0-0/ontologies/RoundaboutDoubleNosignal|Refer to BSI PAS-1883 Section 5.2.4.c.1|RoundaboutDouble|
|Signalised|https://openlabel.asam.net/V1-0-0/ontologies/RoundaboutLargeNosignal|Refer to BSI PAS-1883 Section 5.2.4.d.1|RoundaboutLarge|
|Signalised|https://openlabel.asam.net/V1-0-0/ontologies/RoundaboutMiniNosignal|Refer to BSI PAS-1883 Section 5.2.4.e.1|RoundaboutMini|
|Signalised|https://openlabel.asam.net/V1-0-0/ontologies/RoundaboutNormalNosignal|Refer to BSI PAS-1883 Section 5.2.4.a.1|RoundaboutNormal|
|Slide|https://openlabel.asam.net/V1-0-0/ontologies/MotionSlide|An activity where a pedestrian is slipping/sliding on the road|BehaviourMotion|
|Slip roads|https://openlabel.asam.net/V1-0-0/ontologies/RoadTypeSlip|Refer to BSI PAS-1883 Section 5.2.3.2.e|DrivableAreaType|
|Smoke and pollution|https://openlabel.asam.net/V1-0-0/ontologies/ParticulatesPollution|Refer to BSI PAS-1883 Section 5.3.2.d|EnvironmentParticulates|
|Snow on drivable area|https://openlabel.asam.net/V1-0-0/ontologies/SurfaceConditionSnow|Refer to BSI PAS-1883 Section 5.2.3.7.iv|DrivableAreaSurfaceCondition|
|Snowfall|https://openlabel.asam.net/V1-0-0/ontologies/WeatherSnow|Refer to BSI PAS-1883 Section 5.3.1.3|EnvironmentWeather|
|Solid barriers (e.g. grating, rails, curb, cones)|https://openlabel.asam.net/V1-0-0/ontologies/EdgeSolidBarriers|Refer to BSI PAS-1883 Section 5.2.3.6.d|DrivableAreaEdge|
|Sound horn|https://openlabel.asam.net/V1-0-0/ontologies/CommunicationHorn|The noise made by a vehicle horn|BehaviourCommunication|
|Special purpose lane|https://openlabel.asam.net/V1-0-0/ontologies/LaneTypeSpecial|Refer to BSI PAS-1883 Section 5.2.3.4|LaneSpecificationType|
|Special structures|https://openlabel.asam.net/V1-0-0/ontologies/ScenerySpecialStructure|Refer to BSI PAS-1883 Section 5.2.1.d|OddScenery|
|Speed|https://openlabel.asam.net/V1-0-0/ontologies/SubjectVehicleSpeed|Refer to BSI PAS-1883 Section 5.4.b|DynamicElementsSubjectVehicle|
|Staggered|https://openlabel.asam.net/V1-0-0/ontologies/IntersectionStaggered|Refer to BSI PAS-1883 Section 5.2.4.ii|JunctionIntersection|
|Standing water|https://openlabel.asam.net/V1-0-0/ontologies/SurfaceConditionStandingWater|Refer to BSI PAS-1883 Section 5.2.3.7.v|DrivableAreaSurfaceCondition|
|Stop|https://openlabel.asam.net/V1-0-0/ontologies/MotionStop|An activity where the road user is stationary|BehaviourMotion|
|Straight lines|https://openlabel.asam.net/V1-0-0/ontologies/HorizontalStraights|Refer to BSI PAS-1883 Section 5.2.3.3|GeometryHorizontal|
|Street furniture (e.g. bollards)|https://openlabel.asam.net/V1-0-0/ontologies/FixedStructureStreetFurniture|Refer to BSI PAS-1883 Section 5.2.6.c|SceneryFixedStructure|
|Street lights|https://openlabel.asam.net/V1-0-0/ontologies/FixedStructureStreetlight|Refer to BSI PAS-1883 Section 5.2.6.b|SceneryFixedStructure|
|Streetlights|https://openlabel.asam.net/V1-0-0/ontologies/ArtificialStreetLighting|Refer to BSI PAS-1883 Section 5.3.3.d.1|IlluminationArtificial|
|Subject vehicle|https://openlabel.asam.net/V1-0-0/ontologies/DynamicElementsSubjectVehicle|Refer to BSI PAS-1883 Section 5.4.b|OddDynamicElements|
|Surface contamination|https://openlabel.asam.net/V1-0-0/ontologies/SurfaceConditionContamination|Refer to BSI PAS-1883 Section 5.2.3.7.vii|DrivableAreaSurfaceCondition|
|Swells|https://openlabel.asam.net/V1-0-0/ontologies/SurfaceFeatureSwell|Refer to BSI PAS-1883 Section 5.2.3.7|DrivableAreaSurfaceFeature|
|Temporary|https://openlabel.asam.net/V1-0-0/ontologies/InformationSignsUniformTemporary|Refer to BSI PAS-1883 Section 5.2.3.5.2|InformationSignsUniform|
|Temporary|https://openlabel.asam.net/V1-0-0/ontologies/InformationSignsVariableTemporary|Refer to BSI PAS-1883 Section 5.2.3.5.2|InformationSignsVariable|
|Temporary|https://openlabel.asam.net/V1-0-0/ontologies/RegulatorySignsUniformTemporary|Refer to BSI PAS-1883 Section 5.2.3.5.2|RegulatorySignsUniform|
|Temporary|https://openlabel.asam.net/V1-0-0/ontologies/RegulatorySignsVariableTemporary|Refer to BSI PAS-1883 Section 5.2.3.5.2|RegulatorySignsVariable|
|Temporary|https://openlabel.asam.net/V1-0-0/ontologies/WarningSignsUniformTemporary|Refer to BSI PAS-1883 Section 5.2.3.5.2|WarningSignsUniform|
|Temporary|https://openlabel.asam.net/V1-0-0/ontologies/WarningSignsVariableTemporary|Refer to BSI PAS-1883 Section 5.2.3.5.2|WarningSignsVariable|
|Temporary line markers|https://openlabel.asam.net/V1-0-0/ontologies/EdgeTemporaryLineMarkers|Refer to BSI PAS-1883 Section 5.2.3.6.e|DrivableAreaEdge|
|Temporary road structures|https://openlabel.asam.net/V1-0-0/ontologies/SceneryTemporaryStructure|Refer to BSI PAS-1883 Section 5.2.1.f|OddScenery|
|TJunctions|https://openlabel.asam.net/V1-0-0/ontologies/IntersectionTJunction|Refer to BSI PAS-1883 Section 5.2.4.i|JunctionIntersection|
|Toll plaza|https://openlabel.asam.net/V1-0-0/ontologies/SpecialStructureTollPlaza|Refer to BSI PAS-1883 Section 5.2.5.f|ScenerySpecialStructure|
|Traffic|https://openlabel.asam.net/V1-0-0/ontologies/DynamicElementsTraffic|Refer to BSI PAS-1883 Section 5.4.a|OddDynamicElements|
|Traffic lane|https://openlabel.asam.net/V1-0-0/ontologies/LaneTypeTraffic|Refer to BSI PAS-1883 Section 5.2.3.4|LaneSpecificationType|
|Traffic management zones|https://openlabel.asam.net/V1-0-0/ontologies/ZoneTrafficManagement|Refer to BSI PAS-1883 Section 5.2.2.b|SceneryZone|
|Trailer|https://openlabel.asam.net/V1-0-0/ontologies/VehicleTrailer|An unpowered vehicle towed by another vehicle|RoadUserVehicle|
|Tram lane|https://openlabel.asam.net/V1-0-0/ontologies/LaneTypeTram|Refer to BSI PAS-1883 Section 5.2.3.4|LaneSpecificationType|
|Transverse plane|https://openlabel.asam.net/V1-0-0/ontologies/GeometryTransverse|Refer to BSI PAS-1883 Section 5.2.3.3.b|DrivableAreaGeometry|
|Truck|https://openlabel.asam.net/V1-0-0/ontologies/VehicleTruck|A large, heavy motor vehicle used for carrying goods and materials|RoadUserVehicle|
|Tunnels|https://openlabel.asam.net/V1-0-0/ontologies/SpecialStructureTunnel|Refer to BSI PAS-1883 Section 5.2.5.e|ScenerySpecialStructure|
|Turn|https://openlabel.asam.net/V1-0-0/ontologies/MotionTurn|An activity where the road user changes their heading|BehaviourMotion|
|Turn left|https://openlabel.asam.net/V1-0-0/ontologies/MotionTurnLeft|An activity where the subject changes direction in reference to a traffic intersection in which the subject exits the intersection on a road to the left of the original road.|BehaviourMotion|
|Turn right|https://openlabel.asam.net/V1-0-0/ontologies/MotionTurnRight|A moving activity where the subject changes direction in reference to a traffic intersection in which the subject exits the intersection on a road to the right of the original road.|BehaviourMotion|
|Types of lanes together|https://openlabel.asam.net/V1-0-0/ontologies/TransverseLanesTogether|Refer to BSI PAS-1883 Section 5.2.3.3.5|GeometryTransverse|
|U-turn|https://openlabel.asam.net/V1-0-0/ontologies/MotionUTurn|An activity where the subject peforms a turn resulting in it heading in the opposite direction to which it started the activity|BehaviourMotion|
|Undivided|https://openlabel.asam.net/V1-0-0/ontologies/TransverseUndivided|Refer to BSI PAS-1883 Section 5.2.3.3.2|GeometryTransverse|
|Uniform|https://openlabel.asam.net/V1-0-0/ontologies/InformationSignsUniform|Refer to BSI PAS-1883 Section 5.2.3.5|SignsInformation|
|Uniform|https://openlabel.asam.net/V1-0-0/ontologies/RegulatorySignsUniform|Refer to BSI PAS-1883 Section 5.2.3.5|SignsRegulatory|
|Uniform|https://openlabel.asam.net/V1-0-0/ontologies/WarningSignsUniform|Refer to BSI PAS-1883 Section 5.2.3.5|SignsWarning|
|Uniform (e.g. asphalt)|https://openlabel.asam.net/V1-0-0/ontologies/SurfaceTypeUniform|Refer to BSI PAS-1883 Section 5.2.3.7.3|DrivableAreaSurfaceType|
|Up-slope (positive gradient)|https://openlabel.asam.net/V1-0-0/ontologies/LongitudinalUpSlope|Refer to BSI PAS-1883 Section 5.2.3.3.i|GeometryLongitudinal|
|Van|https://openlabel.asam.net/V1-0-0/ontologies/VehicleVan|A medium-sized motor vehicle, typically without side windows in the rear part, for transporting goods|RoadUserVehicle|
|Variable|https://openlabel.asam.net/V1-0-0/ontologies/InformationSignsVariable|Refer to BSI PAS-1883 Section 5.2.3.5|SignsInformation|
|Variable|https://openlabel.asam.net/V1-0-0/ontologies/RegulatorySignsVariable|Refer to BSI PAS-1883 Section 5.2.3.5|SignsRegulatory|
|Variable|https://openlabel.asam.net/V1-0-0/ontologies/WarningSignsVariable|Refer to BSI PAS-1883 Section 5.2.3.5|SignsWarning|
|Vegetation|https://openlabel.asam.net/V1-0-0/ontologies/FixedStructureVegetation|Refer to BSI PAS-1883 Section 5.2.6.d|SceneryFixedStructure|
|Vehicle|https://openlabel.asam.net/V1-0-0/ontologies/RoadUserVehicle|A mode of transport that can be operated on a road; human or computer controlled|RoadUser|
|Vehicle to infrastructure communication (V2I)|https://openlabel.asam.net/V1-0-0/ontologies/CommunicationV2i|Refer to BSI PAS-1883 Section 5.3.4.a.2|ConnectivityCommunication|
|Vehicle to vehicle communication (V2V)|https://openlabel.asam.net/V1-0-0/ontologies/CommunicationV2v|Refer to BSI PAS-1883 Section 5.3.4.a.1|ConnectivityCommunication|
|Volcanic ash|https://openlabel.asam.net/V1-0-0/ontologies/ParticulatesVolcanic|Refer to BSI PAS-1883 Section 5.3.2.e|EnvironmentParticulates|
|Volume of traffic|https://openlabel.asam.net/V1-0-0/ontologies/TrafficVolume|Refer to BSI PAS-1883 Section 5.4.a.2|DynamicElementsTraffic|
|Walk|https://openlabel.asam.net/V1-0-0/ontologies/MotionWalk|Locomotion mode of humans (and animals) in which at least one foot is always on the ground|BehaviourMotion|
|Warning signs|https://openlabel.asam.net/V1-0-0/ontologies/SignsWarning|Refer to BSI PAS-1883 Section 5.2.3.5.c|DrivableAreaSigns|
|Wave|https://openlabel.asam.net/V1-0-0/ontologies/CommunicationWave|A person, including drivers, pedestrians, riders, making a waving gesture|BehaviourCommunication|
|Weather|https://openlabel.asam.net/V1-0-0/ontologies/EnvironmentWeather|Refer to BSI PAS-1883 Section 5.3.1|OddEnvironment|
|Wet road|https://openlabel.asam.net/V1-0-0/ontologies/SurfaceConditionWet|Refer to BSI PAS-1883 Section 5.2.3.7.vi|DrivableAreaSurfaceCondition|
|Wheelchair|https://openlabel.asam.net/V1-0-0/ontologies/VehicleWheelchair|A chair fitted with wheels for use as a means of transport|RoadUserVehicle|
|Wheelchair user|https://openlabel.asam.net/V1-0-0/ontologies/HumanWheelchairUser|A person who is travelling in a wheelchair|RoadUserHuman|
|Wind|https://openlabel.asam.net/V1-0-0/ontologies/WeatherWind|Refer to BSI PAS-1883 Section 5.3.1.1|EnvironmentWeather|
|With active traffic management (smart motorways)|https://openlabel.asam.net/V1-0-0/ontologies/MotorwayManaged|Refer to BSI PAS-1883 Section 5.2.3.2.1|RoadTypeMotorway|
|Without active traffic management|https://openlabel.asam.net/V1-0-0/ontologies/MotorwayUnmanaged|Refer to BSI PAS-1883 Section 5.2.3.2.2|RoadTypeMotorway|
|YJunction|https://openlabel.asam.net/V1-0-0/ontologies/IntersectionYJunction|Refer to BSI PAS-1883 Section 5.2.4.iii|JunctionIntersection|
|Zones|https://openlabel.asam.net/V1-0-0/ontologies/SceneryZone|Refer to BSI PAS-1883 Section 5.2.1.a|OddScenery|

## Prefixes

- brick: <https://brickschema.org/schema/Brick#>
- csvw: <http://www.w3.org/ns/csvw#>
- dc: <http://purl.org/dc/elements/1.1/>
- dcam: <http://purl.org/dc/dcam/>
- dcat: <http://www.w3.org/ns/dcat#>
- dcmitype: <http://purl.org/dc/dcmitype/>
- dcterms: <http://purl.org/dc/terms/>
- doap: <http://usefulinc.com/ns/doap#>
- foaf: <http://xmlns.com/foaf/0.1/>
- geo: <http://www.opengis.net/ont/geosparql#>
- odrl: <http://www.w3.org/ns/odrl/2/>
- openlabel: <https://openlabel.asam.net/V1-0-0/ontologies/>
- org: <http://www.w3.org/ns/org#>
- owl: <http://www.w3.org/2002/07/owl#>
- prof: <http://www.w3.org/ns/dx/prof/>
- prov: <http://www.w3.org/ns/prov#>
- qb: <http://purl.org/linked-data/cube#>
- rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
- rdfs: <http://www.w3.org/2000/01/rdf-schema#>
- schema: <https://schema.org/>
- sh: <http://www.w3.org/ns/shacl#>
- skos: <http://www.w3.org/2004/02/skos/core#>
- sosa: <http://www.w3.org/ns/sosa/>
- ssn: <http://www.w3.org/ns/ssn/>
- time: <http://www.w3.org/2006/time#>
- vann: <http://purl.org/vocab/vann/>
- void: <http://rdfs.org/ns/void#>
- wgs: <https://www.w3.org/2003/01/geo/wgs84_pos#>
- xml: <http://www.w3.org/XML/1998/namespace>
- xsd: <http://www.w3.org/2001/XMLSchema#>

### SHACL Properties

|Shape|Property prefix|Property|MinCount|MaxCount|Description|Datatype/NodeKind|Filename|
|---|---|---|---|---|---|---|---|
|TagShape|openlabel|AdminTag|0||||openlabel.shacl.ttl|
|TagShape|openlabel|Behaviour|0||||openlabel.shacl.ttl|
|TagShape|openlabel|Odd|0||||openlabel.shacl.ttl|
|TagShape|openlabel|RoadUser|0||||openlabel.shacl.ttl|
|AdminTagShape|openlabel|licenseURI|||The type of license which governs usage of the scenario|<http://www.w3.org/2000/01/rdf-schema#Literal>|openlabel.shacl.ttl|
|AdminTagShape|openlabel|ownerEmail|||Scenario owner email|<http://www.w3.org/2000/01/rdf-schema#Literal>|openlabel.shacl.ttl|
|AdminTagShape|openlabel|ownerName|||Scenario owner name|<http://www.w3.org/2000/01/rdf-schema#Literal>|openlabel.shacl.ttl|
|AdminTagShape|openlabel|ownerURL|||Scenario owner URL|<http://www.w3.org/2000/01/rdf-schema#Literal>|openlabel.shacl.ttl|
|AdminTagShape|openlabel|scenarioCreatedDate|||Scenario created date|<http://www.w3.org/2000/01/rdf-schema#Literal>|openlabel.shacl.ttl|
|AdminTagShape|openlabel|scenarioDefinition|||Scenario definition SDL|<http://www.w3.org/2000/01/rdf-schema#Literal>|openlabel.shacl.ttl|
|AdminTagShape|openlabel|scenarioDefinitionLanguageURI|||Scenario definition type|<http://www.w3.org/2000/01/rdf-schema#Literal>|openlabel.shacl.ttl|
|AdminTagShape|openlabel|scenarioDescription|||Scenario description|<http://www.w3.org/2000/01/rdf-schema#Literal>|openlabel.shacl.ttl|
|AdminTagShape|openlabel|scenarioName|||Scenario name|<http://www.w3.org/2000/01/rdf-schema#Literal>|openlabel.shacl.ttl|
|AdminTagShape|openlabel|scenarioParentReference|||Scenario parent reference|<http://www.w3.org/2000/01/rdf-schema#Literal>|openlabel.shacl.ttl|
|AdminTagShape|openlabel|scenarioUniqueReference|||Scenario unique reference|<http://www.w3.org/2000/01/rdf-schema#Literal>|openlabel.shacl.ttl|
|AdminTagShape|openlabel|scenarioVersion|||Scenario version|<http://www.w3.org/2000/01/rdf-schema#Literal>|openlabel.shacl.ttl|
|AdminTagShape|openlabel|scenarioVisualisationURL|||Scenario visualization|<http://www.w3.org/2000/01/rdf-schema#Literal>|openlabel.shacl.ttl|
|RoadUserShape|openlabel|motionDriveValue|||Speed (km/h).|<http://www.w3.org/2001/XMLSchema#decimal>|openlabel.shacl.ttl|
|RoadUserShape|openlabel|RoadUserVehicle|||Validation class for RoadUserVehicle||openlabel.shacl.ttl|
|RoadUserShape|openlabel|RoadUserHuman|||Validation class for RoadUserHuman|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|RoadUserShape|openlabel|RoadUserAnimal|||Validation class for RoadUserAnimal|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|BehaviourShape|openlabel|BehaviourCommunication|||Validation class for BehaviourCommunication||openlabel.shacl.ttl|
|BehaviourShape|openlabel|MotionAway|||Validation class for MotionAway|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|BehaviourShape|openlabel|MotionCross|||Validation class for MotionCross|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|BehaviourShape|openlabel|MotionCutIn|||Validation class for MotionCutIn|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|BehaviourShape|openlabel|MotionCutOut|||Validation class for MotionCutOut|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|BehaviourShape|openlabel|MotionLaneChangeLeft|||Validation class for MotionLaneChangeLeft|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|BehaviourShape|openlabel|MotionLaneChangeRight|||Validation class for MotionLaneChangeRight|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|BehaviourShape|openlabel|MotionOvertake|||Validation class for MotionOvertake|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|BehaviourShape|openlabel|MotionReverse|||Validation class for MotionReverse|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|BehaviourShape|openlabel|MotionRun|||Validation class for MotionRun|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|BehaviourShape|openlabel|MotionSlide|||Validation class for MotionSlide|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|BehaviourShape|openlabel|MotionStop|||Validation class for MotionStop|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|BehaviourShape|openlabel|MotionTowards|||Validation class for MotionTowards|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|BehaviourShape|openlabel|MotionTurn|||Validation class for MotionTurn|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|BehaviourShape|openlabel|MotionTurnLeft|||Validation class for MotionTurnLeft|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|BehaviourShape|openlabel|MotionTurnRight|||Validation class for MotionTurnRight|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|BehaviourShape|openlabel|MotionUTurn|||Validation class for MotionUTurn|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|BehaviourShape|openlabel|MotionWalk|||Validation class for MotionWalk|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|BehaviourShape|openlabel|MotionAccelerate|||Validation class for motionAccelerate|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|BehaviourShape|openlabel|MotionDecelerate|||Validation class for motionDecelerate|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|BehaviourShape|openlabel|MotionDrive|||Validation class for motionDrive|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|BehaviourShape|openlabel|motionAccelerateValue|||Rate of acceleration (ms-2).||openlabel.shacl.ttl|
|BehaviourShape|openlabel|motionDecelerateValue|||MotionDecelerateValue can be a single decimal or a range (ms-2).||openlabel.shacl.ttl|
|BehaviourShape|openlabel|motionDriveValue|||Motion drive value can be a single decimal or a range Speed (km/h).||openlabel.shacl.ttl|
|OddShape|openlabel|DrivableAreaEdge|||Validation class for DrivableAreaEdge||openlabel.shacl.ttl|
|OddShape|openlabel|GeometryTransverse|||Validation class for GeometryTransverse||openlabel.shacl.ttl|
|OddShape|openlabel|LaneSpecificationTravelDirection|||Validation class for LaneSpecificationTravelDirection||openlabel.shacl.ttl|
|OddShape|openlabel|LaneSpecificationType|||Validation class for LaneSpecificationType||openlabel.shacl.ttl|
|OddShape|openlabel|SignsInformation|||Validation class for SignsInformation||openlabel.shacl.ttl|
|OddShape|openlabel|SignsRegulatory|||Validation class for SignsRegulatory||openlabel.shacl.ttl|
|OddShape|openlabel|SignsWarning|||Validation class for SignsWarning||openlabel.shacl.ttl|
|OddShape|openlabel|DrivableAreaSurfaceCondition|||Validation class for DrivableAreaSurfaceCondition||openlabel.shacl.ttl|
|OddShape|openlabel|DrivableAreaSurfaceFeature|||Validation class for DrivableAreaSurfaceFeature||openlabel.shacl.ttl|
|OddShape|openlabel|DrivableAreaSurfaceType|||Validation class for DrivableAreaSurfaceType||openlabel.shacl.ttl|
|OddShape|openlabel|DrivableAreaType|||Validation class for DrivableAreaType||openlabel.shacl.ttl|
|OddShape|openlabel|SceneryFixedStructure|||Validation class for SceneryFixedStructure||openlabel.shacl.ttl|
|OddShape|openlabel|JunctionIntersection|||Validation class for JunctionIntersection||openlabel.shacl.ttl|
|OddShape|openlabel|JunctionRoundabout|||Validation class for JunctionRoundabout||openlabel.shacl.ttl|
|OddShape|openlabel|ScenerySpecialStructure|||Validation class for ScenerySpecialStructure||openlabel.shacl.ttl|
|OddShape|openlabel|SceneryTemporaryStructure|||Validation class for SceneryTemporaryStructure||openlabel.shacl.ttl|
|OddShape|openlabel|SceneryZone|||Validation class for SceneryZone||openlabel.shacl.ttl|
|OddShape|openlabel|ConnectivityCommunication|||Validation class for ConnectivityCommunication||openlabel.shacl.ttl|
|OddShape|openlabel|ConnectivityPositioning|||Validation class for ConnectivityPositioning||openlabel.shacl.ttl|
|OddShape|openlabel|IlluminationArtificial|||Validation class for IlluminationArtificial||openlabel.shacl.ttl|
|OddShape|openlabel|IlluminationLowLight|||Validation class for IlluminationLowLight||openlabel.shacl.ttl|
|OddShape|openlabel|RainType|||Validation class for RainType||openlabel.shacl.ttl|
|OddShape|openlabel|EnvironmentParticulates|||Validation class for EnvironmentParticulates||openlabel.shacl.ttl|
|OddShape|openlabel|LaneSpecificationMarking|||Validation class for LaneSpecificationMarking|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|OddShape|openlabel|HorizontalStraights|||Validation class for HorizontalStraights|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|OddShape|openlabel|LongitudinalLevelPlane|||Validation class for LongitudinalLevelPlane|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|OddShape|openlabel|DaySunPosition|||Validation class for DaySunPosition|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|OddShape|openlabel|ParticulatesDust|||Validation class for ParticulatesDust|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|OddShape|openlabel|ParticulatesMarine|||Validation class for ParticulatesMarine|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|OddShape|openlabel|ParticulatesPollution|||Validation class for ParticulatesPollution|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|OddShape|openlabel|ParticulatesVolcanic|||Validation class for ParticulatesVolcanic|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|OddShape|openlabel|TrafficSpecialVehicle|||Validation class for TrafficSpecialVehicle|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|OddShape|openlabel|SubjectVehicleSpeed|||Validation class for subjectVehicleSpeed|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|OddShape|openlabel|subjectVehicleSpeedValue|||Speed (km/h) (Refer to BSI PAS-1883 Section 5.4.b).||openlabel.shacl.ttl|
|OddShape|openlabel|WeatherRain|||Validation class for weatherRain|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|OddShape|openlabel|weatherRainValue|||Rainfall Intensity (mm/h) (Refer to BSI PAS-1883 Section 5.3.1.2).|<http://www.w3.org/2001/XMLSchema#decimal>|openlabel.shacl.ttl|
|OddShape|openlabel|WeatherSnow|||Validation class for weatherSnow|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|OddShape|openlabel|weatherSnowValue|||Visibility (km) (Refer to BSI PAS-1883 Section 5.3.1.3).|<http://www.w3.org/2001/XMLSchema#decimal>|openlabel.shacl.ttl|
|OddShape|openlabel|WeatherWind|||Validation class for weatherWind|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|OddShape|openlabel|weatherWindValue|||Wind Speed (m/s) (Refer to BSI PAS-1883 Section 5.3.1.1).|<http://www.w3.org/2001/XMLSchema#decimal>|openlabel.shacl.ttl|
|OddShape|openlabel|IlluminationCloudiness|||Validation class for illuminationCloudiness|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|OddShape|openlabel|illuminationCloudinessValue|||Cloud cover (okta) (Refer to BSI PAS-1883 Section 5.3.3.c).|<http://www.w3.org/2001/XMLSchema#decimal>|openlabel.shacl.ttl|
|OddShape|openlabel|DaySunElevation|||Validation class for daySunElevation|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|OddShape|openlabel|daySunElevationValue|||Sun Elevation (degrees) (Refer to BSI PAS-1883 Section 5.3.3.a.1).|<http://www.w3.org/2001/XMLSchema#decimal>|openlabel.shacl.ttl|
|OddShape|openlabel|TrafficAgentDensity|||Validation class for trafficAgentDensity|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|OddShape|openlabel|trafficAgentDensityValue|||Density (vehicles/km) (Refer to BSI PAS-1883 Section 5.4.a.1).|<http://www.w3.org/2001/XMLSchema#integer>|openlabel.shacl.ttl|
|OddShape|openlabel|TrafficFlowRate|||Validation class for trafficFlowRate|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|OddShape|openlabel|trafficFlowRateValue|||Rate (vehicles/h) (Refer to BSI PAS-1883 Section 5.4.a.3).|<http://www.w3.org/2001/XMLSchema#integer>|openlabel.shacl.ttl|
|OddShape|openlabel|TrafficVolume|||Validation class for trafficVolume|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|OddShape|openlabel|trafficVolumeValue|||Volume (vehicle km) (Refer to BSI PAS-1883 Section 5.4.a.2).|<http://www.w3.org/2001/XMLSchema#integer>|openlabel.shacl.ttl|
|OddShape|openlabel|LaneSpecificationDimensions|||Validation class for laneSpecificationDimensions|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|OddShape|openlabel|laneSpecificationDimensionsValue|||Lane width (m) (Refer to BSI PAS-1883 Section 5.2.3.4.a).||openlabel.shacl.ttl|
|OddShape|openlabel|LaneSpecificationLaneCount|||Validation class for laneSpecificationLaneCount|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|OddShape|openlabel|laneSpecificationLaneCountValue|||Number of lanes (Unit) (Refer to BSI PAS-1883 Section 5.2.3.4.d).||openlabel.shacl.ttl|
|OddShape|openlabel|HorizontalCurves|||Validation class for horizontalCurves|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|OddShape|openlabel|horizontalCurvesValue|||Curve Radius (m) (Refer to BSI PAS-1883 Section 5.2.3.3).|<http://www.w3.org/2001/XMLSchema#decimal>|openlabel.shacl.ttl|
|OddShape|openlabel|LongitudinalDownSlope|||Validation class for longitudinalDownSlope|<http://www.w3.org/2001/XMLSchema#boolean>|openlabel.shacl.ttl|
|OddShape|openlabel|longitudinalDownSlopeValue|||Gradient (%) (Refer to BSI PAS-1883 Section 5.2.3.3.ii).|<http://www.w3.org/2001/XMLSchema#decimal>|openlabel.shacl.ttl|
|QuantitativeValueShape|schema|minValue|1||||openlabel.shacl.ttl|
|QuantitativeValueShape|schema|maxValue|1||||openlabel.shacl.ttl|
