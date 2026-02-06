## survey Properties

### Class Diagram

```mermaid
classDiagram
class Class_definition_for_SurveyResultDataOffering
class Class_definition_for_SurveyServiceOffering
```

### Class Hierarchy

- Class definition for SurveyResultDataOffering (https://w3id.org/gaia-x4plcaad/ontologies/survey/v6/SurveyResultDataOffering)
- Class definition for SurveyServiceOffering (https://w3id.org/gaia-x4plcaad/ontologies/survey/v6/SurveyServiceOffering)

### Class Definitions

|Class|IRI|Description|Parents|
|---|---|---|---|
|Class definition for SurveyResultDataOffering|https://w3id.org/gaia-x4plcaad/ontologies/survey/v6/SurveyResultDataOffering|The survey result refers to the data obtained from conducting the survey. It represents the collective responses gathered from all survey participants in relation to the specific topic of the survey.|DataResource|
|Class definition for SurveyServiceOffering|https://w3id.org/gaia-x4plcaad/ontologies/survey/v6/SurveyServiceOffering|The survey service offering refers to the invitation to a participate in a survey.|SoftwareResource|

## Prefixes

- brick: <https://brickschema.org/schema/Brick#>
- csvw: <http://www.w3.org/ns/csvw#>
- dc: <http://purl.org/dc/elements/1.1/>
- dcam: <http://purl.org/dc/dcam/>
- dcat: <http://www.w3.org/ns/dcat#>
- dcmitype: <http://purl.org/dc/dcmitype/>
- dcterms: <http://purl.org/dc/terms/>
- doap: <http://usefulinc.com/ns/doap#>
- foaf: <http://xmlns.com/foaf/0.1/>
- general: <https://w3id.org/gaia-x4plcaad/ontologies/general/v3/>
- geo: <http://www.opengis.net/ont/geosparql#>
- gx: <https://w3id.org/gaia-x/development/>
- odrl: <http://www.w3.org/ns/odrl/2/>
- org: <http://www.w3.org/ns/org#>
- owl: <http://www.w3.org/2002/07/owl#>
- prof: <http://www.w3.org/ns/dx/prof/>
- prov: <http://www.w3.org/ns/prov#>
- qb: <http://purl.org/linked-data/cube#>
- rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
- rdfs: <http://www.w3.org/2000/01/rdf-schema#>
- schema: <https://schema.org/>
- sh: <http://www.w3.org/ns/shacl#>
- skos: <http://www.w3.org/2004/02/skos/core#>
- sosa: <http://www.w3.org/ns/sosa/>
- ssn: <http://www.w3.org/ns/ssn/>
- survey: <https://w3id.org/gaia-x4plcaad/ontologies/survey/v6/>
- time: <http://www.w3.org/2006/time#>
- vann: <http://purl.org/vocab/vann/>
- void: <http://rdfs.org/ns/void#>
- wgs: <https://www.w3.org/2003/01/geo/wgs84_pos#>
- xml: <http://www.w3.org/XML/1998/namespace>
- xsd: <http://www.w3.org/2001/XMLSchema#>

### SHACL Properties

#### survey:belongsTo {: #prop-https---w3id-org-gaia-x4plcaad-ontologies-survey-v6-belongsto .property-anchor }
#### survey:general {: #prop-https---w3id-org-gaia-x4plcaad-ontologies-survey-v6-general .property-anchor }
#### survey:surveyCloseTime {: #prop-https---w3id-org-gaia-x4plcaad-ontologies-survey-v6-surveyclosetime .property-anchor }
#### survey:surveyCreationTime {: #prop-https---w3id-org-gaia-x4plcaad-ontologies-survey-v6-surveycreationtime .property-anchor }
#### survey:surveyEndTime {: #prop-https---w3id-org-gaia-x4plcaad-ontologies-survey-v6-surveyendtime .property-anchor }
#### survey:surveyStartTime {: #prop-https---w3id-org-gaia-x4plcaad-ontologies-survey-v6-surveystarttime .property-anchor }
#### survey:surveyUrl {: #prop-https---w3id-org-gaia-x4plcaad-ontologies-survey-v6-surveyurl .property-anchor }

|Shape|Property prefix|Property|MinCount|MaxCount|Description|Datatype/NodeKind|Filename|
|---|---|---|---|---|---|---|---|
|SurveyResultDataOfferingShape|survey|<a id="prop-https---w3id-org-gaia-x4plcaad-ontologies-survey-v6-surveystarttime"></a>surveyStartTime|1|1|When the survey was started.|<http://www.w3.org/2001/XMLSchema#dateTime>|survey-result-data-offering.shacl.ttl|
|SurveyResultDataOfferingShape|survey|<a id="prop-https---w3id-org-gaia-x4plcaad-ontologies-survey-v6-surveyclosetime"></a>surveyCloseTime|1|1|When the survey was closed.|<http://www.w3.org/2001/XMLSchema#dateTime>|survey-result-data-offering.shacl.ttl|
|SurveyResultDataOfferingShape|survey|<a id="prop-https---w3id-org-gaia-x4plcaad-ontologies-survey-v6-belongsto"></a>belongsTo|1|1|Accompanied survey service offering.|<http://www.w3.org/ns/shacl#IRI>|survey-result-data-offering.shacl.ttl|
|SurveyResultDataOfferingShape|survey|<a id="prop-https---w3id-org-gaia-x4plcaad-ontologies-survey-v6-general"></a>general|1|1|||survey-result-data-offering.shacl.ttl|
|SurveyServiceOfferingShape|survey|<a id="prop-https---w3id-org-gaia-x4plcaad-ontologies-survey-v6-surveyurl"></a>surveyUrl|1|1||<http://www.w3.org/2001/XMLSchema#string>|survey-service-offering.shacl.ttl|
|SurveyServiceOfferingShape|survey|<a id="prop-https---w3id-org-gaia-x4plcaad-ontologies-survey-v6-surveycreationtime"></a>surveyCreationTime|1|1|When the survey was created|<http://www.w3.org/2001/XMLSchema#dateTime>|survey-service-offering.shacl.ttl|
|SurveyServiceOfferingShape|survey|<a id="prop-https---w3id-org-gaia-x4plcaad-ontologies-survey-v6-surveyendtime"></a>surveyEndTime|1|1|When the survey will end automatically|<http://www.w3.org/2001/XMLSchema#dateTime>|survey-service-offering.shacl.ttl|
|SurveyServiceOfferingShape|survey|general|1|1|||survey-service-offering.shacl.ttl|
