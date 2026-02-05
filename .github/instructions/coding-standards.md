# Coding Standards

## Module Docstring Template

Every module MUST have a docstring header following this format:

```python
#!/usr/bin/env python3
"""
Module Name - Brief Description

One or two sentences explaining the module's purpose and role in the system.

FEATURE SET:
============
1. function_one - Brief description of what it does
2. function_two - Brief description of what it does
3. ClassName - Brief description of the class

USAGE:
======
    from src.tools.module.submodule import function_one, ClassName

    # Example 1: Basic usage
    result = function_one(arg1, arg2)

    # Example 2: With options
    obj = ClassName(config)
    obj.process(data)

STANDALONE TESTING:
==================
    python3 -m src.tools.module.submodule [--test] [options]

    Options:
      --test      Run self-tests
      --verbose   Verbose output

DEPENDENCIES:
=============
- rdflib: RDF graph handling
- pyshacl: SHACL validation (validators only)

NOTES:
======
- Important architectural decision or constraint
- Known limitation or edge case
"""
```

## Function Documentation

Every public function MUST have a docstring:

```python
def validate_data(
    files: List[Path],
    root_dir: Path,
    inference_mode: str = "rdfs",
) -> Tuple[int, str]:
    """
    Validate JSON-LD files against SHACL shapes.

    Args:
        files: List of JSON-LD file paths to validate
        root_dir: Repository root directory for path resolution
        inference_mode: Inference mode (rdfs|owlrl|none|both)

    Returns:
        Tuple of (return_code, output_message) where:
        - return_code: 0 for success, non-zero for failure
        - output_message: Human-readable result or error

    Raises:
        CatalogError: If required schemas not found in catalog
        ValidationError: If validation cannot proceed

    Example:
        >>> code, msg = validate_data([Path("data.json")], Path("/repo"))
        >>> if code == 0:
        ...     print("Valid!")
    """
```

## Logging

### Configuration

Use the centralized logger from `core/logging.py`:

```python
from src.tools.core.logging import get_logger

logger = get_logger(__name__)

def my_function():
    logger.info("Starting process")
    logger.debug("Detail: %s", some_var)
    logger.warning("Potential issue: %s", warning)
    logger.error("Failed: %s", error)
```

### Log Levels

| Level     | Use Case                                 |
| --------- | ---------------------------------------- |
| `DEBUG`   | Detailed tracing, variable values        |
| `INFO`    | Progress messages, milestones            |
| `WARNING` | Recoverable issues, deprecations         |
| `ERROR`   | Failures that stop the current operation |

### CLI Output vs Logging

- **Logging** (`logger.info`): Internal progress, can be silenced
- **Print** (`print()`): Direct user output (results, reports)

```python
# Good: Use logger for progress
logger.info("Loading %d files...", len(files))

# Good: Use print for final output
print(f"✅ Validation passed: {domain}")

# Bad: Don't use print for internal progress
print("Loading files...")  # Should be logger.info
```

## Error Handling

### Use Specific Exceptions

```python
from src.tools.core.exceptions import CatalogError, ValidationError

def get_schema_path(domain: str) -> Path:
    path = self._catalog.get(domain)
    if not path:
        raise CatalogError(f"Domain '{domain}' not found in catalog")
    return path
```

### Return Codes

Use `ReturnCodes` from `core/result.py`:

```python
from src.tools.core.result import ReturnCodes

def check_syntax(file: Path) -> Tuple[int, str]:
    try:
        # ... validation logic
        return ReturnCodes.SUCCESS, "Syntax OK"
    except json.JSONDecodeError as e:
        return ReturnCodes.JSON_SYNTAX_ERROR, f"Invalid JSON: {e}"
```

### No Silent Failures

```python
# Bad: Silent fallback
def get_ontology(domain):
    path = catalog.get(domain)
    if not path:
        return None  # Caller might not check!

# Good: Explicit error
def get_ontology(domain):
    path = catalog.get(domain)
    if not path:
        raise CatalogError(f"Ontology for '{domain}' not in catalog")
    return path
```

## Path Handling

### Always Use Path Objects

```python
from pathlib import Path

# Good
file_path = Path(input_str)
full_path = root_dir / "artifacts" / domain / f"{domain}.owl.ttl"

# Bad
file_path = input_str
full_path = os.path.join(root_dir, "artifacts", domain, f"{domain}.owl.ttl")
```

### Normalize for Display

```python
from src.tools.utils.print_formatter import normalize_path_for_display

# Good: Hide user paths in output
display = normalize_path_for_display(abs_path, root_dir)
logger.info("Processing: %s", display)

# Bad: Leak full paths
logger.info("Processing: %s", abs_path)  # Shows /home/user/...
```

## Import Organization

```python
#!/usr/bin/env python3
"""Module docstring..."""

# 1. Standard library
import json
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# 2. Third-party
from rdflib import Graph, Namespace

# 3. Local - core (no relative imports)
from src.tools.core.constants import FAST_STORE
from src.tools.core.logging import get_logger
from src.tools.core.result import ReturnCodes, ValidationResult

# 4. Local - utils
from src.tools.utils.graph_loader import load_graph
from src.tools.utils.registry_resolver import RegistryResolver

logger = get_logger(__name__)
```

## Type Hints

Always use type hints for function signatures:

```python
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple, Union

def process_files(
    paths: List[Path],
    options: Optional[Dict[str, str]] = None,
) -> Tuple[int, List[str]]:
    ...
```

## Main Function Pattern

Every module MUST have a `main()` function for standalone testing:

```python
def _run_tests() -> bool:
    """Run self-tests for the module."""
    print("Running module self-tests...")
    all_passed = True

    # Test 1
    try:
        result = some_function("test")
        assert result == expected
        print("PASS: test description")
    except AssertionError:
        print("FAIL: test description")
        all_passed = False

    return all_passed


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--test", action="store_true", help="Run self-tests")
    # ... other arguments

    args = parser.parse_args()

    if args.test:
        success = _run_tests()
        sys.exit(0 if success else 1)

    # ... main logic


if __name__ == "__main__":
    main()
```
