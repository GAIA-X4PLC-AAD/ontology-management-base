# Properties of SHACL Files in this folder

## Prefixes

- manifest: <https://ontologies.envited-x.net/manifest/v5/ontology#>
- scenario: <https://ontologies.envited-x.net/scenario/v5/ontology#>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ScenarioShape | scenario | hasDataResource | 1 | 1 |  |  | scenario_shacl.ttl |
| ScenarioShape | scenario | hasDataResourceExtension | 1 | 1 |  |  | scenario_shacl.ttl |
| ScenarioShape | scenario | hasManifest | 1 | 1 |  |  | scenario_shacl.ttl |
| ScenarioManifestConstraints | manifest | hasReferencedArtifacts |  |  |  |  | scenario_shacl.ttl |
| DataResourceExtensionShape | scenario | hasContent | 1 |  | Attributes describing the content of the scenario. |  | scenario_shacl.ttl |
| DataResourceExtensionShape | scenario | hasFormat | 1 | 1 |  |  | scenario_shacl.ttl |
| DataResourceExtensionShape | scenario | hasQuality | 1 | 1 |  |  | scenario_shacl.ttl |
| DataResourceExtensionShape | scenario | hasQuantity | 1 | 1 |  |  | scenario_shacl.ttl |
| DataResourceExtensionShape | scenario | hasDataSource | 1 | 1 |  |  | scenario_shacl.ttl |
| DataResourceExtensionShape | scenario | hasGeoreference | 1 | 1 |  |  | scenario_shacl.ttl |
| FormatShape | scenario | formatType | 1 |  |  | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| FormatShape | scenario | version | 1 |  |  | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
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
| QuantityShape | scenario | numberTrafficObjects |  |  |  | <http://www.w3.org/2001/XMLSchema#unsignedInt> | scenario_shacl.ttl |
| QuantityShape | scenario | permanentTrafficObjects |  |  |  | <http://www.w3.org/2001/XMLSchema#unsignedInt> | scenario_shacl.ttl |
| QuantityShape | scenario | temporaryTrafficObjects |  |  |  | <http://www.w3.org/2001/XMLSchema#unsignedInt> | scenario_shacl.ttl |
| QuantityShape | scenario | controllers |  |  |  | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| QualityShape | scenario | accuracyObjects |  |  |  | <http://www.w3.org/2001/XMLSchema#float> | scenario_shacl.ttl |
| QualityShape | scenario | calibration |  |  |  | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| DataSourceShape | scenario | sourceType | 1 |  |  | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
| DataSourceShape | scenario | sourceDescription |  |  |  | <http://www.w3.org/2001/XMLSchema#string> | scenario_shacl.ttl |
