# Variables of SHACL Files in this folder

## Prefixes

- service: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/service/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ServiceShape | service | general | 1 | 1 |  |  | service_shacl.ttl |
| ServiceShape | service | requiredFile |  |  |  |  | service_shacl.ttl |
| ServiceShape | service | resultingFile | 1 |  |  |  | service_shacl.ttl |
| RequiredFileShape | service | description | 1 | 1 | Human readable description of the required file | <http://www.w3.org/2001/XMLSchema#string> | service_shacl.ttl |
| RequiredFileShape | service | specification |  | 1 | Link to a formal specification of the file | <http://www.w3.org/2001/XMLSchema#anyURI> | service_shacl.ttl |
| RequiredFileShape | service | tooling |  | 1 | Link to a tool to help create the file | <http://www.w3.org/2001/XMLSchema#anyURI> | service_shacl.ttl |
| ResultingFileShape | service | description | 1 | 1 | Human readable description | <http://www.w3.org/2001/XMLSchema#string> | service_shacl.ttl |
| ResultingFileShape | service | specification | 1 | 1 | Link to specification | <http://www.w3.org/2001/XMLSchema#anyURI> | service_shacl.ttl |
