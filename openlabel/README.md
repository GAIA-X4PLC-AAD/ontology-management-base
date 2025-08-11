# OpenLABEL Ontology & SHACL Validation

## Overview

This folder helps users **describe OpenLABEL annotations** and **check** that those annotations are valid.

- The **OpenLABEL integration model** (ontology) defines the key tags and properties used to annotate digital assets in scenarios.
- The **validation rules** (SHACL) automatically verify a JSON-LD file and report what is missing or incorrect.

> **Note:** `openlabel_ontology_scenario_tags.ttl` is sourced from the
> ASAM OpenLABEL standard. The `openlabel_shacl.ttl` shape file is a
> project-authored integration artifact and **not** an official ASAM deliverable.

---

## What’s in this folder?

- **`openlabel_ontology_scenario_tags.ttl`**  
  An RDF/Turtle file defining classes and properties used for **scenario tagging** with OpenLABEL concepts (e.g., `openlabel:Tag`).

- **`openlabel_shacl.ttl`**  
  SHACL shapes that **validate** OpenLABEL instances. These shapes check structure (required properties, allowed values, etc.) for OpenLABEL tags.

- **`openlabel_instance.json`**  
  A small **JSON-LD** example showing how to express OpenLABEL tags in data.

- **`tests/`**  
  Failing test cases used to demonstrate validation:
  - `fail_wrong_value_openlabel_instance.json` – an invalid instance (e.g., wrong values or missing fields).
  - `fail_wrong_value_openlabel_instance.expected` – expected validator output indicating failure.

---

## Typical use

1. **Model** your OpenLABEL annotations in JSON-LD using the vocabulary IRIs (e.g., `openlabel:Tag`).
2. **Validate** your JSON-LD against `openlabel_shacl.ttl` to catch structural or value errors early.
3. Optionally **combine** with other domain models (e.g., HDMap) by referencing OpenLABEL classes via their IRIs.

### Minimal example (illustrative)

```json
{
  "@context": {
    "openlabel": "https://openlabel.asam.net/V1-0-0/ontologies/",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@type": "openlabel:Tag",
  "openlabel:LaneSpecificationDimensions": true,
  "openlabel:laneSpecificationDimensionsValue": { "@type": "xsd:decimal", "@value": "3.5" }
}
```
### How to Run SHACL Validation Tests

See the root guide for the canonical commands and explanations:  
[Running Tests Locally](../README.md#running-tests-locally)

Example command for this folder:
```bash
python3 check_jsonld_against_shacl_schema.py \hdmap\open_instance.json
```

## Citation & Licensing

**Citation**  
This project uses the OpenLABEL ontology defined by the **ASAM OpenLABEL®** standard.  
Original source: [ASAM OpenLABEL Ontology (TTL)](https://www.asam.net/index.php?eID=dumpFile&t=f&f=4566&token=9d976f840af04adee33b9f85aa3c22f2de4968dd)  
Standard reference: ASAM e.V. *ASAM OpenLABEL Standard Version 1.0.0*. Available at: [https://www.asam.net/standards/detail/openlabel/](https://www.asam.net/standards/detail/openlabel/)

**Licensing**  
- The ontology file `openlabel_ontology_scenario_tags.ttl` is used under the license of ASAM, which can be found here: [https://www.asam.net/license](https://www.asam.net/license).  
- OpenLABEL® and ASAM are names/marks of ASAM e.V. All rights reserved.

**Disclaimer**  
This repository is not affiliated with or endorsed by ASAM. The legal text of the ASAM license is authoritative.
