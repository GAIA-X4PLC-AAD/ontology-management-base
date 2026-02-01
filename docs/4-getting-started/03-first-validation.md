# Your First Ontology Validation

In this hands-on guide, you'll validate some sample data against an ontology from this repository. This should take 10-15 minutes.

## What You'll Learn

- How to fetch an ontology via its persistent IRI
- How to use SHACL to validate data
- How validation reports show data quality issues
- The feedback loop for fixing data problems

## Prerequisites

You'll need:

- A terminal or command line
- `curl` (to fetch files from the web)
- Python 3.7+ with `pip`
- Git (recommended but optional)

## Step 1: Install Validation Tools

First, install the Python RDF validation library:

```bash
pip install rdflib pySHACL
```

Verify installation:

```bash
python3 -c "import rdflib, pyshacl; print('Ready to validate!')"
```

## Step 2: Download the Scenario Ontology

The Scenario ontology defines concepts for test scenarios. Let's fetch it:

```bash
# Create a working directory
mkdir -p ~/ontology-validation
cd ~/ontology-validation

# Download the ontology (in Turtle format)
curl -L -H "Accept: text/turtle" \
  https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/ \
  -o scenario-ontology.ttl

# Verify the file was downloaded
ls -lh scenario-ontology.ttl
```

You should see a file ~10-20 KB with ontology definitions.

## Step 3: Create Sample Data

Now create some sample scenario data. Create a file called `sample-scenario.ttl`:

```turtle
@prefix ex: <https://example.com/scenarios/> .
@prefix scenario: <https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

# A test scenario
ex:city-driving-test
    a scenario:Scenario ;
    rdfs:label "City Driving Test" ;
    rdfs:comment "Basic urban driving scenario" ;
    scenario:hasComplexity 3 ;
    scenario:hasDescription "Vehicle drives through city with traffic" .

# Another scenario with potential issues
ex:highway-test
    a scenario:Scenario ;
    rdfs:label "Highway Driving Test" ;
    # Missing hasDescription (may be required)
    scenario:hasComplexity "high" ;  # Wrong type (should be integer)
    .
```

Save this as `sample-scenario.ttl` in your working directory.

## Step 4: Understand the Ontology

Let's see what the scenario ontology defines. View the key parts:

```bash
# Look for the Scenario class definition
grep -A5 "class Scenario" scenario-ontology.ttl | head -20
```

You'll see definitions for:

- `Scenario` class
- Properties like `hasComplexity`, `hasDescription`
- Property constraints and domains

## Step 5: Create Validation Shapes

The ontology defines what properties _can_ be used. Now create explicit validation rules using SHACL.

Create a file called `scenario-shapes.ttl`:

```turtle
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix scenario: <https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

# Validation shape for Scenario class
scenario:ScenarioShape
    a sh:NodeShape ;
    sh:targetClass scenario:Scenario ;

    # Every scenario must have a label
    sh:property [
        sh:path rdfs:label ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:datatype xsd:string ;
        sh:message "Scenario must have exactly one rdfs:label as string"@en ;
    ] ;

    # Every scenario must have a description
    sh:property [
        sh:path scenario:hasDescription ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:datatype xsd:string ;
        sh:message "Scenario must have exactly one hasDescription"@en ;
    ] ;

    # Complexity must be an integer between 1-10
    sh:property [
        sh:path scenario:hasComplexity ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:datatype xsd:integer ;
        sh:minInclusive 1 ;
        sh:maxInclusive 10 ;
        sh:message "Complexity must be integer 1-10"@en ;
    ] .
```

Save as `scenario-shapes.ttl`.

## Step 6: Validate Your Data

Now run the validation:

```bash
# Create a Python script to validate
cat > validate.py << 'EOF'
from rdflib import Graph
from pyshacl import validate

# Load data
data_graph = Graph()
data_graph.parse("sample-scenario.ttl", format="turtle")

# Load shapes
shapes_graph = Graph()
shapes_graph.parse("scenario-shapes.ttl", format="turtle")

# Validate
conforms, results_graph, results_text = validate(
    data_graph,
    shacl_graph=shapes_graph,
    onlyValidationShapes=False,
    inference=None,
    debug=False
)

print("=" * 60)
print(f"Validation Result: {'PASSED' if conforms else 'FAILED'}")
print("=" * 60)
print(results_text)

if not conforms:
    print("\nViolations found - see details above")
    exit(1)
else:
    print("\nAll data is valid!")
    exit(0)
EOF

# Run the validation
python3 validate.py
```

You should see something like:

```
============================================================
Validation Result: FAILED
============================================================
Validation Report
 Conforms: False
 Results (2):
   Focus Node: http://example.com/scenarios/highway-test
   Severity: sh:Violation
   Source Shape: [shape for hasDescription]
   Message: Scenario must have exactly one hasDescription

   Focus Node: http://example.com/scenarios/highway-test
   Severity: sh:Violation
   Source Shape: [shape for hasComplexity]
   Message: Complexity must be integer 1-10
```

## Step 7: Fix the Data

Looking at the validation report, `highway-test` has problems:

1. Missing `hasDescription`
2. `hasComplexity` is a string "high" instead of integer

Fix the data:

```turtle
# Fix in sample-scenario.ttl

ex:highway-test
    a scenario:Scenario ;
    rdfs:label "Highway Driving Test" ;
    rdfs:comment "Vehicle drives on highway" ;
    scenario:hasDescription "Vehicle drives on highway with multiple lane changes" ;  # Added
    scenario:hasComplexity 8 ;  # Fixed to integer
    .
```

Update the file and run validation again:

```bash
python3 validate.py
```

Now you should see:

```
============================================================
Validation Result: PASSED
============================================================
Conforms: True
```

Great! Your data now passes validation.

## Step 8: Understand What Just Happened

Let's recap the validation workflow:

```
Your Data (RDF)
      ↓
  [Validation]
      ↓
    ↙ ↘
  PASS  FAIL
          ↓
    [Fix Data]
          ↓
    [Re-validate]
```

You:

1. **Defined data** in RDF format (using ontology classes)
2. **Created shapes** to express validation rules
3. **Validated data** against shapes
4. **Received feedback** on what was wrong
5. **Fixed data** based on feedback
6. **Re-validated** and confirmed success

## Next Steps

### Try Other Ontologies

Repeat this process with other ontologies:

- **Service Ontology**: `https://w3id.org/gaia-x4plcaad/ontologies/service/v2/`
- **Automotive Simulator**: `https://w3id.org/gaia-x4plcaad/ontologies/automotive-simulator/v2/`
- **General Ontology**: `https://w3id.org/gaia-x4plcaad/ontologies/general/v2/`

### Automate Validation

In production, you'd typically:

```bash
# Validate all data files against ontology
for datafile in data/*.ttl; do
    python3 validate.py "$datafile"
done
```

### Learn More

- **Validation Tools**: See [Validation Tools](../6-validation-tools/) for detailed tool reference
- **SHACL Shapes**: See [RDF, OWL, and SHACL](../1-foundations/02-rdf-owl-shacl.md#shacl-validation) for more constraint types
- **More Examples**: Check [Repository Structure](04-repository-structure.md) for example data

### Use in Your Application

To integrate ontology validation into your code:

```python
from rdflib import Graph, Namespace
from pyshacl import validate

# Load your application data
data = Graph()
data.parse("my-data.ttl", format="turtle")

# Load ontology and shapes
ontology = Graph()
ontology.parse("ontology.ttl", format="turtle")

shapes = Graph()
shapes.parse("shapes.ttl", format="turtle")

# Validate
conforms, report_graph, report_text = validate(
    data,
    shacl_graph=shapes,
)

if not conforms:
    print("Data validation failed:")
    print(report_text)
else:
    print("Data is valid!")
    # Continue with your application logic
```

## Troubleshooting

### "IRI not found" error

Make sure you're using the correct, versioned IRI:

```bash
# ✅ Correct
https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/

# ❌ Wrong (no version)
https://w3id.org/gaia-x4plcaad/ontologies/scenario/
```

### Validation doesn't find shapes

Make sure both data and shapes graphs are loaded:

```python
conforms, report_g, report_t = validate(
    data_graph,
    shacl_graph=shapes_graph,  # Must specify shapes!
)
```

### "Class not found" in ontology

Check that the ontology was downloaded correctly:

```bash
grep -c "class" scenario-ontology.ttl
# Should be > 0
```

If empty, try fetching again:

```bash
curl -L -H "Accept: text/turtle" \
  https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/
```

## Quick Reference

| Action               | Command                                                                                                   |
| -------------------- | --------------------------------------------------------------------------------------------------------- |
| Download ontology    | `curl -L -H "Accept: text/turtle" https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/ -o ontology.ttl` |
| Validate data        | `python3 validate.py`                                                                                     |
| Check file size      | `ls -lh *.ttl`                                                                                            |
| View RDF content     | `head -50 data.ttl`                                                                                       |
| Count RDF statements | `grep -c ";" data.ttl`                                                                                    |

## Summary

You've successfully:

✅ Fetched an ontology from w3id.org  
✅ Created sample RDF data  
✅ Wrote SHACL validation shapes  
✅ Validated data and got feedback  
✅ Fixed data based on validation report  
✅ Confirmed fixed data passes validation

Congratulations! You now understand the ontology validation workflow.

Next: Read [Repository Structure](04-repository-structure.md) to understand where all the files are, or explore [Ontology Domains](../3-ontology-domains/) to find the right ontology for your domain.
