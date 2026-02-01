# ENVITED-X Core Ontology

## Overview

This folder contains the core **ENVITED-X ontology** – the foundational semantic model that defines key concepts and relationships for simulation assets, data resources, and manifest structures.

- The **ENVITED-X model** (ontology) defines core concepts like `DataResource`, `Asset`, and their properties.
- The **validation rules** (SHACL) automatically verify instances conform to the ENVITED-X specification.
- It integrates with domain-specific ontologies (HDMap, Scenario, Environment Model, etc.) and the Gaia-X Trust Framework.

This ontology adheres to the [ENVITED Ecosystem Specification (EVES-003)](https://ascs-ev.github.io/EVES/EVES-003/eves-003.html).

---

## Capabilities

- Describe digital simulation assets in **JSON-LD**.
- Include **asset metadata**, **resource information**, and **manifest references**.
- Run a **validation** that reports whether an asset conforms to ENVITED-X standards.

---

## Contents of this folder

- **`envited-x.owl.ttl`** – The ENVITED-X core ontology (concepts and relationships).
- **`envited-x.shacl.ttl`** – SHACL rules used to validate JSON-LD instances.
- **`envited-x_instance.json`** – A sample JSON-LD instance of an ENVITED-X DataResource.
- **`PROPERTIES.md`** – An auto-generated summary of SHACL properties.
- **`README.md`** – This readme file.

---

## What a valid ENVITED-X instance looks like

A typical instance includes:

- **@context**: Namespace definitions for ENVITED-X, manifest, and other ontologies.
- **@type**: `envited-x:DataResource` or related types.
- **@id**: A unique IRI for the resource.
- **Name & Description**: Human-readable metadata.
- **Links to related resources**: References to simulation data, documentation, media.

### Example: Basic ENVITED-X instance

```json
{
  "@context": {
    "envited-x": "https://w3id.org/ascs-ev/envited-x/envited-x/v3/",
    "manifest": "https://w3id.org/ascs-ev/envited-x/manifest/v5/",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@type": "envited-x:DataResource",
  "@id": "https://example.com/assets/my-asset",
  "envited-x:name": "My Simulation Asset",
  "envited-x:description": "A high-definition map scenario for autonomous driving",
  "envited-x:hasVersion": "1.0.0"
}
```

---

## How to Run SHACL Validation Tests

See the root guide for the canonical commands and explanations:  
[Running Tests Locally](../../README.md#validation)

Example command for this folder:

```bash
python3 -m src.tools.validators.check_jsonld_against_shacl_schema \
  --ontology artifacts/envited-x/envited-x.owl.ttl \
  --shacl artifacts/envited-x/envited-x.shacl.ttl \
  --instance tests/data/envited-x/valid/envited-x_instance.json
```

---

## Integration with Other Ontologies

ENVITED-X is designed to work with and reference other domain ontologies:

- **HDMap**: Describes high-definition maps
- **Scenario**: Defines simulation scenarios
- **Manifest**: Structures asset packaging and metadata
- **Environment Model**: Captures 3D environment data
- **GX (Gaia-X)**: Integrates with the Gaia-X Trust Framework

These ontologies can be combined in a single asset by using their respective IRIs in the JSON-LD `@context`.

---

## See Also

- [Ontology Domains](../../3-ontology-domains/) – Browse all available ontologies
- [Validation Tools](../../6-validation-tools/) – Complete validation tool reference
- [Architecture](../../2-architecture/) – Technical details about the ontology structure
- [ENVITED Specification](https://ascs-ev.github.io/EVES/) – Full ENVITED ecosystem documentation
