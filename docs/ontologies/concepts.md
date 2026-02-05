# Concepts: OWL, SHACL, Context

This project separates semantic modeling from validation and serialization.

## Ontologies (OWL)

OWL files describe classes, properties, and relationships. They define the vocabulary and reasoning model for each domain.

## Shapes (SHACL)

SHACL files describe validation constraints. They test data quality and enforce rules such as cardinality, datatype, and allowed values.

## JSON-LD Contexts

Contexts map compact JSON keys to full IRIs. They are used for authoring and parsing JSON-LD instances.

## How They Work Together

- Data instances declare `@context` and `@type` using W3ID IRIs.
- The validator discovers the relevant OWL and SHACL files via catalogs.
- Inference expands the data graph before SHACL validation.

## Interactive Class Diagrams

Class pages embed **WebVOWL** for interactive ontology visualization. The viewer
loads the OWL file via the published raw GitHub URL and renders an interactive
graph directly in the docs.
