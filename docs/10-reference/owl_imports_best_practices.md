# OWL Imports Best Practices and Analysis

## Executive Summary

This document analyzes the current `owl:imports` usage across the ontology repository and establishes best practices for when and how to use `owl:imports` statements, based on W3C specifications and repository analysis.

**Current State:** Only 1 out of 18 ontologies uses `owl:imports`, yet most ontologies reference external concepts. This creates implicit dependencies that should be made explicit.

---

## 1. Understanding owl:imports vs Prefix Declarations

### 1.1 Fundamental Difference

| Aspect         | Prefix Declaration                     | owl:imports                                 |
| -------------- | -------------------------------------- | ------------------------------------------- |
| **Purpose**    | Syntactic convenience for writing URIs | Semantic inclusion of another ontology      |
| **Effect**     | Shorthand notation only                | Imports ALL axioms, classes, and properties |
| **Scope**      | Local to the file                      | Affects ontology semantics                  |
| **Transitive** | No                                     | Yes (imports closure)                       |

### 1.2 Prefix Declaration Example

```turtle
@prefix general: <https://w3id.org/gaia-x4plcaad/ontologies/general/v3/> .
```

**Effect:** You can write `general:Description` instead of `<https://w3id.org/gaia-x4plcaad/ontologies/general/v3/Description>`

**What it does NOT do:**

- Does NOT import any definitions
- Does NOT make classes/properties from `general:` available for reasoning
- Does NOT validate that referenced IRIs exist

### 1.3 owl:imports Example

```turtle
<https://w3id.org/gaia-x4plcaad/ontologies/automotive-simulator/v1> a owl:Ontology ;
    owl:imports <https://w3id.org/gaia-x4plcaad/ontologies/general/v3> .
```

**Effect:** Imports the ENTIRE general ontology into automotive-simulator

**What it DOES do:**

- Makes ALL classes, properties, and axioms from general available
- Creates dependency that tools must resolve
- Enables reasoning over the combined ontology
- Transitive: if general imports X, automotive-simulator also imports X

---

## 2. When to Use owl:imports

### 2.1 The Core Principle

**Use `owl:imports` when your ontology DEFINES classes or properties that USE (reference, subclass, restrict) concepts from another ontology.**

### 2.2 Decision Matrix

| Your Ontology Does...                        | Use owl:imports? | Reason                                                                                          |
| -------------------------------------------- | ---------------- | ----------------------------------------------------------------------------------------------- |
| **Subclasses external class**                | ✅ YES           | `automotive-simulator:AutomotiveSimulator rdfs:subClassOf gx:DataResource` needs gx definitions |
| **Uses external property**                   | ✅ YES           | `scenario:hasManifest rdfs:range manifest:Manifest` needs manifest definitions                  |
| **References external class in restriction** | ✅ YES           | `owl:allValuesFrom envited-x:DataResource` needs envited-x definitions                          |
| **Only mentions in documentation**           | ❌ NO            | `rdfs:comment "See also gx:DataResource"` is just text                                          |
| **Used only in instances (JSON-LD)**         | ❌ NO            | Instance files can reference anything via @context                                              |
| **Used only in SHACL constraints**           | ⚠️ DEPENDS       | If ontology defines classes, YES. If only validation rules, NO (SHACL imports ontology instead) |

### 2.3 Real Examples from This Repository

#### ✅ CORRECT: automotive-simulator Ontology

```turtle
<https://w3id.org/gaia-x4plcaad/ontologies/automotive-simulator/v1> a owl:Ontology ;
    owl:imports <https://w3id.org/gaia-x4plcaad/ontologies/general/v3> ;
    # ... other metadata ...

automotive-simulator:AutomotiveSimulator a owl:Class ;
    rdfs:subClassOf gx:DataResource ;  # Uses external class!
    # ... properties that reference general:Description would also justify import
```

**Why imports general?**

- Although it subclasses `gx:DataResource`, the general ontology is imported
- **ISSUE IDENTIFIED:** Should also import gx ontology OR use general concepts
- automotive-simulator likely has properties that reference `general:Description` (common pattern)

#### ❌ INCORRECT: scenario Ontology (Current State)

```turtle
<https://w3id.org/ascs-ev/envited-x/scenario/v5> a owl:Ontology ;
    # NO owl:imports!

scenario:Scenario a owl:Class ;
    # But the ontology likely has properties like:
    # scenario:hasManifest rdfs:range manifest:Manifest ;
    # Uses manifest:, envited-x:, georeference: concepts without importing!
```

**Why this is problematic:**

- Ontology uses external concepts but doesn't declare dependency
- Reasoners can't find referenced class definitions
- Validation tools can't resolve the full ontology closure

---

## 3. Current Repository Analysis

### 3.1 Import Status by Ontology

| Ontology                 | Has owl:imports? | Prefixes Used                                                          | Should Import?                             |
| ------------------------ | ---------------- | ---------------------------------------------------------------------- | ------------------------------------------ |
| **automotive-simulator** | ✅ YES (general) | gx, openlabel                                                          | ⚠️ Partial - missing gx import             |
| **scenario**             | ❌ NO            | envited-x, manifest, georeference, hdmap, environment-model, openlabel | ✅ YES - should import envited-x, manifest |
| **hdmap**                | ❌ NO            | envited-x, manifest, georeference, openlabel                           | ✅ YES - should import envited-x, manifest |
| **environment-model**    | ❌ NO            | envited-x, manifest, georeference                                      | ✅ YES - should import envited-x, manifest |
| **surface-model**        | ❌ NO            | envited-x, manifest, georeference, gx                                  | ✅ YES - should import envited-x, manifest |
| **manifest**             | ❌ NO            | (self-contained)                                                       | ✅ MAYBE - check if it extends gx concepts |
| **ositrace**             | ❌ NO            | envited-x, manifest, georeference                                      | ✅ YES - should import envited-x, manifest |
| **simulated-sensor**     | ❌ NO            | (self-contained?)                                                      | 🔍 NEEDS ANALYSIS                          |
| **simulation-model**     | ❌ NO            | general                                                                | ✅ YES - should import general             |
| **survey**               | ❌ NO            | general                                                                | ✅ YES - should import general             |
| **georeference**         | ❌ NO            | (self-contained?)                                                      | 🔍 NEEDS ANALYSIS                          |
| **envited-x**            | ❌ NO            | manifest                                                               | ✅ YES - should import manifest            |
| **general**              | ❌ NO            | gx                                                                     | ✅ YES - if it extends gx:DataResource     |

### 3.2 Critical Issues Identified

#### Issue 1: Implicit Dependencies

**Problem:** Most ontologies use external concepts without declaring `owl:imports`

**Impact:**

- Reasoners cannot build complete inference closure
- Ontology editors (Protégé) cannot resolve referenced classes
- Validation tools cannot verify that referenced IRIs exist
- Circular dependency detection is impossible

**Example:**

```turtle
# scenario_ontology.ttl
@prefix envited-x: <https://w3id.org/ascs-ev/envited-x/envited-x/v3/> .

# Somewhere in the file:
scenario:hasManifest rdfs:range manifest:Manifest .
```

Without `owl:imports`, reasoners don't know what `manifest:Manifest` is.

#### Issue 2: automotive-simulator Import Mismatch

**Problem:** automotive-simulator imports general but:

- Doesn't declare `general:` prefix
- Uses `gx:` prefix (which might come from general) but doesn't directly import gx
- Declares `openlabel:` prefix but never uses it

**Impact:**

- Unclear what concepts from general are actually used
- Implicit dependency on gx through general's imports
- Unused prefix declarations clutter the file

#### Issue 3: SHACL vs Ontology Divergence

**Observation:** SHACL files correctly declare prefixes for external shapes they reference, but ontology files don't do the same for external classes/properties.

**Pattern:**

```turtle
# automotive-simulator_shacl.ttl
@prefix general: <https://w3id.org/gaia-x4plcaad/ontologies/general/v3/> .
@prefix simulated-sensor: <https://w3id.org/gaia-x4plcaad/ontologies/simulated-sensor/v2> .

<https://w3id.org/gaia-x4plcaad/ontologies/automotive-simulator/v1/shapes>
    a owl:Ontology ;
    owl:imports <https://w3id.org/gaia-x4plcaad/ontologies/automotive-simulator/v1> .

automotive-simulator:AutomotiveSimulatorShape a sh:NodeShape ;
    sh:property [
        sh:node general:GeneralShape ;  # References external shape
```

**But automotive-simulator_ontology.ttl doesn't declare `general:` prefix!**

---

## 4. Best Practices (W3C-Aligned)

### 4.1 When to Import

✅ **DO import when you:**

1. Subclass an external class
2. Use an external property in domain/range restrictions
3. Reference external classes in property restrictions (owl:allValuesFrom, owl:someValuesFrom)
4. Extend external property chains
5. Need the full semantics of the external ontology for reasoning

❌ **DO NOT import when you:**

1. Only mention external concepts in documentation (rdfs:comment, rdfs:seeAlso)
2. Reference external ontologies in metadata (dcterms:references)
3. Use external concepts only in instance data (JSON-LD files)
4. Need only the IRI for linking, not the full semantics

### 4.2 Import Closure Considerations

**Key principle from W3C:** owl:imports is transitive

```turtle
# If A imports B, and B imports C, then A also imports C
```

**Implication:** Be aware of deep import chains

- Check what your imports themselves import
- Can lead to large ontology closures
- May import more than intended

**Example:**

```turtle
automotive-simulator imports general
general imports gx
gx imports multiple other ontologies
→ automotive-simulator gets ALL of these!
```

### 4.3 Prefix Declaration Guidelines

**Always declare a prefix for any namespace you import:**

```turtle
<https://w3id.org/ascs-ev/envited-x/scenario/v5> a owl:Ontology ;
    owl:imports <https://w3id.org/ascs-ev/envited-x/envited-x/v3> ,
                <https://w3id.org/ascs-ev/envited-x/manifest/v5> ,
                <https://w3id.org/ascs-ev/envited-x/georeference/v5> .

@prefix scenario: <https://w3id.org/ascs-ev/envited-x/scenario/v5/> .
@prefix envited-x: <https://w3id.org/ascs-ev/envited-x/envited-x/v3/> .
@prefix manifest: <https://w3id.org/ascs-ev/envited-x/manifest/v5/> .
@prefix georeference: <https://w3id.org/ascs-ev/envited-x/georeference/v5/> .
```

**Don't declare prefixes you don't use in class/property definitions** (except for common metadata prefixes like dcterms, foaf, prov)

---

## 5. Relationship to @context in JSON-LD

### 5.1 Key Distinction

**@context in JSON-LD ≠ owl:imports in Ontology**

```json
{
  "@context": {
    "scenario": "https://w3id.org/ascs-ev/envited-x/scenario/v5/",
    "manifest": "https://w3id.org/ascs-ev/envited-x/manifest/v5/"
  },
  "@type": "scenario:Scenario",
  "scenario:hasManifest": {
    "@type": "manifest:Manifest"
  }
}
```

**What @context does:**

- Tells JSON-LD processor how to expand compact IRIs
- Purely for instance data
- Doesn't import any ontology definitions

**What it DOESN'T do:**

- Doesn't affect ontology semantics
- Doesn't create dependencies for reasoners
- Doesn't validate that IRIs exist

### 5.2 Independence Principle

**Instance files can reference ANY ontology in @context, regardless of what the ontology imports**

Example:

```turtle
# scenario_ontology.ttl might NOT import hdmap
owl:imports <https://w3id.org/ascs-ev/envited-x/envited-x/v3> .
```

```json
// scenario_instance.json CAN still reference hdmap
{
  "@context": {
    "scenario": "...",
    "hdmap": "..." // OK! Instance can reference hdmap even if ontology doesn't import it
  }
}
```

**Why this works:**

- Instances are not bound by ontology imports
- @context is for URI resolution, not semantic validation
- SHACL validation happens separately using the shapes graph

---

## 6. Relationship to SHACL Imports

### 6.1 SHACL Shapes MUST Import Their Domain Ontology

**Correct pattern (already implemented):**

```turtle
# automotive-simulator_shacl.ttl
<https://w3id.org/gaia-x4plcaad/ontologies/automotive-simulator/v1/shapes>
    a owl:Ontology ;
    owl:imports <https://w3id.org/gaia-x4plcaad/ontologies/automotive-simulator/v1> .
```

**Why:**

- SHACL validator needs class/property definitions to validate instances
- Shapes reference domain classes (sh:targetClass automotive-simulator:AutomotiveSimulator)
- Import ensures all definitions are available

### 6.2 SHACL Prefixes vs Ontology Prefixes

**SHACL files can (and should) declare additional prefixes for external shapes they reference:**

```turtle
# automotive-simulator_shacl.ttl
@prefix general: <https://w3id.org/gaia-x4plcaad/ontologies/general/v3/> .
@prefix simulated-sensor: <https://w3id.org/gaia-x4plcaad/ontologies/simulated-sensor/v2> .

automotive-simulator:AutomotiveSimulatorShape a sh:NodeShape ;
    sh:property [
        sh:node general:GeneralShape ;  # References external shape
    ] .
```

**But the domain ontology (automotive-simulator_ontology.ttl) might not need these prefixes if it doesn't define classes that reference those concepts.**

**Exception:** If the ontology DOES reference these concepts, it should:

1. Declare the prefix
2. Add owl:imports

---

## 7. Recommended Actions

### 7.1 Immediate Fixes Required

#### Fix 1: Add Missing owl:imports to Ontologies

Based on the analysis, these ontologies should add imports:

```turtle
# scenario_ontology.ttl
<https://w3id.org/ascs-ev/envited-x/scenario/v5> a owl:Ontology ;
    owl:imports <https://w3id.org/ascs-ev/envited-x/envited-x/v3> ,
                <https://w3id.org/ascs-ev/envited-x/manifest/v5> ;
    # Add georeference only if scenario defines properties with georeference ranges
```

```turtle
# hdmap_ontology.ttl
<https://w3id.org/ascs-ev/envited-x/hdmap/v5> a owl:Ontology ;
    owl:imports <https://w3id.org/ascs-ev/envited-x/envited-x/v3> ,
                <https://w3id.org/ascs-ev/envited-x/manifest/v5> ,
                <https://w3id.org/ascs-ev/envited-x/georeference/v5> ;
```

```turtle
# environment-model_ontology.ttl
<https://w3id.org/ascs-ev/envited-x/environment-model/v5> a owl:Ontology ;
    owl:imports <https://w3id.org/ascs-ev/envited-x/envited-x/v3> ,
                <https://w3id.org/ascs-ev/envited-x/manifest/v5> ,
                <https://w3id.org/ascs-ev/envited-x/georeference/v5> ;
```

```turtle
# surface-model_ontology.ttl
<https://w3id.org/ascs-ev/envited-x/surface-model/v6> a owl:Ontology ;
    owl:imports <https://w3id.org/ascs-ev/envited-x/envited-x/v3> ,
                <https://w3id.org/ascs-ev/envited-x/manifest/v5> ,
                <https://w3id.org/ascs-ev/envited-x/georeference/v5> ;
```

```turtle
# ositrace_ontology.ttl
<https://w3id.org/ascs-ev/envited-x/ositrace/v5> a owl:Ontology ;
    owl:imports <https://w3id.org/ascs-ev/envited-x/envited-x/v3> ,
                <https://w3id.org/ascs-ev/envited-x/manifest/v5> ,
                <https://w3id.org/ascs-ev/envited-x/georeference/v5> ;
```

```turtle
# simulation-model_ontology.ttl
<https://w3id.org/ascs-ev/envited-x/simulation-model/v2> a owl:Ontology ;
    owl:imports <https://w3id.org/gaia-x4plcaad/ontologies/general/v3> ;
```

```turtle
# survey_ontology.ttl (if it exists as a single file)
<https://w3id.org/ascs-ev/envited-x/survey/v6> a owl:Ontology ;
    owl:imports <https://w3id.org/gaia-x4plcaad/ontologies/general/v3> ;
```

```turtle
# envited-x_ontology.ttl
<https://w3id.org/ascs-ev/envited-x/envited-x/v3> a owl:Ontology ;
    owl:imports <https://w3id.org/ascs-ev/envited-x/manifest/v5> ;
```

#### Fix 2: Clean Up automotive-simulator

```turtle
# Remove unused prefix:
# @prefix openlabel: <https://openlabel.asam.net/V1-0-0/ontologies/> .

# Add missing prefix if using general concepts:
@prefix general: <https://w3id.org/gaia-x4plcaad/ontologies/general/v3/> .

# OR clarify that gx: concepts come from general's imports
```

### 7.2 Verification Steps

After adding owl:imports:

1. **Test in Protégé:**

   ```
   - Open ontology in Protégé
   - Check that imported classes are visible
   - Verify no circular import errors
   ```

2. **Test with Reasoner:**

   ```bash
   robot reason --input scenario_ontology.ttl --reasoner ELK
   ```

3. **Test Validation Script:**

   ```bash
   python3 src/tools/validation/validate_data_conformance.py scenario/scenario_instance.json --root .
   ```

   Should show registry correctly resolves ALL dependencies including transitive imports

4. **Check Import Closure:**

   ```bash
   robot merge --input scenario_ontology.ttl --output scenario_merged.ttl
   ```

   Inspect merged file to see full import closure

### 7.3 Long-term Maintenance

1. **New Ontology Checklist:**
   - [ ] For each prefix declared, ask: "Do I define classes/properties that USE this?"
   - [ ] If YES → Add owl:imports
   - [ ] If NO but needed for SHACL → Only add to SHACL file
   - [ ] If NO and only for instances → Only add to @context in JSON-LD

2. **Review Process:**
   - Before committing new ontology, verify imports match usage
   - Use linter or script to detect missing imports
   - Document justification if intentionally not importing

3. **Documentation:**
   - Update main README.md with import policy
   - Add examples of correct import patterns
   - Link to this best practices document

---

## 8. References

- [W3C OWL Imports Specification](https://www.w3.org/2007/OWL/wiki/Imports)
- [W3C OWL Web Ontology Language Reference](https://www.w3.org/TR/owl-ref/)
- [Protege Wiki: How OWL Imports Work](https://protegewiki.stanford.edu/wiki/How_Owl_Imports_Work)
- [bobdc.blog: Using owl:imports](https://www.bobdc.com/blog/using-owlincludes/)
- Repository Validation Strategy: `docs/ontology_repo_restructuring_for_validation.md`

---

**Document Version:** 1.0
**Last Updated:** 2026-01-31
**Status:** ANALYSIS COMPLETE - AWAITING IMPLEMENTATION
**Next Steps:** Apply recommended fixes to ontology files
