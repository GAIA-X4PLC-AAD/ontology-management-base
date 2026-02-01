# Architecture

This section covers the architectural foundations and design patterns used throughout this ontology repository.

## Overview

The architecture documentation is organized around several key themes:

1. **[IRI Patterns](02-iri-patterns.md)** - How we design persistent identifiers for ontologies
2. **[Ontology Discovery](03-ontology-discovery.md)** - How to find and understand available ontologies
3. **[OWL Imports](04-owl-imports.md)** - Best practices for managing ontology dependencies
4. **[Ontology Domains and Namespaces](05-domains.md)** - Understanding GAIA-X vs ENVITED-X split
5. **[W3ID Publishing](06-w3id-publishing.md)** - Technical details on IRI resolution and content negotiation

## Quick Navigation

### For Users Wanting to Understand the Big Picture

Start here to grasp how this ontology repository is organized:

- [Ontology Domains and Namespaces](05-domains.md) - Two distinct namespaces (GAIA-X and ENVITED-X)
- [Ontology Discovery](03-ontology-discovery.md) - Where to find specific ontologies
- [IRI Patterns](02-iri-patterns.md) - How identifiers work

### For Developers and Contributors

These resources help you build on existing ontologies:

- [OWL Imports](04-owl-imports.md) - Managing dependencies between ontologies
- [W3ID Publishing](06-w3id-publishing.md) - Getting your ontology published and discoverable
- [IRI Patterns](02-iri-patterns.md) - Design patterns for semantic resources

### For Infrastructure and Platform Teams

Technical architecture for deployment and hosting:

- [W3ID Publishing](06-w3id-publishing.md) - Content negotiation and IRI resolution
- [Ontology Discovery](03-ontology-discovery.md) - Metadata and registry patterns

## Key Concepts

### Ontologies as Persistent Resources

All ontologies in this repository are published as **persistent resources** with stable IRIs. This means:

- IRIs like `https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/` are permanent
- Content can be fetched in multiple formats (Turtle, JSON-LD, RDF/XML)
- Version management ensures backward compatibility

### Two-Namespace Architecture

The repository maintains two distinct ontology namespaces:

- **GAIA-X 4 PLC-AAD** - Stable, production-ready ontologies from the GAIA-X project (2021-2024)
- **ENVITED-X** - Active development ontologies for post-GAIA-X innovations (2024+)

This separation allows:

- Stable GAIA-X ontologies to remain unchanged
- ENVITED-X to innovate and experiment
- Cross-domain imports where beneficial

See [Ontology Domains and Namespaces](05-domains.md) for detailed governance and use case guidance.

### Modular Design

Ontologies are designed to be modular and composable:

- **Core ontologies** provide foundational concepts
- **Domain ontologies** extend core concepts for specific use cases
- **Importing** makes ontologies available to others
- **Versioning** preserves compatibility across time

### Content Negotiation

The w3id.org service provides **content negotiation**, meaning:

- Same IRI can serve multiple formats
- HTTP Accept headers determine which format is returned
- Tools like Protégé automatically request appropriate formats
- RDF/XML, Turtle, JSON-LD, N-Triples all available

## Architecture Principles

### 1. Stability and Versioning

- Every ontology has a version in its IRI
- Version numbers follow semantic versioning
- Older versions remain accessible
- Breaking changes require new version IRIs

### 2. Modularity

- Ontologies are designed to be imported and composed
- Dependencies are explicit and versioned
- Circular dependencies are avoided
- Loose coupling encourages reuse

### 3. Discoverability

- Ontologies are registered in a central registry
- Metadata is available in multiple formats
- Links between ontologies are explicit
- Documentation is comprehensive and searchable

### 4. Interoperability

- Standard RDF serialization formats
- Aligned with semantic web standards
- SHACL validation shapes for conformance
- JSON-LD contexts for JSON integration

### 5. Governance

- GAIA-X ontologies governed by GAIA-X committee
- ENVITED-X follows lighter governance for innovation
- Both support community contributions
- Clear upgrade paths between versions

## Related Documentation

- [Getting Started](../4-getting-started/) - Quick start guide for using ontologies
- [Ontology Domains](../3-ontology-domains/) - Comprehensive catalog of all ontologies
- [Validation Tools](../6-validation-tools/) - Tools for checking conformance
- [Contributing](../5-building-contributing/) - How to add or modify ontologies

## Glossary

**IRI (Internationalized Resource Identifier)**
A generalization of URI that supports Unicode characters, used as persistent identifiers for ontologies and their elements.

**Ontology**
A formal representation of concepts and relationships within a domain, expressed in OWL (Web Ontology Language).

**Namespace**
A collection of ontologies grouped under a common IRI base, like `https://w3id.org/gaia-x4plcaad/ontologies/`.

**Content Negotiation**
HTTP mechanism that allows a single URL to serve different representations (formats) based on client request headers.

**Semantic Versioning**
Versioning scheme (MAJOR.MINOR.PATCH) where numbers indicate type of changes (breaking, feature, bugfix).

**SHACL (Shapes Constraint Language)**
Language for defining constraints and validation rules on RDF data, used alongside ontologies.

**JSON-LD (JSON Linked Data)**
JSON representation of linked data, allowing RDF concepts to be used in JSON documents.
