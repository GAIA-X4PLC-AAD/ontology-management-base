# Variables of SHACL Files in this folder

## Prefixes

- gx: <https://registry.lab.gaia-x.eu/development/api/trusted-shape-registry/v1/shapes/jsonld/trustframework#>
- survey: <http://semanticweb.org/metadatasurveylogy/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SurveyResultDataOfferingShape | survey | surveyStartTime | 1 |  | When the survey was started. | <http://www.w3.org/2001/XMLSchema#dateTime> | survey-result-data-offering_shacl.ttl |
| SurveyResultDataOfferingShape | survey | surveyCloseTime | 1 |  | When the survey was closed. | <http://www.w3.org/2001/XMLSchema#dateTime> | survey-result-data-offering_shacl.ttl |
| SurveyResultDataOfferingShape | gx | contractId | 1 | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | survey-result-data-offering_shacl.ttl |
| SurveyResultDataOfferingShape | survey | belongsTo | 1 |  | Accompanied survey service offering. | <http://www.w3.org/ns/shacl#IRI> | survey-result-data-offering_shacl.ttl |
| SurveyServiceOfferingShape | survey | surveyId | 1 |  |  | <http://www.w3.org/2001/XMLSchema#string> | survey-service-offering_shacl.ttl |
| SurveyServiceOfferingShape | survey | surveyUrl | 1 |  |  | <http://www.w3.org/2001/XMLSchema#string> | survey-service-offering_shacl.ttl |
| SurveyServiceOfferingShape | survey | surveyCreationTime | 1 |  | When the survey was created | <http://www.w3.org/2001/XMLSchema#dateTime> | survey-service-offering_shacl.ttl |
| SurveyServiceOfferingShape | survey | surveyEndTime | 1 |  | When the survey will end automatically | <http://www.w3.org/2001/XMLSchema#dateTime> | survey-service-offering_shacl.ttl |
| SurveyServiceOfferingShape | gx | providedBy | 1 | 1 | Who created the survey | <http://www.w3.org/2001/XMLSchema#string> | survey-service-offering_shacl.ttl |
| SurveyServiceOfferingShape | gx | name | 1 | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | survey-service-offering_shacl.ttl |
| SurveyServiceOfferingShape | gx | description | 1 | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | survey-service-offering_shacl.ttl |
