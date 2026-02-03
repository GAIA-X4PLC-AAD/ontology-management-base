## automotive-simulator Properties

### Class Diagram

```mermaid
classDiagram
class Class_definition_for_AutomotiveSimulator
```

### Class Hierarchy

- Class definition for AutomotiveSimulator (https://w3id.org/gaia-x4plcaad/ontologies/automotive-simulator/v1/AutomotiveSimulator)

### Class Definitions

|Class|IRI|Description|Parents|
|---|---|---|---|
|Class definition for AutomotiveSimulator|https://w3id.org/gaia-x4plcaad/ontologies/automotive-simulator/v1/AutomotiveSimulator|An implementation of an automotive simulator.|DataResource|

## Prefixes

- automotive-simulator: <https://w3id.org/gaia-x4plcaad/ontologies/automotive-simulator/v1/>
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
- simulated-sensor: <https://w3id.org/gaia-x4plcaad/ontologies/simulated-sensor/v2/>
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
|AutomotiveSimulatorShape|automotive-simulator|general|1|1|General object with properties for description and data.||automotive-simulator.shacl.ttl|
|AutomotiveSimulatorShape|automotive-simulator|simulatorMake|1|1|Make/Type of automotive simulator.|<http://www.w3.org/2001/XMLSchema#string>|automotive-simulator.shacl.ttl|
|AutomotiveSimulatorShape|automotive-simulator|softwareVersion|1|1|Sofware version of the simulator.|<http://www.w3.org/2001/XMLSchema#string>|automotive-simulator.shacl.ttl|
|AutomotiveSimulatorShape|automotive-simulator|sensorFailureFlag|1|1|If true, the simulator supports the simulation of sensor failures.|<http://www.w3.org/2001/XMLSchema#boolean>|automotive-simulator.shacl.ttl|
|AutomotiveSimulatorShape|automotive-simulator|sensorAttackFlag|1|1|If true, the simulator supports the simulation of sensor attacks.|<http://www.w3.org/2001/XMLSchema#boolean>|automotive-simulator.shacl.ttl|
|AutomotiveSimulatorShape|automotive-simulator|scenarioDefinition|0||Description language for defining driving scenarios supported by the simulator.|<http://www.w3.org/2001/XMLSchema#string>|automotive-simulator.shacl.ttl|
|AutomotiveSimulatorShape|automotive-simulator|interface|0||Communcation interface provided by the simulator to communicate with different assets (e.g. agents/vehicle implementations).|<http://www.w3.org/2001/XMLSchema#string>|automotive-simulator.shacl.ttl|
|AutomotiveSimulatorShape|simulated-sensor|simulatedSensor|0||Type and kinds of sensors that are natively included in the simulator.||automotive-simulator.shacl.ttl|
