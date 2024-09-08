# Variables of SHACL Files in this folder

## Prefixes

- general: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/general/>
- gx: <https://registry.lab.gaia-x.eu/development/api/trusted-shape-registry/v1/shapes/jsonld/trustframework#>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| GeneralShape | general | description | 1 | 1 | description object with property for name and description |  | general_shacl.ttl |
| GeneralShape | general | data | 1 | 1 | data object with property for size, id and record time |  | general_shacl.ttl |
| GeneralShape | general | links | 1 | 1 | link object with links to asset and media files |  | general_shacl.ttl |
| GeneralShape | general | bundleData | 1 | 1 | bundle object with links to required and optional related data |  | general_shacl.ttl |
| DescriptionShape | gx | name | 1 | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | general_shacl.ttl |
| DescriptionShape | gx | description | 1 | 1 | A free text description of the entity. | <http://www.w3.org/2001/XMLSchema#string> | general_shacl.ttl |
| DataShape | general | size | 1 | 1 | Size of the file to be downloaded in MB. | <http://www.w3.org/2001/XMLSchema#float> | general_shacl.ttl |
| DataShape | general | contractId | 1 | 1 | Contract information in regards to the data exchange component. | <http://www.w3.org/2001/XMLSchema#string> | general_shacl.ttl |
| DataShape | general | recordingTime |  | 1 | Time of data acquisition used to generate the asset, if partial measurement: oldest date | <http://www.w3.org/2001/XMLSchema#dateTime> | general_shacl.ttl |
| BundleDataShape | general | requiredData |  |  | Reference to required assets |  | general_shacl.ttl |
| BundleDataShape | general | relatedData |  |  | Reference to optional related assets |  | general_shacl.ttl |
| LinksShape | general | media |  |  | Reference to media data |  | general_shacl.ttl |
| LinksShape | general | data | 1 | 1 | Reference to the data asset as url/uri of the EDC |  | general_shacl.ttl |
| LinkShape | general | type | 1 | 1 | Choose type of link. | <http://www.w3.org/2001/XMLSchema#string> | general_shacl.ttl |
| LinkShape | general | url | 1 | 1 | Enter link as URL or DID. | <http://www.w3.org/2001/XMLSchema#anyURI> | general_shacl.ttl |
| Range2DShape | general | max |  |  |  | <http://www.w3.org/2001/XMLSchema#float> | general_shacl.ttl |
| Range2DShape | general | min |  |  |  | <http://www.w3.org/2001/XMLSchema#float> | general_shacl.ttl |
