# Properties of SHACL Files for example

## Prefixes

- example_ontology: <https://w3id.org/gaia-x4plcaad/ontologies/example/v1/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ExampleServiceOfferingShape | example_ontology | property1 | 1 |  | A description that describes property 1. | <http://www.w3.org/2001/XMLSchema#string> | example.shacl.ttl |
| ExampleServiceOfferingShape | example_ontology | property2 | 1 |  | A description that describes property 2. | <http://www.w3.org/2001/XMLSchema#string> | example.shacl.ttl |
| ExampleServiceOfferingShape | example_ontology | belongsTo | 1 |  | Identifier of related Self Description. | <http://www.w3.org/ns/shacl#IRI> | example.shacl.ttl |
| ExampleServiceOfferingShape | example_ontology | hasJunctionIntersection | 1 | 1 | Further description of the content of the scenario | <http://www.w3.org/ns/shacl#IRI> | example.shacl.ttl |
