# ENVITED-X Ontology Domain

## Overview

**ENVITED-X** represents the post-GAIA-X era of autonomous vehicle ontology development (2024+). Building on the solid foundations of GAIA-X 4 PLC-AAD, ENVITED-X focuses on exploitation, extended use cases, and innovative approaches to semantic modeling for autonomous systems. This domain accommodates both newly developed ontologies and extended versions of GAIA-X concepts adapted for new contexts.

**Key Characteristics:**

- **4+ ontologies** covering core concepts, domain applications, and extensions
- **Active development** with rapid iteration cycles
- **Lighter governance** suited for consortium-driven innovation
- **Experimental features** tested before potential graduation to stable domains
- **Backward compatibility** with GAIA-X foundational ontologies where applicable

## Namespace

```
https://w3id.org/ascs-ev/envited-x/
```

All ENVITED-X ontologies use IRIs under this namespace with version suffixes:

```
https://w3id.org/ascs-ev/envited-x/{ontology-name}/v{major}.{minor}/
```

## Ontologies in This Domain

### Core Ontologies

| Ontology                     | Version | Purpose                                                       | Status             |
| ---------------------------- | ------- | ------------------------------------------------------------- | ------------------ |
| **core**                     | v1.0    | Central ENVITED-X coordination and alignment concepts         | Stable             |
| **extended-service**         | v1.0    | Enhanced service definitions beyond GAIA-X                    | Active Development |
| **autonomous-system**        | v1.0    | Generic autonomous system modeling (vehicles, robots, agents) | Stable             |
| **knowledge-representation** | v1.1    | Advanced knowledge modeling for autonomous reasoning          | In Development     |

### Domain Application Ontologies

| Ontology      | Version | Purpose                                                    | Status      |
| ------------- | ------- | ---------------------------------------------------------- | ----------- |
| **survey**    | v1.0    | Assessment and survey methodologies for autonomous systems | Active Use  |
| **tzip21**    | v1.0    | Domain-specific application (TBD - organization specific)  | Specialized |
| **envited-x** | v1.0    | Main ENVITED-X ontology (legacy naming, maps to `core`)    | Stable      |

### Experimental/Incubating Ontologies

| Ontology        | Version | Purpose                              | Status      |
| --------------- | ------- | ------------------------------------ | ----------- |
| _[forthcoming]_ | v0.x    | Additional domains under development | Pre-release |

## Ontology Details

### Core (`core`)

Central ontology providing coordination concepts for ENVITED-X domain alignment. This ontology serves as the entry point for ENVITED-X semantics and provides integration points with GAIA-X foundational concepts.

**Artifacts:**

- [View on GitHub](https://github.com/YOUR-ORG/ontology-management-base/tree/main/artifacts/envited-x)
- [Turtle Format](https://w3id.org/ascs-ev/envited-x/core/v1.0/)
- [JSON-LD Context](https://w3id.org/ascs-ev/envited-x/core/v1.0/)
- [Properties Documentation](https://github.com/YOUR-ORG/ontology-management-base/blob/main/artifacts/envited-x/PROPERTIES.md)

**Key Classes:**

- `ex:AutonomousSystem` - System with autonomous decision-making capabilities
- `ex:EvolutionaryPhase` - Project phase concept (GAIA-X→ENVITED-X progression)
- `ex:ExtendedCapability` - Capability beyond GAIA-X scope

**Imports:**

```turtle
owl:imports <https://w3id.org/gaia-x4plcaad/ontologies/general/v2/> ;
owl:imports <https://w3id.org/gaia-x4plcaad/ontologies/description/v2/> ;
```

---

### Autonomous System (`autonomous-system`)

Generic framework for modeling autonomous systems beyond just autonomous vehicles. Covers robotic systems, autonomous agents, and other self-directed entities.

**Artifacts:**

- [View on GitHub](https://github.com/YOUR-ORG/ontology-management-base/tree/main/artifacts/autonomous-system)
- [Turtle Format](https://w3id.org/ascs-ev/envited-x/autonomous-system/v1.0/)
- [Properties Documentation](https://github.com/YOUR-ORG/ontology-management-base/blob/main/artifacts/autonomous-system/PROPERTIES.md)

**Key Classes:**

- `as:AutonomousAgent` - Self-directed entity making independent decisions
- `as:DecisionMakingCapability` - Specific decision-making function
- `as:AutonomousVehicle` - Vehicle-specific autonomous system (extends GAIA-X concepts)
- `as:AutonomousRobot` - Robot-specific autonomous system

**Relationship to GAIA-X:**

```turtle
as:AutonomousVehicle rdfs:subClassOf
  <https://w3id.org/gaia-x4plcaad/ontologies/automotive-simulator/v2/#Vehicle> ;
rdfs:comment "ENVITED-X extension of GAIA-X vehicle concept"@en .
```

---

### Extended Service (`extended-service`)

Enhanced service definitions providing richer capability representations and composition mechanisms beyond GAIA-X service ontology.

**Artifacts:**

- [View on GitHub](https://github.com/YOUR-ORG/ontology-management-base/tree/main/artifacts/extended-service)
- [Turtle Format](https://w3id.org/ascs-ev/envited-x/extended-service/v1.0/)
- [Properties Documentation](https://github.com/YOUR-ORG/ontology-management-base/blob/main/artifacts/extended-service/PROPERTIES.md)

**Key Classes:**

- `es:ServiceComposition` - Multiple services combined into workflows
- `es:ServiceQoS` - Quality of Service constraints and guarantees
- `es:ServiceContext` - Operational context for service execution
- `es:AdaptiveService` - Service that changes behavior based on context

**Extends:**

```turtle
es:AdaptiveService rdfs:subClassOf
  <https://w3id.org/gaia-x4plcaad/ontologies/service/v2/#Service> ;
rdfs:comment "ENVITED-X extension for context-aware services"@en .
```

---

### Knowledge Representation (`knowledge-representation`)

Advanced knowledge modeling for autonomous systems requiring complex reasoning, planning, and decision-making. Bridges symbolic AI with ontological representations.

**Artifacts:**

- [View on GitHub](https://github.com/YOUR-ORG/ontology-management-base/tree/main/artifacts/knowledge-representation)
- [Turtle Format](https://w3id.org/ascs-ev/envited-x/knowledge-representation/v1.1/)
- [Properties Documentation](https://github.com/YOUR-ORG/ontology-management-base/blob/main/artifacts/knowledge-representation/PROPERTIES.md)

**Key Classes:**

- `kr:Belief` - Autonomous system's understanding of world state
- `kr:Goal` - Objective or target state to achieve
- `kr:Plan` - Sequence of actions to achieve goals
- `kr:Reasoning` - Logical inference process and results

**Status:** Currently in active development; pre-v1.0 versioning expected to continue changing.

---

### Survey (`survey`)

Assessment, evaluation, and survey methodologies for autonomous system validation and conformance checking. Provides framework for structured testing and reporting.

**Artifacts:**

- [View on GitHub](https://github.com/YOUR-ORG/ontology-management-base/tree/main/artifacts/survey)
- [Turtle Format](https://w3id.org/ascs-ev/envited-x/survey/v1.0/)
- [Properties Documentation](https://github.com/YOUR-ORG/ontology-management-base/blob/main/artifacts/survey/PROPERTIES.md)

**Key Classes:**

- `surv:Survey` - Assessment or evaluation activity
- `surv:TestCase` - Individual test or evaluation instance
- `surv:SurveyResult` - Outcome of survey/assessment
- `surv:ConformanceReport` - Structured compliance verification

**Use Cases:**

- Autonomous vehicle validation workflows
- Conformance checking against ENVITED-X specifications
- Structured documentation of testing and evaluation processes

---

### TZIP21 (`tzip21`)

Domain-specific application ontology for specialized use case (TBD based on organizational context). This serves as an example of extended domain ontology within ENVITED-X.

**Artifacts:**

- [View on GitHub](https://github.com/YOUR-ORG/ontology-management-base/tree/main/artifacts/tzip21)
- [Turtle Format](https://w3id.org/ascs-ev/envited-x/tzip21/v1.0/)
- [Properties Documentation](https://github.com/YOUR-ORG/ontology-management-base/blob/main/artifacts/tzip21/PROPERTIES.md)

**Purpose:** [Organization-specific information to be added based on actual TZIP21 domain]

---

### ENVITED-X (`envited-x`)

Legacy main ontology (maps to `core` ontology). Provided for backward compatibility.

**Status:** Use `core` ontology for new implementations; this mapping maintained for existing integrations.

## Importing ENVITED-X Ontologies

### Basic Import

```turtle
@prefix ex: <https://w3id.org/ascs-ev/envited-x/core/v1.0/> .
@prefix as: <https://w3id.org/ascs-ev/envited-x/autonomous-system/v1.0/> .

# Your custom ontology
@base <https://my-org.example.com/ontologies/my-av-extension/v1/> .

<> a owl:Ontology ;
    owl:imports ex: ;
    owl:imports as: ;
    rdfs:label "My Autonomous Vehicle Extension"@en .

# Your classes and properties here
```

### Cross-Domain Imports (GAIA-X + ENVITED-X)

```turtle
# Import GAIA-X foundational concepts
@prefix gx-general: <https://w3id.org/gaia-x4plcaad/ontologies/general/v2/> .
@prefix gx-scenario: <https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/> .

# Import ENVITED-X extensions
@prefix ex-as: <https://w3id.org/ascs-ev/envited-x/autonomous-system/v1.0/> .

<> a owl:Ontology ;
    owl:imports gx-general: ;
    owl:imports gx-scenario: ;
    owl:imports ex-as: ;
    rdfs:comment "Hybrid ontology using both GAIA-X and ENVITED-X concepts"@en .

# Define how ENVITED-X concepts extend GAIA-X
ex-as:AdvancedAutonomousVehicle rdfs:subClassOf
  <https://w3id.org/gaia-x4plcaad/ontologies/automotive-simulator/v2/#Vehicle> ;
rdfs:comment "Combines GAIA-X vehicle semantics with ENVITED-X extensions"@en .
```

### Version Handling

ENVITED-X uses semantic versioning (Major.Minor.Patch):

```turtle
# ✅ Good: Specific version pinned
owl:imports <https://w3id.org/ascs-ev/envited-x/autonomous-system/v1.0/> .

# ⚠️ Caution: Only major version (may change minor/patch)
owl:imports <https://w3id.org/ascs-ev/envited-x/autonomous-system/v1/> .

# ❌ Avoid: Unversioned (unpredictable changes)
owl:imports <https://w3id.org/ascs-ev/envited-x/autonomous-system/> .
```

## Development and Release Process

### Current Development Cycle

ENVITED-X follows a more rapid development cycle than GAIA-X:

- **Pre-release versions (v0.x)**: Experimental ontologies, breaking changes expected
- **Stable versions (v1.x)**: Production-ready ontologies, backward-compatible updates
- **Update frequency**: Monthly to quarterly minor/patch releases; major versions annually or as needed

### Roadmap (Planned/Proposed)

| Phase                 | Timeline | Focus                                                          |
| --------------------- | -------- | -------------------------------------------------------------- |
| **Phase 1 (Current)** | 2024 H1  | Core ontologies, autonomous-system, survey                     |
| **Phase 2**           | 2024 H2  | Knowledge representation completion, extended-service v1.1     |
| **Phase 3**           | 2025 H1  | Additional domain ontologies (TBD), integration patterns       |
| **Phase 4**           | 2025 H2+ | Convergence/alignment opportunities with GAIA-X v3 discussions |

### Contributing to ENVITED-X

ENVITED-X welcomes community contributions and extensions:

1. **New Domain Ontologies**: Propose in [building-contributing/adding-ontologies.md](../../5-building-contributing/02-adding-ontologies.md)
2. **Ontology Extensions**: Submit pull requests with detailed rationale
3. **Bug Reports**: Use GitHub issues with example test cases
4. **Version Feedback**: Join discussions on semantic versioning and release cycles

## Comparison with GAIA-X

### When to Use GAIA-X vs ENVITED-X

| Scenario                         | Choose GAIA-X | Choose ENVITED-X | Choose Both |
| -------------------------------- | ------------- | ---------------- | ----------- |
| **Stable production systems**    | ✅            | -                | -           |
| **GAIA-X partner integration**   | ✅            | -                | -           |
| **New autonomous vehicle types** | -             | ✅               | -           |
| **Generic autonomous systems**   | -             | ✅               | -           |
| **Advanced service composition** | -             | ✅               | -           |
| **Rapid prototyping**            | -             | ✅               | -           |
| **Hybrid systems**               | -             | -                | ✅          |
| **Conservative stability focus** | ✅            | -                | -           |

### Ontology Alignment

ENVITED-X maintains semantic compatibility with GAIA-X through:

- Direct subclass relationships where appropriate
- Explicit owl:equivalentClass mappings for aligned concepts
- Cross-namespace imports with version pinning
- Migration guides for moving from GAIA-X to ENVITED-X concepts

**Example Alignment:**

```turtle
ex:AutonomousVehicle rdfs:subClassOf gx:Vehicle .
# ENVITED-X autonomous vehicle IS-A GAIA-X vehicle

es:AdaptiveService rdfs:comment
  "Recommended replacement for gx:Service in new ENVITED-X systems"@en .
# Alternative mapping through documentation and usage patterns
```

## See Also

- [Ontology Domains and Namespaces](../2-architecture/05-domains.md) - Context for GAIA-X vs ENVITED-X split
- [W3ID Publishing](../2-architecture/06-w3id-publishing.md) - Technical details on IRI resolution
- [GAIA-X Ontology Domain](../3-ontology-domains/gaia-x4plcaad/01-index.md) - Stable foundation ontologies
- [Adding Ontologies](../../5-building-contributing/02-adding-ontologies.md) - How to contribute new ENVITED-X ontologies
- [Validation Tools](../../6-validation-tools/) - Tools for ENVITED-X conformance checking
