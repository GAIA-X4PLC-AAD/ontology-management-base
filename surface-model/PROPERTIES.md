# Properties of SHACL Files in this folder

## Prefixes

- surface-model: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/surface-model/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SurfaceModelShape | surface-model | general | 1 | 1 | General properties for defining a surface-model asset, including format, data, quantity, and quality attributes. |  | surface-model_shacl.ttl |
| SurfaceModelShape | surface-model | format | 1 | 1 | Contains properties that describe the format of the surface-model asset. |  | surface-model_shacl.ttl |
| SurfaceModelShape | surface-model | data | 1 | 1 | Contains properties that describe the data type of the surface-model asset. |  | surface-model_shacl.ttl |
| SurfaceModelShape | surface-model | quality | 1 | 1 | Contains properties that describe the accuracy of the surface-model asset. |  | surface-model_shacl.ttl |
| SurfaceModelShape | surface-model | quantity | 1 | 1 | Contains properties that describe the quantity of the surface-model asset. |  | surface-model_shacl.ttl |
| SurfaceModelShape | surface-model | georeference | 1 | 1 | General properties for defining the location and projection of the asset. |  | surface-model_shacl.ttl |
| DataShape | surface-model | dataType |  | 1 | Specifies the data type (e.g., height, friction) used in the surface-model asset. | <http://www.w3.org/2001/XMLSchema#string> | surface-model_shacl.ttl |
| FormatShape | surface-model | formatType |  | 1 | Defines the data type of the surface-model asset. | <http://www.w3.org/2001/XMLSchema#string> | surface-model_shacl.ttl |
| FormatShape | surface-model | version |  | 1 | Defines the version of the surface-model asset's data type. | <http://www.w3.org/2001/XMLSchema#string> | surface-model_shacl.ttl |
| QualityShape | surface-model | resolutionLongitudinal |  | 1 | Specifies the longitudinal resolution (s) in metres. | <http://www.w3.org/2001/XMLSchema#float> | surface-model_shacl.ttl |
| QualityShape | surface-model | orientation |  | 1 | Specifies the alignment at the starting position in radians. | <http://www.w3.org/2001/XMLSchema#float> | surface-model_shacl.ttl |
| QualityShape | surface-model | platformExists |  | 1 | Indicates whether a horizontal start platform exists. | <http://www.w3.org/2001/XMLSchema#boolean> | surface-model_shacl.ttl |
| QualityShape | surface-model | resolutionLateral |  | 1 | Specifies the lateral resolution (t) in metres. | <http://www.w3.org/2001/XMLSchema#float> | surface-model_shacl.ttl |
| QualityShape | surface-model | rampExists |  | 1 | Indicates whether there is a smooth ramp from the platform to the road. | <http://www.w3.org/2001/XMLSchema#boolean> | surface-model_shacl.ttl |
| QuantityShape | surface-model | mapDataField |  | 1 | Indicates whether the projection system is included in the dataset. | <http://www.w3.org/2001/XMLSchema#boolean> | surface-model_shacl.ttl |
| QuantityShape | surface-model | elevationRange | 0 | 1 | Indicates the difference between the maximum and minimum elevation values in metres. | <http://www.w3.org/2001/XMLSchema#float> | surface-model_shacl.ttl |
| QuantityShape | surface-model | length |  | 1 | Defines the total length of all elements in kilometres. | <http://www.w3.org/2001/XMLSchema#float> | surface-model_shacl.ttl |
