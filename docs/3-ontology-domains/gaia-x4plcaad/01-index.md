# GAIA-X 4 PLC-AAD Ontology Domain

## Overview

The **GAIA-X 4 Pilots Large-Scale Competence Centre for Advanced Autonomous Driving (GAIA-X 4 PLC-AAD)** is a comprehensive ontology domain developed during the GAIA-X initiative (2021-2024). These ontologies provide standardized semantic representations for autonomous driving systems, vehicles, sensors, simulation environments, and related concepts within the GAIA-X federated infrastructure.

**Key Characteristics:**

- **16 core ontologies** covering vehicle modeling, simulation, scenarios, services, and validation
- **Stable semantics** with version management (v1, v2, v3)
- **GAIA-X governance** through the GAIA-X Steering Committee
- **Production-ready** ontologies used in real GAIA-X partner deployments

## Namespace

```
https://w3id.org/gaia-x4plcaad/ontologies/
```

All GAIA-X 4 PLC-AAD ontologies use IRIs under this namespace with version suffixes:

```
https://w3id.org/gaia-x4plcaad/ontologies/{ontology-name}/v{major-version}/
```

## Ontologies in This Domain

### Core Ontologies

| Ontology              | Version | Purpose                                       | Dependencies          |
| --------------------- | ------- | --------------------------------------------- | --------------------- |
| **general**           | v2      | Common concepts applicable across all domains | (none)                |
| **description**       | v2      | Generic entity description and metadata       | general               |
| **service**           | v2      | Service definitions and capabilities          | description, general  |
| **scenario**          | v2      | Test scenarios and operational conditions     | description, general  |
| **simulation-model**  | v2      | Entity modeling for simulation environments   | description, scenario |
| **simulated-sensor**  | v2      | Sensor simulation specifications              | simulation-model      |
| **environment-model** | v2      | Road and environmental feature representation | description, general  |
| **georeference**      | v2      | Geospatial coordinate system definitions      | general               |

### Domain-Specific Ontologies

| Ontology                 | Version | Purpose                               | Dependencies                       |
| ------------------------ | ------- | ------------------------------------- | ---------------------------------- |
| **automotive-simulator** | v2      | Autonomous driving simulator entities | simulation-model, simulated-sensor |
| **hdmap**                | v2      | High-definition map representation    | environment-model, georeference    |
| **scenario**             | v2      | Realistic test scenario encoding      | description, environment-model     |
| **ositrace**             | v2      | Simulated object interaction traces   | automotive-simulator               |
| **openlabel**            | v2      | OpenLABEL standard alignment          | ositrace, scenario                 |

### Validation and Governance Ontologies

| Ontology         | Version | Purpose                                      | Dependencies         |
| ---------------- | ------- | -------------------------------------------- | -------------------- |
| **gx**           | v2      | GAIA-X governance and federation concepts    | description          |
| **manifest**     | v2      | Data packaging, provenance, and distribution | description, general |
| **leakage-test** | v2      | Data quality and integrity assertions        | description          |

### Utility Ontologies

| Ontology    | Version | Purpose                           | Dependencies       |
| ----------- | ------- | --------------------------------- | ------------------ |
| **example** | v2      | Reference data and usage examples | (all core domains) |

## Ontology Details

### General (`general`)

Foundational concepts used across all GAIA-X ontologies including basic entity types, relationships, and properties.

**Artifacts:**

- [View on GitHub](https://github.com/YOUR-ORG/ontology-management-base/tree/main/artifacts/general)
- [Turtle Format](https://w3id.org/gaia-x4plcaad/ontologies/general/v2/)
- [Properties Documentation](https://github.com/YOUR-ORG/ontology-management-base/blob/main/artifacts/general/PROPERTIES.md)

**Key Classes:**

- `general:Entity` - Base class for all domain entities
- `general:Attribute` - Property or characteristic of an entity
- `general:Relationship` - Connection between entities

---

### Description (`description`)

Generic metadata and description framework for entities, providing common properties for documentation and classification.

**Artifacts:**

- [View on GitHub](https://github.com/YOUR-ORG/ontology-management-base/tree/main/artifacts/description)
- [Turtle Format](https://w3id.org/gaia-x4plcaad/ontologies/description/v2/)
- [Properties Documentation](https://github.com/YOUR-ORG/ontology-management-base/blob/main/artifacts/description/PROPERTIES.md)

**Key Classes:**

- `description:HasMetadata` - Mixin for metadata-bearing entities
- `description:HasProperties` - Mixin for property aggregation

---

### Service (`service`)

Service definitions including autonomous driving services, data services, and validation services.

**Artifacts:**

- [View on GitHub](https://github.com/YOUR-ORG/ontology-management-base/tree/main/artifacts/service)
- [Turtle Format](https://w3id.org/gaia-x4plcaad/ontologies/service/v2/)
- [Properties Documentation](https://github.com/YOUR-ORG/ontology-management-base/blob/main/artifacts/service/PROPERTIES.md)

**Key Classes:**

- `service:Service` - Abstract service definition
- `service:AutonomousDrivingService` - Autonomous vehicle control service
- `service:DataService` - Service providing data access

---

### Scenario (`scenario`)

Encoded scenarios for testing autonomous driving systems including environmental conditions, traffic patterns, and test objectives.

**Artifacts:**

- [View on GitHub](https://github.com/YOUR-ORG/ontology-management-base/tree/main/artifacts/scenario)
- [Turtle Format](https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/)
- [Properties Documentation](https://github.com/YOUR-ORG/ontology-management-base/blob/main/artifacts/scenario/PROPERTIES.md)

**Key Classes:**

- `scenario:Scenario` - Test or operational scenario
- `scenario:ScenarioCondition` - Environmental or traffic condition
- `scenario:ScenarioParameter` - Parameterized scenario variant

---

### Simulation Model (`simulation-model`)

Core simulation framework for modeling entities and their behaviors in virtual environments.

**Artifacts:**

- [View on GitHub](https://github.com/YOUR-ORG/ontology-management-base/tree/main/artifacts/simulation-model)
- [Turtle Format](https://w3id.org/gaia-x4plcaad/ontologies/simulation-model/v2/)
- [Properties Documentation](https://github.com/YOUR-ORG/ontology-management-base/blob/main/artifacts/simulation-model/PROPERTIES.md)

**Key Classes:**

- `sim:SimulationEntity` - Entity in simulation environment
- `sim:SimulationRun` - Execution of a simulation scenario
- `sim:SimulationParameter` - Input parameter to simulation

---

### Automotive Simulator (`automotive-simulator`)

Autonomous driving simulation specific entities including vehicles, traffic participants, and sensor implementations.

**Artifacts:**

- [View on GitHub](https://github.com/YOUR-ORG/ontology-management-base/tree/main/artifacts/automotive-simulator)
- [Turtle Format](https://w3id.org/gaia-x4plcaad/ontologies/automotive-simulator/v2/)
- [Properties Documentation](https://github.com/YOUR-ORG/ontology-management-base/blob/main/artifacts/automotive-simulator/PROPERTIES.md)

**Key Classes:**

- `as:Vehicle` - Autonomous or manually-controlled vehicle
- `as:TrafficParticipant` - Pedestrians, bicycles, other vehicles
- `as:SensorModel` - Simulated sensor implementation

---

### HD Map (`hdmap`)

High-definition map representation for autonomous driving including road networks, lanes, traffic signs, and landmarks.

**Artifacts:**

- [View on GitHub](https://github.com/YOUR-ORG/ontology-management-base/tree/main/artifacts/hdmap)
- [Turtle Format](https://w3id.org/gaia-x4plcaad/ontologies/hdmap/v2/)
- [Properties Documentation](https://github.com/YOUR-ORG/ontology-management-base/blob/main/artifacts/hdmap/PROPERTIES.md)

**Key Classes:**

- `hdmap:RoadNetwork` - Collection of roads and intersections
- `hdmap:Lane` - Individual traffic lane with boundaries
- `hdmap:TrafficSign` - Regulatory or informational sign

---

### Simulated Sensor (`simulated-sensor`)

Sensor simulation specifications for cameras, LiDAR, radar, and other sensor types used in autonomous driving testing.

**Artifacts:**

- [View on GitHub](https://github.com/YOUR-ORG/ontology-management-base/tree/main/artifacts/simulated-sensor)
- [Turtle Format](https://w3id.org/gaia-x4plcaad/ontologies/simulated-sensor/v2/)
- [Properties Documentation](https://github.com/YOUR-ORG/ontology-management-base/blob/main/artifacts/simulated-sensor/PROPERTIES.md)

**Key Classes:**

- `sensor:Sensor` - Abstract sensor definition
- `sensor:Camera` - Camera sensor with optical properties
- `sensor:LiDAR` - Light Detection and Ranging sensor
- `sensor:Radar` - Radar sensor implementation

---

### OSITrace (`ositrace`)

OpenSCENARIO I (OSI) trace data representation for recording and analyzing simulation results.

**Artifacts:**

- [View on GitHub](https://github.com/YOUR-ORG/ontology-management-base/tree/main/artifacts/ositrace)
- [Turtle Format](https://w3id.org/gaia-x4plcaad/ontologies/ositrace/v2/)
- [Properties Documentation](https://github.com/YOUR-ORG/ontology-management-base/blob/main/artifacts/ositrace/PROPERTIES.md)

**Key Classes:**

- `ositrace:OSITrace` - Container for OSI trace data
- `ositrace:TimeStep` - Single moment in simulation recording
- `ositrace:ObjectState` - State of entity at time step

---

### OpenLabel (`openlabel`)

Alignment with OpenLABEL standard for annotation and labeling of autonomous driving datasets.

**Artifacts:**

- [View on GitHub](https://github.com/YOUR-ORG/ontology-management-base/tree/main/artifacts/openlabel)
- [Turtle Format](https://w3id.org/gaia-x4plcaad/ontologies/openlabel/v2/)
- [Properties Documentation](https://github.com/YOUR-ORG/ontology-management-base/blob/main/artifacts/openlabel/PROPERTIES.md)

**Key Classes:**

- `openlabel:Dataset` - Labeled dataset collection
- `openlabel:FrameAnnotation` - Per-frame annotation
- `openlabel:ObjectAnnotation` - Object-level annotation

---

### GAIA-X (`gx`)

GAIA-X specific governance and federation concepts for data space participation.

**Artifacts:**

- [View on GitHub](https://github.com/YOUR-ORG/ontology-management-base/tree/main/artifacts/gx)
- [Turtle Format](https://w3id.org/gaia-x4plcaad/ontologies/gx/v2/)
- [Properties Documentation](https://github.com/YOUR-ORG/ontology-management-base/blob/main/artifacts/gx/PROPERTIES.md)

**Key Classes:**

- `gx:DataSpace` - GAIA-X data space definition
- `gx:Provider` - Service or data provider
- `gx:Credential` - GAIA-X credential assertion

---

### Manifest (`manifest`)

Data packaging, versioning, and distribution metadata for ontology releases and data exports.

**Artifacts:**

- [View on GitHub](https://github.com/YOUR-ORG/ontology-management-base/tree/main/artifacts/manifest)
- [Turtle Format](https://w3id.org/gaia-x4plcaad/ontologies/manifest/v2/)
- [Properties Documentation](https://github.com/YOUR-ORG/ontology-management-base/blob/main/artifacts/manifest/PROPERTIES.md)

**Key Classes:**

- `manifest:Package` - Versioned distribution package
- `manifest:Release` - Ontology release metadata
- `manifest:Artifact` - Individual file artifact

---

### Leakage Test (`leakage-test`)

Data quality and integrity validation constraints for detecting data consistency issues.

**Artifacts:**

- [View on GitHub](https://github.com/YOUR-ORG/ontology-management-base/tree/main/artifacts/leakage-test)
- [Turtle Format](https://w3id.org/gaia-x4plcaad/ontologies/leakage-test/v2/)
- [Properties Documentation](https://github.com/YOUR-ORG/ontology-management-base/blob/main/artifacts/leakage-test/PROPERTIES.md)

**Key Classes:**

- `leak:ValidationRule` - Data quality assertion
- `leak:IntegrityConstraint` - Consistency requirement
- `leak:ValidationReport` - Results of validation run

---

### Environment Model (`environment-model`)

Road and environmental feature representation for simulation and planning contexts.

**Artifacts:**

- [View on GitHub](https://github.com/YOUR-ORG/ontology-management-base/tree/main/artifacts/environment-model)
- [Turtle Format](https://w3id.org/gaia-x4plcaad/ontologies/environment-model/v2/)
- [Properties Documentation](https://github.com/YOUR-ORG/ontology-management-base/blob/main/artifacts/environment-model/PROPERTIES.md)

**Key Classes:**

- `env:EnvironmentalFeature` - Weather, road conditions, etc.
- `env:RoadElement` - Roads, intersections, bridges
- `env:TrafficCondition` - Dynamic traffic state

---

### Georeference (`georeference`)

Geospatial coordinate system definitions and transformations for map and sensor data.

**Artifacts:**

- [View on GitHub](https://github.com/YOUR-ORG/ontology-management-base/tree/main/artifacts/georeference)
- [Turtle Format](https://w3id.org/gaia-x4plcaad/ontologies/georeference/v2/)
- [Properties Documentation](https://github.com/YOUR-ORG/ontology-management-base/blob/main/artifacts/georeference/PROPERTIES.md)

**Key Classes:**

- `geo:CoordinateSystem` - CRS definition (WGS84, UTM, etc.)
- `geo:Transformation` - Coordinate transformation between systems
- `geo:GeographicLocation` - Location referenced to Earth

---

### Example (`example`)

Reference implementations and example data demonstrating usage of all GAIA-X ontologies.

**Artifacts:**

- [View on GitHub](https://github.com/YOUR-ORG/ontology-management-base/tree/main/artifacts/example)
- [Turtle Format](https://w3id.org/gaia-x4plcaad/ontologies/example/v2/)
- [Properties Documentation](https://github.com/YOUR-ORG/ontology-management-base/blob/main/artifacts/example/PROPERTIES.md)

**Purpose:** Provides concrete examples of how to use GAIA-X ontologies for representing autonomous driving scenarios, sensor data, and simulation configurations.

## Importing GAIA-X Ontologies

### Basic Import

```turtle
@prefix as: <https://w3id.org/gaia-x4plcaad/ontologies/automotive-simulator/v2/> .

# Import general ontology
@prefix general: <https://w3id.org/gaia-x4plcaad/ontologies/general/v2/> .

# Import scenario ontology for test scenarios
@prefix scenario: <https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/> .

# Your custom ontology
@base <https://my-org.example.com/ontologies/my-ad-system/v1/> .

<> a owl:Ontology ;
    owl:imports general: ;
    owl:imports scenario: ;
    owl:imports as: .

# Your classes and properties here
```

### Specific Version Handling

Always pin specific versions to avoid breaking changes:

```turtle
# ✅ Good: Version explicitly specified
owl:imports <https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/> .

# ❌ Avoid: Version omitted (may change unexpectedly)
owl:imports <https://w3id.org/gaia-x4plcaad/ontologies/scenario/> .
```

## Version History

### Version 2.0 (Current - 2023)

- Refined scenario representation
- Enhanced sensor simulation support
- Improved georeference handling
- Better alignment with OpenLABEL standard

### Version 1.0 (Legacy - 2021)

- Initial GAIA-X ontology set
- Core autonomous driving concepts
- No longer recommended for new projects

## Related Resources

- [Ontology Domains and Namespaces](../2-architecture/05-domains.md) - Context for GAIA-X vs ENVITED-X split
- [W3ID Publishing](../2-architecture/06-w3id-publishing.md) - Technical details on IRI resolution
- [ENVITED-X Ontology Domain](../3-ontology-domains/envited-x/01-index.md) - Post-GAIA-X ontologies
- [Validation Tools](../6-validation-tools/) - Tools for validating GAIA-X conformance
