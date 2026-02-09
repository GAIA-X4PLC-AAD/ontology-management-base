# Domain Migration Guide

Per-domain migration plan for introducing the ENVITED-X asset wrapper classes. See [GX Integration Pattern](gx-integration-pattern.md) for the underlying concept.

## Migration Overview

Each domain currently declares its main class as `rdfs:subClassOf gx:VirtualResource`. The migration changes each domain to subclass the appropriate envited-x wrapper class instead, following the same pattern that `hdmap`, `ositrace`, `scenario`, `environment-model`, and `surface-model` already use with `SimulationAsset`.

### Domain Assignments

| Domain | Main Class | Current Parent | Target Wrapper | Target GX Type |
|--------|-----------|---------------|----------------|----------------|
| **hdmap** | `hdmap:HdMap` | `envited-x:SimulationAsset` | `envited-x:SimulationAsset` | `gx:VirtualResource` |
| **ositrace** | `ositrace:OsiTrace` | `envited-x:SimulationAsset` | `envited-x:SimulationAsset` | `gx:VirtualResource` |
| **scenario** | `scenario:Scenario` | `envited-x:SimulationAsset` | `envited-x:SimulationAsset` | `gx:VirtualResource` |
| **environment-model** | `environment-model:EnvironmentModel` | `envited-x:SimulationAsset` | `envited-x:SimulationAsset` | `gx:VirtualResource` |
| **surface-model** | `surface-model:SurfaceModel` | `envited-x:SimulationAsset` | `envited-x:SimulationAsset` | `gx:VirtualResource` |
| **automotive-simulator** | `automotive-simulator:AutomotiveSimulator` | `gx:VirtualResource` | **`envited-x:SoftwareAsset`** | `gx:SoftwareResource` |
| **simulated-sensor** | `simulated-sensor:SimulatedSensor` | `gx:VirtualResource` | **`envited-x:SoftwareAsset`** | `gx:SoftwareResource` |
| **simulation-model** | `simulation-model:SimulationModel` | `gx:VirtualResource` | **`envited-x:SoftwareAsset`** | `gx:SoftwareResource` |
| **service** | `service:Service` | `gx:VirtualResource` | **`envited-x:ServiceAsset`** | `gx:ServiceOffering` |
| **survey** | `survey:SurveyResultDataOffering` | `gx:VirtualResource` | **`envited-x:ServiceAsset`** | `gx:ServiceOffering` |
| **survey** | `survey:SurveyServiceOffering` | `gx:VirtualResource` | **`envited-x:ServiceAsset`** | `gx:ServiceOffering` |
| **tzip21** | `tzip21:Asset` | `gx:VirtualResource` | **`envited-x:ServiceAsset`** | `gx:ServiceOffering` |
| **leakage-test** | `leakage-test:LeakageTest` | `gx:VirtualResource` | **`envited-x:CodeAsset`** | `gx:CodeArtifact` |
| **vv-report** | `vv-report:VvReport` | `gx:VirtualResource` | **`envited-x:CodeAsset`** | `gx:CodeArtifact` |

!!! info "Already migrated"
    The first five domains (hdmap, ositrace, scenario, environment-model, surface-model) already use the `SimulationAsset` wrapper pattern. They require **no changes**.

## Migration Priority

| Priority | Domains | Rationale |
|----------|---------|-----------|
| **P0 — Prerequisite** | envited-x | Define new wrapper classes + base resources in `envited-x.owl.ttl` and `envited-x.shacl.ttl` |
| **P1 — Software** | automotive-simulator, simulated-sensor, simulation-model | Most semantically mismatched (software ≠ virtual resource) |
| **P2 — Code** | leakage-test, vv-report | Code artifacts with test/report semantics |
| **P3 — Service** | service, survey, tzip21 | Service offerings and marketplace assets |

## File Change Checklist Per Domain

For each domain being migrated, the following files need changes:

### 1. OWL definition (`artifacts/<domain>/<domain>.owl.ttl`)

- [ ] Change `rdfs:subClassOf gx:VirtualResource` → `rdfs:subClassOf envited-x:<WrapperClass>`
- [ ] Add `owl:imports` for the envited-x ontology (if not already present)
- [ ] Add domain-specific `DataResourceExtension`, `Content`, `Format` subclasses (following hdmap pattern)
- [ ] Add domain-specific object properties (`has<Domain>Resource`, etc.)

### 2. SHACL shapes (`artifacts/<domain>/<domain>.shacl.ttl`)

- [ ] Add a shape for the wrapper structure (`has<Resource>`, `hasManifest`, `hasDataResourceExtension`)
- [ ] Move GX property constraints to a separate resource shape (targeting the base resource class)
- [ ] Keep domain-specific property shapes on the domain extension shape

### 3. Context file (`artifacts/<domain>/<domain>.context.jsonld`)

- [ ] Add entries for new linking properties (`hasSoftwareResource`, etc.)
- [ ] Add entries for extension structure (`hasDataResourceExtension`, `hasContent`, `hasFormat`)

### 4. Test data (`tests/data/<domain>/valid/<domain>_instance.json`)

- [ ] Restructure from flat to nested format
- [ ] Move GX properties into the resource node (Layer 1)
- [ ] Move domain metadata into extension nodes (Layer 3)
- [ ] Add manifest link

### 5. Invalid test data (`tests/data/<domain>/invalid/`)

- [ ] Update to match the new nested structure
- [ ] Update `.expected` files for changed error messages

## Full Migration Example: automotive-simulator

### OWL Before

```turtle
# artifacts/automotive-simulator/automotive-simulator.owl.ttl (current)
automotive-simulator:AutomotiveSimulator a owl:Class ;
    rdfs:label "Class definition for AutomotiveSimulator"@en ;
    rdfs:comment "An implementation of an automotive simulator."@en ;
    rdfs:subClassOf gx:VirtualResource .
```

### OWL After

```turtle
# artifacts/automotive-simulator/automotive-simulator.owl.ttl (migrated)
@prefix envited-x: <https://w3id.org/ascs-ev/envited-x/envited-x/v3/> .
@prefix manifest: <https://w3id.org/ascs-ev/envited-x/manifest/v5/> .

automotive-simulator:AutomotiveSimulator a owl:Class ;
    rdfs:label "Class definition for AutomotiveSimulator"@en ;
    rdfs:comment "An implementation of an automotive simulator."@en ;
    rdfs:subClassOf envited-x:SoftwareAsset .

# Domain-specific extension classes
automotive-simulator:DataResourceExtension a owl:Class ;
    rdfs:label "Class definition for DataResourceExtension"@en ;
    rdfs:comment "Automotive simulator extension metadata."@en ;
    rdfs:subClassOf envited-x:DataResourceExtension .

automotive-simulator:Content a owl:Class ;
    rdfs:label "Class definition for Content"@en ;
    rdfs:comment "Content metadata for automotive simulator assets."@en ;
    rdfs:subClassOf envited-x:Content .

automotive-simulator:Format a owl:Class ;
    rdfs:label "Class definition for Format"@en ;
    rdfs:comment "Format metadata for automotive simulator assets."@en ;
    rdfs:subClassOf envited-x:Format .
```

### Instance Data Before

```json
{
  "@context": {
    "automotive-simulator": "https://w3id.org/gaia-x4plcaad/ontologies/automotive-simulator/v1/",
    "gx": "https://w3id.org/gaia-x/development#",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@id": "did:web:test.automotive-simulator.net:AutomotiveSimulator:test_instance",
  "@type": "automotive-simulator:AutomotiveSimulator",
  "automotive-simulator:simulatorMake": "CARLA",
  "automotive-simulator:softwareVersion": "0.9.15",
  "automotive-simulator:sensorFailureFlag": true,
  "automotive-simulator:sensorAttackFlag": true,
  "automotive-simulator:scenarioDefinition": ["ASAM OpenSCENARIO 2.x"],
  "automotive-simulator:interface": ["ROS1", "ROS2"],
  "gx:producedBy": { "@id": "did:web:..." },
  "gx:copyrightOwnedBy": { "@id": "did:web:..." },
  "gx:license": "EPL-2.0",
  "gx:containsPII": false,
  "gx:resourcePolicy": "allow intent"
}
```

### Instance Data After

```json
{
  "@context": {
    "automotive-simulator": "https://w3id.org/gaia-x4plcaad/ontologies/automotive-simulator/v1/",
    "envited-x": "https://w3id.org/ascs-ev/envited-x/envited-x/v3/",
    "manifest": "https://w3id.org/ascs-ev/envited-x/manifest/v5/",
    "gx": "https://w3id.org/gaia-x/development#",
    "sh": "http://www.w3.org/ns/shacl#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@id": "did:web:test.automotive-simulator.net:AutomotiveSimulator:test_instance",
  "@type": "automotive-simulator:AutomotiveSimulator",
  "automotive-simulator:hasSoftwareResource": {
    "@id": "did:web:registry.envited-x.net::SoftwareResourceBase:pX8mN4kL2vR9ZjW5bS7yH3cW1dGf6A8",
    "@type": "envited-x:SoftwareResourceBase",
    "gx:name": "CARLA Simulator Extension",
    "gx:description": "Modified CARLA simulator with sensor degradation models.",
    "gx:version": "0.9.15",
    "gx:license": "EPL-2.0",
    "gx:resourcePolicy": "allow intent",
    "gx:containsPII": false,
    "gx:copyrightOwnedBy": {
      "@id": "did:web:test.fixture.net:LegalPerson:test_gx_legalperson_reference"
    },
    "gx:producedBy": {
      "@id": "did:web:test.fixture.net:LegalPerson:test_gx_legalperson_reference"
    }
  },
  "automotive-simulator:hasDataResourceExtension": {
    "@type": "automotive-simulator:DataResourceExtension",
    "automotive-simulator:hasContent": {
      "@type": "automotive-simulator:Content",
      "automotive-simulator:simulatorMake": "CARLA",
      "automotive-simulator:sensorFailureFlag": true,
      "automotive-simulator:sensorAttackFlag": true
    },
    "automotive-simulator:hasFormat": {
      "@type": "automotive-simulator:Format",
      "automotive-simulator:softwareVersion": "0.9.15",
      "automotive-simulator:scenarioDefinition": [
        "ASAM OpenSCENARIO 2.x",
        "ASAM OpenSCENARIO 1.x",
        "scenic"
      ],
      "automotive-simulator:interface": ["ROS1", "ROS2", "TCP"]
    }
  },
  "automotive-simulator:hasManifest": {
    "@type": "manifest:Link",
    "manifest:iri": {
      "@id": "did:web:test.fixture.net:Manifest:test_automotive-simulator_manifest_reference"
    },
    "skos:note": {
      "@value": "Reference to the automotive simulator asset manifest.",
      "@type": "xsd:string"
    },
    "sh:conformsTo": [
      { "@id": "https://w3id.org/ascs-ev/envited-x/envited-x/v3/" },
      { "@id": "https://w3id.org/ascs-ev/envited-x/manifest/v5/" }
    ],
    "manifest:hasAccessRole": {
      "@type": "manifest:AccessRole",
      "@id": "envited-x:isPublic"
    },
    "manifest:hasCategory": {
      "@type": "manifest:Category",
      "@id": "envited-x:isManifest"
    },
    "manifest:hasFileMetadata": {
      "@type": "manifest:FileMetadata",
      "manifest:filePath": {
        "@value": "./base-references/automotive-simulator_manifest_reference.json",
        "@type": "xsd:anyURI"
      },
      "manifest:mimeType": {
        "@value": "application/ld+json",
        "@type": "xsd:string"
      }
    }
  }
}
```

## Key Structural Changes

### Property migration pattern

For each domain, properties are reorganized into three categories:

| Property category | Before (flat) | After (nested) |
|---|---|---|
| GX compliance (`gx:name`, `gx:license`, `gx:producedBy`, etc.) | On domain node | On `<Base>Resource` node (Layer 1) |
| Domain metadata (e.g., `simulatorMake`, `formatType`) | On domain node | On `DataResourceExtension` → `Content` / `Format` nodes (Layer 3) |
| Structural (`hasManifest`) | Not present | On domain node (Layer 2) |

### Ontology import changes

Domains that currently import only `gx:` will need to import the envited-x ontology:

```turtle
# Before
owl:imports <https://w3id.org/gaia-x4plcaad/ontologies/general/v3> .

# After
owl:imports <https://w3id.org/ascs-ev/envited-x/envited-x/v3> ,
            <https://w3id.org/gaia-x4plcaad/ontologies/general/v3> .
```

## Notes

- The `description` and `example` domains are for documentation and testing purposes. They should be updated to demonstrate the wrapper pattern but are not production domains.
- The `survey` domain has two classes (`SurveyResultDataOffering` and `SurveyServiceOffering`). Both should migrate to `ServiceAsset`.
- The `simulated-sensor` domain is closely tied to `automotive-simulator`. Both use `SoftwareAsset`.
