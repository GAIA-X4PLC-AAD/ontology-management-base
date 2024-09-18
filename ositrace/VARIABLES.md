# Variables of SHACL Files in this folder

## Prefixes

- ositrace: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/ositrace/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| OSITraceShape | ositrace | general | 1 | 1 |  |  | ositrace_shacl.ttl |
| OSITraceShape | ositrace | format | 1 | 1 |  |  | ositrace_shacl.ttl |
| OSITraceShape | ositrace | content | 1 | 1 |  |  | ositrace_shacl.ttl |
| OSITraceShape | ositrace | quality | 1 | 1 |  |  | ositrace_shacl.ttl |
| OSITraceShape | ositrace | quantity | 1 | 1 |  |  | ositrace_shacl.ttl |
| OSITraceShape | ositrace | dataSource | 1 | 1 |  |  | ositrace_shacl.ttl |
| OSITraceShape | ositrace | georeference | 1 | 1 |  |  | ositrace_shacl.ttl |
| ContentShape | ositrace | roadTypes |  |  | Covered/used road types, defined over ODR element t_road_type, see ODR spec section 8.3 | <http://www.w3.org/2001/XMLSchema#string> | ositrace_shacl.ttl |
| ContentShape | ositrace | laneTypes |  |  | Covered lane types, see ODR spec section 9.5.3. | <http://www.w3.org/2001/XMLSchema#string> | ositrace_shacl.ttl |
| ContentShape | ositrace | levelOfDetail |  |  | Covered object classes, see ODR spec section 11 | <http://www.w3.org/2001/XMLSchema#string> | ositrace_shacl.ttl |
| ContentShape | ositrace | trafficDirection |  | 1 | Traffic direction, i.e. right-hand or left-hand traffic | <http://www.w3.org/2001/XMLSchema#string> | ositrace_shacl.ttl |
| ContentShape | ositrace | granularity | 1 |  | Level of granularity of sensor data | <http://www.w3.org/2001/XMLSchema#string> | ositrace_shacl.ttl |
| ContentShape | ositrace | scenarioIdentifier |  |  | Identifier of scenario performed in the trace file | <http://www.w3.org/2001/XMLSchema#string> | ositrace_shacl.ttl |
| ContentShape | ositrace | startTime | 1 | 1 | Exact start timestamp of the recorded trace | <http://www.w3.org/2001/XMLSchema#dateTimeStamp> | ositrace_shacl.ttl |
| ContentShape | ositrace | stopTime | 1 | 1 | Exact stop timestamp of the recorded trace | <http://www.w3.org/2001/XMLSchema#dateTimeStamp> | ositrace_shacl.ttl |
| ContentShape | ositrace | hostMovingObject |  | 1 | Host moving object in trace file |  | ositrace_shacl.ttl |
| ContentShape | ositrace | targetMovingObject |  |  | Target moving object in trace file |  | ositrace_shacl.ttl |
| ContentShape | ositrace | event |  |  | Description of event of interest in trace file |  | ositrace_shacl.ttl |
| DataSourceShape | ositrace | measurementSystem |  | 1 | Main acquisition device | <http://www.w3.org/2001/XMLSchema#string> | ositrace_shacl.ttl |
| DataSourceShape | ositrace | usedDataSources |  |  | Basic data for the creation of the trace  | <http://www.w3.org/2001/XMLSchema#string> | ositrace_shacl.ttl |
| FormatShape | ositrace | version |  | 1 | Version of data format | <http://www.w3.org/2001/XMLSchema#string> | ositrace_shacl.ttl |
| FormatShape | ositrace | formatType |  | 1 | Format type definition | <http://www.w3.org/2001/XMLSchema#string> | ositrace_shacl.ttl |
| QualityShape | ositrace | accuracySignals | 0 | 1 | Accuracy of traffic relevant objects, signs and signals | <http://www.w3.org/2001/XMLSchema#float> | ositrace_shacl.ttl |
| QualityShape | ositrace | accuracyObjects | 0 | 1 | Accuracy of objects in the traffic space, which do not directly affect the traffic | <http://www.w3.org/2001/XMLSchema#float> | ositrace_shacl.ttl |
| QualityShape | ositrace | accuracyLaneModelHeight | 0 | 1 | Accuracy lane modell height | <http://www.w3.org/2001/XMLSchema#float> | ositrace_shacl.ttl |
| QualityShape | ositrace | precision | 0 | 1 | Precision of measured road network (relative accuracy) | <http://www.w3.org/2001/XMLSchema#float> | ositrace_shacl.ttl |
| QualityShape | ositrace | accuracyLaneModel2d | 0 | 1 | Accuracy of lane modell 2d | <http://www.w3.org/2001/XMLSchema#float> | ositrace_shacl.ttl |
| QualityShape | ositrace | calibration | 0 | 1 | Description of any calibration steps performed prior to measurement | <http://www.w3.org/2001/XMLSchema#string> | ositrace_shacl.ttl |
| QuantityShape | ositrace | numberFrames |  | 1 | Number of frames/messages in the trace file | <http://www.w3.org/2001/XMLSchema#unsignedInt> | ositrace_shacl.ttl |
| MovingObjectShape | ositrace | identifier |  |  | Moving object identifier in trace file | <http://www.w3.org/2001/XMLSchema#unsignedLong> | ositrace_shacl.ttl |
| MovingObjectShape | ositrace | description |  | 1 | Description of moving object in the trace file | <http://www.w3.org/2001/XMLSchema#string> | ositrace_shacl.ttl |
| EventShape | ositrace | time | 1 | 1 | Exact timestamp of the event in the recorded trace | <http://www.w3.org/2001/XMLSchema#dateTimeStamp> | ositrace_shacl.ttl |
| EventShape | ositrace | tag |  |  | Unique tag of the event in trace file | <http://www.w3.org/2001/XMLSchema#string> | ositrace_shacl.ttl |
| EventShape | ositrace | description |  | 1 | Description of event in the trace file | <http://www.w3.org/2001/XMLSchema#string> | ositrace_shacl.ttl |
