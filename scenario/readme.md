# Scenario Ontology & SHACL Validation

### Key Files in This Directory

1. **scenario_ontology.ttl**  
   The RDF Turtle file defining the **Scenario** ontology. This file formalizes the **Scenario** class, including its properties such as `hasContent`, and its relationship with **OpenLABEL** content.

   - **Scenario:ContentOrTag**: A union class combining **scenario:Content** and **openlabel:Tag**, allowing flexibility in the types of content that can be included in a scenario.
   - **scenario:hasContent**: An object property linking the scenario to its content, which can either be **Scenario:Content** or **OpenLABEL:Tag**.

2. **scenario_shacl.ttl**  
   This file contains the SHACL validation rules used to ensure that **Scenario** instances conform to the defined ontology structure. SHACL ensures that the content of the scenario complies with the defined classes and properties.

   - The shape for **scenario:hasContent** ensures that the content is either of type **scenario:Content**, **openlabel:Tag**, or a boolean flag. This provides flexibility to integrate **OpenLABEL** tags in the **Scenario** content model.

3. **tests/**  
   A directory containing the validation tests for the **Scenario** ontology. The tests check if **Scenario** instances follow the SHACL rules and constraints specified in `scenario_shacl.ttl`. The tests include both positive and negative cases.

   - **fail_false_value_scenario_instance.json**: A test case for an invalid instance of **Scenario**, where a boolean value (`openlabel:LaneSpecificationDimensions`) is incorrectly set to `false`.
   - **fail_false_value_scenario_instance.expected**: The expected result when running the invalid instance, asserting that the instance fails the SHACL validation.

## How to Run SHACL Validation Tests

1. Clone the repository.
2. Navigate to the `scenario/tests/` directory.
3. Run `src/check_jsonld_against_shacl_schema.py` on the test file. Or run `src/run_all_checks_locally.py`

Example command:
```bash
python3 check_jsonld_against_shacl_schema.py \scenario\scenario_instance.json
