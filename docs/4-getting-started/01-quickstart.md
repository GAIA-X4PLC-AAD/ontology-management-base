# Quick Start

This guide walks you through validating a JSON-LD instance file against SHACL shapes.

## 1. Prepare Your Instance File

Create a JSON-LD file following the ontology structure. Here's an example for the `hdmap` domain:

```json
{
  "@context": {
    "hdmap": "https://w3id.org/2023/10/2023/11/2024/06/2025/01/2025/01/2025/01/2025/02/2025/02/2025/02/hdmap/"
  },
  "@type": "hdmap:HDMap",
  "@id": "did:web:example.com:hdmap:001",
  "hdmap:name": "My HD Map"
}
```

## 2. Run SHACL Validation

### Option A: Validate a Specific File

```bash
python3 -m src.tools.validators.validation_suite \
  --run check-data-conformance \
  --path path/to/your/instance.json
```

### Option B: Validate All Instances for a Domain

```bash
python3 -m src.tools.validators.validation_suite \
  --run check-data-conformance \
  --domain hdmap
```

## 3. Understanding the Output

### Success Output

```
✅ hdmap conforms to SHACL constraints.
```

### Failure Output

```
❌ Error during JSON-LD SHACL validation for domain 'hdmap'.

Validation Report:
  Constraint Violation in MinCountConstraintComponent:
    Property: hdmap:name
    Message: Less than 1 values on ex:instance->hdmap:name
```

## 4. Run All Checks

To run the complete validation suite:

```bash
python3 -m src.tools.validators.validation_suite --run all
```

This runs:

1. **Syntax checks** - JSON-LD and Turtle parsing
2. **Target class checks** - OWL consistency
3. **SHACL validation** - Constraint conformance
4. **Failing tests** - Regression test suite

## Next Steps

- Browse the [Validation Tools Catalog](../validation/index.md) for detailed tool documentation
- Explore available [Ontologies](../ontologies/index.md)
- Learn about [IRI Patterns](../architecture/iri-patterns.md) for creating valid identifiers
