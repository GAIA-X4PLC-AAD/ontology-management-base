# HDMap Ontology & SHACL Validation

## Overview

This folder enables users to **describe** a High-Definition Map (HDMap) and **check** that the description is valid.

- The **HDMap model** (ontology) defines the key concepts relevant to an HD map (road types, lane types, traffic direction, etc.).
- The **validation rules** (SHACL) automatically verify a file and report what is missing or incorrect.

It also supports **mixing standard HDMap content with OpenLABEL annotations** (e.g., ODD information) in one place.

---

## Capabilities

- Describe an HD map in **JSON-LD**.
- Include **map content** (roads/lanes) and optional **OpenLABEL** content (e.g., ODD flags).
- Run a **validation** that reports whether a file is complete and well-formed.

---

## Contents of this folder

- **`tests/`** – Example files used for validation.
- **`hdmap_instance.json`**: A sample JSON-LD instance of an HDMap asset for reference and testing.
- **`hdmap_ontology.ttl`** – The HDMap model (concepts and relationships).
- **`hdmap_shacl.ttl`** – SHACL rules used to check JSON-LD data.
- **`manifest_reference.json`**: A machine-readable manifest that lists all files in the package and relevant external references. It follows the ENVITED-X/Manifest model so tools can reliably discover content and permissions.
- **`PROPERTIES.md`**: An auto-generated summary of SHACL properties found in this folder.
- **`README.md`**: This readme file.

---

## What a valid HDMap looks like

A typical file includes the property **`hdmap:hasContent`**.  
Each item under this property may be **either**:

1. **HDMap content** (roads/lanes), or
2. **OpenLABEL ODD** content (e.g., flags + values), or
3. **A simple boolean flag** (for minimal OpenLABEL cases)

### Example: mixing HDMap + OpenLABEL

```json
{
  "@context": {
    "hdmap": "https://ontologies.envited-x.net/hdmap/v4/ontology#",
    "openlabel": "https://openlabel.asam.net/V1-0-0/ontologies/",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "hdmap:hasContent": [
    {
      "@type": "hdmap:Content",
      "hdmap:roadTypes": "town",
      "hdmap:laneTypes": ["driving", "walking"],
      "hdmap:levelOfDetail": "crosswalk",
      "hdmap:trafficDirection": "right-hand"
    },
    {
      "@type": "openlabel:Odd",
      "openlabel:LaneSpecificationDimensions": true,
      "openlabel:laneSpecificationDimensionsValue": {
        "@type": "xsd:decimal",
        "@value": "3.5"
      }
    }
  ]
}
```

If an item under hdmap:hasContent does not match one of these three options, validation will fail.

### How to Run SHACL Validation Tests

See the root guide for the canonical commands and explanations:  
[Running Tests Locally](../README.md#running-tests-locally)

Example command for this folder:

```bash
python3 check_jsonld_against_shacl_schema.py \hdmap\hdmap_instance.json
```

## Common validation issues

- Misspelled values
  Example: a lane type written as "drivng" instead of "driving".
  Fix: Use allowed values shown in the examples or documentation.

- Missing required content
  A report indicating a missing section means that section must be added (e.g., an item of type hdmap:Content under hasContent).

- Properties in the wrong place
  Some shapes are “closed,” allowing only listed properties.
  Fix: Remove extra properties or move them to the correct section.

- OpenLABEL flags without values
  If a flag such as openlabel:LaneSpecificationDimensions is set to true, and the shape expects a companion value (e.g., laneSpecificationDimensionsValue), include that value.
