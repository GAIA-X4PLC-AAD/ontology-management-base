# Properties of SHACL Files in this folder

## Prefixes

- manifest: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/manifest/>
- scenario: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/scenario/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ScenarioShape | scenario | hasDataResource | 1 | 1 |  |  | scenario_shacl.ttl |
| ScenarioShape | scenario | hasDataResourceExtension | 1 | 1 |  |  | scenario_shacl.ttl |
| ScenarioShape | scenario | hasManifest | 1 | 1 |  |  | scenario_shacl.ttl |
| ManifestShape | manifest | hasArtifacts |  |  |  |  | scenario_shacl.ttl |
| ManifestShape | manifest | hasReferencedArtifacts |  |  |  |  | scenario_shacl.ttl |
| ManifestShape | manifest | hasReferencedArtifacts |  |  | Each Scenario manifest must reference at least one HD Map, either inline or via `manifest:Link` referencing `hdmap:HdMap`. |  | scenario_shacl.ttl |
| ManifestShape | manifest | hasReferencedArtifacts |  |  | Each Scenario manifest must reference at least one Environment Model, either inline or via `manifest:Link` referencing `environment-model:EnvironmentModel`. |  | scenario_shacl.ttl |
| ManifestShape | scenario | hasArtifact |  |  | Each Scenario manifest must reference at least one catalog via a `manifest:Link`. |  | scenario_shacl.ttl |
| DataResourceExtensionShape | scenario | hasContent | 1 | 1 | Attributes describing the content of the scenario. |  | scenario_shacl.ttl |
| DataResourceExtensionShape | scenario | hasFormat | 1 | 1 | File format details of the scenario. |  | scenario_shacl.ttl |
| DataResourceExtensionShape | scenario | hasQuality | 1 | 1 | Quality metrics of the scenario. |  | scenario_shacl.ttl |
| DataResourceExtensionShape | scenario | hasQuantity | 1 | 1 | Quantitative metrics describing the scenario. |  | scenario_shacl.ttl |
| DataResourceExtensionShape | scenario | hasDataSource | 1 | 1 | Data sources used to create the scenario. |  | scenario_shacl.ttl |
| DataResourceExtensionShape | scenario | hasGeoreference | 1 | 1 | Georeferencing information for the scenario. |  | scenario_shacl.ttl |
| FormatShape | scenario | formatType |  | 1 | Defines the type of data format used for the scenario asset. |  | scenario_shacl.ttl |
| FormatShape | scenario | version |  | 1 | Defines the version of the data format used for the scenario asset. | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| ContentShape | scenario | abstractionLevel |  | 1 | Specifies the abstraction level (as defined in the Pegasus project) of the scenario asset. |  | scenario_shacl.ttl |
| ContentShape | scenario | timeDate | 0 | 1 | Optionally specifies the time associated with the scenario asset (e.g., time of recording or time of event for a synthetic scenario). | <http://www.w3.org/2001/XMLSchema#dateTime> | scenario_shacl.ttl |
| ContentShape | scenario | aim | 0 | 1 | Defines the purpose of the scenario asset. | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| ContentShape | scenario | usedStandardFunctions | 0 | 1 | Specifies which functions (e.g., actions) from the standard are utilized. | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| ContentShape | scenario | movementDescription |  | 1 | Indicates the type of movement employed by traffic participants according to the ASAM OpenSCENARIO standard. | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| ContentShape | scenario | customCommands | 0 | 1 | Defines scenario- or domain-specific commands or actions used in the scenario asset. | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
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
| DataSourceShape | scenario | sourceType | 0 | 1 | Specifies the category of source data used to create the scenario. |  | scenario_shacl.ttl |
| DataSourceShape | scenario | sourceDescription | 0 | 1 | Provides a detailed description of the source data used. | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
