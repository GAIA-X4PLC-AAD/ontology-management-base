# Properties of SHACL Files in this folder

## Prefixes

- description_ontology: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/examples/description_ontology/>
- example_ontology: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/examples/example_ontology/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ExampleServiceOfferingShape | description_ontology | property1 | 1 |  | A description that describes property 1. | <http://www.w3.org/2001/XMLSchema#string> | description_shacl.ttl |
| ExampleServiceOfferingShape | description_ontology | property2 | 1 |  | A description that describes property 2. | <http://www.w3.org/2001/XMLSchema#string> | description_shacl.ttl |
| ExampleServiceOfferingShape | description_ontology | belongsTo | 1 |  | Identifier of related Self Description. | <http://www.w3.org/ns/shacl#IRI> | description_shacl.ttl |
| ExampleServiceOfferingShape | description_ontology | hasJunctionIntersection | 1 | 1 | Further description of the content of the scenario | <http://www.w3.org/ns/shacl#IRI> | description_shacl.ttl |
| ExampleServiceOfferingShape | example_ontology | property1 | 1 |  | A description that describes property 1. | <http://www.w3.org/2001/XMLSchema#string> | example_shacl.ttl |
| ExampleServiceOfferingShape | example_ontology | property2 | 1 |  | A description that describes property 2. | <http://www.w3.org/2001/XMLSchema#string> | example_shacl.ttl |
| ExampleServiceOfferingShape | example_ontology | belongsTo | 1 |  | Identifier of related Self Description. | <http://www.w3.org/ns/shacl#IRI> | example_shacl.ttl |
| ExampleServiceOfferingShape | example_ontology | hasJunctionIntersection | 1 | 1 | Further description of the content of the scenario | <http://www.w3.org/ns/shacl#IRI> | example_shacl.ttl |
