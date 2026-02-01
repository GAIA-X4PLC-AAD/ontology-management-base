# Semantic Versioning for Ontologies

This document explains how semantic versioning is applied to ontologies in this repository.

## Overview

**Semantic Versioning (SemVer)** is a standardized way of numbering releases that communicates the type and magnitude of changes made.

**Version Format:**

```
MAJOR.MINOR.PATCH

Example: 2.1.3
         ↑ ↑ ↑
         │ │ └── Patch: Bug fixes, clarifications
         │ └──── Minor: New features, backward compatible
         └────── Major: Breaking changes
```

## Version Numbers Explained

### MAJOR Version

Increment when making **breaking changes** that may affect existing users.

**Examples of breaking changes:**

- Removing a class or property
- Changing the meaning of a concept
- Making a previously optional property required
- Changing a property's domain or range incompatibly

**Example:**

```
Ontology v1.0.0 → v2.0.0

Reason: Removed deprecated concepts that users relied on
Impact: Systems using removed concepts must update
```

**In IRIs:**

```
https://w3id.org/gaia-x4plcaad/ontologies/scenario/v1/
https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/  ← New major version
```

Old version remains available and working!

### MINOR Version

Increment when adding **new features** in a backward-compatible way.

**Examples of minor changes:**

- Adding a new class
- Adding a new optional property
- Adding new constraints (if existing data still validates)
- Improving documentation or comments

**Example:**

```
Ontology v2.0.0 → v2.1.0

Reason: Added new class for autonomous vehicle type
Impact: No changes needed for existing users
```

**In IRIs:**

```
https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2.0/
https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2.1/  ← New minor version
```

Backward compatible—old code still works.

### PATCH Version

Increment for **bug fixes** and minor clarifications that don't change ontology semantics.

**Examples of patch changes:**

- Fixing typos in comments
- Clarifying rdfs:comment without changing meaning
- Correcting incorrect owl:deprecated statements
- Improving logical organization (cosmetic changes)

**Example:**

```
Ontology v2.1.0 → v2.1.1

Reason: Fixed typo in class documentation
Impact: No changes needed, fixes documentation clarity
```

**In IRIs:**

Usually patch versions are NOT explicitly in IRIs. Instead, they're indicated in the ontology itself:

```turtle
<https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/> a owl:Ontology ;
    owl:versionInfo "2.1.1"@en ;
    .
```

The IRI stays `v2` because v2.1.1 is a patch update to v2.

## OWL Version Properties

### owl:versionIRI

The **canonical IRI for this specific version**:

```turtle
@base <https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/> .

<> a owl:Ontology ;
    owl:versionIRI <https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/> ;
    owl:versionInfo "2.0.0"@en ;
    .
```

The base IRI and versionIRI should match for consistency.

### owl:versionInfo

A **human-readable version string**:

```turtle
<https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/> a owl:Ontology ;
    owl:versionInfo "2.1.3"@en ;
    .
```

### owl:imports with Versions

Always import **specific versions** to avoid breaking changes:

```turtle
@prefix scenario: <https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/> .
@prefix general: <https://w3id.org/gaia-x4plcaad/ontologies/general/v2/> .

<> a owl:Ontology ;
    owl:imports scenario: ;   # ✅ Good: Version pinned
    owl:imports general: ;
    .
```

Not:

```turtle
owl:imports <https://w3id.org/gaia-x4plcaad/ontologies/scenario/> ;  # ❌ Bad: Unversioned
```

### owl:priorVersion

Links to the previous version:

```turtle
<https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/> a owl:Ontology ;
    owl:versionInfo "2.0.0"@en ;
    owl:priorVersion <https://w3id.org/gaia-x4plcaad/ontologies/scenario/v1/> ;
    .
```

This helps systems understand version history.

## Versioning Decisions in This Repository

### GAIA-X Ontologies

**Current Strategy:**

- Major versions in the IRI (v1, v2, v3)
- Patch versions tracked in owl:versionInfo
- Minor versions NOT included in IRI for simplicity
- Long-term stability goal

**Example:**

```
IRI: https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/
owl:versionInfo: "2.3.5"
```

This represents:

- Major version 2 (in IRI)
- Minor version 3 (in versionInfo)
- Patch version 5 (in versionInfo)

**Rationale:**

- GAIA-X values stability
- Major changes warrant new IRI
- Minor improvements backward compatible
- Simpler IRI structure

### ENVITED-X Ontologies

**Current Strategy:**

- Semantic versioning in the IRI (v1.0, v1.1, etc.)
- Compatible with rapid iteration
- Explicit minor versions for tracking evolution
- Pre-1.0 versions use v0.x for experimental ontologies

**Example:**

```
IRI: https://w3id.org/ascs-ev/envited-x/autonomous-system/v1.1/
owl:versionInfo: "1.1.3"
```

**Rationale:**

- ENVITED-X expects more frequent releases
- Explicit minor versions help users track evolution
- Pre-1.0 signals experimental status
- Full semantic versioning transparency

## Practical Workflow

### When to Release a New Version

**Release v2.1.0 (minor) if you:**

- Add a new optional class
- Add new optional properties
- Improve documentation substantially
- Want to mark a release milestone

**Release v2.0.0 (major) if you:**

- Remove or rename existing classes
- Change property domains/ranges
- Make previously optional properties required
- Significantly restructure the ontology

**Release v2.0.1 (patch) if you:**

- Fix documentation typos
- Clarify comments without changing meaning
- Correct a logical error that doesn't affect instances
- Need to push a quick clarification

### Example Release

**Scenario: Adding a new sensor type to automotive-simulator ontology**

**Current state:**

```
automotive-simulator v2 ontology
owl:versionInfo "2.3.0"
```

**Changes made:**

```turtle
# New class added (backward compatible)
as:UltrasonicSensor a owl:Class ;
    rdfs:subClassOf as:Sensor ;
    rdfs:label "Ultrasonic Sensor"@en ;
    .
```

**Decision:** This is a minor version bump (new feature, backward compatible)

**New version:**

```
automotive-simulator v2 ontology
owl:versionInfo "2.4.0"
```

**Update the ontology file:**

```turtle
<https://w3id.org/gaia-x4plcaad/ontologies/automotive-simulator/v2/>
    a owl:Ontology ;
    owl:versionInfo "2.4.0"@en ;
    owl:priorVersion <previous-version-iri> ;
    dct:issued "2024-02-01"^^xsd:date ;
    .
```

**Old version remains:**

```
https://w3id.org/gaia-x4plcaad/ontologies/automotive-simulator/v2/
   → Version 2.3.0 (still available, still works)
```

## User Impact: Backward Compatibility

### Old Code Still Works

If you're using GAIA-X scenario v2.0.0:

```turtle
@prefix scenario: <https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/> .

my-scenario:scenario-001
    a scenario:Scenario ;
    scenario:hasComplexity "high" ;
    .
```

And the ontology is updated to v2.4.0, **your code still works** because:

- No classes were removed
- No properties were removed
- No meanings were changed
- Only new optional features were added

### When You MUST Update

Only if a major version changes (v2 → v3):

```turtle
# Old import
owl:imports <https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/> ;

# Must update to
owl:imports <https://w3id.org/gaia-x4plcaad/ontologies/scenario/v3/> ;
```

Major versions may break compatibility. Your code needs review.

## Version Deprecation

### Deprecation Process

1. **Version N is current**

   ```
   Scenario v3.0.0 (current)
   ```

2. **New features in v3.1.0**

   ```
   Scenario v3.1.0 (current)
   ```

3. **New major version v4.0.0 planned**

   ```
   Scenario v4.0.0 introduces breaking changes
   ```

4. **During development, mark v3 as deprecated**

   ```turtle
   <https://w3id.org/gaia-x4plcaad/ontologies/scenario/v3/>
       owl:deprecated true ;
       owl:deprecatedProperty [
           rdfs:label "Migrate to scenario v4"@en ;
       ] ;
       .
   ```

5. **Set end-of-life date**

   ```turtle
   <https://w3id.org/gaia-x4plcaad/ontologies/scenario/v3/>
       dcat:endOfLife "2025-12-31"^^xsd:date ;
       .
   ```

6. **Old version still works for 12+ months**
   - Systems can plan migration
   - Documentation provided
   - Support available

### Best Practices for Deprecation

- Announce deprecation 12+ months before removal
- Provide clear migration path
- Maintain old version during transition
- Offer tools or mapping documents
- Document the reasons for change

## Release Checklist

Before releasing a new ontology version:

- [ ] **Decide version type**: Major, Minor, or Patch?
- [ ] **Test ontology**: Validate with OWL reasoner
- [ ] **Check imports**: All imported ontologies specified with versions
- [ ] **Update version strings**: Update owl:versionInfo and owl:versionIRI
- [ ] **Document changes**: Create release notes describing what changed
- [ ] **Update PROPERTIES.md**: Regenerate with new version
- [ ] **Registry update**: Update docs/registry.json with new version
- [ ] **w3id configuration**: Ensure w3id.org routes new version correctly
- [ ] **Test resolution**: Verify IRI resolves to correct ontology file
- [ ] **Announce**: Notify users of new version availability

## See Also

- [OWL Specification - Versioning](https://www.w3.org/TR/owl2-syntax/#Ontology_URIs_and_Version_IRIs) - W3C official guide
- [W3ID Publishing](../2-architecture/06-w3id-publishing.md) - How versions are published and resolved
- [Ontology Discovery](../2-architecture/03-ontology-discovery.md) - How to find specific versions
- [Building & Contributing - Release Process](../5-building-contributing/04-release.md) - Detailed release process
