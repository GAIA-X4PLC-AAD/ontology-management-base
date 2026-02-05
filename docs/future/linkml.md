# LinkML Migration

The current workflow maintains OWL, SHACL, and JSON-LD contexts as separate artifacts. This creates consistency risks when updates are applied unevenly.

## Current Consistency Challenges

- Ontology changes not mirrored in SHACL constraints
- Context mappings drifting from OWL property IRIs
- Domain-specific patterns duplicated across files

## Planned Direction

The roadmap includes a migration to LinkML as a single source of truth. LinkML can generate OWL, SHACL, and JSON-LD contexts from one schema definition.

## Expected Benefits

- Single source of truth for classes and properties
- Automated regeneration of OWL, SHACL, and contexts
- Reduced manual inconsistencies
- Easier validation and documentation pipelines

