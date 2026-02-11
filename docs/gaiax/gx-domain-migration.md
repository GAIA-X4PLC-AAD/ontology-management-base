# Domain Migration Guide

Per-domain migration status for the ENVITED-X asset wrapper classes. See [GX Integration Pattern](gx-integration-pattern.md) for the underlying concept.

## Migration Overview

Each domain previously declared its main class as `rdfs:subClassOf gx:VirtualResource`. The migration changed each domain to subclass the appropriate envited-x wrapper class instead, replacing the deprecated `general:General` dependency with the three-layer wrapper pattern (GX base resource + DomainSpecification + Manifest).

### Domain Assignments

| Domain | Main Class | Wrapper | GX Type | Status |
|--------|-----------|---------|---------|--------|
| **hdmap** | `hdmap:HdMap` | `envited-x:SimulationAsset` | `gx:VirtualResource` | Already migrated (v2) |
| **ositrace** | `ositrace:OsiTrace` | `envited-x:SimulationAsset` | `gx:VirtualResource` | Already migrated (v2) |
| **scenario** | `scenario:Scenario` | `envited-x:SimulationAsset` | `gx:VirtualResource` | Already migrated (v2) |
| **environment-model** | `environment-model:EnvironmentModel` | `envited-x:SimulationAsset` | `gx:VirtualResource` | Already migrated (v2) |
| **surface-model** | `surface-model:SurfaceModel` | `envited-x:SimulationAsset` | `gx:VirtualResource` | Already migrated (v2) |
| **automotive-simulator** | `automotive-simulator:AutomotiveSimulator` | **`envited-x:SoftwareAsset`** | `gx:SoftwareResource` | Migrated |
| **simulation-model** | `simulation-model:SimulationModel` | **`envited-x:SoftwareAsset`** | `gx:SoftwareResource` | Migrated |
| **service** | `service:Service` | **`envited-x:ServiceAsset`** | `gx:ServiceOffering` | Migrated |
| **survey** | `survey:SurveyServiceOffering` | **`envited-x:ServiceAsset`** | `gx:ServiceOffering` | Migrated |
| **survey** | `survey:SurveyResultDataOffering` | **`envited-x:SimulationAsset`** | `gx:VirtualResource` | Migrated |
| **leakage-test** | `leakage-test:LeakageTest` | **`envited-x:CodeAsset`** | `gx:CodeArtifact` | Migrated |
| **vv-report** | `vv-report:VvReport` | **`envited-x:CodeAsset`** | `gx:CodeArtifact` | Migrated |
| **simulated-sensor** | `simulated-sensor:SimulatedSensor` | — | `gx:VirtualResource` | Not migrated |
| **tzip21** | `tzip21:Asset` | — | `gx:VirtualResource` | Not migrated |

!!! info "Domains not migrated"
    **simulated-sensor** remains as `rdfs:subClassOf gx:VirtualResource`. It is nested within automotive-simulator instances as a component — making it a SoftwareAsset would force every nested sensor node to carry `hasSoftwareResource` and `hasManifest`, breaking the composition pattern.

    **tzip21** remains as `rdfs:subClassOf gx:VirtualResource`. It uses the unique TZIP-21 NFT metadata standard with its own structure and already imports envited-x/v3. Since `gx:VirtualResource` is open (`sh:closed false`), no migration is needed for GX compliance.

!!! note "Survey dual-wrapper"
    The survey domain uses **two different wrappers**: `SurveyServiceOffering` extends `ServiceAsset` (with `hasServiceOffering` linking to `ServiceOfferingBase`), while `SurveyResultDataOffering` extends `SimulationAsset` (with `hasResourceDescription` linking to `ResourceDescription`). This reflects the semantic difference between a survey invitation (service) and survey results (data resource).

## Deprecated: `general` ontology

The `general` ontology (`artifacts/general/general.owl.ttl`) is marked as `owl:deprecated true`. Its role (common metadata like name, description, size) is superseded by the envited-x wrapper architecture:

- `general:name` / `general:description` → `gx:name` / `gx:description` (on ResourceDescription) or `schema:name` / `schema:description` (on SoftwareResourceBase, ServiceOfferingBase, CodeArtifactBase)
- `general:size` → `manifest:fileSize` (xsd:integer, in manifest FileMetadata)
- `general:recordingTime` → `manifest:timestamp` (xsd:dateTime, in manifest FileMetadata)
- `general:General` / `general:Data` / `general:Description` → no longer needed; the wrapper pattern handles metadata structuring

Domain ontologies that previously imported `general/v3` now import `envited-x/v3` instead.

## File Changes Per Domain

For each migrated domain, the following files were changed:

### 1. OWL definition (`artifacts/<domain>/<domain>.owl.ttl`)

- Changed `owl:imports` from `general/v3` to `envited-x/v3`
- Changed `rdfs:subClassOf gx:VirtualResource` to `rdfs:subClassOf envited-x:<WrapperClass>`
- Added `DomainSpecification`, `Content`, and optionally `Format` subclasses
- Added linking properties (`has<Resource>`, `hasDomainSpecification`, `hasManifest`, `hasContent`)
- Removed `general` property (replaced by wrapper pattern)
- Moved domain properties from main class domain to `Content`/`Format` domains

### 2. SHACL shapes (`artifacts/<domain>/<domain>.shacl.ttl`)

- Added wrapper shape validating three properties: `has<Resource>`, `hasDomainSpecification`, `hasManifest`
- Added `DomainSpecificationShape` requiring `hasContent`
- Added `ContentShape` with domain-specific property constraints (moved from main shape)
- Removed `general:GeneralShape` reference

### 3. Test data (`tests/data/<domain>/valid/<domain>_instance.json`)

- Restructured from flat to nested three-layer JSON-LD
- GX properties moved into resource node (Layer 1)
- Domain properties moved into DomainSpecification/Content nodes (Layer 3)
- Added manifest link (Layer 2)
- Updated `@context` prefixes

### 4. Manifest fixture (`tests/fixtures/<domain>_manifest_reference.json`)

- Created new manifest fixture with all 4 required artifact categories: `isSimulationData`, `isDocumentation`, `isMetadata`, `isMedia`
- `isMedia` artifact includes `manifest:hasDimensions` with width/height

### 5. Test catalog (`tests/catalog-v001.xml`)

- Added fixture entry for the new manifest reference

## Key Structural Changes

### Property migration pattern

For each domain, properties are reorganized into three layers:

| Property category | Before (flat) | After (nested) |
|---|---|---|
| GX compliance (name, description, etc.) | On domain node | On base resource node (Layer 1) |
| Domain metadata (e.g., `simulatorMake`, `formatType`) | On domain node | On `DomainSpecification` → `Content` / `Format` nodes (Layer 3) |
| Structural (`hasManifest`) | Not present | On domain node (Layer 2) |

!!! warning "GX properties vary by wrapper type"
    The allowed GX properties on the base resource node (Layer 1) differ by wrapper:

    | Wrapper | Base Class | Name/Description | `gx:license` | `gx:producedBy` |
    |---------|-----------|-----------------|--------------|-----------------|
    | SimulationAsset | `ResourceDescription` (gx:VirtualResource) | `gx:name` / `gx:description` | Allowed | Allowed |
    | SoftwareAsset | `SoftwareResourceBase` (gx:SoftwareResource) | `schema:name` / `schema:description` | Allowed | Not allowed (closed shape) |
    | ServiceAsset | `ServiceOfferingBase` (gx:ServiceOffering) | `schema:name` / `schema:description` | Not allowed | Not allowed (closed shape) |
    | CodeAsset | `CodeArtifactBase` (gx:CodeArtifact) | `schema:name` / `schema:description` | Allowed | Not allowed (effectively closed) |

    Only `gx:VirtualResource` is open (`sh:closed false`). All other GX base types have closed SHACL shapes that restrict which properties are permitted.

### Ontology import changes

```turtle
# Before
owl:imports <https://w3id.org/gaia-x4plcaad/ontologies/general/v3> .

# After
owl:imports <https://w3id.org/ascs-ev/envited-x/envited-x/v3> .
```

## Naming Changes (Part 2)

The envited-x base classes and properties were renamed for clarity:

| Old Name | New Name | Rationale |
|----------|----------|-----------|
| `DataResource` | `ResourceDescription` | Describes GX metadata; avoids confusion with removed `gx:DataResource` |
| `hasDataResource` | `hasResourceDescription` | Follows from class name |
| `DataResourceExtension` | `DomainSpecification` | Domain-specific structured metadata |
| `hasDataResourceExtension` | `hasDomainSpecification` | Follows from class name |

These renames affected all ENVITED-X domains (hdmap, scenario, ositrace, environment-model, surface-model) as well as the newly migrated domains.
