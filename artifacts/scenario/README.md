# Scenario Ontology & SHACL Validation

## Overview

This folder enables users to **describe** a Scenario and **check** that the description is valid.

- The **Scenario model** (ontology) defines key concepts relevant to a scenario (e.g., content, data resources).
- The **validation rules** (SHACL) automatically verify a file and report what is missing or incorrect.

It also supports **mixing native scenario content with OpenLABEL annotations** (e.g., tags) in one place.

---

## Capabilities

- Describe a scenario in **JSON-LD**.
- Include **scenario content** and optional **OpenLABEL** content (e.g., tags and flags).
- Run a **validation** that reports whether a file is complete and well-formed.

---

## Contents of this folder

- **`tests/`** – Example files used for validation.
- **`scenario_instance.json`** – A sample JSON-LD instance of a Scenario asset for reference and testing.
- **`scenario.owl.ttl`** – The Scenario model (concepts and relationships).
- **`scenario.shacl.ttl`** – SHACL rules used to check JSON-LD data.
- **`PROPERTIES.md`** – An auto-generated summary of SHACL properties found in this folder.
- **`README.md`** – This readme file.

---

## What a valid Scenario looks like

A typical file includes the property **`scenario:hasContent`**.  
Each item under this property may be **either**:

1. **Scenario content**, or
2. **OpenLABEL tag** content, or
3. **A simple boolean flag** (for minimal OpenLABEL cases)

### Example: mixing Scenario + OpenLABEL

```json
{
  "@context": {
    "scenario": "https://w3id.org/ascs-ev/envited-x/scenario/v5/",
    "openlabel": "https://openlabel.asam.net/V1-0-0/ontologies/",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@type": "scenario:Scenario",
  "scenario:hasContent": [
    {
      "@type": "scenario:Content",
      "scenario:description": "Overtake on rural road",
      "scenario:actors": ["car", "truck"]
    },
    {
      "@type": "openlabel:Tag",
      "openlabel:WeatherRain": true
    }
  ]
}
```

---

## How to Run SHACL Validation Tests

See the root guide for the canonical commands and explanations:  
[Running Tests Locally](../../README.md#validation)

Example command for this folder:

```bash
python3 -m src.tools.validators.validation_suite \
  --run check-data-conformance \
  --domain scenario
```

---

## See Also

- [Ontology Domains](../../docs/ontologies/catalog.md) – Browse all available ontologies
- [Validation Tools](../../docs/validation/tools.md) – Complete validation tool reference
- [Architecture](../../docs/discovery/catalogs.md) – Technical details about the ontology structure
