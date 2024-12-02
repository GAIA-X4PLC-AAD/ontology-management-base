# Variables of SHACL Files in this folder

## Prefixes

- simulation-model: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/simulation-model/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SimulationModelShape | simulation-model | general | 1 | 1 | general object with properties for descriptions, data, links, bundle |  | simulation-model_shacl.ttl |
| SimulationModelShape | simulation-model | format | 1 | 1 | format object with properties for format informations |  | simulation-model_shacl.ttl |
| SimulationModelShape | simulation-model | content | 1 | 1 | content object with properties for simulation-model intrinsic attributes |  | simulation-model_shacl.ttl |
| SimulationModelShape | simulation-model | quantity | 1 | 1 | quantity object with properties for quantity informations |  | simulation-model_shacl.ttl |
| SimulationModelShape | simulation-model | quality | 1 | 1 | quality object with properties for quality informations |  | simulation-model_shacl.ttl |
| SimulationModelShape | simulation-model | dataSource | 1 | 1 | dataSource object with properties for data sources |  | simulation-model_shacl.ttl |
| FormatShape | simulation-model | model.implementation.format | 1 | 1 | Format of model implementation, e.g. OSMP 1.0/OSI 3.1.2/FMI 2.0 | <http://www.w3.org/2001/XMLSchema#string> | simulation-model_shacl.ttl |
| FormatShape | simulation-model | model.preconditions |  | 1 | Preconditions for model validity, e.g. things that the rest of the simulation should provide the model with so that the model can work within its foreseen validity range. | <http://www.w3.org/2001/XMLSchema#string> | simulation-model_shacl.ttl |
| FormatShape | simulation-model | model.implementation.preconditions |  | 1 | Implementation requirements. | <http://www.w3.org/2001/XMLSchema#string> | simulation-model_shacl.ttl |
| FormatShape | simulation-model | model.integration.requirements |  | 1 | Provide a link to requirements and considerations for operating the model. | <http://www.w3.org/2001/XMLSchema#anyURI> | simulation-model_shacl.ttl |
| ContentShape | simulation-model | model.type | 1 | 1 | Type of model. This entry defines what domain specific entries are relevant and is mandatory | <http://www.w3.org/2001/XMLSchema#string> | simulation-model_shacl.ttl |
| ContentShape | simulation-model | model.manufacturer | 1 | 1 | Provider of the Model, no specific convention defined, it can be a company, a department a person or a combination of those. | <http://www.w3.org/2001/XMLSchema#string> | simulation-model_shacl.ttl |
| ContentShape | simulation-model | model.family |  | 1 | Model Family Name, in some case a model is a concrete instance of a more generic model belonging to a family. In this case, the family can be mentioned here. | <http://www.w3.org/2001/XMLSchema#string> | simulation-model_shacl.ttl |
| ContentShape | simulation-model | model.name | 1 | 1 | Model Name. This can be the name of the model file or the name of the model as it is called | <http://www.w3.org/2001/XMLSchema#string> | simulation-model_shacl.ttl |
| ContentShape | simulation-model | model.version | 1 | 1 | Model Version, no specific convention defined | <http://www.w3.org/2001/XMLSchema#string> | simulation-model_shacl.ttl |
| ContentShape | simulation-model | model.releasedate | 1 | 1 | Model Release Date in ISO8601 | <http://www.w3.org/2001/XMLSchema#dateTime> | simulation-model_shacl.ttl |
| ContentShape | simulation-model | model.releasestatus | 1 | 1 | The status of the model version released in the life cycle of the model. | <http://www.w3.org/2001/XMLSchema#string> | simulation-model_shacl.ttl |
| ContentShape | simulation-model | model.use-restrictions |  | 1 | Legal or contractual restrictions on the use and distribution of the model that have to be respected. Applicable Licenses should be mentioned here. | <http://www.w3.org/2001/XMLSchema#string> | simulation-model_shacl.ttl |
| ContentShape | simulation-model | model.guid |  | 1 | For FMU-based models, this should be the GUID of the FMU. | <http://www.w3.org/2001/XMLSchema#string> | simulation-model_shacl.ttl |
| ContentShape | simulation-model | model.purpose |  | 1 | Purpose for which the model has been built/validated. | <http://www.w3.org/2001/XMLSchema#string> | simulation-model_shacl.ttl |
| ContentShape | simulation-model | model.modelling-approach |  | 1 | Description of the modelling approach taken. | <http://www.w3.org/2001/XMLSchema#string> | simulation-model_shacl.ttl |
| QuantityShape | simulation-model | maxDetections | 0 | 1 | The maximum number of detections. | <http://www.w3.org/2001/XMLSchema#positiveInteger> | simulation-model_shacl.ttl |
| QuantityShape | simulation-model | maxObjects | 0 | 1 | The maximum number of objects. | <http://www.w3.org/2001/XMLSchema#positiveInteger> | simulation-model_shacl.ttl |
| QualityShape | simulation-model | model.limitations | 0 | 1 | Description of all limitations that apply to the model and its usage. | <http://www.w3.org/2001/XMLSchema#string> | simulation-model_shacl.ttl |
| QualityShape | simulation-model | model.validity-range | 0 | 1 | Restrictions on the model validity, typically on quantifiable aspects. | <http://www.w3.org/2001/XMLSchema#string> | simulation-model_shacl.ttl |
| QualityShape | simulation-model | model.verification.status | 1 | 1 | Is the model verified | <http://www.w3.org/2001/XMLSchema#boolean> | simulation-model_shacl.ttl |
| QualityShape | simulation-model | model.verification.report | 0 | 1 | Link to model verification report, if any exists | <http://www.w3.org/2001/XMLSchema#anyURI> | simulation-model_shacl.ttl |
| QualityShape | simulation-model | model.validation.status | 1 | 1 | Is the model validated, according to the validation concept | <http://www.w3.org/2001/XMLSchema#boolean> | simulation-model_shacl.ttl |
| QualityShape | simulation-model | model.validation.platform | 0 | 1 | Specification of simulation environment used for model validation. | <http://www.w3.org/2001/XMLSchema#string> | simulation-model_shacl.ttl |
| QualityShape | simulation-model | model.validation.report | 0 | 1 | Link to model validation report, if any exists | <http://www.w3.org/2001/XMLSchema#string> | simulation-model_shacl.ttl |
| QualityShape | simulation-model | model.validation.concept | 0 | 1 | Link to document detailing the validation concepts used for model validation, if any exists | <http://www.w3.org/2001/XMLSchema#string> | simulation-model_shacl.ttl |
| QualityShape | simulation-model | model.implementation.performance-characteristics | 0 | 1 | Description of model performance characteristics. | <http://www.w3.org/2001/XMLSchema#string> | simulation-model_shacl.ttl |
| DataSourceShape | simulation-model | model.specification | 0 | 1 | Provide a link to the model specification document | <http://www.w3.org/2001/XMLSchema#anyURI> | simulation-model_shacl.ttl |
