# Install, Test, Build

This page covers the full setup flow for users and contributors.

## Requirements

- Python 3.12
- Git

## Install

```bash
git clone https://github.com/gaia-x4plc-aad/ontology-management-base.git
cd ontology-management-base

git submodule update --init --recursive

python3 -m venv .venv
source .venv/bin/activate

python3 -m pip install --upgrade pip

python3 -m pip install -e .
```

For development:

```bash
python3 -m pip install -e ".[dev]"
pre-commit install
```

## VS Code: Auto-activate virtual environment

Install the Python extension, then select the interpreter for this workspace so terminals auto-activate it.

1. Command Palette → "Python: Select Interpreter" → choose `.venv`.
2. Ensure these settings are enabled:

```json
{
  "python.terminal.activateEnvironment": true,
  "python.venvFolders": [".venv", "venv", "env"]
}
```

## Test

Run the full validation suite:

```bash
make test
```

Run a single domain:

```bash
python3 -m src.tools.validators.validation_suite --run all --domain hdmap
```

## Build Documentation

Install docs extras first:

```bash
python3 -m pip install -e ".[docs]"
```

Build the site:

```bash
mkdocs build
```

To preview locally (auto-generates docs assets):

```bash
DOCS_SITE_URL=http://127.0.0.1:8000/ontology-management-base mkdocs serve
```

Notes:

Hook flow (via `hooks/copy_artifacts.py`):

1. The hook runs `properties_updater` and `class_page_generator` (DOCS_SITE_URL is optional and only affects local diagram links).
2. `properties_updater` writes tracked `artifacts/<domain>/PROPERTIES.md`, generates `docs/ontologies/properties/<domain>.md` (ignored by git), builds the `docs/ontologies/properties.md` domains overview, and refreshes `docs/ontologies/catalog.md`.
3. `class_page_generator` writes `docs/ontologies/classes/<domain>/*.md` and uses `DOCS_SITE_URL` to build local diagram links.
4. The hook copies `artifacts/<domain>/` into `docs/artifacts/<domain>/<versionInfo>/` and adds example instances from `tests/data/`.

## Common Troubleshooting

- If `pyshacl` is missing, install dev dependencies.
- If catalogs are missing, run the registry updater:

```bash
python3 -m src.tools.utils.registry_updater
```
