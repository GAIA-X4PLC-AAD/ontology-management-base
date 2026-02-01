# Properties of SHACL Files for description

## Prefixes

- description_ontology: <https://w3id.org/gaia-x4plcaad/ontologies/description/v1/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ExampleServiceOfferingShape | description_ontology | property1 | 1 |  | A description that describes property 1. | <http://www.w3.org/2001/XMLSchema#string> | description.shacl.ttl |
| ExampleServiceOfferingShape | description_ontology | property2 | 1 |  | A description that describes property 2. | <http://www.w3.org/2001/XMLSchema#string> | description.shacl.ttl |
| ExampleServiceOfferingShape | description_ontology | belongsTo | 1 |  | Identifier of related Self Description. | <http://www.w3.org/ns/shacl#IRI> | description.shacl.ttl |
| ExampleServiceOfferingShape | description_ontology | hasJunctionIntersection | 1 | 1 | Further description of the content of the scenario | <http://www.w3.org/ns/shacl#IRI> | description.shacl.ttl |
