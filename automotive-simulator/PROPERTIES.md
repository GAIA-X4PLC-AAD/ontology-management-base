# Properties of SHACL Files in this folder

## Prefixes

- automotive-simulator: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/automotive-simulator/>
- simulated-sensor: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/simulated-sensor/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AutomotiveSimulatorShape | automotive-simulator | general | 1 | 1 | General object with properties for description and data. |  | automotive-simulator_shacl.ttl |
| AutomotiveSimulatorShape | automotive-simulator | simulatorMake | 1 | 1 | Make/Type of automotive simulator. | <http://www.w3.org/2001/XMLSchema#string> | automotive-simulator_shacl.ttl |
| AutomotiveSimulatorShape | automotive-simulator | softwareVersion | 1 | 1 | Sofware version of the simulator. | <http://www.w3.org/2001/XMLSchema#string> | automotive-simulator_shacl.ttl |
| AutomotiveSimulatorShape | automotive-simulator | sensorFailureFlag | 1 | 1 | If true, the simulator supports the simulation of sensor failures. | <http://www.w3.org/2001/XMLSchema#boolean> | automotive-simulator_shacl.ttl |
| AutomotiveSimulatorShape | automotive-simulator | sensorAttackFlag | 1 | 1 | If true, the simulator supports the simulation of sensor attacks. | <http://www.w3.org/2001/XMLSchema#boolean> | automotive-simulator_shacl.ttl |
| AutomotiveSimulatorShape | automotive-simulator | scenarioDefinition | 0 |  | Description language for defining driving scenarios supported by the simulator. | <http://www.w3.org/2001/XMLSchema#string> | automotive-simulator_shacl.ttl |
| AutomotiveSimulatorShape | automotive-simulator | interface | 0 |  | Communcation interface provided by the simulator to communicate with different assets (e.g. agents/vehicle implementations). | <http://www.w3.org/2001/XMLSchema#string> | automotive-simulator_shacl.ttl |
| AutomotiveSimulatorShape | simulated-sensor | simulatedSensor | 0 |  | Type and kinds of sensors that are natively included in the simulator. |  | automotive-simulator_shacl.ttl |
