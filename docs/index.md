# ENVITED-X Ontology Management Base

Welcome to the **Ontology Management Base** repository - the central hub for managing, validating, and documenting ontologies within the ENVITED-X ecosystem.

## Overview

This repository provides:

- **Ontology Definitions** - OWL ontology files defining the semantic models
- **SHACL Shapes** - Validation constraints for data instances
- **Validation Tools** - Python scripts for automated validation
- **Test Fixtures** - Example instances and regression tests
- **Documentation** - Auto-generated and manually curated docs

## Quick Links

<div class="grid cards" markdown>

-   :material-check-circle:{ .lg .middle } **Validation Tools**

    ---

    Validate your JSON-LD data against SHACL schemas

    [:octicons-arrow-right-24: Validation Catalog](validation/index.md)

-   :material-book-open-variant:{ .lg .middle } **Getting Started**

    ---

    Set up your environment and run your first validation

    [:octicons-arrow-right-24: Quick Start](getting-started/quickstart.md)

-   :material-graph:{ .lg .middle } **Ontologies**

    ---

    Browse available ontology domains and their properties

    [:octicons-arrow-right-24: Ontology Catalog](ontologies/index.md)

-   :material-architecture:{ .lg .middle } **Architecture**

    ---

    Understand IRI patterns and ontology discovery

    [:octicons-arrow-right-24: Architecture Guide](architecture/ontology-discovery.md)

</div>

## Repository Structure

```
ontology-management-base/
├── artifacts/              # Output: Ontology files
│   ├── owl/               # *_ontology.ttl files
│   ├── shacl/             # *_shacl.ttl files
│   └── docs/              # Generated documentation
├── imports/               # External ontology dependencies
├── tests/
│   ├── data/              # Test instances by domain
│   └── fixtures/          # Reference data
├── src/
│   ├── tools/             # Python validation tools
│   └── linkml/            # Future LinkML schemas
├── docs/                  # MkDocs documentation
└── scripts/               # Automation scripts
```

## Ontology Resolution

Ontologies are published via [w3id.org](https://w3id.org) and can be resolved using:

```
https://w3id.org/ascs-ev/envited-x/{ontology}/{version}
```

For example:
- `https://w3id.org/ascs-ev/envited-x/envited-x/v3` - ENVITED-X core ontology v3
- `https://w3id.org/ascs-ev/envited-x/hdmap/v5` - HD Map ontology v5

## Contributing

See the [Contributing Guide](https://github.com/gaia-x4plc-aad/ontology-management-base/blob/main/CONTRIBUTING.md) for details on how to contribute.

## License

This project is licensed under the terms specified in the [LICENSE](https://github.com/gaia-x4plc-aad/ontology-management-base/blob/main/LICENSE) file.
