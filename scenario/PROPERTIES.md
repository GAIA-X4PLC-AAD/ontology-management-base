# Properties of SHACL Files in this folder

## Prefixes

- scenario: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/scenario/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ScenarioShape | scenario | general | 1 | 1 | General properties common for all simulation assets. |  | scenario_shacl.ttl |
| ScenarioShape | scenario | format | 1 | 1 | Contains properties that describe the format of the scenario asset. |  | scenario_shacl.ttl |
| ScenarioShape | scenario | content | 1 | 1 | Defines the content of the scenario asset, such as time, abstraction level, and links. |  | scenario_shacl.ttl |
| ScenarioShape | scenario | quantity | 1 | 1 | Contains properties that describe the quantity of the scenario asset (e.g., number of traffic objects, controllers). |  | scenario_shacl.ttl |
| ScenarioShape | scenario | quality | 1 | 1 | Contains properties that describe the accuracy of objects and the calibration of the scenario asset. |  | scenario_shacl.ttl |
| ScenarioShape | scenario | dataSource | 1 | 1 | Defines which data resources were used to create the scenario asset. |  | scenario_shacl.ttl |
| ScenarioShape | scenario | georeference | 1 | 1 | General properties for defining the location and projection of the scenario asset. |  | scenario_shacl.ttl |
| FormatShape | scenario | formatType |  | 1 | Defines the type of data format used for the scenario asset. | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| FormatShape | scenario | version |  | 1 | Defines the version of the data format used for the scenario asset. | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| ContentShape | scenario | abstractionLevel |  | 1 | Specifies the abstraction level (as defined in the Pegasus project) of the scenario asset. | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| ContentShape | scenario | timeDate | 0 | 1 | Optionally specifies the time associated with the scenario asset (e.g., time of recording or time of event for a synthetic scenario). | <http://www.w3.org/2001/XMLSchema#dateTime> | scenario_shacl.ttl |
| ContentShape | scenario | aim | 0 | 1 | Defines the purpose of the scenario asset. | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| ContentShape | scenario | usedStandardFunctions | 0 | 1 | Specifies which functions (e.g., actions) from the standard are utilized. | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| ContentShape | scenario | movementDescription |  | 1 | Indicates the type of movement employed by traffic participants according to the ASAM OpenSCENARIO standard. | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| ContentShape | scenario | customCommands | 0 | 1 | Defines scenario- or domain-specific commands or actions used in the scenario asset. | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| ContentShape | scenario | catalogs | 0 |  | Specifies the catalogues used in the scenario asset (provided as links). |  | scenario_shacl.ttl |
| ContentShape | scenario | environmentModels | 0 |  | Specifies the environment models used in the scenario asset (provided as links). |  | scenario_shacl.ttl |
| ContentShape | scenario | trafficSpace | 0 | 1 | Specifies the traffic space used in the scenario asset (provided as a link). |  | scenario_shacl.ttl |
| ContentShape | scenario | sunAzimuth | 0 |  | Defines the azimuth of the sun in degrees. | <http://www.w3.org/2001/XMLSchema#float> | scenario_shacl.ttl |
| ContentShape | scenario | countrySpecificSign | 0 | 1 | Indicates which country-specific traffic signs are used in the scenario asset. | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| ContentShape | scenario | countrySpecificTrafficParticipants | 0 | 1 | Indicates which country-specific participants are used in the scenario asset. | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| ContentShape | scenario | country | 0 | 1 | Indicates the country of origin for the scenario asset. | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| QuantityShape | scenario | temporaryTrafficObjects |  | 1 | Specifies the total number of temporary traffic objects defined in the scenario asset. | <http://www.w3.org/2001/XMLSchema#unsignedInt> | scenario_shacl.ttl |
| QuantityShape | scenario | numberTrafficObjects |  | 1 | Specifies the total number of traffic objects defined in the scenario asset. | <http://www.w3.org/2001/XMLSchema#unsignedInt> | scenario_shacl.ttl |
| QuantityShape | scenario | controllers | 0 |  | Specifies the simulation core controllers (internal or external) used in the scenario. | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| QuantityShape | scenario | permanentTrafficObjects |  | 1 | Specifies the total number of permanent traffic objects defined in the scenario asset. | <http://www.w3.org/2001/XMLSchema#unsignedInt> | scenario_shacl.ttl |
| QualityShape | scenario | accuracyObjects | 0 | 1 | Defines the accuracy of moving objects in the scenario asset (only applicable for scenarios based on real measurements). | <http://www.w3.org/2001/XMLSchema#float> | scenario_shacl.ttl |
| QualityShape | scenario | calibration | 0 | 1 | Describes the calibration steps performed prior to the measurements. | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| DataSourceShape | scenario | sourceType | 0 | 1 | Specifies the category of source data used to create the scenario. | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| DataSourceShape | scenario | sourceDescription | 0 | 1 | Provides a detailed description of the source data used. | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
