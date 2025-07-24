# HDMap Ontology & SHACL Validation

## Overview

This folder contains the ontology and SHACL (Shapes Constraint Language) validation rules for **HDMap** (High Definition Maps). The ontology defines the structure and semantics of HDMap assets, including various features such as road types, lane types, and traffic directions. The SHACL shapes ensure that instances conform to the defined structure and constraints.

### Key Files in This Directory

1. **hdmap_ontology.ttl**  
   The RDF Turtle file defining the **HDMap** ontology. This file provides a formal specification of the entities, classes, properties, and relationships that describe an HDMap asset.

2. **hdmap_shacl.ttl**  
   This file contains the SHACL validation rules used to ensure that the instances of **HDMap** data conform to the defined ontology structure. SHACL helps to check data integrity and ensures that the instances are valid.

3. **tests/**  
   A directory containing the validation tests for the **HDMap** ontology. Each test ensures that **HDMap** instances follow the SHACL rules and constraints specified in `hdmap_shacl.ttl`. The tests include both positive and negative cases.

   - **fail_false_value_hdmap_instance.json**: A test case for an invalid instance of **HDMap** where a boolean value (`openlabel:LaneSpecificationDimensions`) is incorrectly set to `false`.
   - **fail_false_value_hdmap_instance.expected**: The expected result when running the invalid instance, asserting that the instance fails the SHACL validation.

## Purpose of HDMap

The **HDMap** ontology provides a standardized way to describe high-definition maps used in autonomous vehicles, geospatial systems, and digital twins. It includes the following features:
- **Road Types**: Defines the classification of roads (e.g., urban, rural).
- **Lane Types**: Classifies lanes (e.g., driving, walking).
- **Traffic Directions**: Specifies the direction of traffic (e.g., right-hand, left-hand).
- **Level of Detail**: Describes the granularity of the map (e.g., crosswalks, intersections).

## Integration with OpenLABEL

The **HDMap** ontology integrates with the **OpenLABEL** standard to allow flexible annotations of digital assets. The SHACL validation rules support both **HDMap** and **OpenLABEL** tags, making it possible to seamlessly use **OpenLABEL** features within the **HDMap** data structure.

### Changes to the SHACL Shape

The **hdmap_shacl.ttl** was updated to allow for:
- Integration of **OpenLABEL** tags, such as **openlabel:Odd** and **openlabel:LaneSpecificationDimensions**.
- The validation rules now accept **boolean** types for certain properties, improving flexibility in handling flag values.

## How to Run SHACL Validation Tests

1. Clone the repository.
2. Navigate to the `hdmap/tests/` directory.
3. Run the `src/check_jsonld_against_shacl_schema.py` on the test file. Or run `src/run_all_checks_locally.py`

Example command:
```bash
python3 check_jsonld_against_shacl_schema.py \hdmap\openlabel_instance.json
