# OWL Imports

This document explains how `owl:imports` are used to establish dependencies between ontologies.

## Overview

OWL imports allow ontologies to reference and reuse definitions from other ontologies. This creates a dependency graph that the validation tools resolve automatically.

## Declaring Imports

In your ontology file, declare imports using `owl:imports`:

```turtle
@prefix owl: <http://www.w3.org/2002/07/owl#> .

<https://w3id.org/ascs-ev/envited-x/hdmap/v5> a owl:Ontology ;
    owl:imports <https://w3id.org/ascs-ev/envited-x/general/v3> ;
    owl:imports <https://w3id.org/ascs-ev/envited-x/georeference/v5> .
```

## Import Resolution

### Resolution Process

1. **Parse ontology** - Extract `owl:imports` triples
2. **Map IRI to file** - Use IRI index to find local file
3. **Load recursively** - Process imports of imported ontologies

### Local Resolution

The validation tools map import IRIs to local files:

| Import IRI                              | Local File                          |
| --------------------------------------- | ----------------------------------- |
| `https://w3id.org/.../general/v3`       | `artifacts/general/general.owl.ttl` |
| `http://www.w3.org/2000/01/rdf-schema#` | `imports/rdfs/rdfs_ontology.ttl`    |

### Catalog Support

For Protege compatibility, `imports/catalog-v001.xml` provides local mappings:

```xml
<catalog xmlns="urn:oasis:names:tc:entity:xmlns:xml:catalog">
  <uri name="http://www.w3.org/2000/01/rdf-schema#"
       uri="rdfs/rdfs_ontology.ttl"/>
</catalog>
```

## Import Hierarchy

### Core Imports

Most domain ontologies import these foundational ontologies:

```
envited-x
├── general
└── manifest

hdmap
├── general
├── georeference
└── manifest

scenario
├── general
├── georeference
└── manifest
```

### Gaia-X Integration

For Gaia-X compliance, ontologies may import:

```
domain
└── gx (Gaia-X ontology)
    └── schema.org
```

## Best Practices

### 1. Import Versioned Ontologies

Always import specific versions:

```turtle
# Good
owl:imports <https://w3id.org/.../general/v3> .

# Risky - version may change
owl:imports <https://w3id.org/.../general> .
```

### 2. Minimize Transitive Imports

Avoid importing ontologies you don't directly use:

```turtle
# If you only need 'general', don't import 'manifest' just because
# 'general' imports it - the transitive closure handles this
owl:imports <https://w3id.org/.../general/v3> .
```

### 3. Use Local Copies for Stability

The `imports/` directory contains stable copies of external ontologies:

```
imports/
├── schema/schema_ontology.ttl  # Schema.org
├── foaf/foaf_ontology.ttl      # FOAF
└── dcterms/dcterms_ontology.ttl # Dublin Core
```

## Validation Behavior

### Import Loading

The SHACL validator automatically loads all imports:

```
🔍 Starting JSON-LD SHACL validation for domain: hdmap
📌 Relevant ontology files to load:
   artifacts/hdmap/hdmap.owl.ttl
   artifacts/general/general.owl.ttl
   artifacts/georeference/georeference.owl.ttl
   imports/schema/schema_ontology.ttl
```

### Missing Imports

If an import cannot be resolved:

```
⚠️ Warning: Import not found: https://example.org/missing
   Validation may fail if classes from this ontology are referenced.
```

## Troubleshooting

### "Class not found" Errors

If validation reports missing classes:

1. Check the class is defined in an imported ontology
2. Verify the import declaration is present
3. Ensure the import file exists in `artifacts/<ontology>/` or `imports/`

### Circular Imports

The validator handles circular imports safely by tracking loaded ontologies:

```python
# Already loaded ontologies are skipped
if ontology_path in loaded_set:
    return
loaded_set.add(ontology_path)
```
