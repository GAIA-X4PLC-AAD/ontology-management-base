# Validation Suite

`validation_suite.py` is the orchestrator for all checks.

## Run All Checks

```bash
python3 -m src.tools.validators.validation_suite --run all
```

## Run a Single Check

```bash
python3 -m src.tools.validators.validation_suite --run check-data-conformance --domain hdmap
```

## Path Mode

Use `--path` to validate arbitrary files via a temporary catalog domain:

```bash
python3 -m src.tools.validators.validation_suite --run check-data-conformance --path path/to/data.jsonld
```

## Check Types

- `check-syntax`
- `check-artifact-coherence`
- `check-data-conformance`
- `check-failing-tests`
- `all`

