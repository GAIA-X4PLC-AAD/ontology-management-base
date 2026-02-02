# Base References Repository

This directory acts as a centralized storage for JSON-LD reference data files that are reused across different ontology instances.

## Automatic Resolution Logic

The validation script (`validate_data_conformance.py`) has been updated to automatically look in this directory when validating an instance file.

1. **Prefix Detection**: When an instance file is loaded (e.g., `envited-x_instance.json`), the script extracts the prefix (everything before the first `_`).
   - Example: `envited-x_instance.json` -> Prefix: `envited-x`

2. **File Matching**: The script scans this `base-references` folder for any file that:
   - Starts with that prefix (e.g., `envited-x...`)
   - Ends with `...reference.json`.

## Naming Convention

To ensure your reference files are picked up automatically, name them using the following pattern:
`<ontology-prefix>_<descriptive-suffix>_reference.json`

**Examples:**

- `environment-model_manifest_reference.json` (Matches `environment-model_instance.json`)
- `envited-x_legalperson_reference.json` (Matches `envited-x_instance.json`)
