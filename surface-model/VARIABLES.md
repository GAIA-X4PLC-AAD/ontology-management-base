# Variables of SHACL Files in this folder

## Prefixes

- surface-model: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/surface-model/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| surfaceModelShape | surface-model | general | 1 | 1 |  |  | surface-model_shacl.ttl |
| surfaceModelShape | surface-model | Format | 1 | 1 |  |  | surface-model_shacl.ttl |
| surfaceModelShape | surface-model | Data | 1 | 1 |  |  | surface-model_shacl.ttl |
| surfaceModelShape | surface-model | Quality | 1 | 1 |  |  | surface-model_shacl.ttl |
| surfaceModelShape | surface-model | Quantity | 1 | 1 |  |  | surface-model_shacl.ttl |
| surfaceModelShape | surface-model | Georeference | 1 | 1 |  |  | surface-model_shacl.ttl |
| DataShape | surface-model | dataType |  | 1 | Height, friction values, grey values | <http://www.w3.org/2001/XMLSchema#string> | surface-model_shacl.ttl |
| FormatShape | surface-model | formatType |  | 1 | Format type definition | <http://www.w3.org/2001/XMLSchema#string> | surface-model_shacl.ttl |
| FormatShape | surface-model | version |  | 1 | Version of data format | <http://www.w3.org/2001/XMLSchema#string> | surface-model_shacl.ttl |
| QualityShape | surface-model | resolutionLongitudinal |  | 1 | Longitudinal resolution  | <http://www.w3.org/2001/XMLSchema#float> | surface-model_shacl.ttl |
| QualityShape | surface-model | orientation |  | 1 | Heading at starting position | <http://www.w3.org/2001/XMLSchema#float> | surface-model_shacl.ttl |
| QualityShape | surface-model | platformExists |  | 1 | Existence of horizontal starting platform | <http://www.w3.org/2001/XMLSchema#boolean> | surface-model_shacl.ttl |
| QualityShape | surface-model | resolutionLateral |  | 1 | Lateral resolutions | <http://www.w3.org/2001/XMLSchema#float> | surface-model_shacl.ttl |
| QualityShape | surface-model | rampExists |  | 1 | Existence of smooth ramp from platform to road | <http://www.w3.org/2001/XMLSchema#boolean> | surface-model_shacl.ttl |
| QuantityShape | surface-model | mapDataField |  | 1 | Is projection system provided within the dataset | <http://www.w3.org/2001/XMLSchema#boolean> | surface-model_shacl.ttl |
| QuantityShape | surface-model | elevationRange | 0 | 1 | Range of elevation values | <http://www.w3.org/2001/XMLSchema#float> | surface-model_shacl.ttl |
| QuantityShape | surface-model | length |  | 1 | Road network length in km | <http://www.w3.org/2001/XMLSchema#float> | surface-model_shacl.ttl |
