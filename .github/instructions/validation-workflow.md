# Validation Workflow

## Overview

The validation suite performs four types of checks:

| Check                      | Purpose                                | Applies To       |
| -------------------------- | -------------------------------------- | ---------------- |
| `check-syntax`             | Verify JSON/Turtle are well-formed     | All modes        |
| `check-artifact-coherence` | Verify SHACL targets match OWL classes | Domain mode only |
| `check-data-conformance`   | Validate data against SHACL shapes     | All modes        |
| `check-failing-tests`      | Verify invalid data fails correctly    | Domain mode only |

## Operation Modes

### 1. Auto Discovery Mode (Default)

```bash
python3 -m src.tools.validators.validation_suite
```

- Reads `tests/catalog-v001.xml`
- Discovers all registered domains
- Runs all checks for each domain

### 2. Domain Selection Mode

```bash
python3 -m src.tools.validators.validation_suite --domain manifest scenario
```

- Reads `tests/catalog-v001.xml`
- Filters to specified domains only
- Runs all checks for those domains

### 3. Path Validation Mode

```bash
python3 -m src.tools.validators.validation_suite --path ./my_data.json ./more_data/
```

- Creates temporary in-memory catalog from provided paths
- Limited checks available (syntax, conformance only)
- Useful for pre-commit validation

## Path Mode Workflow

When `--path` is used, the system builds a temporary catalog:

```
┌──────────────────────────────────────────────────────────┐
│  Step 1: Collect Files                                   │
│  registry_updater.create_temporary_catalog(paths)        │
│                                                          │
│  Uses file_collector.py to find:                         │
│  • *.json, *.jsonld files                               │
└──────────────────────────────────────────────────────────┘
                          │
                          ▼
┌──────────────────────────────────────────────────────────┐
│  Step 2: Analyze Types                                   │
│                                                          │
│  For each JSON-LD file:                                  │
│  • Parse @context to find ontology prefixes              │
│  • Extract rdf:type values                               │
│  • Map types to domains via registry_resolver            │
└──────────────────────────────────────────────────────────┘
                          │
                          ▼
┌──────────────────────────────────────────────────────────┐
│  Step 3: Build Temporary Catalog                         │
│                                                          │
│  Create in-memory catalog entries:                       │
│  • Test data files (from --path)                         │
│  • Required ontologies (from artifacts/catalog)          │
│  • Required SHACL shapes (from artifacts/catalog)        │
│  • Required fixtures (from tests/catalog)                │
└──────────────────────────────────────────────────────────┘
                          │
                          ▼
┌──────────────────────────────────────────────────────────┐
│  Step 4: Validate via Standard Pipeline                  │
│                                                          │
│  registry_resolver reads from temp catalog               │
│  Validators work identically to domain mode              │
└──────────────────────────────────────────────────────────┘
```

## SHACL Validation Pipeline (check-data-conformance)

```
┌─────────────────────────────────────────────────────────┐
│  1. Load Data Files                                     │
│                                                         │
│  graph_loader.load_jsonld_files(paths)                  │
│  → Returns data_graph + prefixes                        │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│  2. Extract RDF Types                                   │
│                                                         │
│  graph_loader.extract_rdf_types(data_graph)             │
│  → Returns set of type IRIs                             │
│  → e.g., {"https://w3id.org/.../Scenario"}              │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│  3. Discover Required Schemas                           │
│                                                         │
│  registry_resolver.discover_required_schemas(types)     │
│  → Maps types to domains                                │
│  → Returns ontology_paths, shacl_paths                  │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│  4. Load Ontology + SHACL Graphs                        │
│                                                         │
│  graph_loader.load_turtle_files(ontology_paths)         │
│  graph_loader.load_turtle_files(shacl_paths)            │
│  Also loads base ontologies from imports/catalog        │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│  5. Resolve External References                         │
│                                                         │
│  For did:web: IRIs in data_graph:                       │
│  → registry_resolver.resolve_fixture_iri(iri)           │
│  → Load fixture file into data_graph                    │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│  6. Apply RDFS Inference                                │
│                                                         │
│  inference.apply_rdfs_inference(data_graph, ont_graph)  │
│  → Expands subclass/subproperty relationships           │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│  7. Run SHACL Validation                                │
│                                                         │
│  pyshacl.validate(data_graph, shacl_graph, ont_graph)   │
│  → Returns conforms, report_graph, report_text          │
└─────────────────────────────────────────────────────────┘
```

## Fixture Resolution

External references (did:web: IRIs) are resolved to local fixture files:

```json
{
  "@id": "did:web:test.fixture.net:LegalPerson:example",
  "gx:copyrightOwnedBy": {
    "@id": "did:web:registry.gaia-x.eu:participant:xyz"
  }
}
```

The `did:web:registry.gaia-x.eu:participant:xyz` IRI is:

1. Looked up in `tests/catalog-v001.xml` (fixtures section)
2. Resolved to local file `tests/fixtures/gx/participant_xyz.json`
3. Loaded into the data graph before validation

## Coherence Validation Pipeline (check-artifact-coherence)

```
┌─────────────────────────────────────────────────────────┐
│  1. Load Ontology Classes                               │
│                                                         │
│  For domain OWL file:                                   │
│  → Extract owl:Class and rdfs:Class definitions         │
│  → Extract rdfs:label mappings                          │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│  2. Load Base Classes                                   │
│                                                         │
│  From imports/catalog:                                  │
│  → Load RDF, RDFS, OWL, SKOS base ontologies            │
│  → Extract standard classes                             │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│  3. Extract SHACL Target Classes                        │
│                                                         │
│  From domain SHACL files:                               │
│  → Extract sh:targetClass values                        │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│  4. Compare Sets                                        │
│                                                         │
│  valid_classes = ontology_classes ∪ base_classes        │
│  missing = shacl_targets - valid_classes                │
│                                                         │
│  If missing is not empty → FAIL                         │
└─────────────────────────────────────────────────────────┘
```

## Return Codes

| Code | Meaning                                     |
| ---- | ------------------------------------------- |
| 0    | Success                                     |
| 1    | General error                               |
| 100  | Skipped                                     |
| 101  | JSON syntax error                           |
| 102  | Turtle syntax error                         |
| 200  | Coherence error (SHACL target not in OWL)   |
| 210  | Conformance error (SHACL validation failed) |
| 99   | Missing dependency (pyshacl not installed)  |

## Failing Tests (check-failing-tests)

Files in `tests/data/{domain}/invalid/` are expected to FAIL validation.

Each invalid file has a corresponding `.expected` file:

```
tests/data/manifest/invalid/
├── missing_required.json
└── missing_required.expected    # Expected error output
```

The test passes if:

1. Validation returns code 210 (SHACL violation)
2. Error output matches the `.expected` file content
