# Properties of SHACL Files for survey

## Prefixes

- survey: <https://w3id.org/gaia-x4plcaad/ontologies/survey/v6/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SurveyResultDataOfferingShape | survey | surveyStartTime | 1 | 1 | When the survey was started. | <http://www.w3.org/2001/XMLSchema#dateTime> | survey-result-data-offering.shacl.ttl |
| SurveyResultDataOfferingShape | survey | surveyCloseTime | 1 | 1 | When the survey was closed. | <http://www.w3.org/2001/XMLSchema#dateTime> | survey-result-data-offering.shacl.ttl |
| SurveyResultDataOfferingShape | survey | belongsTo | 1 | 1 | Accompanied survey service offering. | <http://www.w3.org/ns/shacl#IRI> | survey-result-data-offering.shacl.ttl |
| SurveyResultDataOfferingShape | survey | general | 1 | 1 |  |  | survey-result-data-offering.shacl.ttl |
| SurveyServiceOfferingShape | survey | surveyUrl | 1 | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | survey-service-offering.shacl.ttl |
| SurveyServiceOfferingShape | survey | surveyCreationTime | 1 | 1 | When the survey was created | <http://www.w3.org/2001/XMLSchema#dateTime> | survey-service-offering.shacl.ttl |
| SurveyServiceOfferingShape | survey | surveyEndTime | 1 | 1 | When the survey will end automatically | <http://www.w3.org/2001/XMLSchema#dateTime> | survey-service-offering.shacl.ttl |
| SurveyServiceOfferingShape | survey | general | 1 | 1 |  |  | survey-service-offering.shacl.ttl |
