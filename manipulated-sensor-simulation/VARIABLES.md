# Variables of SHACL Files in this folder

## Prefixes

- manipulated-sensor-simulation: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/manipulated-sensor-simulation/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ManipulatedSensorSimulationShape | manipulated-sensor-simulation | service | 1 | 1 |  |  | manipulated-sensor-simulation_shacl.ttl |
| ManipulatedSensorSimulationShape | manipulated-sensor-simulation | simulatedSensor | 1 |  |  |  | manipulated-sensor-simulation_shacl.ttl |
| ManipulatedSensorSimulationShape | manipulated-sensor-simulation | sensorSpecification | 1 |  |  |  | manipulated-sensor-simulation_shacl.ttl |
| ManipulatedSensorSimulationShape | manipulated-sensor-simulation | sensorSpecification | 0 | 1 |  |  | manipulated-sensor-simulation_shacl.ttl |
| ManipulatedSensorSimulationShape | manipulated-sensor-simulation | keyPerformanceIndicator | 1 | 3 |  |  | manipulated-sensor-simulation_shacl.ttl |
| ScenarioShape | manipulated-sensor-simulation | scenario |  |  | Identifier string of CARLAs ScenarioRUNNER scenario | <http://www.w3.org/2001/XMLSchema#string> | manipulated-sensor-simulation_shacl.ttl |
| VehicleModelShape | manipulated-sensor-simulation | vehicleModel |  |  | Desired vehicle model provided as the identifier in CARLAs blueprint library | <http://www.w3.org/2001/XMLSchema#string> | manipulated-sensor-simulation_shacl.ttl |
| KeyPerformanceIndicatorShape | manipulated-sensor-simulation | keyPerformanceIndicator |  |  | ecu.test KPI for ALKS simulation | <http://www.w3.org/2001/XMLSchema#string> | manipulated-sensor-simulation_shacl.ttl |
