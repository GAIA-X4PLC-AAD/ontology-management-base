# Variables of SHACL Files in this folder

## Prefixes

- georeference: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/georeference/>
- scenario: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/scenario/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ScenarioShape | scenario | general | 1 | 1 |  |  | scenario_shacl.ttl |
| ScenarioShape | scenario | environmental | 1 | 1 |  |  | scenario_shacl.ttl |
| ScenarioShape | scenario | common | 1 | 1 |  |  | scenario_shacl.ttl |
| ScenarioShape | scenario | source | 1 | 1 |  |  | scenario_shacl.ttl |
| ScenarioShape | scenario | structural | 1 | 1 |  |  | scenario_shacl.ttl |
| ScenarioShape | scenario | traffic | 1 | 1 |  |  | scenario_shacl.ttl |
| ScenarioShape | scenario | trafficParticipants | 1 | 1 |  |  | scenario_shacl.ttl |
| ScenarioShape | scenario | format | 1 | 1 |  |  | scenario_shacl.ttl |
| ScenarioShape | georeference | georeference | 0 | 1 |  |  | scenario_shacl.ttl |
| DataSourceShape | scenario | source | 0 | 1 | Capture type | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| EnvironmentalShape | scenario | sunAzimuth | 0 |  | Azimuth of the sun | <http://www.w3.org/2001/XMLSchema#float> | scenario_shacl.ttl |
| FormatShape | scenario | dataFormat |  | 1 | Format type definition | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| FormatShape | scenario | version |  | 1 | Version of data format | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| ScenarioCommonShape | scenario | abstractionLevel |  | 1 | Pegasus type of scenario | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| ScenarioCommonShape | scenario | timeDate | 0 | 1 | Time of the scenario if applicaple. Either time of recording or if synthetic the time it happens. | <http://www.w3.org/2001/XMLSchema#dateTime> | scenario_shacl.ttl |
| ScenarioCommonShape | scenario | aim | 0 | 1 | Purpose of this scenario. | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| ScenarioCommonShape | scenario | usedStandardFunctions | 0 | 1 |  Use of the functionalities from the standard. E.g. which Actions are used. | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| TrafficParticipantsShape | scenario | temporaryTrafficObjects |  | 1 | Count of traffic temporary objects | <http://www.w3.org/2001/XMLSchema#unsignedInt> | scenario_shacl.ttl |
| TrafficParticipantsShape | scenario | numberTrafficObjects |  | 1 | Count of traffic objects | <http://www.w3.org/2001/XMLSchema#unsignedInt> | scenario_shacl.ttl |
| TrafficParticipantsShape | scenario | controllers | 0 |  | Usage of simulation Core internal or external controllers. | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| TrafficParticipantsShape | scenario | permanentTrafficObjects |  | 1 | Count of traffic permanent objects | <http://www.w3.org/2001/XMLSchema#unsignedInt> | scenario_shacl.ttl |
| TrafficParticipantsShape | scenario | movementDescription |  | 1 | Type of movement used by traffic participants according to the OpenSCENARIO standard. | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| TrafficParticipantsShape | scenario | customCommands | 0 | 1 | Scenario/domain specific commands or actions | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| StructuralShape | scenario | catalogs | 0 |  | Link to Catalogs |  | scenario_shacl.ttl |
| StructuralShape | scenario | 3dModels | 0 |  | Link to 3D models |  | scenario_shacl.ttl |
| StructuralShape | scenario | trafficSpace | 0 | 1 | Link to traffic space |  | scenario_shacl.ttl |
| TrafficShape | scenario | countrySpecificSign | 0 | 1 | Country specific traffic signs | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| TrafficShape | scenario | countrySpecificTP | 0 | 1 | Country specific traffic participants | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| TrafficShape | scenario | country | 0 | 1 | Country where this scenario is from | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
