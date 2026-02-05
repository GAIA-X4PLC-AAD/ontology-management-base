## service Properties

### Class Diagram

```mermaid
classDiagram
class Class_definition_for_RequiredFile
class Class_definition_for_ResultingFile
class Class_definition_for_Service
```

### Class Hierarchy

- Class definition for RequiredFile (https://w3id.org/gaia-x4plcaad/ontologies/service/v1/RequiredFile)
- Class definition for ResultingFile (https://w3id.org/gaia-x4plcaad/ontologies/service/v1/ResultingFile)
- Class definition for Service (https://w3id.org/gaia-x4plcaad/ontologies/service/v1/Service)

### Class Definitions

|Class|IRI|Description|Parents|
|---|---|---|---|
|Class definition for RequiredFile|https://w3id.org/gaia-x4plcaad/ontologies/service/v1/RequiredFile|Attributes for required files of simulation services.||
|Class definition for ResultingFile|https://w3id.org/gaia-x4plcaad/ontologies/service/v1/ResultingFile|Attributes for resulting files of simulation services.||
|Class definition for Service|https://w3id.org/gaia-x4plcaad/ontologies/service/v1/Service|Attributes for simulation services.|SoftwareResource|

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
- service: <https://w3id.org/gaia-x4plcaad/ontologies/service/v1/>
- sh: <http://www.w3.org/ns/shacl#>
- skos: <http://www.w3.org/2004/02/skos/core#>
- sosa: <http://www.w3.org/ns/sosa/>
- ssn: <http://www.w3.org/ns/ssn/>
- time: <http://www.w3.org/2006/time#>
- vann: <http://purl.org/vocab/vann/>
- void: <http://rdfs.org/ns/void#>
- wgs: <https://www.w3.org/2003/01/geo/wgs84_pos#>
- xml: <http://www.w3.org/XML/1998/namespace>
- xsd: <http://www.w3.org/2001/XMLSchema#>

### SHACL Properties

|Shape|Property prefix|Property|MinCount|MaxCount|Description|Datatype/NodeKind|Filename|
|---|---|---|---|---|---|---|---|
|ServiceShape|service|general|1|1|General object with properties for name and description.||service.shacl.ttl|
|ServiceShape|service|requiredFile|||Required file object with properties for urls and description.||service.shacl.ttl|
|ServiceShape|service|resultingFile|1||Resulting file object with properties for url and description.||service.shacl.ttl|
|RequiredFileShape|service|description|1|1|Human readable description of the required file.|<http://www.w3.org/2001/XMLSchema#string>|service.shacl.ttl|
|RequiredFileShape|service|specification||1|Uniform Resource Identifier (URI) to identify to a formal specification of the file.|<http://www.w3.org/2001/XMLSchema#anyURI>|service.shacl.ttl|
|RequiredFileShape|service|tooling||1|Uniform Resource Identifier (URI) to identify to a tool to help create the file.|<http://www.w3.org/2001/XMLSchema#anyURI>|service.shacl.ttl|
|ResultingFileShape|service|description|1|1|Human readable description.|<http://www.w3.org/2001/XMLSchema#string>|service.shacl.ttl|
|ResultingFileShape|service|specification|1|1|Uniform Resource Identifier (URI) to identify to a formal specification of the file.|<http://www.w3.org/2001/XMLSchema#anyURI>|service.shacl.ttl|
