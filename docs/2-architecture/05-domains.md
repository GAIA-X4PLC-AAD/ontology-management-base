# Ontology Domains and Namespaces

This repository maintains two distinct IRI namespaces for different project phases and governance contexts. Understanding the distinction between **GAIA-X 4 PLC-AAD** and **ENVITED-X** is crucial for developers, contributors, and users.

## Overview

| Aspect               | GAIA-X 4 PLC-AAD                             | ENVITED-X                             |
| -------------------- | -------------------------------------------- | ------------------------------------- |
| **Project**          | GAIA-X 4 Pilots (2021-2024)                  | ENVITED-X Exploitation (2024+)        |
| **Namespace**        | `https://w3id.org/gaia-x4plcaad/ontologies/` | `https://w3id.org/ascs-ev/envited-x/` |
| **Ontologies**       | 16 core ontologies                           | 4+ domain-specific ontologies         |
| **Governance**       | GAIA-X Steering Committee                    | ASCS/ENVITED Consortium               |
| **Maturity**         | Stable, released                             | Active development                    |
| **Cross-domain Use** | Production pipelines                         | Experimental integration              |

## GAIA-X 4 PLC-AAD Domain

### Project Context

The GAIA-X 4 Pilots Large-Scale Competence Centre for Advanced Autonomous Driving (GAIA-X 4 PLC-AAD) was a European research initiative (2021-2024) focusing on standardized data representation for autonomous driving and mobility services.

**Key Characteristics:**

- Endorsed ontology set for the GAIA-X federated infrastructure
- Stable semantics with version history (v1, v2, v3)
- Strong governance through GAIA-X committee
- Primarily used in production scenarios within GAIA-X partner systems

### Ontologies in This Domain

```
artifacts/
├── automotive-simulator/      # Simulation environment definitions
├── description/               # Generic entity descriptions
├── environment-model/         # Road and environmental features
├── example/                   # Reference data and usage examples
├── general/                   # Common concepts across domains
├── georeference/             # Geospatial coordinate systems
├── gx/                       # GAIA-X-specific governance concepts
├── hdmap/                    # High-definition map representation
├── leakage-test/             # Data quality and integrity checks
├── manifest/                 # Data packaging and provenance
├── openlabel/                # OpenLABEL standard alignment
├── ositrace/                 # Simulated object interaction traces
├── scenario/                 # Test and operational scenarios
├── service/                  # Service definitions and capabilities
├── simulated-sensor/         # Sensor simulation specifications
└── simulation-model/         # Simulation entity modeling
```

### IRI Pattern Examples

```turtle
# Automotive Simulator Ontology
@base <https://w3id.org/gaia-x4plcaad/ontologies/automotive-simulator/v2/> .
@prefix as: <https://w3id.org/gaia-x4plcaad/ontologies/automotive-simulator/v2/> .

as:Vehicle a owl:Class ;
    rdfs:label "Vehicle"@en ;
    rdfs:comment "A motorized entity capable of motion"@en .
```

### Governance and Versioning

- **Stable Release Cycle**: Releases follow semantic versioning (v1.0, v2.0, etc.)
- **Backwards Compatibility**: Version increments respect OWL versioning guidelines
- **Import Management**: Ontologies import specific versions of dependencies
- **Publication**: All ontologies published through w3id.org with GitHub artifact backing

### Cross-Domain Imports

GAIA-X ontologies reference each other for compositional modeling:

```turtle
# Example: simulation-model imports from scenario and description
@prefix scenario: <https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/> .
@prefix description: <https://w3id.org/gaia-x4plcaad/ontologies/description/v2/> .

gx:SimulationRun owl:imports scenario:Scenario ;
    owl:imports description:Entity .
```

## ENVITED-X Domain

### Project Context

ENVITED-X (2024+) represents the post-GAIA-X era, focusing on exploitation and extended autonomous vehicle technology. It expands beyond GAIA-X scope with additional domain-specific ontologies while maintaining compatibility where possible.

**Key Characteristics:**

- Newer namespace reflecting post-project independence
- Active development with frequent updates
- Lighter governance suitable for rapid iteration
- Experimental cross-domain integration approaches
- Building on GAIA-X foundations but diverging for innovation

### Ontologies in This Domain

```
artifacts/
├── envited-x/               # Core ENVITED-X coordination ontology
├── survey/                  # Survey and assessment methodologies
├── tzip21/                  # Specific domain applications
└── [additional ontologies in development]
```

### IRI Pattern Examples

```turtle
@base <https://w3id.org/ascs-ev/envited-x/core/v1/> .
@prefix ex: <https://w3id.org/ascs-ev/envited-x/core/v1/> .

ex:AutonomousSystem a owl:Class ;
    rdfs:label "Autonomous System"@en ;
    rdfs:comment "System with autonomous decision-making capabilities"@en .
```

### Development and Versioning

- **Rapid Iteration**: Updates released more frequently than GAIA-X
- **Experimental Features**: New concepts tested in ENVITED-X before possible GAIA-X adoption
- **Semantic Versioning**: Major.Minor.Patch (e.g., v1.0.0)
- **Publication**: Similar w3id.org approach with GitHub backing

### Cross-Domain Imports and Compatibility

ENVITED-X ontologies can reference GAIA-X ontologies for foundational concepts while adding new extensions:

```turtle
# Example: ENVITED-X extending GAIA-X foundations
@prefix gx-service: <https://w3id.org/gaia-x4plcaad/ontologies/service/v2/> .

ex:EnhancedService rdfs:subClassOf gx-service:Service ;
    rdfs:label "Enhanced Service"@en ;
    rdfs:comment "Service with ENVITED-X extensions"@en .
```

## Interoperability and Cross-Domain References

### When to Import from GAIA-X

Use GAIA-X ontologies when:

- Seeking stable, well-governed concepts
- Working with GAIA-X partner systems or infrastructure
- Needing production-ready semantics with version stability
- Implementing core autonomous driving concepts

### When to Use ENVITED-X

Use ENVITED-X ontologies when:

- Exploring new domains or experimental features
- Rapid prototyping with potential future evolution
- Implementing post-GAIA-X autonomous vehicle technologies
- Contributing to expanding the ontology ecosystem

### Integration Best Practices

1. **Version Pinning**: Always explicitly specify versions in imports

   ```turtle
   owl:imports <https://w3id.org/gaia-x4plcaad/ontologies/service/v2/> ;
   ```

2. **Namespace Isolation**: Use distinct prefixes for each domain

   ```turtle
   @prefix gx-svc: <https://w3id.org/gaia-x4plcaad/ontologies/service/v2/> .
   @prefix ex-svc: <https://w3id.org/ascs-ev/envited-x/service/v1/> .
   ```

3. **Bridging Classes**: Create alignment ontologies for cross-domain mapping if needed
   ```turtle
   ex:ServiceAlignment rdfs:comment "Maps GAIA-X services to ENVITED-X extensions"@en .
   ```

## Migration and Future Direction

### Consolidation Possibilities

If both domains need to converge (unlikely in near term):

- Maintain backward-compatible imports in new unified namespace
- Version both as separate branches initially
- Coordinate through shared governance committee

### Long-term Evolution

- **GAIA-X**: Remain stable foundation; selective evolutionary updates
- **ENVITED-X**: Lead innovation and experimental modeling; proven concepts may graduate to GAIA-X

## See Also

- [W3ID Publishing Guide](06-w3id-publishing.md) - Technical details on IRI resolution and content negotiation
- [GAIA-X Ontology Domain](../3-ontology-domains/gaia-x4plcaad/01-index.md) - Complete GAIA-X ontologies list and documentation
- [ENVITED-X Ontology Domain](../3-ontology-domains/envited-x/01-index.md) - ENVITED-X ontologies and roadmap
- [Architecture Overview](01-index.md) - Broader architectural context
