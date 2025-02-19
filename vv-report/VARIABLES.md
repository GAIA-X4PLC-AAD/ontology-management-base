# Variables of SHACL Files in this folder

## Prefixes

- vv-report: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/vv-report/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| VvReportShape | vv-report | general | 1 | 1 | general object with properties for descriptions, data, links, bundle |  | vv-report_shacl.ttl |
| VvReportShape | vv-report | systemUnderTest | 1 | 1 | A unique reference or identifier to the tested artifact, like a simulation model | <http://www.w3.org/2001/XMLSchema#anyURI> | vv-report_shacl.ttl |
| VvReportShape | vv-report | evaluations | 1 |  | A list of all measures carried out on the subject under test |  | vv-report_shacl.ttl |
| EvaluationShape | vv-report | metric | 1 | 1 | The definition of the quality metric that has been used in this evaluation item |  | vv-report_shacl.ttl |
| EvaluationShape | vv-report | inputData | 1 |  | The definition of a dataset that has been used as input to the quality metric |  | vv-report_shacl.ttl |
| EvaluationShape | vv-report | result | 1 | 1 | The summary of the result of this evaluation item |  | vv-report_shacl.ttl |
| EvaluationShape | vv-report | conceptSpecificData | 0 |  | Additional arbitrary V&V-concept specific data, to further describe the evaluation |  | vv-report_shacl.ttl |
| MetricShape | vv-report | metricTitle | 1 | 1 | A meaningful name of this metric | <http://www.w3.org/2001/XMLSchema#string> | vv-report_shacl.ttl |
| MetricShape | vv-report | metricDescription | 1 | 1 | A short description of what is tested within this quality metric. | <http://www.w3.org/2001/XMLSchema#string> | vv-report_shacl.ttl |
| MetricShape | vv-report | metricReference | 1 | 1 | A unique reference or identifier to identify the metric, e.g. an URL | <http://www.w3.org/2001/XMLSchema#anyURI> | vv-report_shacl.ttl |
| InputDataShape | vv-report | inputDescription | 1 | 1 | A short description for interpreting this input data element | <http://www.w3.org/2001/XMLSchema#string> | vv-report_shacl.ttl |
| InputDataShape | vv-report | inputReference | 1 | 1 | A unique reference or identifier to identify the utilized input data element | <http://www.w3.org/2001/XMLSchema#anyURI> | vv-report_shacl.ttl |
| ResultShape | vv-report | resultTestPassed | 1 | 1 | Statement if the test has been passed or not | <http://www.w3.org/2001/XMLSchema#boolean> | vv-report_shacl.ttl |
| ResultShape | vv-report | resultLog | 0 |  | Additional information about the test result, e.g., why it has failed | <http://www.w3.org/2001/XMLSchema#string> | vv-report_shacl.ttl |
| ResultShape | vv-report | resultVerifiable | 1 | 1 | Information if the result can be verified by a third party | <http://www.w3.org/2001/XMLSchema#boolean> | vv-report_shacl.ttl |
| ResultShape | vv-report | resultVerification | 0 | 1 | The necessary attributes to carry out verification of the result by a third party |  | vv-report_shacl.ttl |
| ResultVerificationShape | vv-report | resultVerificationDescription | 1 | 1 | A short description of how the result can be verified with the given reference |  | vv-report_shacl.ttl |
| ResultVerificationShape | vv-report | resultVerificationReference | 1 |  | A reference used to verify the result of this evalation | <http://www.w3.org/2001/XMLSchema#anyURI> | vv-report_shacl.ttl |
