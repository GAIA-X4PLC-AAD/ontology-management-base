#!/usr/bin/env python3
"""
Unit tests for src.tools.core.result.
"""

from src.tools.core.result import ReturnCodes, ValidationResult


def test_return_codes_values():
    assert ReturnCodes.SUCCESS == 0
    assert ReturnCodes.SYNTAX_ERROR == 100
    assert ReturnCodes.COHERENCE_ERROR == 200
    assert ReturnCodes.CONFORMANCE_ERROR == 210
    assert ReturnCodes.SKIPPED == 100


def test_validation_result_success():
    result = ValidationResult.success("ok", ["file.json"])
    assert result.conforms is True
    assert result.return_code == ReturnCodes.SUCCESS
    assert result.is_success() is True
    assert result.is_error() is False


def test_validation_result_error():
    result = ValidationResult.error(ReturnCodes.SYNTAX_ERROR, "bad", ["file.json"])
    assert result.conforms is False
    assert result.return_code == ReturnCodes.SYNTAX_ERROR
    assert result.is_success() is False
    assert result.is_error() is True


def test_validation_result_skipped():
    result = ValidationResult.skipped("skip")
    assert result.return_code == ReturnCodes.SKIPPED
    assert result.is_error() is False
