# Variables of SHACL Files in this folder

## Prefixes

- simulated-sensor: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/simulated-sensor/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SimulatedSensorShape | simulated-sensor | sensorType | 1 | 1 | Type of Sensor used in the simulation | <http://www.w3.org/2001/XMLSchema#string> | simulated_sensor_shacl.ttl |
| SimulatedSensorShape | simulated-sensor | mountingPosition | 1 | 1 | Position of the sensor on the vehicle. The precise coordinates are calculated in the world-coordinate system. Note that any back options will also induce a rotation of the sensor so that its field of view covers the vehicle rear. | <http://www.w3.org/2001/XMLSchema#string> | simulated_sensor_shacl.ttl |
| SimulatedSensorShape | simulated-sensor | numberOfBeams | 1 | 1 | Number of beams the radar or lidar sensor shall send | <http://www.w3.org/2001/XMLSchema#integer> | simulated_sensor_shacl.ttl |
| SimulatedSensorShape | simulated-sensor | distance | 1 | 1 | Covered distance or range in meters | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| SimulatedSensorShape | simulated-sensor | fieldOfView | 3 | 3 | For RADAR: horizontal and vertical angles; For LIDAR: horizontal FoV, upper FoV, lower FoV | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| SimulatedSensorShape | simulated-sensor | manipulationModel | 1 |  | Manipulation (failure and attack patterns) model(s) of the sensor. Each definition will lead to another independent simulation. Note that always one reference simulation with a non-manipulated sensor is performed. |  | simulated_sensor_shacl.ttl |
| PackageLossShape | simulated-sensor | start | 1 | 1 | First occurrence of the pattern of manipulation in the simulation in seconds | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| PackageLossShape | simulated-sensor | interval | 1 | 1 | Interval of re-occurrence of the manipulation pattern in seconds | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| PackageLossShape | simulated-sensor | duration | 1 | 1 | Time the pattern of manipulation is active in seconds | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| PackageLossShape | simulated-sensor | intervalDegradation | 0 | 1 | Change/worsening (decrease) of the time of re-occurrence | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| PackageLossShape | simulated-sensor | durationDegradation | 0 | 1 | Change/worsening (decrease) of the duration between re-ocurrences | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| PackageDelayShape | simulated-sensor | start | 1 | 1 | First occurrence of the pattern of manipulation in the simulation in seconds | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| PackageDelayShape | simulated-sensor | interval | 1 | 1 | Interval of re-occurrence of the manipulation pattern in seconds | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| PackageDelayShape | simulated-sensor | delaySize | 0 | 1 | Occupancy of the ringbuffer at start of the simulation | <http://www.w3.org/2001/XMLSchema#integer> | simulated_sensor_shacl.ttl |
| PackageDelayShape | simulated-sensor | degradationSize | 1 | 1 | Amount of packages that are delayed | <http://www.w3.org/2001/XMLSchema#integer> | simulated_sensor_shacl.ttl |
| PackageDelayShape | simulated-sensor | ringBufferMaxUseSize | 0 | 1 | Amount of raw data packages that fit into the ringbuffer before it overflows and causes package loss | <http://www.w3.org/2001/XMLSchema#integer> | simulated_sensor_shacl.ttl |
| DetectionPointShiftShape | simulated-sensor | start | 1 | 1 | First occurrence of the pattern of manipulation in the simulation in seconds | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| DetectionPointShiftShape | simulated-sensor | interval | 1 | 1 | Interval of re-occurrence of the manipulation pattern in seconds | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| DetectionPointShiftShape | simulated-sensor | duration | 1 | 1 | Time the pattern of manipulation is active in seconds | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| DetectionPointShiftShape | simulated-sensor | intervalDegradation | 0 | 1 | Change/worsening (decrease) of the time of re-occurrence | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| DetectionPointShiftShape | simulated-sensor | durationDegradation | 0 | 1 | Change/worsening (decrease) of the duration between re-ocurrences | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| DetectionPointShiftShape | simulated-sensor | maxDepthDisturbance | 0 | 1 | Maximal shifting distance between the sensor and detection point | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| DetectionPointShiftShape | simulated-sensor | maxAzimuthDisturbance | 0 | 1 | Maximal shifting Azimuth between the sensor and detection point | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| DetectionPointShiftShape | simulated-sensor | maxAltitudeDisturbance | 0 | 1 | Maximal shifting Altitude between the sensor and detection point | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| DetectionPointShiftShape | simulated-sensor | distribution | 1 | 1 | Kind of distrbution used to calculate the detection point shift | <http://www.w3.org/2001/XMLSchema#integer> | simulated_sensor_shacl.ttl |
| VelocityPointShiftShape | simulated-sensor | start | 1 | 1 | First occurrence of the pattern of manipulation in the simulation in seconds | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| VelocityPointShiftShape | simulated-sensor | interval | 1 | 1 | Interval of re-occurrence of the manipulation pattern in seconds | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| VelocityPointShiftShape | simulated-sensor | duration | 1 | 1 | Time the pattern of manipulation is active in seconds | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| VelocityPointShiftShape | simulated-sensor | intervalDegradation | 0 | 1 | Change/worsening (decrease) of the time of re-occurrence | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| VelocityPointShiftShape | simulated-sensor | durationDegradation | 0 | 1 | Change/worsening (decrease) of the duration between re-ocurrences | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| VelocityPointShiftShape | simulated-sensor | maxVelocityDisturbance | 1 | 1 | Maximal shift/change of the velocity | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| VelocityPointShiftShape | simulated-sensor | distribution | 1 | 1 | Kind of distrbution used to calculate the velocity shift | <http://www.w3.org/2001/XMLSchema#integer> | simulated_sensor_shacl.ttl |
| RangeReductionShape | simulated-sensor | start | 1 | 1 | First occurrence of the pattern of manipulation in the simulation in seconds | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| RangeReductionShape | simulated-sensor | interval | 1 | 1 | Interval of re-occurrence of the manipulation pattern in seconds | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| RangeReductionShape | simulated-sensor | duration | 1 | 1 | Time the pattern of manipulation is active in seconds | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| RangeReductionShape | simulated-sensor | intervalDegradation | 0 | 1 | Change/worsening (decrease) of the time of re-occurrence | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| RangeReductionShape | simulated-sensor | durationDegradation | 0 | 1 | Change/worsening (decrease) of the duration between re-ocurrences | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| RangeReductionShape | simulated-sensor | rangeReductionValue | 1 | 1 | Distance of the range reduction in meters | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| DetectNonExistingPointsShape | simulated-sensor | start | 1 | 1 | First occurrence of the pattern of manipulation in the simulation in seconds | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| DetectNonExistingPointsShape | simulated-sensor | interval | 1 | 1 | Interval of re-occurrence of the manipulation pattern in seconds | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| DetectNonExistingPointsShape | simulated-sensor | duration | 1 | 1 | Time the pattern of manipulation is active in seconds | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| DetectNonExistingPointsShape | simulated-sensor | intervalDegradation | 0 | 1 | Change/worsening (decrease) of the time of re-occurrence | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| DetectNonExistingPointsShape | simulated-sensor | durationDegradation | 0 | 1 | Change/worsening (decrease) of the duration between re-ocurrences | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| DetectNonExistingPointsShape | simulated-sensor | amountDetections | 1 | 1 | Amount of non-existant points that shall be spawned | <http://www.w3.org/2001/XMLSchema#integer> | simulated_sensor_shacl.ttl |
| DetectNonExistingPointsShape | simulated-sensor | horFOVFlag | 1 | 1 | Flag to indicate where the ghost points are spawned (horizontal) | <http://www.w3.org/2001/XMLSchema#integer> | simulated_sensor_shacl.ttl |
| DetectNonExistingPointsShape | simulated-sensor | vertFOVFlag | 1 | 1 | Flag to indicate where the ghost points are spawned (vertical) | <http://www.w3.org/2001/XMLSchema#integer> | simulated_sensor_shacl.ttl |
| CollisionSensorShiftShape | simulated-sensor | start | 1 | 1 | First occurrence of the pattern of manipulation in the simulation in seconds | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| CollisionSensorShiftShape | simulated-sensor | yaw | 1 | 1 | Yaw rotation of the shift | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| CollisionSensorShiftShape | simulated-sensor | pitch | 1 | 1 | Pitch rotation of the shift | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| CollisionSensorShiftShape | simulated-sensor | roll | 1 | 1 | Roll rotation of the shift | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| CollisionSensorShiftShape | simulated-sensor | shiftTriggerFlag | 1 | 1 | If true, the shift will happen at the first collision | <http://www.w3.org/2001/XMLSchema#boolean> | simulated_sensor_shacl.ttl |
| ConstantSensorShiftShape | simulated-sensor | start | 1 | 1 | First occurrence of the pattern of manipulation in the simulation in seconds | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| ConstantSensorShiftShape | simulated-sensor | interval | 1 | 1 | Interval of re-occurrence of the manipulation pattern in seconds | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| ConstantSensorShiftShape | simulated-sensor | duration | 1 | 1 | Time the pattern of manipulation is active in seconds | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| ConstantSensorShiftShape | simulated-sensor | intervalDegradation | 0 | 1 | Change/worsening (decrease) of the time of re-occurrence | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| ConstantSensorShiftShape | simulated-sensor | durationDegradation | 0 | 1 | Change/worsening (decrease) of the duration between re-ocurrences | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| ConstantSensorShiftShape | simulated-sensor | yaw | 1 | 1 | Yaw rotation of the shift | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| ConstantSensorShiftShape | simulated-sensor | pitch | 1 | 1 | Pitch rotation of the shift | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| ConstantSensorShiftShape | simulated-sensor | roll | 1 | 1 | Roll rotation of the shift | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| ConstantSensorShiftShape | simulated-sensor | shiftFlag | 1 | 1 | If true, the shift occurs once at the beginning of the failur event, otherwise a constant shift is simulated | <http://www.w3.org/2001/XMLSchema#boolean> | simulated_sensor_shacl.ttl |
| ConstantSensorShiftShape | simulated-sensor | shiftTriggerFlag | 1 | 1 | If true, the shift will happen at the first collision | <http://www.w3.org/2001/XMLSchema#boolean> | simulated_sensor_shacl.ttl |
| SensorBlockageRandomLifetimeShape | simulated-sensor | start | 1 | 1 | First occurrence of the pattern of manipulation in the simulation in seconds | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| SensorBlockageRandomLifetimeShape | simulated-sensor | interval | 1 | 1 | Interval of re-occurrence of the manipulation pattern in seconds | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| SensorBlockageRandomLifetimeShape | simulated-sensor | intervalDegradation | 0 | 1 | Change/worsening (decrease) of the time of re-occurrence | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| SensorBlockageRandomLifetimeShape | simulated-sensor | amountOfBlockingObjects | 1 | 1 | Change (decrease) of the duration between re-ocurrences | <http://www.w3.org/2001/XMLSchema#integer> | simulated_sensor_shacl.ttl |
| SensorBlockageRandomLifetimeShape | simulated-sensor | type | 1 | 1 | If true, blockage points are spawend in the entire FOV of the sensor. Otherwise in 1m distance to the sensor | <http://www.w3.org/2001/XMLSchema#boolean> | simulated_sensor_shacl.ttl |
| SensorBlockageRandomLifetimeShape | simulated-sensor | lifeTime | 1 | 1 | If true, the blocking object will have a random lifetime, otherwise the lifetime has to be defined | <http://www.w3.org/2001/XMLSchema#boolean> | simulated_sensor_shacl.ttl |
| SensorBlockageRandomLifetimeShape | simulated-sensor | maxBlockingObjectLifeTime | 0 | 1 | Maximum lifetime of the blocking object(s) in seconds | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| SensorBlockageRandomLifetimeShape | simulated-sensor | blockageDropSpeed | 0 | 1 | Fall speed of the blocking object (e.g. to simulate dirt falling off the lense) | <http://www.w3.org/2001/XMLSchema#integer> | simulated_sensor_shacl.ttl |
| SensorBlockageRandomLifetimeShape | simulated-sensor | horFOVFlag | 1 | 1 | Flag to indicate where the blocking objects are spawned (horizontal) | <http://www.w3.org/2001/XMLSchema#integer> | simulated_sensor_shacl.ttl |
| SensorBlockageRandomLifetimeShape | simulated-sensor | vertFOVFlag | 1 | 1 | Flag to indicate where the blocking objects are spawned (vertical) | <http://www.w3.org/2001/XMLSchema#integer> | simulated_sensor_shacl.ttl |
| SensorBlockageDefinedLifetimeShape | simulated-sensor | start | 1 | 1 | First occurrence of the pattern of manipulation in the simulation in seconds | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| SensorBlockageDefinedLifetimeShape | simulated-sensor | interval | 1 | 1 | Interval of re-occurrence of the manipulation pattern in seconds | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| SensorBlockageDefinedLifetimeShape | simulated-sensor | intervalDegradation | 0 | 1 | Change/worsening (decrease) of the time of re-occurrence | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| SensorBlockageDefinedLifetimeShape | simulated-sensor | amountOfBlockingObjects | 1 | 1 | Change (decrease) of the duration between re-ocurrences | <http://www.w3.org/2001/XMLSchema#integer> | simulated_sensor_shacl.ttl |
| SensorBlockageDefinedLifetimeShape | simulated-sensor | type | 1 | 1 | If true, blockage points are spawend in the entire FOV of the sensor. Otherwise in 1m distance to the sensor | <http://www.w3.org/2001/XMLSchema#boolean> | simulated_sensor_shacl.ttl |
| SensorBlockageDefinedLifetimeShape | simulated-sensor | lifeTime | 1 | 1 | If true, the blocking object will have a random lifetime, otherwise the lifetime has to be defined | <http://www.w3.org/2001/XMLSchema#boolean> | simulated_sensor_shacl.ttl |
| SensorBlockageDefinedLifetimeShape | simulated-sensor | blockingObjectLifeTime | 1 | 1 | Lifetime of each blocking object in seconds | <http://www.w3.org/2001/XMLSchema#float> | simulated_sensor_shacl.ttl |
| SensorBlockageDefinedLifetimeShape | simulated-sensor | blockageDropSpeed | 0 | 1 | Fall speed of the blocking object (e.g. to simulate dirt falling off the lense) | <http://www.w3.org/2001/XMLSchema#integer> | simulated_sensor_shacl.ttl |
| SensorBlockageDefinedLifetimeShape | simulated-sensor | horFOVFlag | 1 | 1 | Flag to indicate where the blocking objects are spawned (horizontal) | <http://www.w3.org/2001/XMLSchema#integer> | simulated_sensor_shacl.ttl |
| SensorBlockageDefinedLifetimeShape | simulated-sensor | vertFOVFlag | 1 | 1 | Flag to indicate where the blocking objects are spawned (vertical) | <http://www.w3.org/2001/XMLSchema#integer> | simulated_sensor_shacl.ttl |
