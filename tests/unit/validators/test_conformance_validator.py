#!/usr/bin/env python3
"""
Unit tests for src.tools.validators.conformance_validator.
"""

from pathlib import Path

from src.tools.core.result import ReturnCodes
from src.tools.validators.conformance_validator import (
    collect_jsonld_files,
    validate_files,
)


def test_collect_jsonld_files_empty_returns_empty():
    assert collect_jsonld_files([]) == []


def test_validate_files_no_files_returns_error(temp_dir: Path):
    result = validate_files([str(temp_dir)])
    assert result.return_code == ReturnCodes.GENERAL_ERROR
    assert "No JSON-LD files found" in result.report_text
