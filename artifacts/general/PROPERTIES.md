# Properties of SHACL Files for general

## Prefixes

- general: <https://w3id.org/gaia-x4plcaad/ontologies/general/v3/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| GeneralShape | general | description | 1 | 1 | General text based description of the simulation asset. |  | general.shacl.ttl |
| GeneralShape | general | data | 1 | 1 | Data properties of the simulation asset. |  | general.shacl.ttl |
| DescriptionShape | general | name | 1 | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | general.shacl.ttl |
| DescriptionShape | general | description | 1 | 1 | A free text description of the entity. | <http://www.w3.org/2001/XMLSchema#string> | general.shacl.ttl |
| DataShape | general | size | 1 | 1 | Size of the data file(s) (e.g. xodr, 3d model zip) to be downloaded in MB (megabyte). | <http://www.w3.org/2001/XMLSchema#float> | general.shacl.ttl |
| DataShape | general | recordingTime |  | 1 | Time of data acquisition used to generate the asset, if partial measurement: oldest date | <http://www.w3.org/2001/XMLSchema#dateTime> | general.shacl.ttl |
