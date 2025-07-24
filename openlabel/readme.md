# OpenLABEL Ontology and SHACL Validation

## Overview

The **OpenLABEL** folder contains the ontology and SHACL (Shapes Constraint Language) validation rules for **OpenLABEL** tags used in digital asset scenarios. The **OpenLABEL** ontology provides a structure for labeling and tagging various digital assets, and the SHACL validation ensures that the instances of these tags adhere to the specified structure.

This folder includes the following key files:

### Key Files in This Directory

1. **openlabel_ontology_scenario_tags.ttl**  
   This file defines the **OpenLABEL** ontology in **Turtle** (TTL) format. It describes the tags used in **OpenLABEL** for labeling digital assets in a scenario. The ontology includes classes and properties relevant to **OpenLABEL** tags, enabling them to be used effectively in digital asset tagging.

   - **openlabel:Tag**: Defines the structure for the OpenLABEL tag.
    
2. **openlabel_shacl.ttl**  
   This file contains the SHACL validation rules for the **OpenLABEL** ontology. SHACL is used to validate the structure and data types of **OpenLABEL** instances, ensuring they conform to the expected ontology constraints. The SHACL shapes define the constraints for properties within **OpenLABEL** tags.
   - **Shape for `openlabel:Tag`**: Ensures that instances of **OpenLABEL:Tag** adhere to the ontology's structure.
3. **openlabel_instance.json**  
   This file contains a sample **OpenLABEL** instance in **JSON-LD** format. 
4. **tests/**  
   The `tests/` folder contains the validation tests for the **OpenLABEL** ontology. These tests are designed to check if **OpenLABEL** instances conform to the SHACL validation rules in `openlabel_shacl.ttl`.

   - **fail_wrong_value_openlabel_instance.json**: A test case for an invalid **OpenLABEL** instance with incorrect values (e.g., invalid data types or missing properties).
   - **fail_wrong_value_openlabel_instance.expected**: The expected result when running the invalid instance, asserting that the instance fails the SHACL validation.

## Purpose of OpenLABEL Ontology

The **OpenLABEL** ontology defines the tagging structure used to label digital assets within a scenario. It provides a standardized way to represent metadata about digital assets, including properties like **LaneSpecificationDimensions**. By combining this ontology with other data models, such as **HDMap**, **OpenLABEL** enhances the flexibility and interoperability of digital asset descriptions.

## How to Run SHACL Validation Tests

1. Clone the repository.
2. Navigate to the `openlabel/tests/` directory.
3. Run `src/check_jsonld_against_shacl_schema.py` on the test file. Or run `src/run_all_checks_locally.py`

Example command:
```bash
python3 check_jsonld_against_shacl_schema.py \openlabel\openlabel_instance.json
