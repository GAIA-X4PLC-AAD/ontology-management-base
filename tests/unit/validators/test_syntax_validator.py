#!/usr/bin/env python3
"""
Unit tests for src.tools.validators.syntax_validator.
"""

import json
from pathlib import Path

from src.tools.core.result import ReturnCodes
from src.tools.validators import syntax_validator


def test_check_json_syntax_success(temp_dir: Path):
    file_path = temp_dir / "ok.json"
    file_path.write_text(json.dumps({"a": 1}))
    code, msg = syntax_validator.check_json_syntax(file_path)
    assert code == ReturnCodes.SUCCESS
    assert "Syntax OK" in msg


def test_check_json_syntax_error(temp_dir: Path):
    file_path = temp_dir / "bad.json"
    file_path.write_text("{bad json}")
    code, msg = syntax_validator.check_json_syntax(file_path)
    assert code == ReturnCodes.JSON_SYNTAX_ERROR
    assert "Syntax Error" in msg


def test_verify_json_syntax_no_files_returns_error():
    code, results = syntax_validator.verify_json_syntax(["nonexistent_path"])
    assert code == ReturnCodes.GENERAL_ERROR
    assert results


def test_check_turtle_syntax_success(temp_dir: Path):
    file_path = temp_dir / "ok.ttl"
    file_path.write_text(
        "<http://example.org/a> <http://example.org/p> <http://example.org/o> ."
    )
    code, msg = syntax_validator.check_turtle_syntax(file_path)
    assert code == ReturnCodes.SUCCESS
    assert "Syntax OK" in msg


def test_check_turtle_syntax_error(temp_dir: Path):
    file_path = temp_dir / "bad.ttl"
    file_path.write_text("not turtle")
    code, msg = syntax_validator.check_turtle_syntax(file_path)
    assert code == ReturnCodes.TURTLE_SYNTAX_ERROR
    assert "Syntax Error" in msg or "Unexpected error" in msg
