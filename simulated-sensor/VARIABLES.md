# Variables of SHACL Files in this folder

## Prefixes

- simulated-sensor: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/simulated-sensor/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SimulatedSensorShape | simulated-sensor | sensorType | 1 | 1 | Perception and other relevant sensors for autonomous driving |  | simulated-sensor_shacl.ttl |
| SimulatedSensorShape | simulated-sensor | sensorIdentifier | 0 | 1 | Name/Identifier of the sensor in the simulator | <http://www.w3.org/2001/XMLSchema#string> | simulated-sensor_shacl.ttl |
| SimulatedSensorShape | simulated-sensor | mountingPosition | 0 | 1 | Possible mounting positions of the radar | <http://www.w3.org/2001/XMLSchema#string> | simulated-sensor_shacl.ttl |
| RadarShape | simulated-sensor | numberOfBeams | 0 | 1 | Number of beams sent by the radar sensor | <http://www.w3.org/2001/XMLSchema#integer> | simulated-sensor_shacl.ttl |
| RadarShape | simulated-sensor | distance | 0 | 1 | Covered distance or range in meters | <http://www.w3.org/2001/XMLSchema#float> | simulated-sensor_shacl.ttl |
| LidarShape | simulated-sensor | numberOfBeams | 0 | 1 | Number of beams sent by the lidar sensor | <http://www.w3.org/2001/XMLSchema#integer> | simulated-sensor_shacl.ttl |
| LidarShape | simulated-sensor | distance | 0 | 1 | Covered distance or range in meters | <http://www.w3.org/2001/XMLSchema#float> | simulated-sensor_shacl.ttl |
| CameraShape | simulated-sensor | rgbFlag | 0 | 1 | If true, camera is RGB camera | <http://www.w3.org/2001/XMLSchema#boolean> | simulated-sensor_shacl.ttl |
| CameraShape | simulated-sensor | 3dflag | 0 | 1 | If true, camera is 3D camera | <http://www.w3.org/2001/XMLSchema#boolean> | simulated-sensor_shacl.ttl |
| CameraShape | simulated-sensor | depthFlag | 0 | 1 | If true, camera is depth camera | <http://www.w3.org/2001/XMLSchema#boolean> | simulated-sensor_shacl.ttl |
| FieldOfViewShape | simulated-sensor | fovAngle1 | 1 | 1 | FoV angle 1 (mandatory if FoV attribute is used) | <http://www.w3.org/2001/XMLSchema#float> | simulated-sensor_shacl.ttl |
| FieldOfViewShape | simulated-sensor | fovAngle2 | 0 | 1 | FoV angle 2 (optional, depending on simulator and sensor type) | <http://www.w3.org/2001/XMLSchema#float> | simulated-sensor_shacl.ttl |
| FieldOfViewShape | simulated-sensor | fovAngle3 | 0 | 1 | FoV angle 3 (optional, depending on simulator and sensor type) | <http://www.w3.org/2001/XMLSchema#float> | simulated-sensor_shacl.ttl |
