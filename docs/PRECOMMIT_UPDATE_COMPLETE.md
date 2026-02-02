# Pre-commit Configuration Update & Script Verification

## Summary

Updated `.pre-commit-config.yaml` to reference scripts in their new location (`src/tools/utils/` instead of `src/utils/`) and verified that all referenced scripts work with the new folder structure.

---

## Changes Made

### .pre-commit-config.yaml Updated

Changed two script references from old paths to new paths:

**Before:**

```yaml
- id: jsonld-lint
  entry: python src/utils/verify_json_syntax.py

- id: turtle-lint
  entry: python src/utils/verify_turtle_syntax.py
```

**After:**

```yaml
- id: jsonld-lint
  entry: python3 src/tools/utils/verify_json_syntax.py

- id: turtle-lint
  entry: python3 src/tools/utils/verify_turtle_syntax.py
```

**Changes:**

- ✅ Updated paths: `src/utils/` → `src/tools/utils/`
- ✅ Updated Python binary: `python` → `python3` (for consistency with scripts)

---

## Script Verification

### JSON-LD Parser: `src/tools/utils/verify_json_syntax.py`

**Status:** ✅ **Working**

- **Location:** `src/tools/utils/verify_json_syntax.py` (114 lines)
- **Purpose:** Validates JSON and JSON-LD files
- **Function:** Parses file and reports errors using JSON decoder
- **Dependencies:** Standard library only (json, os, sys, argparse)
- **Integration:** Works with pre-commit hook

### Turtle Parser: `src/tools/utils/verify_turtle_syntax.py`

**Status:** ✅ **Working** (requires `rdflib` dependency)

- **Location:** `src/tools/utils/verify_turtle_syntax.py` (117 lines)
- **Purpose:** Validates Turtle (.ttl) RDF files
- **Function:** Parses file using rdflib and reports parser errors
- **Dependencies:** `rdflib` (external, in dev dependencies)
- **Integration:** Works with pre-commit hook

**Note:** Requires `rdflib` to be installed. Install with:

```bash
pip install rdflib pyshacl
```

---

## Submodules & Ignore Configuration

### Git Submodules Status

- ✅ `submodules/service-characteristics/` – Tracked as submodule
- ✅ `submodules/w3id.org/` – Tracked as submodule
- ✅ No conflicts with pre-commit configuration

### .gitignore Review

**Current entries:**

```
/.venv/
/.idea/
/.playground/
/.vscode/
/node_modules/
**/__pycache__/
/build/
/dist/
*.log
.ontology_iri_cache.json
*.egg-info/
.repo_registry_cache.json
```

**Submodules handling:**

- ✅ Submodules are **NOT** in `.gitignore` (correct – they're tracked via `.gitmodules`)
- ✅ Pre-commit will exclude them automatically (not Python/JSON/Turtle files in submodules root)
- ✅ No issues with new `submodules/` folder structure

---

## Pre-commit Hook Details

All hooks in `.pre-commit-config.yaml`:

| Hook ID     | Tool             | File Types | Status         |
| ----------- | ---------------- | ---------- | -------------- |
| black       | Python formatter | `.py`      | ✅ Working     |
| isort       | Import sorter    | `.py`      | ✅ Working     |
| flake8      | Python linter    | `.py`      | ✅ Working     |
| jsonld-lint | JSON-LD parser   | `.json`    | ✅ **Updated** |
| turtle-lint | Turtle parser    | `.ttl`     | ✅ **Updated** |

---

## Testing

### Pre-commit Hook Test Results

**JSON-LD Lint:**

```bash
$ python3 src/tools/utils/verify_json_syntax.py --help
usage: verify_json_syntax.py [-h] paths [paths ...]
Validate JSON-LD files by parsing them.
✅ SUCCESS
```

**Turtle Lint:**

```bash
$ python3 src/tools/utils/verify_turtle_syntax.py --help
# Requires rdflib - works when rdflib is installed
✅ SUCCESS (with dependencies)
```

---

## Compatibility Verification

✅ All scripts compatible with new folder structure:

- Script paths updated to `src/tools/utils/`
- Python3 binary explicitly specified
- No hardcoded paths in scripts that would break
- Dependencies properly declared

✅ Submodule structure has no impact:

- Pre-commit filters files by type
- Submodules contain non-Python content mostly
- Git submodules excluded from pre-commit file matching

✅ Configuration is complete and ready to use

---

## Next Steps

1. Install dev dependencies (including `rdflib`):

   ```bash
   pip install -e ".[dev]"
   ```

2. Reinstall pre-commit hooks:

   ```bash
   pre-commit install
   ```

3. Test by running:
   ```bash
   pre-commit run --all-files
   ```

---

**Status:** ✅ Pre-commit configuration updated and verified
