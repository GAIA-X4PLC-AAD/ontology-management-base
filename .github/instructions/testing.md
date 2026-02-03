# Testing

## Test Structure

```
tests/
├── conftest.py              # Shared pytest fixtures
├── catalog-v001.xml         # Test data catalog
├── data/                    # Test data organized by domain
│   ├── manifest/
│   │   ├── valid/           # Files that should pass validation
│   │   │   └── manifest_instance.json
│   │   └── invalid/         # Files that should fail validation
│   │       ├── missing_required.json
│   │       └── missing_required.expected
│   └── scenario/
│       └── ...
├── fixtures/                # Mock external references (did:web:)
│   ├── gx/
│   │   └── legalperson_reference.json
│   └── ...
├── unit/                    # Unit tests
│   ├── core/
│   ├── utils/
│   └── validators/
└── integration/             # Integration tests
```

## Test Categories

### 1. Unit Tests

Test individual functions in isolation:

```python
# tests/unit/utils/test_file_collector.py

def test_collect_jsonld_files_empty_input():
    """Empty input should return empty list."""
    result = collect_jsonld_files([])
    assert result == []


def test_collect_jsonld_files_finds_nested(temp_dir):
    """Should find JSON files in subdirectories."""
    (temp_dir / "sub").mkdir()
    (temp_dir / "sub" / "test.json").write_text("{}")

    result = collect_jsonld_files([temp_dir])

    assert len(result) == 1
    assert result[0].name == "test.json"
```

### 2. Feature/End-to-End Tests

Test complete features from user perspective:

```python
# tests/integration/test_validation_suite_e2e.py

def test_domain_mode_validates_manifest(root_dir):
    """Domain mode should validate all manifest test files."""
    result = subprocess.run(
        ["python", "-m", "src.tools.validators.validation_suite",
         "--domain", "manifest"],
        capture_output=True,
        cwd=root_dir,
    )
    assert result.returncode == 0
    assert "manifest conforms" in result.stdout.decode()
```

### 3. Integration Tests

Test module interactions:

```python
# tests/integration/test_catalog_workflow.py

def test_path_mode_creates_temp_catalog(temp_dir, sample_jsonld):
    """Path mode should create temporary catalog and validate."""
    # Setup
    data_file = temp_dir / "test.json"
    data_file.write_text(sample_jsonld)

    # Execute
    resolver = RegistryResolver(temp_dir)
    temp_domain = resolver.create_temporary_domain([str(data_file)])

    # Verify
    assert temp_domain is not None
    files = resolver.get_test_files(temp_domain)
    assert len(files) == 1
```

## Required Test Coverage

Every module function MUST have tests for:

| Category        | What to Test                             |
| --------------- | ---------------------------------------- |
| **Happy Path**  | Normal inputs produce expected outputs   |
| **Edge Cases**  | Empty inputs, single items, large inputs |
| **Error Cases** | Invalid inputs raise appropriate errors  |
| **Boundary**    | Min/max values, special characters       |

## Test Fixtures (conftest.py)

Common fixtures are defined in `tests/conftest.py`:

```python
@pytest.fixture
def root_dir() -> Path:
    """Repository root directory."""
    return Path(__file__).parent.parent.resolve()


@pytest.fixture
def temp_catalog(temp_dir) -> Path:
    """Create a minimal test catalog."""
    catalog = temp_dir / "catalog.xml"
    catalog.write_text(MINIMAL_CATALOG_XML)
    return catalog


@pytest.fixture
def sample_ontology(temp_dir) -> Path:
    """Create a minimal OWL ontology file."""
    owl_file = temp_dir / "test.owl.ttl"
    owl_file.write_text(MINIMAL_OWL_ONTOLOGY)
    return owl_file


@pytest.fixture
def sample_shacl(temp_dir) -> Path:
    """Create minimal SHACL shapes."""
    shacl_file = temp_dir / "test.shacl.ttl"
    shacl_file.write_text(MINIMAL_SHACL_SHAPES)
    return shacl_file


@pytest.fixture
def sample_instance(temp_dir) -> Path:
    """Create a minimal valid JSON-LD instance."""
    instance = temp_dir / "instance.json"
    instance.write_text(json.dumps(MINIMAL_JSONLD_INSTANCE))
    return instance
```

## Self-Tests in Modules

Each module has a `_run_tests()` function for quick verification:

```python
def _run_tests() -> bool:
    """Run self-tests for the module."""
    print("Running module self-tests...")
    all_passed = True

    # Test 1: Basic functionality
    try:
        result = function_under_test("input")
        assert result == "expected"
        print("PASS: Basic functionality")
    except AssertionError as e:
        print(f"FAIL: Basic functionality - {e}")
        all_passed = False

    # Test 2: Edge case
    try:
        result = function_under_test("")
        assert result == []
        print("PASS: Empty input handling")
    except AssertionError as e:
        print(f"FAIL: Empty input handling - {e}")
        all_passed = False

    print()
    if all_passed:
        print("All tests passed!")
    else:
        print("Some tests FAILED!")

    return all_passed
```

Run with:

```bash
python3 -m src.tools.utils.file_collector --test
```

## Test Naming Conventions

```python
# Pattern: test_{function}_{scenario}_{expected_outcome}

def test_load_graph_valid_jsonld_returns_triples():
    ...

def test_load_graph_missing_file_raises_error():
    ...

def test_resolve_iri_unknown_domain_returns_none():
    ...
```

## Mocking External Dependencies

For tests that shouldn't touch real files/network:

```python
from unittest.mock import Mock, patch

def test_validate_without_pyshacl():
    """Should return error code when pyshacl not installed."""
    with patch.dict("sys.modules", {"pyshacl": None}):
        result = validate_data([Path("test.json")])
        assert result.return_code == ReturnCodes.MISSING_DEPENDENCY
```

## Running Tests

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=src/tools --cov-report=html

# Run specific test file
pytest tests/unit/utils/test_file_collector.py

# Run tests matching pattern
pytest tests/ -k "test_load"

# Run with verbose output
pytest tests/ -v

# Run self-tests in a module
python3 -m src.tools.utils.file_collector --test
```

## CI Requirements

All PRs must pass:

1. `pytest tests/` - All tests pass
2. `pytest tests/ --cov=src/tools` - Coverage > 80%
3. `python3 -m src.tools.validators.validation_suite` - Full suite passes
