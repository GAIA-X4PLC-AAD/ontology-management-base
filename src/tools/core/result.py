#!/usr/bin/env python3
"""
Validation result types and return codes.

FEATURE SET:
============
1. ReturnCodes enum - Standardized exit codes for all validation operations
2. ValidationResult dataclass - Structured validation outcome with metadata
3. Helper functions for creating common result types

USAGE:
======
    from src.tools.core.result import ValidationResult, ReturnCodes

    # Create a successful result
    result = ValidationResult(
        conforms=True,
        return_code=ReturnCodes.SUCCESS,
        report_text="All validations passed"
    )

    # Check result
    if result.conforms:
        print("Validation passed!")
    else:
        print(f"Error: {result.report_text}")
        sys.exit(result.return_code)

STANDALONE TESTING:
==================
    python3 -m src.tools.core.result [--test]

DEPENDENCIES:
=============
- rdflib: For Graph type annotation

NOTES:
======
- Return codes follow Unix conventions (0 = success, non-zero = error)
- Codes are grouped by category (syntax: 10x, coherence: 20x, etc.)
"""

from dataclasses import dataclass, field
from enum import IntEnum
from typing import List, Optional

from rdflib import Graph


class ReturnCodes(IntEnum):
    """
    Standardized return codes for validation operations.

    Grouped by category:
    - 0: Success
    - 1: General error
    - 10x: Syntax errors
    - 20x: Coherence/consistency errors
    - 21x: Conformance/SHACL errors
    - 99: System/dependency errors
    - 100: Skip/missing file
    """

    SUCCESS = 0
    GENERAL_ERROR = 1

    # Syntax validation (10x)
    SYNTAX_ERROR = 100
    JSON_SYNTAX_ERROR = 101
    TURTLE_SYNTAX_ERROR = 102

    # Coherence validation (20x)
    COHERENCE_ERROR = 200
    MISSING_TARGET_CLASS = 201

    # Conformance validation (21x)
    CONFORMANCE_ERROR = 210
    SHACL_VIOLATION = 211

    # System errors (99)
    MISSING_DEPENDENCY = 99

    # Skip conditions (100)
    SKIPPED = 100


@dataclass
class ValidationResult:
    """
    Result of a validation operation.

    This dataclass provides a structured way to represent validation outcomes,
    including both success/failure status and detailed metadata about the
    validation run.

    Attributes:
        conforms: Whether the validation passed (True) or failed (False)
        return_code: Exit code for CLI usage (0 = success)
        report_text: Human-readable report or error message
        report_graph: Optional RDF graph with SHACL validation report
        files_validated: List of files that were validated
        triples_count: Total number of RDF triples processed
        inferred_count: Number of triples added by inference
        duration_seconds: Time taken for validation
        errors: List of specific error messages
        warnings: List of warning messages
    """

    conforms: bool
    return_code: int
    report_text: str
    report_graph: Optional[Graph] = None
    files_validated: List[str] = field(default_factory=list)
    triples_count: int = 0
    inferred_count: int = 0
    duration_seconds: float = 0.0
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)

    @classmethod
    def success(
        cls, report_text: str = "Validation passed", files: List[str] = None
    ) -> "ValidationResult":
        """Create a successful validation result."""
        return cls(
            conforms=True,
            return_code=ReturnCodes.SUCCESS,
            report_text=report_text,
            files_validated=files or [],
        )

    @classmethod
    def error(
        cls,
        return_code: int,
        report_text: str,
        files: List[str] = None,
        errors: List[str] = None,
    ) -> "ValidationResult":
        """Create a failed validation result."""
        return cls(
            conforms=False,
            return_code=return_code,
            report_text=report_text,
            files_validated=files or [],
            errors=errors or [],
        )

    @classmethod
    def skipped(cls, reason: str, files: List[str] = None) -> "ValidationResult":
        """Create a skipped validation result."""
        return cls(
            conforms=True,  # Skipped is not a failure
            return_code=ReturnCodes.SKIPPED,
            report_text=reason,
            files_validated=files or [],
            warnings=[reason],
        )

    def is_success(self) -> bool:
        """Check if this is a successful result."""
        return self.conforms and self.return_code == ReturnCodes.SUCCESS

    def is_error(self) -> bool:
        """Check if this is an error result."""
        return not self.conforms or self.return_code not in (
            ReturnCodes.SUCCESS,
            ReturnCodes.SKIPPED,
        )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Show result types")
    parser.add_argument("--test", action="store_true", help="Run self-tests")
    args = parser.parse_args()

    if args.test:
        print("Running self-tests...")

        # Test ReturnCodes
        assert ReturnCodes.SUCCESS == 0
        assert ReturnCodes.SYNTAX_ERROR == 100
        assert ReturnCodes.CONFORMANCE_ERROR == 210

        # Test ValidationResult
        success = ValidationResult.success("Test passed", ["file1.json"])
        assert success.conforms is True
        assert success.return_code == 0
        assert success.is_success() is True
        assert success.is_error() is False

        error = ValidationResult.error(ReturnCodes.SYNTAX_ERROR, "Parse error")
        assert error.conforms is False
        assert error.return_code == 100
        assert error.is_success() is False
        assert error.is_error() is True

        skipped = ValidationResult.skipped("No files found")
        assert skipped.conforms is True
        assert skipped.return_code == ReturnCodes.SKIPPED
        assert skipped.is_success() is False
        assert skipped.is_error() is False

        print("All tests passed!")
    else:
        print("ReturnCodes:")
        for code in ReturnCodes:
            print(f"  {code.name}: {code.value}")
