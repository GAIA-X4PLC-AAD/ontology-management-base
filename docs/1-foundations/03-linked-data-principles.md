# Linked Data Principles

This document explains the principles of Linked Data and how they're applied in this ontology repository.

## What is Linked Data?

**Linked Data** is a set of best practices for publishing and connecting structured data on the web using standard web technologies (HTTP, URIs, RDF).

**Core Idea:** Data on the web should be:

1. Accessible via standard HTTP
2. Identified by persistent URIs/IRIs
3. Expressed using open standards (RDF)
4. Linked to other data for context

## The Four Principles

### 1. Use URIs as Names for Things

Every concept, ontology, and piece of data should have a unique, persistent Internationalized Resource Identifier (IRI).

**Good Example:**

```
https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/Scenario
```

This IRI:

- Is globally unique
- Is resolvable (you can visit it in a browser)
- Persists over time
- Points to a specific concept in a specific ontology version

**Bad Example:**

```
Scenario
scenario
my_scenario
```

These don't tell you:

- Which ontology they belong to
- Which version
- Where to find them

### 2. Use HTTP URIs so that People Can Look Up Those Names

IRIs should be resolvable using standard HTTP. When someone visits the IRI, they should get useful information.

**In this repository:**

```
https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/
```

When you visit this URL, the w3id.org service:

- Detects your Accept header (what format you want)
- Returns the ontology in your requested format (Turtle, JSON-LD, RDF/XML)
- Provides documentation or landing page for browsers

**Supported Formats:**

| Accept Header                 | Result                     |
| ----------------------------- | -------------------------- |
| `Accept: text/turtle`         | Turtle-formatted ontology  |
| `Accept: application/ld+json` | JSON-LD formatted ontology |
| `Accept: application/rdf+xml` | RDF/XML formatted ontology |
| `Accept: text/html`           | HTML documentation page    |

### 3. When Someone Looks Up an IRI, Provide Useful Information

IRIs must resolve to meaningful data, not errors. The information returned should describe the resource and link to related resources.

**Good Response (RDF/Turtle):**

```turtle
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/Scenario>
    a owl:Class ;
    rdfs:label "Scenario"@en ;
    rdfs:comment "A test or operational scenario"@en ;
    rdfs:isDefinedBy <https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/> ;
    rdfs:seeAlso <https://w3id.org/gaia-x4plcaad/ontologies/simulation-model/v2/> ;
    rdfs:subClassOf <https://w3id.org/gaia-x4plcaad/ontologies/general/v2/Entity> .
```

This response:

- Identifies what the resource is (an OWL Class)
- Provides human-readable labels and comments
- Links back to the defining ontology
- Links to related concepts
- Shows the class hierarchy

### 4. Include Links to Other IRIs When You Publish Data

Resources should link to other resources, creating a web of connected data.

**In OWL Ontologies:**

```turtle
@prefix scenario: <https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/> .
@prefix general: <https://w3id.org/gaia-x4plcaad/ontologies/general/v2/> .
@prefix env: <https://w3id.org/gaia-x4plcaad/ontologies/environment-model/v2/> .

scenario:Scenario
    rdfs:subClassOf general:Entity ;  # Link to parent class
    rdfs:comment "Scenario in an environment" ;
    rdfs:seeAlso env:EnvironmentalFeature ;  # Link to related concept
    .
```

**In Data Instances:**

```turtle
@prefix gx-scenario: <https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/> .
@prefix my-app: <https://my-company.example.com/scenarios/> .

my-app:scenario-001
    a gx-scenario:Scenario ;  # Link to ontology class
    ex:relatedScenario my-app:scenario-002 ;  # Link to other scenario
    ex:usesOntology <https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/> .
```

## Why Linked Data Matters

### 1. Interoperability

When different systems use the same IRIs, they can understand each other's data automatically.

**Scenario:**

- System A uses `https://w3id.org/gaia-x4plcaad/ontologies/service/v2/Service`
- System B uses the same IRI
- They can exchange data and understand it means the same thing

### 2. Discoverability

Following links makes it possible to discover related resources and build graphs of information.

**Scenario:**

- You fetch one ontology
- It links to imported ontologies
- You can automatically discover the full dependency tree

### 3. Longevity

Persistent IRIs and HTTP access mean data remains accessible even when source systems change.

**Scenario:**

- A company moves their server
- The w3id.org IRI remains the same and redirects to the new location
- All links still work

### 4. Semantic Clarity

Using standardized vocabularies and explicit links ensures machine-readable meaning.

**Scenario:**

- Instead of a field called `color: "red"`
- You use `https://example.com/property/hasColor` with value `"red"`
- Systems can understand the field's meaning

## Linked Data in This Repository

### Ontology IRIs

Each ontology has a persistent, versioned IRI:

```
https://w3id.org/gaia-x4plcaad/ontologies/{ontology}/v{major}/
```

**Examples:**

- `https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/`
- `https://w3id.org/gaia-x4plcaad/ontologies/service/v2/`
- `https://w3id.org/ascs-ev/envited-x/autonomous-system/v1.0/`

### Class and Property IRIs

Every class and property has an IRI:

```
https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/Scenario
https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/hasEnvironment
```

### Namespace Organization

Ontologies are organized under domain namespaces:

```
https://w3id.org/gaia-x4plcaad/ontologies/
├── scenario/v2/
├── service/v2/
├── automotive-simulator/v2/
└── ... (other ontologies)

https://w3id.org/ascs-ev/envited-x/
├── core/v1.0/
├── autonomous-system/v1.0/
└── ... (other ontologies)
```

### Linked Ontologies

Ontologies link to each other through imports:

```turtle
@prefix scenario: <https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/> .
@prefix env: <https://w3id.org/gaia-x4plcaad/ontologies/environment-model/v2/> .
@prefix general: <https://w3id.org/gaia-x4plcaad/ontologies/general/v2/> .

scenario: a owl:Ontology ;
    owl:imports env: ;    # Links to environment-model ontology
    owl:imports general: ;  # Links to general ontology
    rdfs:seeAlso <https://w3id.org/ascs-ev/envited-x/core/v1.0/> ;  # Cross-namespace link
    .
```

### Registry

The central registry (`docs/registry.json`) links to all ontologies:

```json
{
  "ontologies": [
    {
      "name": "scenario",
      "namespace": "gaia-x4plcaad",
      "version": "v2",
      "iri": "https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/",
      "artifactPath": "artifacts/scenario/scenario.owl.ttl"
    }
  ]
}
```

## Best Practices for Linked Data

### 1. Use Persistent IRIs

✅ **Good:**

```turtle
ex:vehicle-001 a gx:Vehicle ;
    ex:hasOwner ex:person-john .
```

❌ **Bad:**

```turtle
ex:vehicle-001 a gx:Vehicle ;
    ex:owner "John Smith" .  # String instead of IRI
```

### 2. Version Your Ontologies

✅ **Good:**

```turtle
owl:imports <https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/> ;
```

❌ **Bad:**

```turtle
owl:imports <https://example.com/scenario/> ;  # No version
```

### 3. Use Published Ontology IRIs

✅ **Good:**

```turtle
ex:MyScenario a <https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/Scenario> ;
```

❌ **Bad:**

```turtle
ex:MyScenario a "Scenario" ;  # String literal
```

### 4. Document Your IRIs

✅ **Good:**

```turtle
ex:hasComplexity
    a owl:DatatypeProperty ;
    rdfs:label "Complexity Level"@en ;
    rdfs:comment "Numerical complexity from 1-10"@en ;
    rdfs:domain gx:Scenario ;
    rdfs:range xsd:integer ;
    .
```

❌ **Bad:**

```turtle
ex:complexity a owl:DatatypeProperty .
```

### 5. Link Related Resources

✅ **Good:**

```turtle
scenario:Scenario
    rdfs:isDefinedBy <https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/> ;
    rdfs:seeAlso simulation:SimulationRun ;
    rdfs:seeAlso env:EnvironmentalFeature ;
    .
```

❌ **Bad:**
No links between related concepts

## Implications for Users and Developers

### For Data Consumers

- You can fetch ontology definitions in multiple formats
- IRIs are stable and resolvable
- You can follow links to understand data relationships
- You can compose ontologies by following imports

### For Data Producers

- Give everything a persistent IRI
- Make those IRIs resolvable over HTTP
- Return useful information at those IRIs
- Link to other relevant resources

### For Ontology Designers

- Use published ontology IRIs in your definitions
- Import other ontologies by their IRIs
- Provide human-readable labels and comments
- Create links between related concepts

## Example: Following Linked Data

**Starting point:**

```
https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/Scenario
```

**Following the links:**

1. Fetch with `Accept: text/turtle` → Get the Scenario class definition
2. See it imports `https://w3id.org/gaia-x4plcaad/ontologies/general/v2/`
3. Fetch that ontology → Discover Entity class
4. See seeAlso links to `https://w3id.org/gaia-x4plcaad/ontologies/environment-model/v2/`
5. Fetch that ontology → Discover EnvironmentalFeature class
6. Now you have a connected understanding of the concept space

All without manual searching—just following links!

## See Also

- [RDF, OWL, and SHACL](02-rdf-owl-shacl.md) - Technical implementation details
- [W3ID Publishing](../2-architecture/06-w3id-publishing.md) - How IRIs are resolved
- [Ontology Discovery](../2-architecture/03-ontology-discovery.md) - How to find ontologies
- [Linked Data Best Practices](https://www.w3.org/DesignIssues/LinkedData.html) - W3C official guide
