# RDF, OWL, and SHACL

This document explains the three core technologies that form the foundation of this ontology repository.

## The Stack

```
┌─────────────────────────────────────┐
│  Application (Your Code)            │
├─────────────────────────────────────┤
│  SHACL: Validation & Constraints    │
├─────────────────────────────────────┤
│  OWL: Semantics & Reasoning         │
├─────────────────────────────────────┤
│  RDF: Data Model & Serialization    │
├─────────────────────────────────────┤
│  URIs/IRIs: Resource Identification │
└─────────────────────────────────────┘
```

## RDF: The Foundation

### What is RDF?

**RDF (Resource Description Framework)** is a simple data model for representing information about resources on the web.

**Core Concept:** Everything is a triple (three-part statement):

```
Subject - Predicate - Object
```

### RDF Triples

| Part          | What It Is                   | Example                                 |
| ------------- | ---------------------------- | --------------------------------------- |
| **Subject**   | The thing being described    | `https://example.com/vehicles/car-123`  |
| **Predicate** | The property or relationship | `https://example.com/property/hasColor` |
| **Object**    | The value or target          | `"red"` (a literal) or another resource |

### Complete RDF Example

```turtle
@prefix ex: <https://example.com/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

# Resource: car-123
ex:car-123
    a ex:Vehicle ;           # RDF type (is-a relationship)
    ex:hasColor "red" ;      # Color property
    ex:hasSpeed 100 ;        # Speed property
    ex:hasOwner ex:john ;    # Reference to another resource
    rdfs:label "My Car" ;    # Human-readable label
    rdfs:comment "A red sedan" .  # Description
```

This represents 6 RDF triples:

1. `car-123` is-a `Vehicle`
2. `car-123` has color `"red"`
3. `car-123` has speed `100`
4. `car-123` has owner `john`
5. `car-123` has label `"My Car"`
6. `car-123` has comment `"A red sedan"`

### RDF Serialization Formats

RDF triples can be serialized (written) in multiple formats:

#### Turtle (Recommended for Authoring)

```turtle
@prefix ex: <https://example.com/> .
ex:car-123 ex:hasColor "red" ;
           ex:hasSpeed 100 .
```

#### JSON-LD (Recommended for Web APIs)

```json
{
  "@context": "https://example.com/context.jsonld",
  "@id": "https://example.com/car-123",
  "type": "Vehicle",
  "hasColor": "red",
  "hasSpeed": 100
}
```

#### RDF/XML (Recommended for XML Systems)

```xml
<?xml version="1.0"?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns:ex="https://example.com/">
  <rdf:Description rdf:about="https://example.com/car-123">
    <rdf:type rdf:resource="https://example.com/Vehicle"/>
    <ex:hasColor>red</ex:hasColor>
  </rdf:Description>
</rdf:RDF>
```

### Key RDF Concepts

**IRIs (Internationalized Resource Identifiers)**

- Global identifiers for everything: resources, properties, concepts
- Enable data to be linked across different systems
- Example: `https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/Scenario`

**Literals**

- Values like strings, numbers, dates, booleans
- Always appear as object of a triple
- Can have language tags: `"hello"@en`, `"hola"@es`

**Blank Nodes**

- Resources without explicit IRIs (locally identified)
- Useful for intermediate structures
- Less recommended for ontology design (prefer explicit IRIs)

## OWL: Adding Semantics

### What is OWL?

**OWL (Web Ontology Language)** extends RDF with richer semantic capabilities:

- Define **classes** (categories of resources)
- Define **properties** (relationships between resources)
- Specify **constraints** (rules about valid data)
- Enable **reasoning** (systems can infer new facts)

### Classes and Inheritance

```turtle
@prefix ex: <https://example.com/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

# Define a class hierarchy
ex:Vehicle a owl:Class ;
    rdfs:label "Vehicle" ;
    rdfs:comment "Any motorized transportation" .

ex:Car a owl:Class ;
    rdfs:subClassOf ex:Vehicle ;  # Car is a kind of Vehicle
    rdfs:label "Car" .

ex:Truck a owl:Class ;
    rdfs:subClassOf ex:Vehicle ;
    rdfs:label "Truck" .
```

**What this means:**

- Anything that is a `Car` is also a `Vehicle`
- Properties defined for `Vehicle` apply to `Car`
- A system can infer that `car-123` is a `Vehicle` (because it's a `Car`)

### Properties (Object Properties)

```turtle
# Object property: relationship between resources
ex:hasOwner a owl:ObjectProperty ;
    rdfs:domain ex:Vehicle ;      # Domain: Vehicle
    rdfs:range ex:Person ;         # Range: Person
    rdfs:label "has owner" ;
    owl:functional ;               # Each vehicle has exactly one owner
    owl:inverse ex:owns .          # Inverse relationship

# Usage in data:
ex:car-123 ex:hasOwner ex:john .
# Can also be queried as:
ex:john ex:owns ex:car-123 .
```

### Properties (Datatype Properties)

```turtle
# Datatype property: relationship with literal values
ex:hasColor a owl:DatatypeProperty ;
    rdfs:domain ex:Vehicle ;
    rdfs:range xsd:string ;
    rdfs:label "color" .

ex:hasSpeed a owl:DatatypeProperty ;
    rdfs:domain ex:Vehicle ;
    rdfs:range xsd:integer ;
    rdfs:label "speed in km/h" .

# Usage in data:
ex:car-123 ex:hasColor "red" ;
           ex:hasSpeed 100 .
```

### Class Restrictions

```turtle
# Describe constraints on classes using restrictions

ex:AutomatedVehicle a owl:Class ;
    rdfs:subClassOf ex:Vehicle ;
    rdfs:subClassOf [
        a owl:Restriction ;
        owl:onProperty ex:hasAutopilot ;
        owl:hasValue true      # All must have autopilot = true
    ] ;
    rdfs:subClassOf [
        a owl:Restriction ;
        owl:onProperty ex:hasLidar ;
        owl:minCardinality 2   # Must have at least 2 LiDARs
    ] .
```

### Equivalence and Disjointness

```turtle
# Classes can be equivalent (same concept, different names)
ex:Car owl:equivalentClass ex:Automobile ;
    owl:equivalentClass ex:Motorcar .

# Classes can be disjoint (mutually exclusive)
ex:Car owl:disjointWith ex:Bicycle ;
        owl:disjointWith ex:Truck .

# A resource cannot be both a Car and Bicycle
ex:bike-123 a ex:Bicycle .
ex:bike-123 a ex:Car .  # Contradictory!
```

## SHACL: Validation

### What is SHACL?

**SHACL (Shapes Constraint Language)** defines validation rules for RDF data. It answers: "Does my data conform to the ontology?"

**Key Difference from OWL:**

- **OWL** defines what concepts _can_ exist and _may_ be inferred
- **SHACL** defines what data _must_ satisfy for validation to pass

### Basic Shape

```turtle
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix ex: <https://example.com/> .

# A shape describes validation rules for a class
ex:CarShape a sh:NodeShape ;
    sh:targetClass ex:Car ;  # Apply to all instances of Car
    sh:property [
        sh:path ex:hasOwner ;
        sh:name "owner" ;
        sh:description "A car must have exactly one owner" ;
        sh:minCount 1 ;       # At least one owner
        sh:maxCount 1 ;       # At most one owner
        sh:nodeKind sh:IRI ;  # Owner must be an IRI (not a literal)
    ] ;
    sh:property [
        sh:path ex:hasColor ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:datatype xsd:string ;  # Color must be a string
    ] .
```

### Property Constraints

```turtle
ex:ScenarioShape a sh:NodeShape ;
    sh:targetClass ex:Scenario ;
    sh:property [
        sh:path ex:hasName ;
        sh:minCount 1 ;
        sh:datatype xsd:string ;
        sh:pattern "^[A-Za-z0-9_]+$" ;  # Only alphanumeric and underscore
    ] ;
    sh:property [
        sh:path ex:hasComplexity ;
        sh:datatype xsd:integer ;
        sh:minInclusive 1 ;
        sh:maxInclusive 10 ;  # Value between 1 and 10
    ] ;
    sh:property [
        sh:path ex:hasDescription ;
        sh:minLength 10 ;     # Minimum 10 characters
        sh:maxLength 500 ;    # Maximum 500 characters
    ] .
```

### Closed Shapes (Allowlist)

```turtle
ex:StrictVehicleShape a sh:NodeShape ;
    sh:targetClass ex:Vehicle ;
    sh:closed true ;          # Only properties listed below are allowed
    sh:ignoredProperties ( rdf:type ) ;  # Exception for rdf:type
    sh:property [
        sh:path ex:hasColor ;
    ] ;
    sh:property [
        sh:path ex:hasSpeed ;
    ] ;
    sh:property [
        sh:path ex:hasOwner ;
    ] .
    # Any other properties will cause validation failure
```

### Complex Constraints

```turtle
# Logical AND constraint (all must be true)
ex:SafeVehicleShape a sh:NodeShape ;
    sh:targetClass ex:Vehicle ;
    sh:and (
        [ sh:path ex:hasBrakes ; sh:minCount 1 ]
        [ sh:path ex:hasLights ; sh:minCount 1 ]
        [ sh:path ex:hasSteeringWheel ; sh:minCount 1 ]
    ) .

# Logical OR constraint (at least one must be true)
ex:PoweredVehicleShape a sh:NodeShape ;
    sh:targetClass ex:Vehicle ;
    sh:or (
        [ sh:path ex:hasEngine ]
        [ sh:path ex:hasMotor ]
        [ sh:path ex:hasBattery ]
    ) .

# If-Then constraint
ex:ConditionalShape a sh:NodeShape ;
    sh:targetClass ex:Vehicle ;
    sh:ifThenElse (
        # IF: hasAutopilot = true
        [ sh:path ex:hasAutopilot ;
          sh:hasValue true ]
        # THEN: must have multiple sensors
        [ sh:path ex:hasSensor ; sh:minCount 3 ]
        # ELSE: can have fewer sensors
        [ sh:path ex:hasSensor ; sh:minCount 1 ]
    ) .
```

### Validation Reports

When SHACL validates data and finds violations:

```turtle
# Validation result (in report)
[] a sh:ValidationReport ;
   sh:conforms false ;          # Did NOT pass validation
   sh:result [
       a sh:ValidationResult ;
       sh:focusNode ex:car-999 ;  # Problematic resource
       sh:resultPath ex:hasOwner ;  # Property with problem
       sh:resultSeverity sh:Violation ;  # Type of problem
       sh:resultMessage "Car must have exactly one owner" ;
   ] .
```

## How They Work Together

### Example: Complete Ontology + Validation

```turtle
# Define ontology (OWL)
ex:Vehicle a owl:Class ;
    rdfs:comment "A motorized transportation device" .

ex:Car a owl:Class ;
    rdfs:subClassOf ex:Vehicle .

ex:hasOwner a owl:ObjectProperty ;
    rdfs:domain ex:Vehicle ;
    rdfs:range ex:Person .

# Define validation rules (SHACL)
ex:CarShape a sh:NodeShape ;
    sh:targetClass ex:Car ;
    sh:property [
        sh:path ex:hasOwner ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
    ] .

# Instance data (RDF)
ex:car-123 a ex:Car ;
    ex:hasOwner ex:john ;
    ex:hasColor "blue" .

# Validation: ✅ PASSES
# - car-123 is a Car (valid by OWL)
# - car-123 has exactly one owner (satisfies SHACL)
```

## Practical Workflow

### 1. Design Phase (OWL)

Create ontologies defining concepts and relationships

### 2. Implementation Phase (RDF)

Create actual data instances based on ontology

### 3. Validation Phase (SHACL)

Validate data conforms to ontology constraints

### 4. Reasoning Phase (OWL)

Let systems infer new facts from data

### 5. Publish Phase

Make ontologies and data available via IRIs

## When to Use What

| Technology | Used For                    | Example                    |
| ---------- | --------------------------- | -------------------------- |
| **RDF**    | Representing facts and data | A vehicle has color "red"  |
| **OWL**    | Defining concepts and rules | A car is a type of vehicle |
| **SHACL**  | Validating data quality     | A car must have an owner   |

## See Also

- [Linked Data Principles](03-linked-data-principles.md) - Design patterns for using RDF/OWL
- [Semantic Versioning](04-semantic-versioning.md) - Managing ontology versions
- [W3C RDF Specification](https://www.w3.org/RDF/) - Official specification
- [W3C OWL Specification](https://www.w3.org/OWL/) - Official specification
- [W3C SHACL Specification](https://www.w3.org/TR/shacl/) - Official specification
