#!/usr/bin/env python3
"""
Conformance Validator - SHACL-based Data Conformance Validation

FEATURE SET:
============
1. validate_data_conformance - Main validation entry point
2. collect_jsonld_files - Collect JSON-LD files for validation
3. ShaclValidator integration - Uses modular SHACL validation pipeline

USAGE:
======
    from src.tools.validators.conformance_validator import (
        validate_data_conformance,
        collect_jsonld_files,
    )

    # Validate files
    files = collect_jsonld_files(["data/", "tests/"])
    return_code, output = validate_data_conformance(files, root_dir)

STANDALONE TESTING:
==================
    python3 -m src.tools.validators.conformance_validator [--test] paths... [options]

DEPENDENCIES:
=============
- rdflib: For RDF graph handling
- pyshacl: For SHACL validation
- src.tools.validators.shacl: Modular validation components

NOTES:
======
- Uses registry-based discovery for ontologies and SHACL shapes
- Supports RDFS inference before validation
- Oxigraph optimization when available
"""

import argparse
import sys
from pathlib import Path
from typing import List, Optional, Tuple

from src.tools.core.result import ReturnCodes, ValidationResult
from src.tools.utils.file_collector import collect_jsonld_files as _collect_jsonld_files

# Import from the modular SHACL structure
from src.tools.validators.shacl.validator import (
    ShaclValidator,
)
from src.tools.validators.shacl.validator import (  # noqa: F401
    ValidationResult as ShaclValidationResult,
)
from src.tools.validators.shacl.validator import (
    validate_data_conformance as _validate_data_conformance,
)


def collect_jsonld_files(paths: List[str]) -> List[Path]:
    """
    Collect all JSON-LD files from the provided paths.

    Args:
        paths: List of file or directory paths

    Returns:
        List of JSON-LD file paths (sorted and deduplicated)

    Note: This function delegates to the central file_collector utility.
    """
    return _collect_jsonld_files(
        paths, warn_on_invalid=False, return_pathlib=True, sort_and_deduplicate=True
    )


def validate_data_conformance(
    jsonld_files: List[Path],
    root_dir: Path,
    inference_mode: str = "rdfs",
    debug: bool = False,
    logfile: Optional[Path] = None,
) -> Tuple[int, str]:
    """
    Validate JSON-LD files against SHACL shapes.

    This function provides the main entry point for SHACL-based conformance
    validation using registry-based ontology discovery.

    Args:
        jsonld_files: List of JSON-LD files to validate
        root_dir: Repository root directory
        inference_mode: Inference mode (rdfs|owlrl|none|both)
        debug: Enable debug logging
        logfile: Optional log file path

    Returns:
        Tuple of (return_code, output_message)
    """
    return _validate_data_conformance(
        jsonld_files, root_dir, inference_mode, debug, logfile
    )


def validate_files(
    paths: List[str],
    root_dir: Path = None,
    inference_mode: str = "rdfs",
) -> ValidationResult:
    """
    Simplified validation interface that returns a ValidationResult.

    Args:
        paths: List of file or directory paths to validate
        root_dir: Repository root directory (default: cwd)
        inference_mode: Inference mode for RDFS/OWL inference

    Returns:
        ValidationResult with validation outcome
    """
    if root_dir is None:
        root_dir = Path.cwd()

    # Collect files
    jsonld_files = collect_jsonld_files(paths)

    if not jsonld_files:
        return ValidationResult.error(
            ReturnCodes.GENERAL_ERROR,
            "No JSON-LD files found to validate",
            files=[],
        )

    # Initialize validator
    validator = ShaclValidator(root_dir, inference_mode=inference_mode, verbose=False)

    # Run validation
    result = validator.validate(jsonld_files)

    # Convert to our ValidationResult type
    return ValidationResult(
        conforms=result.conforms,
        return_code=result.return_code,
        report_text=result.report_text,
        report_graph=result.report_graph,
        files_validated=result.files_validated,
        triples_count=result.triples_count,
        inferred_count=result.inferred_count,
        duration_seconds=result.duration_seconds,
    )


def _run_tests() -> bool:
    """Run self-tests for the module."""
    import json
    import tempfile

    print("Running conformance_validator self-tests...")
    all_passed = True

    # Test 1: collect_jsonld_files with empty list
    result = collect_jsonld_files([])
    if result != []:
        print("FAIL: Empty input should return empty list")
        all_passed = False
    else:
        print("PASS: Empty input handling")

    # Test 2: Create temp file and collect it
    with tempfile.TemporaryDirectory() as tmpdir:
        tmppath = Path(tmpdir)

        # Create test JSON-LD file
        test_file = tmppath / "test.json"
        test_content = {
            "@context": {"@vocab": "http://example.org/"},
            "@id": "http://example.org/test",
            "@type": "Thing",
        }
        test_file.write_text(json.dumps(test_content))

        files = collect_jsonld_files([str(tmppath)])
        if len(files) != 1:
            print(f"FAIL: Expected 1 file, got {len(files)}")
            all_passed = False
        else:
            print("PASS: File collection")

    if all_passed:
        print("\nAll tests passed!")
    else:
        print("\nSome tests failed!")

    return all_passed


def main():
    """Command-line entry point."""
    parser = argparse.ArgumentParser(
        description="Validate JSON-LD files against SHACL shapes using registry discovery"
    )
    parser.add_argument(
        "paths", nargs="*", help="JSON-LD files or directories to validate"
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Repository root directory (default: current directory)",
    )
    parser.add_argument(
        "--inference",
        choices=["rdfs", "owlrl", "none", "both"],
        default="rdfs",
        help="Inference mode for validation (default: rdfs)",
    )
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    parser.add_argument("--logfile", type=Path, help="Write detailed logs to file")
    parser.add_argument("--test", action="store_true", help="Run self-tests")

    args = parser.parse_args()

    if args.test:
        success = _run_tests()
        sys.exit(0 if success else 1)

    if not args.paths:
        parser.print_help()
        sys.exit(1)

    # Collect files
    jsonld_files = collect_jsonld_files(args.paths)

    if not jsonld_files:
        print("Error: No JSON-LD files found", file=sys.stderr)
        sys.exit(1)

    # Run validation
    return_code, _ = validate_data_conformance(
        jsonld_files, args.root.resolve(), args.inference, args.debug, args.logfile
    )

    sys.exit(return_code)


if __name__ == "__main__":
    main()
