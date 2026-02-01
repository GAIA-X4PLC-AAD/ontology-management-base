# Foundations

This section provides the theoretical and conceptual foundations needed to understand and use this ontology repository.

## Overview

Whether you're new to semantic web technologies or looking to deepen your understanding, this section covers essential concepts:

1. **[RDF, OWL, and SHACL](02-rdf-owl-shacl.md)** - Core semantic web technologies explained
2. **[Linked Data Principles](03-linked-data-principles.md)** - Design patterns for connected data
3. **[Semantic Versioning](04-semantic-versioning.md)** - How we manage ontology versions

## Quick Start for Different Audiences

### I'm New to Semantic Web / Linked Data

Read in this order:

1. [Linked Data Principles](03-linked-data-principles.md) - Why we use these technologies
2. [RDF, OWL, and SHACL](02-rdf-owl-shacl.md) - What the core technologies do
3. [Semantic Versioning](04-semantic-versioning.md) - How versions work

Then move to [Getting Started](../4-getting-started/) for practical guidance.

### I Know RDF but Not OWL

Start with:

1. [RDF, OWL, and SHACL](02-rdf-owl-shacl.md) - Focus on OWL section
2. [Linked Data Principles](03-linked-data-principles.md) - Understanding design patterns
3. [Architecture section](../2-architecture/) - How ontologies are organized

### I'm Already Familiar with Semantic Web Technologies

You can jump directly to:

- [Architecture](../2-architecture/) - How this repository is structured
- [Ontology Domains](../3-ontology-domains/) - Which ontologies are available
- [Validation Tools](../6-validation-tools/) - How to validate conformance

## Core Concepts

### What is an Ontology?

An **ontology** is a formal specification of concepts and relationships within a domain. In this repository:

- Ontologies are expressed in **OWL (Web Ontology Language)**
- They define what kinds of things exist (classes)
- They define how things relate to each other (properties)
- They specify constraints and rules (through SHACL)

**Example:** An autonomous vehicle ontology defines concepts like `Vehicle`, `Sensor`, `SimulationEnvironment` and how they relate (e.g., a vehicle has sensors).

### What is RDF?

**RDF (Resource Description Framework)** is the foundation of all semantic web technologies:

- Everything is described using **triples**: Subject-Predicate-Object
- Resources are identified by **URIs/IRIs** (persistent identifiers)
- Data is connected and machine-readable

**Example triple:**

```
<vehicle-123> <hasColor> "red" .
```

### What is OWL?

**OWL (Web Ontology Language)** extends RDF with richer semantics:

- Define **classes** (categories of things)
- Define **properties** (relationships between things)
- Add **constraints** (rules about valid data)
- Enable **reasoning** (systems can infer new facts)

**Example OWL definition:**

```
Vehicle rdfs:subClassOf Agent ;
  rdfs:label "Vehicle" ;
  rdfs:comment "A motorized entity capable of motion" .
```

### What is SHACL?

**SHACL (Shapes Constraint Language)** validates RDF data:

- Define **validation rules** for data
- Check that data **conforms** to ontology
- Create **test suites** for quality assurance
- Generate **validation reports**

**Example SHACL constraint:**

```
VehicleShape sh:property [
  sh:path ex:hasModel ;
  sh:minCount 1 ;
  sh:maxCount 1 ;
] .
```

## Why Ontologies Matter

### 1. Semantic Clarity

Ontologies formally specify meaning so machines can understand concepts, not just parse syntax.

### 2. Data Integration

Systems using shared ontologies can automatically understand each other's data and exchange information.

### 3. Validation

SHACL shapes enable automated validation, catching errors before they cause problems.

### 4. Reasoning

Ontologies enable systems to infer new facts and relationships from existing data.

### 5. Documentation

Ontologies serve as living documentation of domain concepts and constraints.

## Technologies Used in This Repository

### RDF Serialization Formats

We use multiple formats to suit different needs:

| Format        | Use Case                                  | File Extension |
| ------------- | ----------------------------------------- | -------------- |
| **Turtle**    | Human-readable, recommended for authoring | `.ttl`         |
| **JSON-LD**   | Integration with JSON systems             | `.jsonld`      |
| **RDF/XML**   | Legacy systems, XML processing            | `.rdf`         |
| **N-Triples** | Streaming, bulk processing                | `.nt`          |

### OWL Profiles

OWL defines profiles of increasing expressivity:

| Profile      | Complexity | Speed  | When to Use                                |
| ------------ | ---------- | ------ | ------------------------------------------ |
| **OWL 2 RL** | Low        | Fast   | Rules-based reasoning, simple constraints  |
| **OWL 2 QL** | Medium     | Medium | Database-like querying, description logics |
| **OWL 2 DL** | High       | Medium | Full OWL expressivity, decidable reasoning |
| **OWL Full** | Very High  | Slow   | Unrestricted RDF, semi-decidable           |

Most ontologies in this repository use **OWL 2 DL** for good balance of expressivity and performance.

### Validation with SHACL

Validation happens at multiple levels:

1. **RDF Syntax** - Is the data valid RDF?
2. **OWL Semantics** - Does data conform to ontology structure?
3. **SHACL Constraints** - Does data satisfy explicit validation rules?
4. **Domain Logic** - Does data make sense in the business domain?

## Key Principles

### 1. Open Standards

We use W3C standards (RDF, OWL, SHACL) rather than proprietary formats.

### 2. Semantic Web

We follow Linked Data principles to make data machine-readable and interoperable.

### 3. Modularity

Ontologies are composed of reusable modules rather than monolithic definitions.

### 4. Versioning

Each ontology version is permanent and accessible, supporting long-term stability.

### 5. Governance

Clear governance distinguishes stable (GAIA-X) from experimental (ENVITED-X) ontologies.

## Learning Path

```
Foundations (You Are Here)
    ↓
Getting Started
    ↓
Architecture
    ↓
Ontology Domains (Choose your focus)
    ├→ GAIA-X (Stable)
    └→ ENVITED-X (Innovation)
    ↓
Validation & Tools
    ↓
Building & Contributing
```

## Common Misconceptions

### "Ontologies are like databases"

**Actually:** Ontologies define _meaning_ and _constraints_. Databases store _instances_ of those meanings.

### "RDF is obsolete"

**Actually:** RDF is the foundation of modern knowledge graphs and linked data, used by major tech companies.

### "You need to learn complex logic"

**Actually:** Most ontologies use straightforward OWL, which is based on familiar programming concepts.

### "Ontologies are just documentation"

**Actually:** Ontologies enable automated validation, reasoning, and integration—they're executable semantics.

## Next Steps

**Ready to use ontologies?**
→ Go to [Getting Started](../4-getting-started/)

**Want to understand architecture?**
→ Go to [Architecture](../2-architecture/)

**Looking for specific ontologies?**
→ Go to [Ontology Domains](../3-ontology-domains/)

**Want to validate data?**
→ Go to [Validation Tools](../6-validation-tools/)

**Ready to contribute?**
→ Go to [Building & Contributing](../5-building-contributing/)

## References and Further Reading

- [W3C RDF Specification](https://www.w3.org/RDF/)
- [W3C OWL Specification](https://www.w3.org/OWL/)
- [W3C SHACL Specification](https://www.w3.org/TR/shacl/)
- [Linked Data Best Practices](https://www.w3.org/DesignIssues/LinkedData.html)
- [Semantic Web for the Working Ontologist](https://www.elsevier.com/books/semantic-web-for-the-working-ontologist/allemang/978-0-12-820195-8) - Recommended textbook
