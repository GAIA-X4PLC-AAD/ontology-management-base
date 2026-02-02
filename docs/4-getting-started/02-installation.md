# Installation

## Prerequisites

- Python 3.12 or higher
- Git

## Clone the Repository

```bash
git clone https://github.com/gaia-x4plc-aad/ontology-management-base.git
cd ontology-management-base
```

## Set Up Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

## Install Dependencies

### For Users (Validation Only)

```bash
pip install -e .
```

### For Developers (Including Linting & Testing)

```bash
pip install -e ".[dev]"
pre-commit install
```

## Verify Installation

```bash
python3 -m src.tools.validators.validation_suite --run check-syntax --domain hdmap
```

You should see output indicating successful validation.

## Optional: Install for Documentation Development

If you want to build the documentation locally:

```bash
pip install mkdocs-material mkdocstrings[python]
mkdocs serve
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.
