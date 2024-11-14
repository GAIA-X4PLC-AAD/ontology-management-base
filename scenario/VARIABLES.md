# Variables of SHACL Files in this folder

## Prefixes

- scenario: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/scenario/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ScenarioShape | scenario | general | 1 | 1 | general object with properties for descriptions, data, links, bundle |  | scenario_shacl.ttl |
| ScenarioShape | scenario | format | 1 | 1 | format object with properties for format informations |  | scenario_shacl.ttl |
| ScenarioShape | scenario | content | 1 | 1 | content object with properties for scenario intrinsic attributes |  | scenario_shacl.ttl |
| ScenarioShape | scenario | quantity | 1 | 1 | quantity object with properties for quantity informations |  | scenario_shacl.ttl |
| ScenarioShape | scenario | quality | 1 | 1 | quality object with properties for quality informations |  | scenario_shacl.ttl |
| ScenarioShape | scenario | dataSource | 1 | 1 | dataSource object with properties for data sources |  | scenario_shacl.ttl |
| ScenarioShape | scenario | georeference | 1 | 1 | georeference object with properties for georeference informations |  | scenario_shacl.ttl |
| FormatShape | scenario | formatType |  | 1 | Format type definition | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| FormatShape | scenario | version |  | 1 | Version of data format | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| ContentShape | scenario | abstractionLevel |  | 1 | Pegasus type of scenario | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| ContentShape | scenario | timeDate | 0 | 1 | Time of the scenario if applicaple. Either time of recording or if synthetic the time it happens. | <http://www.w3.org/2001/XMLSchema#dateTime> | scenario_shacl.ttl |
| ContentShape | scenario | aim | 0 | 1 | Purpose of this scenario. | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| ContentShape | scenario | usedStandardFunctions | 0 | 1 | Use of the functionalities from the standard. E.g. which Actions are used. | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| ContentShape | scenario | movementDescription |  | 1 | Type of movement used by traffic participants according to the OpenSCENARIO standard. | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| ContentShape | scenario | customCommands | 0 | 1 | Scenario/domain specific commands or actions | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| ContentShape | scenario | catalogs | 0 |  | Link to Catalogs |  | scenario_shacl.ttl |
| ContentShape | scenario | 3dModels | 0 |  | Link to 3D models |  | scenario_shacl.ttl |
| ContentShape | scenario | trafficSpace | 0 | 1 | Link to traffic space |  | scenario_shacl.ttl |
| ContentShape | scenario | sunAzimuth | 0 |  | Azimuth of the sun | <http://www.w3.org/2001/XMLSchema#float> | scenario_shacl.ttl |
| ContentShape | scenario | countrySpecificSign | 0 | 1 | Country specific traffic signs | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| ContentShape | scenario | countrySpecificTP | 0 | 1 | Country specific traffic participants | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| ContentShape | scenario | country | 0 | 1 | Country where this scenario is from | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| QuantityShape | scenario | temporaryTrafficObjects |  | 1 | Count of traffic temporary objects | <http://www.w3.org/2001/XMLSchema#unsignedInt> | scenario_shacl.ttl |
| QuantityShape | scenario | numberTrafficObjects |  | 1 | Count of traffic objects | <http://www.w3.org/2001/XMLSchema#unsignedInt> | scenario_shacl.ttl |
| QuantityShape | scenario | controllers | 0 |  | Usage of simulation core internal or external controllers. | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| QuantityShape | scenario | permanentTrafficObjects |  | 1 | Count of traffic permanent objects | <http://www.w3.org/2001/XMLSchema#unsignedInt> | scenario_shacl.ttl |
| QualityShape | scenario | accuracyObjects | 0 | 1 | Accuracy of moving objects (only applicable if scenario is based on real measurments). | <http://www.w3.org/2001/XMLSchema#float> | scenario_shacl.ttl |
| QualityShape | scenario | calibration | 0 | 1 | Description of any calibration steps performed prior to measurement | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| DataSourceShape | scenario | source | 0 | 1 | Capture type | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
