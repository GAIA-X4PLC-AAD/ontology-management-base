# Repository Structure

This document explains the organization of the Ontology Management Base repository.

## Directory Layout

```
ontology-management-base/
├── .github/
│   └── workflows/           # CI/CD pipelines
│       ├── ci.yml          # Main CI pipeline
│       ├── release.yml     # Release workflow
│       └── docs.yml        # Documentation deployment
│
├── artifacts/               # [OUTPUT] Generated/Handcrafted ontology files
│   ├── owl/                # Ontology definitions (*_ontology.ttl)
│   ├── shacl/              # SHACL shapes (*_shacl.ttl)
│   └── docs/               # Generated documentation (PROPERTIES.md)
│
├── config/                  # Configuration files
│   └── ontoenv.toml        # Dependency declarations
│
├── imports/                 # [DEPENDENCIES] External ontologies
│   ├── catalog-v001.xml    # Protege catalog for local resolution
│   ├── rdf/                # W3C RDF ontology
│   ├── rdfs/               # W3C RDFS ontology
│   ├── owl/                # W3C OWL ontology
│   ├── shacl/              # W3C SHACL ontology
│   └── ...                 # Other standard ontologies
│
├── src/
│   ├── tools/              # [PYTHON] Validation & utility scripts
│   │   ├── validators/     # Validation scripts
│   │   ├── uploaders/      # FC upload utilities
│   │   └── utils/          # Shared utilities
│   └── linkml/             # [FUTURE] LinkML schema sources
│       └── modules/        # Reusable LinkML fragments
│
├── scripts/                 # [AUTOMATION] CI/CD glue scripts
│   └── utils/registry_updater.py  # Registry update script
│
├── tests/
│   ├── fixtures/           # [SHARED DATA] Reference files
│   ├── data/               # [TEST CASES] Organized by domain
│   │   ├── hdmap/
│   │   │   ├── valid/      # Working examples
│   │   │   └── invalid/    # Fail-test cases
│   │   └── ...
│   └── unit/               # Python unit tests
│
├── docs/                    # [GITHUB PAGES] MkDocs content
│   ├── resolve/            # Smart resolver for w3id
│   │   └── index.html
│   ├── registry.json       # Version mapping for w3id
│   └── ...                 # Documentation pages
│
├── Makefile                 # Build command center
├── mkdocs.yml              # MkDocs configuration
└── pyproject.toml          # Python project configuration
```

## Key Directories

### `artifacts/`

Contains the ontology output files:

| Subdirectory | Contents                 | Naming Convention        |
| ------------ | ------------------------ | ------------------------ |
| `owl/`       | OWL ontology definitions | `{domain}_ontology.ttl`  |
| `shacl/`     | SHACL validation shapes  | `{domain}_shacl.ttl`     |
| `docs/`      | Generated documentation  | `{domain}/PROPERTIES.md` |

### `imports/`

External ontologies used as dependencies. These are typically standard W3C ontologies (RDF, RDFS, OWL, SHACL) plus domain-specific imports.

The `catalog-v001.xml` file provides Protege-compatible local resolution.

### `tests/data/`

Test data organized by ontology domain:

```
tests/data/{domain}/
├── valid/           # Valid instances that should pass validation
│   └── {domain}_instance.json
└── invalid/         # Invalid instances that should fail validation
    ├── fail_01_*.json
    └── fail_01_*.expected
```

### `src/tools/`

Python validation and utility scripts:

| Directory     | Purpose                                |
| ------------- | -------------------------------------- |
| `validators/` | SHACL and OWL validation               |
| `uploaders/`  | Federated Catalog upload               |
| `utils/`      | Shared utilities (parsing, formatting) |

## File Naming Conventions

| Pattern                     | Description            | Example                         |
| --------------------------- | ---------------------- | ------------------------------- |
| `{domain}_ontology.ttl`     | OWL ontology file      | `hdmap_ontology.ttl`            |
| `{domain}_shacl.ttl`        | SHACL shapes file      | `hdmap_shacl.ttl`               |
| `{domain}_instance.json`    | Valid instance example | `hdmap_instance.json`           |
| `fail_{nn}_{desc}.json`     | Failing test case      | `fail_01_missing_name.json`     |
| `fail_{nn}_{desc}.expected` | Expected error output  | `fail_01_missing_name.expected` |
