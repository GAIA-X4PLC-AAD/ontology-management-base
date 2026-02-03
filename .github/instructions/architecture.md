# Architecture

## Module Hierarchy

```
src/tools/
├── core/                    # Foundation layer (no internal dependencies)
│   ├── constants.py         # FAST_STORE, Extensions, Namespaces
│   ├── result.py            # ReturnCodes, ValidationResult
│   ├── logging.py           # Centralized logger configuration
│   └── iri_utils.py         # IRI string manipulation utilities
│
├── utils/                   # Utility layer (depends on core/)
│   ├── file_collector.py    # File discovery (INTERNAL - used by registry_updater only)
│   ├── registry_updater.py  # Catalog writer (creates/updates XML catalogs)
│   ├── registry_resolver.py # Catalog reader (lookups, path resolution)
│   ├── graph_loader.py      # RDF graph loading utilities
│   └── print_formatter.py   # Output formatting for CLI
│
├── validators/              # Validation layer (depends on core/, utils/)
│   ├── validation_suite.py  # Main CLI orchestrator
│   ├── syntax_validator.py  # JSON/Turtle syntax checking
│   ├── coherence_validator.py # SHACL↔OWL alignment checking
│   ├── conformance_validator.py # SHACL data validation
│   └── shacl/               # SHACL validation internals
│       ├── validator.py     # ShaclValidator class
│       ├── schema_discovery.py # Type→schema mapping
│       └── inference.py     # RDFS/OWL inference
```

## Dependency Rules

1. **core/** → No internal dependencies (only stdlib + rdflib)
2. **utils/** → May import from `core/`
3. **validators/** → May import from `core/` and `utils/`
4. **Never** import upward (utils cannot import from validators)

## Data Flow

```
User Request
    │
    ├─── --domain manifest ─────┐
    │                           │
    └─── --path ./data/*.json   │
              │                 │
              ▼                 │
    ┌─────────────────────┐     │
    │  registry_updater   │     │
    │ (build temp catalog)│     │
    └─────────────────────┘     │
              │                 │
              ▼                 ▼
    ┌─────────────────────────────┐
    │       XML Catalogs          │
    │ (single source of truth)    │
    │                             │
    │ • artifacts/catalog-v001.xml│
    │ • imports/catalog-v001.xml  │
    │ • tests/catalog-v001.xml    │
    │ • (temp in-memory catalog)  │
    └─────────────────────────────┘
              │
              ▼
    ┌─────────────────────┐
    │  registry_resolver  │
    │  (lookup paths)     │
    └─────────────────────┘
              │
              ▼
    ┌─────────────────────┐
    │    graph_loader     │
    │  (load RDF files)   │
    └─────────────────────┘
              │
              ▼
    ┌─────────────────────┐
    │     validators      │
    │  (validate data)    │
    └─────────────────────┘
```

## Catalog Structure

### artifacts/catalog-v001.xml

Maps ontology IRIs to local OWL/SHACL/context files:

```xml
<uri name="https://w3id.org/.../scenario/v5/" uri="scenario/scenario.owl.ttl"/>
<uri name="https://w3id.org/.../scenario/v5/shapes" uri="scenario/scenario.shacl.ttl"/>
```

### imports/catalog-v001.xml

Maps base ontology IRIs (RDF, RDFS, OWL, SKOS) to local copies:

```xml
<uri name="http://www.w3.org/1999/02/22-rdf-syntax-ns#" uri="rdf/rdf.ttl"/>
```

### tests/catalog-v001.xml

Maps test files with metadata (domain, test-type, category):

```xml
<uri name="test:scenario:valid:001" uri="data/scenario/valid/instance.json"
     domain="scenario" test-type="valid" category="test-data"/>
```

## Module Responsibilities

### file_collector.py

- **Purpose**: Scan file system for files by extension/pattern
- **Used by**: `registry_updater.py` ONLY
- **Never used by**: validators, registry_resolver

### registry_updater.py

- **Purpose**: Create and update XML catalog files
- **Key functions**:
  - `update_artifacts_catalog()` - Scan artifacts/, update catalog
  - `update_tests_catalog()` - Scan tests/data/, update catalog
  - `create_temporary_catalog()` - Build in-memory catalog from arbitrary paths
- **Uses**: `file_collector.py`

### registry_resolver.py

- **Purpose**: Read catalogs, resolve IRIs to paths
- **Key functions**:
  - `get_ontology_path(domain)` - Get OWL file path
  - `get_shacl_paths(domain)` - Get SHACL file paths
  - `get_test_files(domain, test_type)` - Get test data files
  - `resolve_fixture_iri(iri)` - Resolve did:web: to local fixture
- **Never does**: File system scanning

### graph_loader.py

- **Purpose**: Load RDF files into graphs
- **Key functions**:
  - `load_graph(path)` - Load single file
  - `load_jsonld_files(paths)` - Load JSON-LD with prefix extraction
  - `load_turtle_files(paths)` - Load Turtle files
  - `extract_external_iris(graph)` - Find did:web: references
- **Used by**: validators (after resolver provides paths)
