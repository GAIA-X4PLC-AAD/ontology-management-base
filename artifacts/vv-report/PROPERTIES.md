# Properties of SHACL Files for vv-report

## Prefixes

- vv-report: <https://w3id.org/gaia-x4plcaad/ontologies/vv-report/v2/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| VvReportShape | vv-report | general | 1 | 1 | General object with properties for descriptions, data, links, bundle. |  | vv-report.shacl.ttl |
| VvReportShape | vv-report | systemUnderTest | 1 | 1 | Uniform Resource Identifier (URI) to identify the tested artifact, like a simulation, model by location, name, or both. | <http://www.w3.org/2001/XMLSchema#anyURI> | vv-report.shacl.ttl |
| VvReportShape | vv-report | evaluations | 1 |  | A list of all measures carried out on the subject under test. |  | vv-report.shacl.ttl |
| EvaluationShape | vv-report | metric | 1 | 1 | The definition of the quality metric that has been used in this evaluation item. |  | vv-report.shacl.ttl |
| EvaluationShape | vv-report | inputData | 1 |  | The definition of a dataset that has been used as input to the quality metric. |  | vv-report.shacl.ttl |
| EvaluationShape | vv-report | parameters | 0 |  | A list of parameters that have been used to configure the quality metric and/or quality criterion. |  | vv-report.shacl.ttl |
| EvaluationShape | vv-report | result | 1 | 1 | The summary of the result of this evaluation item. |  | vv-report.shacl.ttl |
| EvaluationShape | vv-report | conceptSpecificData | 0 |  | Additional arbitrary V&V-concept specific data, to further describe the evaluation. |  | vv-report.shacl.ttl |
| MetricShape | vv-report | metricTitle | 1 | 1 | A meaningful name of this metric. | <http://www.w3.org/2001/XMLSchema#string> | vv-report.shacl.ttl |
| MetricShape | vv-report | metricDescription | 1 | 1 | A short description of what is tested within this quality metric. | <http://www.w3.org/2001/XMLSchema#string> | vv-report.shacl.ttl |
| MetricShape | vv-report | metricReference | 1 | 1 | Uniform Resource Identifier (URI) to identify the metric by location, name, or both. | <http://www.w3.org/2001/XMLSchema#anyURI> | vv-report.shacl.ttl |
| InputDataShape | vv-report | inputDescription | 1 | 1 | A short description for interpreting this input data element | <http://www.w3.org/2001/XMLSchema#string> | vv-report.shacl.ttl |
| InputDataShape | vv-report | inputReference | 1 | 1 | Uniform Resource Identifier (URI) to identify the utilized input data element by location, name, or both. | <http://www.w3.org/2001/XMLSchema#anyURI> | vv-report.shacl.ttl |
| ParameterShape | vv-report | parameterName | 1 | 1 | The formal name of the parameter, as it appears in the validation system | <http://www.w3.org/2001/XMLSchema#string> | vv-report.shacl.ttl |
| ParameterShape | vv-report | parameterDescription | 1 | 1 | A short description of the parameter in order to unambigously interpret it. | <http://www.w3.org/2001/XMLSchema#string> | vv-report.shacl.ttl |
| ParameterShape | vv-report | parameterValue | 1 | 1 | The value of the parameter. |  | vv-report.shacl.ttl |
| ResultShape | vv-report | resultTestPassed | 1 | 1 | Statement if the test has been passed or not. | <http://www.w3.org/2001/XMLSchema#boolean> | vv-report.shacl.ttl |
| ResultShape | vv-report | resultLog | 0 |  | Additional information about the test result, e.g., why it has failed. | <http://www.w3.org/2001/XMLSchema#string> | vv-report.shacl.ttl |
| ResultShape | vv-report | resultVerifiable | 1 | 1 | Information if the result can be verified by a third party. | <http://www.w3.org/2001/XMLSchema#boolean> | vv-report.shacl.ttl |
| ResultShape | vv-report | resultVerification | 0 | 1 | The necessary attributes to carry out verification of the result by a third party. |  | vv-report.shacl.ttl |
| ResultVerificationShape | vv-report | resultVerificationDescription | 1 | 1 | A short description of how the result can be verified with the given reference. | <http://www.w3.org/2001/XMLSchema#string> | vv-report.shacl.ttl |
| ResultVerificationShape | vv-report | resultVerificationReference | 1 |  | Uniform Resource Identifier (URI) to identify the reference used to verify the result of this evalation by location, name, or both. | <http://www.w3.org/2001/XMLSchema#anyURI> | vv-report.shacl.ttl |
