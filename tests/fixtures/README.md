# Base References Repository

This directory acts as a centralized storage for JSON-LD reference data files that are reused across different ontology instances.

## Automatic Resolution Logic

Fixture files in this directory are loaded via the tests catalog (`tests/catalog-v001.xml`).
When instance data references an external `did:web:` IRI, the validator resolves it using
the catalog and loads the corresponding JSON-LD fixture file.

## Naming Convention

Fixture filenames can be arbitrary, but the `tests/catalog-v001.xml` entry must map the
fixture IRI (`name`) to the local file (`uri`).
