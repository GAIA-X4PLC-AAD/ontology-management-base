# Variables of SHACL Files in this folder

## Prefixes

- simulated-sensor: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/simulated-sensor/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SimulatedSensorShape | simulated-sensor | sensorType | 1 | 1 | Perception and other relevant sensors for autonomous driving |  | simulated_sensor_shacl.ttl |
| SimulatedSensorShape | simulated-sensor | sensorIdentifier | 0 | 1 | Name/Identifier of the sensor in the simulator | <http://www.w3.org/2001/XMLSchema#string> | simulated_sensor_shacl.ttl |
| SimulatedSensorShape | simulated-sensor | mountingPosition | 0 | 1 | Possible mounting positions of the radar | <http://www.w3.org/2001/XMLSchema#string> | simulated_sensor_shacl.ttl |
| Radar | simulated-sensor | numberOfBeams | 0 |  | Number of beams sent by the radar sensor | <http://www.w3.org/2001/XMLSchema#integer> | simulated_sensor_shacl.ttl |
| Radar | simulated-sensor | distance | 0 | 1 | Covered distance or range in meters | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| Radar | simulated-sensor | fieldOfView | 0 | 1 | Depending on the simulator, either horizontal and vertical angles or horizontal FoV, upper FoV and lower FoV | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| Lidar | simulated-sensor | numberOfBeams | 0 |  | Number of beams sent by the lidar sensor | <http://www.w3.org/2001/XMLSchema#integer> | simulated_sensor_shacl.ttl |
| Lidar | simulated-sensor | distance | 0 | 1 | Covered distance or range in meters | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| Lidar | simulated-sensor | fieldOfView | 0 | 1 | Depending on the simulator, either horizontal and vertical angles or horizontal FoV, upper FoV and lower FoV | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| Camera | simulated-sensor | rgbFlag | 0 | 1 | If true, camera is RGB camera | <http://www.w3.org/2001/XMLSchema#boolean> | simulated_sensor_shacl.ttl |
| Camera | simulated-sensor | 3dflag | 0 | 1 | If true, camera is 3D camera | <http://www.w3.org/2001/XMLSchema#boolean> | simulated_sensor_shacl.ttl |
| Camera | simulated-sensor | detphFlag | 0 | 1 | If true, camera is depth camera | <http://www.w3.org/2001/XMLSchema#boolean> | simulated_sensor_shacl.ttl |
| Camera | simulated-sensor | fieldOfView | 0 | 1 | Depending on the simulator, either horizontal and vertical angles or horizontal FoV, upper FoV and lower FoV | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
