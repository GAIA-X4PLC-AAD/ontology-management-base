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
- **`manifest_reference.json`**: A machine-readable manifest that lists all files in the package and relevant external references.
- **`PROPERTIES.md`**: An auto-generated summary of SHACL properties found in this folder.
- **`README.md`**: This readme file.
- **`scenario_instance.json`**: A sample JSON-LD instance of a Scenario asset for reference and testing (name may vary).
- **`scenario_ontology.ttl`** – The Scenario model (concepts and relationships).
- **`scenario_shacl.ttl`** – SHACL rules used to check JSON-LD data.

---

## What a valid Scenario looks like

A typical file includes the property **`scenario:hasContent`**.  
Each item under this property may be **either**:

1) **Scenario content**, or  
2) **OpenLABEL tag** content, or  
3) **A simple boolean flag** (for minimal OpenLABEL cases)

### Example: mixing Scenario + OpenLABEL

```json
{
  "@context": {
    "scenario": "https://ontologies.envited-x.net/scenario/v4/ontology#",
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
### How to Run SHACL Validation Tests

See the root guide for the canonical commands and explanations:  
[Running Tests Locally](../README.md#running-tests-locally)

Example command for this folder:
```bash
python3 check_jsonld_against_shacl_schema.py \scenario\scenario_instance.json
