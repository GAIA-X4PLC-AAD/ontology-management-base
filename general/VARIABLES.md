# Variables of SHACL Files in this folder

## Prefixes

- general: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/general/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| GeneralShape | general | description | 1 | 1 | description object with property for name and description |  | general_shacl.ttl |
| GeneralShape | general | data | 1 | 1 | data object with property for size and record time |  | general_shacl.ttl |
| DescriptionShape | general | name | 1 | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | general_shacl.ttl |
| DescriptionShape | general | description | 1 | 1 | A free text description of the entity. | <http://www.w3.org/2001/XMLSchema#string> | general_shacl.ttl |
| DataShape | general | size | 1 | 1 | Size of the asset file(e.g. xodr, 3d model zip) to be downloaded in MB. | <http://www.w3.org/2001/XMLSchema#float> | general_shacl.ttl |
| DataShape | general | recordingTime |  | 1 | Time of data acquisition used to generate the asset, if partial measurement: oldest date | <http://www.w3.org/2001/XMLSchema#dateTime> | general_shacl.ttl |
| Range2DShape | general | max |  |  |  | <http://www.w3.org/2001/XMLSchema#float> | general_shacl.ttl |
| Range2DShape | general | min |  |  |  | <http://www.w3.org/2001/XMLSchema#float> | general_shacl.ttl |
