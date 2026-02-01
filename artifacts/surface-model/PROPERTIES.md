# Properties of SHACL Files for surface-model

## Prefixes

- surface-model: <https://w3id.org/ascs-ev/envited-x/surface-model/v6/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SurfaceModelShape | surface-model | hasDataResource | 1 | 1 |  |  | surface-model.shacl.ttl |
| SurfaceModelShape | surface-model | hasDataResourceExtension | 1 | 1 |  |  | surface-model.shacl.ttl |
| SurfaceModelShape | surface-model | hasManifest | 1 | 1 |  |  | surface-model.shacl.ttl |
| DataResourceExtensionShape | surface-model | hasContent | 1 | 1 | Attributes describing the content type of the surface model. |  | surface-model.shacl.ttl |
| DataResourceExtensionShape | surface-model | hasFormat | 1 | 1 | File format details of the surface model. |  | surface-model.shacl.ttl |
| DataResourceExtensionShape | surface-model | hasQuality | 1 | 1 | Quality metrics of the surface model. |  | surface-model.shacl.ttl |
| DataResourceExtensionShape | surface-model | hasQuantity | 1 | 1 | Quantitative metrics describing the surface model. |  | surface-model.shacl.ttl |
| DataResourceExtensionShape | surface-model | hasGeoreference | 1 | 1 | Georeferencing information for the surface model. |  | surface-model.shacl.ttl |
| ContentShape | surface-model | contentType |  | 1 | Specifies the content type (e.g., height, friction) used in the surface-model asset. | <http://www.w3.org/2001/XMLSchema#string> | surface-model.shacl.ttl |
| FormatShape | surface-model | formatType |  | 1 | Defines the format type of the surface model asset. |  | surface-model.shacl.ttl |
| FormatShape | surface-model | version |  | 1 | Defines the version of the surface model's format. | <http://www.w3.org/2001/XMLSchema#string> | surface-model.shacl.ttl |
| QualityShape | surface-model | resolutionLongitudinal |  | 1 | Specifies the longitudinal resolution (s) in meters. | <http://www.w3.org/2001/XMLSchema#float> | surface-model.shacl.ttl |
| QualityShape | surface-model | orientation |  | 1 | Specifies the alignment at the starting position in radians. | <http://www.w3.org/2001/XMLSchema#float> | surface-model.shacl.ttl |
| QualityShape | surface-model | platformExists |  | 1 | Indicates whether a horizontal start platform exists. | <http://www.w3.org/2001/XMLSchema#boolean> | surface-model.shacl.ttl |
| QualityShape | surface-model | rampExists |  | 1 | Indicates whether there is a smooth ramp from the platform to the road. | <http://www.w3.org/2001/XMLSchema#boolean> | surface-model.shacl.ttl |
| QualityShape | surface-model | resolutionLateral |  | 1 | Specifies the lateral resolution (t) in meters. | <http://www.w3.org/2001/XMLSchema#float> | surface-model.shacl.ttl |
| QuantityShape | surface-model | mapDataField |  | 1 | Indicates whether the projection system is included in the dataset. | <http://www.w3.org/2001/XMLSchema#boolean> | surface-model.shacl.ttl |
| QuantityShape | surface-model | elevationRange |  | 1 | Indicates the difference between the maximum and minimum elevation values in meters. | <http://www.w3.org/2001/XMLSchema#float> | surface-model.shacl.ttl |
| QuantityShape | surface-model | length |  | 1 | Defines the total length of all elements in kilometers. | <http://www.w3.org/2001/XMLSchema#float> | surface-model.shacl.ttl |
