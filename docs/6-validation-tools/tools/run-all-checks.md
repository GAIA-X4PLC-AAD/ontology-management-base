# Run All Checks Tool

**Module:** `src.tools.validators.validation_suite`

This is the main orchestrator that runs all validation checks across ontology domains.

## Usage

### Command Line

```bash
# Run all checks on all domains
python3 -m src.tools.validators.validation_suite --run all

# Run specific check
python3 -m src.tools.validators.validation_suite --run check-data-conformance

# Run on specific domains
python3 -m src.tools.validators.validation_suite --run all --domain hdmap scenario
```

### Options

| Option             | Description                                                                                                    |
| ------------------ | -------------------------------------------------------------------------------------------------------------- |
| `--run TYPE`       | Check type: `all`, `check-syntax`, `check-artifact-coherence`, `check-data-conformance`, `check-failing-tests` |
| `--domain DOMAINS` | Space-separated list of domains to check (default: all)                                                        |
| `--path PATHS`     | File(s) or directory path(s) to validate; builds a temporary catalog domain                                    |

## Check Types

### `check-syntax`

Validates file syntax without semantic checks:

- JSON-LD parsing for `*.json` files
- Turtle parsing for `*.ttl` files

### `check-artifact-coherence`

Verifies SHACL target classes exist in OWL ontologies.

### `check-data-conformance`

Full SHACL validation of JSON-LD instances against shapes.

### `check-failing-tests`

Runs regression test suite - instances in `tests/data/{domain}/invalid/` that should fail validation with expected error messages.

### `all`

Runs all checks in order:

1. Syntax
2. Target Classes
3. SHACL
4. Failing Tests

## Domain Discovery

Domains are discovered from `tests/catalog-v001.xml` (test-data entries).
When `--path` is used, a temporary domain is created from the provided files.

## Artifacts Resolution

For each domain, the tool resolves files via catalogs:

| Artifact        | Path                                        |
| --------------- | ------------------------------------------- |
| Ontology        | `artifacts/catalog-v001.xml` entries        |
| SHACL           | `artifacts/catalog-v001.xml` entries        |
| Valid instances | `tests/catalog-v001.xml` entries            |
| Invalid tests   | `tests/catalog-v001.xml` entries            |

## Output Format

```
Detected ontology domains: ['hdmap', 'scenario', 'envited-x']

🚀 Running check mode: ALL ...

=== Checking JSON-LD syntax ===
✅ hdmap_instance.json
✅ scenario_instance.json

=== Checking TTL syntax ===
✅ hdmap_ontology.ttl
✅ hdmap_shacl.ttl

=== Checking target classes against OWL classes ===
✅ Target classes are correctly defined for hdmap.

=== Checking JSON-LD against SHACL ===
✅ hdmap conforms to SHACL constraints.

=== Running failing tests ===
✅ Test fail_01_missing_name.json for domain hdmap failed as expected.

✅ ALL checks completed successfully!
```

## Exit Codes

| Code  | Meaning                              |
| ----- | ------------------------------------ |
| 0     | All checks passed                    |
| 1     | Python version < 3.12 or not in venv |
| Other | First failing check's exit code      |

## CI Integration

This tool is called by the CI workflow with domain-specific arguments:

```yaml
- name: Run SHACL Checks
  run: python3 -m src.tools.validators.validation_suite \
    --run check-data-conformance \
    ${{ needs.changes.outputs.folders_arg }}
```

Where `folders_arg` is `--domain hdmap scenario` or empty for full suite.
