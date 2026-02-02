# Validation Tools Troubleshooting

This guide helps you resolve common issues when using validation tools.

## Common Issues and Solutions

### Issue: "File not found" error

**Symptoms:**

```
FileNotFoundError: [Errno 2] No such file or directory: 'artifacts/scenario/scenario.owl.ttl'
```

**Solutions:**

1. **Check file exists:**

   ```bash
   ls -la artifacts/scenario/scenario.owl.ttl
   ```

2. **Use absolute path:**

   ```bash
   python src/tools/validators/validate_artifact_coherence.py \
     --ontology-file /full/path/to/artifacts/scenario/scenario.owl.ttl \
     --shapes-file /full/path/to/artifacts/scenario/scenario.shacl.ttl
   ```

3. **Run from correct directory:**

   ```bash
   cd /home/carlo/workspace/ontology-management-base
   python src/tools/validators/validate_artifact_coherence.py ...
   ```

4. **Check capitalization** (Linux is case-sensitive):

   ```bash
   # ❌ Wrong
   python check_target_CLASSES.py

   # ✅ Correct
   python validate_artifact_coherence.py
   ```

---

### Issue: "ModuleNotFoundError" or "ImportError"

**Symptoms:**

```
ModuleNotFoundError: No module named 'rdflib'
ImportError: cannot import name 'Graph' from 'rdflib'
```

**Solutions:**

1. **Install required packages:**

   ```bash
   pip install rdflib pyshacl
   ```

2. **Check Python version** (requires 3.7+):

   ```bash
   python --version
   ```

3. **Use correct Python interpreter:**

   ```bash
   python3 src/tools/...  # Use python3 explicitly
   ```

4. **Check installation:**

   ```bash
   python -c "import rdflib; print(rdflib.__version__)"
   ```

5. **Virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

---

### Issue: "Invalid RDF/Turtle syntax"

**Symptoms:**

```
rdflib.exceptions.ParsingError: Expected end of file
Parsing error on line 42: Unexpected token
```

**Solutions:**

1. **Validate Turtle syntax:**

   ```bash
   # Try parsing with rapper (if installed)
   rapper -i turtle artifacts/scenario/scenario.owl.ttl

   # Or use Python
   python -c "from rdflib import Graph; g = Graph(); g.parse('file.ttl')"
   ```

2. **Check for common mistakes:**

   ```turtle
   # ❌ Missing period at end of triple
   ex:property ex:value "value"

   # ✅ Correct
   ex:property ex:value "value" .
   ```

3. **Validate namespace declarations:**

   ```turtle
   # ❌ Missing @prefix
   ex:property ex:value .

   # ✅ Correct
   @prefix ex: <http://example.com/> .
   ex:property ex:value .
   ```

4. **Check for special characters:**

   ```turtle
   # ❌ Unescaped quotes
   ex:label "He said "hello"" .

   # ✅ Correct
   ex:label "He said \"hello\"" .
   ```

---

### Issue: "No validation violations found but data seems wrong"

**Symptoms:**

- Validator says data is valid
- But you know there's a problem
- Expected violations not reported

**Solutions:**

1. **Check shapes are loaded:**

   ```bash
   # Count shapes in file
   grep -c "sh:NodeShape\|sh:PropertyShape" artifacts/scenario/scenario.shacl.ttl
   # Should be > 0
   ```

2. **Verify shapes target correct classes:**

   ```bash
   # Check shape targets
   grep "sh:targetClass" artifacts/scenario/scenario.shacl.ttl

   # Compare to data being validated
   grep "a scenario:" my-data.ttl
   ```

3. **Enable debug output:**

   ```bash
   python -u src/tools/validators/validate_data_conformance.py \
     --ontology-file scenario.owl.ttl \
     --shacl-file scenario.shacl.ttl \
     --data-file my-data.ttl \
     --debug
   ```

4. **Check SHACL shape severity:**
   ```turtle
   # Shapes with sh:Warning might not cause validation failure
   sh:severity sh:Warning .  # Only warns, doesn't fail
   sh:severity sh:Violation .  # Causes failure
   ```

---

### Issue: "Validation hangs or very slow"

**Symptoms:**

- Tool runs but takes very long time
- Process seems stuck
- Memory usage very high

**Solutions:**

1. **Check data size:**

   ```bash
   # Count RDF triples
   wc -l my-data.ttl

   # For >100K triples, expect slower validation
   ```

2. **Enable timeout:**

   ```bash
   # Linux/Mac: timeout after 60 seconds
   timeout 60 python src/tools/validators/validate_data_conformance.py ...
   ```

3. **Optimize SHACL shapes:**

   ```bash
   python src/tools/optimize_shacl_validation.py \
     --shacl-file scenario.shacl.ttl \
     --analysis detailed
   ```

4. **Validate subset of data:**

   ```bash
   # Extract first 1000 lines
   head -1000 my-data.ttl > my-data-subset.ttl

   # Validate subset
   python src/tools/validators/validate_data_conformance.py \
     --data-file my-data-subset.ttl ...
   ```

5. **Use streaming approach:**
   - Split large file into smaller chunks
   - Validate each chunk separately
   - Aggregate results

---

### Issue: "ValidationResult shows wrong focus node"

**Symptoms:**

- Violation report shows different node than expected
- Tracing error is confusing

**Solutions:**

1. **Understand focus node:**

   ```
   Focus Node = The IRI/blank node being validated
   Property Path = Which property has the issue
   Message = What the problem is
   ```

2. **Check your shapes:**

   ```turtle
   # Make sure sh:targetClass is correct
   sh:targetClass scenario:Scenario ;  # Does this match your data?
   ```

3. **Verify data IRIs:**

   ```bash
   # Extract all IRIs from data
   grep "^<" my-data.ttl | cut -d' ' -f1 | sort | uniq

   # Do these match shape targets?
   ```

---

### Issue: "SHACL shape validation passes but OWL reasoning fails"

**Symptoms:**

- Data validates against SHACL shapes
- But OWL reasoner detects inconsistencies
- Seems contradictory

**This is normal!** OWL and SHACL have different purposes:

- **SHACL**: Checks structural constraints ("does data have required properties?")
- **OWL**: Checks semantic consistency ("are the logical meanings contradictory?")

**Solution:**
Run both validations:

```bash
# 1. Check structure with SHACL
python src/tools/validators/validate_data_conformance.py ...

# 2. Check semantics with OWL reasoner
python -c "
from rdflib import Graph
from rdflib.plugins.inferencing.FuXL import RETE_OWL_Semantics

g = Graph()
g.parse('my-data.ttl', format='turtle')
# Run reasoner...
"
```

---

### Issue: "Different results running tool multiple times"

**Symptoms:**

- Same input produces different validation results
- Inconsistent behavior between runs
- Blank nodes treated differently

**Solutions:**

1. **Check for blank nodes in shapes:**

   ```bash
   grep "_:" artifacts/scenario/scenario.shacl.ttl
   # Blank nodes may have different treatment
   ```

2. **Use stable identifiers:**

   ```turtle
   # ❌ Problematic (blank node)
   [] a sh:NodeShape ;
       sh:targetClass scenario:Scenario .

   # ✅ Better (stable IRI)
   scenario:ScenarioShape
       a sh:NodeShape ;
       sh:targetClass scenario:Scenario .
   ```

3. **Check ontology imports:**
   - Ensure consistent versions are imported
   - Avoid circular dependencies
   - Verify import paths

4. **Reproducibility:**
   ```bash
   # Use fixed seed for any randomization
   export PYTHONHASHSEED=0
   python src/tools/validators/...
   ```

---

### Issue: "JSON-LD context not recognized"

**Symptoms:**

```
No property found for JSON-LD context: "@context"
Context mismatch: expected http://example.com/context, got http://example.com/v2/context
```

**Solutions:**

1. **Verify context file:**

   ```bash
   # Check context file exists
   ls -la artifacts/scenario/scenario.context.jsonld
   ```

2. **Update context reference:**

   ```json
   {
     "@context": "https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/",
     "@id": "urn:uuid:...",
     "type": "Scenario"
   }
   ```

3. **Inline context if needed:**

   ```json
   {
     "@context": {
       "scenario": "https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/",
       "hasComplexity": "scenario:hasComplexity"
     },
     ...
   }
   ```

4. **Test context resolution:**
   ```bash
   curl -H "Accept: application/ld+json" \
     https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/
   ```

---

## Debug Mode

Most tools support verbose/debug output:

```bash
# Enable debug logging
export DEBUG=1
python src/tools/validators/validate_data_conformance.py \
  --ontology scenario.owl.ttl \
  --shacl scenario.shacl.ttl \
  --data my-data.ttl \
  --verbose \
  --debug
```

Output will show:

- File loading steps
- RDF parsing details
- Graph composition
- Validation stages
- Detailed violation reasons

## Getting Help

If you still have issues:

1. **Check the tool documentation:** See [Validation Tools](00-index.md) for tool-specific info
2. **Enable debug mode** and capture output
3. **Simplify your test case** to minimal example
4. **Check RDF/OWL/SHACL specs:**
   - [W3C RDF](https://www.w3.org/RDF/)
   - [W3C OWL](https://www.w3.org/OWL/)
   - [W3C SHACL](https://www.w3.org/TR/shacl/)
5. **Open an issue** with:
   - Tool version
   - Python version
   - Minimal reproducible example
   - Debug output
   - Expected vs actual behavior

## Performance Checklist

If tools are slow:

- [ ] Check data size (is it >100K triples?)
- [ ] Check system resources (CPU, memory, disk I/O)
- [ ] Simplify SHACL shapes (remove unnecessary constraints)
- [ ] Use shape optimization: `optimize_shacl_validation.py`
- [ ] Profile tool: `python -m cProfile -s cumtime ...`
- [ ] Consider streaming validation for huge datasets
- [ ] Ensure you're not validating unnecessarily large subset

## See Also

- [Validation Tools](00-index.md) - Tool overview and comparison
- [First Validation](../4-getting-started/03-first-validation.md) - Tutorial
- [RDF, OWL, SHACL](../1-foundations/02-rdf-owl-shacl.md) - Technology reference
