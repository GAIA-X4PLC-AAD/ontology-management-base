# Syntax Checks

Syntax checks verify that JSON-LD and Turtle files are well-formed.

## Recommended Usage

```bash
python3 -m src.tools.validators.validation_suite --run check-syntax --domain hdmap
```

## Direct Module Usage

```bash
python3 -m src.tools.validators.syntax_validator --json tests/data/hdmap/
python3 -m src.tools.validators.syntax_validator --turtle artifacts/hdmap/
```

