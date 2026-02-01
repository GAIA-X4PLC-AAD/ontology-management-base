# Properties of SHACL Files for service

## Prefixes

- service: <https://w3id.org/gaia-x4plcaad/ontologies/service/v1/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ServiceShape | service | general | 1 | 1 | General object with properties for name and description. |  | service.shacl.ttl |
| ServiceShape | service | requiredFile |  |  | Required file object with properties for urls and description. |  | service.shacl.ttl |
| ServiceShape | service | resultingFile | 1 |  | Resulting file object with properties for url and description. |  | service.shacl.ttl |
| RequiredFileShape | service | description | 1 | 1 | Human readable description of the required file. | <http://www.w3.org/2001/XMLSchema#string> | service.shacl.ttl |
| RequiredFileShape | service | specification |  | 1 | Uniform Resource Identifier (URI) to identify to a formal specification of the file. | <http://www.w3.org/2001/XMLSchema#anyURI> | service.shacl.ttl |
| RequiredFileShape | service | tooling |  | 1 | Uniform Resource Identifier (URI) to identify to a tool to help create the file. | <http://www.w3.org/2001/XMLSchema#anyURI> | service.shacl.ttl |
| ResultingFileShape | service | description | 1 | 1 | Human readable description. | <http://www.w3.org/2001/XMLSchema#string> | service.shacl.ttl |
| ResultingFileShape | service | specification | 1 | 1 | Uniform Resource Identifier (URI) to identify to a formal specification of the file. | <http://www.w3.org/2001/XMLSchema#anyURI> | service.shacl.ttl |
