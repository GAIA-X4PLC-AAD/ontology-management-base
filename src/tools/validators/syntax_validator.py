#!/usr/bin/env python3
"""
Syntax Validator - Unified JSON-LD and Turtle Syntax Validation

FEATURE SET:
============
1. check_json_syntax - Validate JSON/JSON-LD syntax for single file
2. check_turtle_syntax - Validate Turtle syntax for single file
3. verify_json_syntax - Batch JSON-LD validation for multiple paths
4. verify_turtle_syntax - Batch Turtle validation for multiple paths
5. verify_all_syntax - Combined validation for both formats

USAGE:
======
    from src.tools.validators.syntax_validator import (
        check_json_syntax,
        check_turtle_syntax,
        verify_json_syntax,
        verify_turtle_syntax,
    )

    # Single file validation
    code, msg = check_json_syntax(Path("data/instance.json"))
    code, msg = check_turtle_syntax(Path("artifacts/domain/domain.owl.ttl"))

    # Batch validation
    ret, results = verify_json_syntax(["data/", "examples/"])
    ret, results = verify_turtle_syntax(["artifacts/"])

STANDALONE TESTING:
==================
    python3 -m src.tools.validators.syntax_validator [--test] [--json] [--turtle] paths...

DEPENDENCIES:
=============
- rdflib: For Turtle parsing
- json: For JSON parsing (stdlib)

NOTES:
======
- This module does NOT validate logical structure or SHACL compliance
- It only checks that files are syntactically well-formed
- Return codes: 0 = OK, non-zero = error
"""

import argparse
import io
import json
import sys
from pathlib import Path
from typing import List, Optional, Tuple, Union

from rdflib import Graph
from rdflib.exceptions import ParserError

from src.tools.core.result import ReturnCodes
from src.tools.utils.file_collector import collect_jsonld_files, collect_turtle_files
from src.tools.utils.print_formatter import normalize_path_for_display

# =============================================================================
# JSON-LD Syntax Validation
# =============================================================================


def check_json_syntax(
    filename: Union[str, Path],
    root_dir: Optional[Path] = None,
) -> Tuple[int, str]:
    """
    Check if a single file contains syntactically correct (well-formed) JSON.

    This does NOT validate the JSON-LD structure or SHACL compliance.
    It merely ensures the file can be parsed by the JSON loader.

    Args:
        filename: Path to the JSON file to check
        root_dir: Optional root directory for path normalization in output

    Returns:
        (return_code, message) tuple where return_code is 0 if OK, non-zero otherwise
    """
    # Normalize path for display
    if root_dir:
        display_path = normalize_path_for_display(filename, root_dir)
    else:
        display_path = str(filename)

    if not Path(filename).is_file():
        return ReturnCodes.JSON_SYNTAX_ERROR, f"File not found: {display_path}"

    try:
        with open(filename, "r", encoding="utf-8") as f:
            json.load(f)
        return ReturnCodes.SUCCESS, f"Syntax OK: {display_path}"
    except json.JSONDecodeError as e:
        msg = f"Syntax Error in {display_path}:\n   Line {e.lineno}, Col {e.colno}: {e.msg}"
        return ReturnCodes.JSON_SYNTAX_ERROR, msg
    except Exception as e:
        msg = f"Unexpected error parsing {display_path}:\n{e}"
        return ReturnCodes.JSON_SYNTAX_ERROR, msg


# Alias for backwards compatibility
check_json_wellformedness = check_json_syntax


def gather_jsonld_files(paths: List[str]) -> List[str]:
    """
    Gather all .json / .jsonld files from the given paths.

    Note: This function delegates to the central file_collector utility.
    """
    return collect_jsonld_files(paths, warn_on_invalid=True, return_pathlib=False)


def verify_json_syntax(
    paths: List[str],
    root_dir: Optional[Path] = None,
) -> Tuple[int, List[Tuple[int, str]]]:
    """
    Verify syntax correctness for all JSON/JSON-LD files found in the given paths.

    Args:
        paths: List of files or directories to check
        root_dir: Optional root directory for path normalization in output

    Returns:
        (return_code, results) tuple where:
        - return_code is 0 if all files are valid, non-zero otherwise
        - results is a list of (code, message) tuples for each file
    """
    results = []
    files = gather_jsonld_files(paths)

    if not files:
        msg = "No JSON-LD files found to check."
        results.append((ReturnCodes.GENERAL_ERROR, msg))
        return ReturnCodes.GENERAL_ERROR, results

    ret = 0
    for filename in files:
        filename = str(Path(filename).resolve())
        code, msg = check_json_syntax(filename, root_dir)
        results.append((code, msg))
        ret |= code

    return ret, results


# =============================================================================
# Turtle Syntax Validation
# =============================================================================


def check_turtle_syntax(
    filename: Union[str, Path],
    root_dir: Optional[Path] = None,
) -> Tuple[int, str]:
    """
    Check if a single file contains syntactically correct (well-formed) Turtle.

    This does NOT validate logical consistency or SHACL compliance.
    It merely ensures the file can be parsed by an RDF parser.

    Args:
        filename: Path to the Turtle file to check
        root_dir: Optional root directory for path normalization in output

    Returns:
        (return_code, message) tuple where return_code is 0 if OK, non-zero otherwise
    """
    # Normalize path for display
    if root_dir:
        display_path = normalize_path_for_display(filename, root_dir)
    else:
        display_path = str(filename)

    if not Path(filename).is_file():
        return ReturnCodes.TURTLE_SYNTAX_ERROR, f"File not found: {display_path}"

    try:
        g = Graph()
        # Strictly parse as turtle
        g.parse(filename, format="turtle")
        return ReturnCodes.SUCCESS, f"Syntax OK: {display_path}"
    except ParserError as e:
        msg = f"Syntax Error in {display_path}:\n{e}"
        return ReturnCodes.TURTLE_SYNTAX_ERROR, msg
    except Exception as e:
        msg = f"Unexpected error parsing {display_path}:\n{e}"
        return ReturnCodes.TURTLE_SYNTAX_ERROR, msg


# Alias for backwards compatibility
check_turtle_wellformedness = check_turtle_syntax


def gather_turtle_files(paths: List[str]) -> List[str]:
    """
    Gather all .ttl files from the given paths.

    Note: This function delegates to the central file_collector utility.
    """
    return collect_turtle_files(paths, warn_on_invalid=True, return_pathlib=False)


def verify_turtle_syntax(
    paths: List[str],
    root_dir: Optional[Path] = None,
) -> Tuple[int, List[Tuple[int, str]]]:
    """
    Verify syntax correctness for all Turtle files found in the given paths.

    Args:
        paths: List of files or directories to check
        root_dir: Optional root directory for path normalization in output

    Returns:
        (return_code, results) tuple where:
        - return_code is 0 if all files are valid, non-zero otherwise
        - results is a list of (code, message) tuples for each file
    """
    results = []
    files = gather_turtle_files(paths)

    if not files:
        msg = "No Turtle files found to check."
        results.append((ReturnCodes.GENERAL_ERROR, msg))
        return ReturnCodes.GENERAL_ERROR, results

    ret = 0
    for filename in files:
        filename = str(Path(filename).resolve())
        code, msg = check_turtle_syntax(filename, root_dir)
        results.append((code, msg))
        ret |= code

    return ret, results


# =============================================================================
# Combined Validation
# =============================================================================


def verify_all_syntax(
    paths: List[str],
    root_dir: Optional[Path] = None,
    check_json: bool = True,
    check_turtle: bool = True,
) -> Tuple[int, List[Tuple[int, str]]]:
    """
    Verify syntax for both JSON-LD and Turtle files.

    Args:
        paths: List of files or directories to check
        root_dir: Optional root directory for path normalization
        check_json: Whether to check JSON-LD files
        check_turtle: Whether to check Turtle files

    Returns:
        (return_code, results) tuple
    """
    all_results = []
    ret = 0

    if check_json:
        json_ret, json_results = verify_json_syntax(paths, root_dir)
        ret |= json_ret
        all_results.extend(json_results)

    if check_turtle:
        turtle_ret, turtle_results = verify_turtle_syntax(paths, root_dir)
        ret |= turtle_ret
        all_results.extend(turtle_results)

    return ret, all_results


# =============================================================================
# Self-Test
# =============================================================================


def _run_tests() -> bool:
    """Run self-tests for the module."""
    import tempfile

    print("Running syntax_validator self-tests...")
    all_passed = True

    with tempfile.TemporaryDirectory() as tmpdir:
        tmppath = Path(tmpdir)

        # Test 1: Valid JSON
        valid_json = tmppath / "valid.json"
        valid_json.write_text('{"key": "value"}')
        code, msg = check_json_syntax(valid_json)
        if code != 0:
            print(f"FAIL: Valid JSON should pass: {msg}")
            all_passed = False
        else:
            print("PASS: Valid JSON syntax")

        # Test 2: Invalid JSON
        invalid_json = tmppath / "invalid.json"
        invalid_json.write_text('{"key": "value",}')
        code, msg = check_json_syntax(invalid_json)
        if code == 0:
            print("FAIL: Invalid JSON should fail")
            all_passed = False
        else:
            print("PASS: Invalid JSON detected")

        # Test 3: Valid Turtle
        valid_ttl = tmppath / "valid.ttl"
        valid_ttl.write_text(
            """@prefix ex: <http://example.org/> .
ex:subject a ex:Thing .
"""
        )
        code, msg = check_turtle_syntax(valid_ttl)
        if code != 0:
            print(f"FAIL: Valid Turtle should pass: {msg}")
            all_passed = False
        else:
            print("PASS: Valid Turtle syntax")

        # Test 4: Invalid Turtle
        invalid_ttl = tmppath / "invalid.ttl"
        invalid_ttl.write_text(
            """@prefix ex: <http://example.org/> .
ex:subject "unclosed string .
"""
        )
        code, msg = check_turtle_syntax(invalid_ttl)
        if code == 0:
            print("FAIL: Invalid Turtle should fail")
            all_passed = False
        else:
            print("PASS: Invalid Turtle detected")

        # Test 5: Missing file
        code, msg = check_json_syntax(tmppath / "nonexistent.json")
        if code == 0:
            print("FAIL: Missing file should fail")
            all_passed = False
        else:
            print("PASS: Missing file detected")

        # Test 6: Batch validation
        valid_dir = tmppath / "batch"
        valid_dir.mkdir()
        (valid_dir / "file1.json").write_text('{"a": 1}')
        (valid_dir / "file2.json").write_text('{"b": 2}')
        ret, results = verify_json_syntax([str(valid_dir)])
        if ret != 0:
            print(f"FAIL: Batch validation should pass: {results}")
            all_passed = False
        else:
            print("PASS: Batch JSON validation")

    if all_passed:
        print("\nAll tests passed!")
    else:
        print("\nSome tests failed!")

    return all_passed


# =============================================================================
# CLI Entry Point
# =============================================================================


def main(args=None):
    """CLI entry point for syntax_validator."""
    parser = argparse.ArgumentParser(
        description="Verify syntax correctness of JSON-LD and Turtle files."
    )
    parser.add_argument("paths", nargs="*", help="Files or directories to check")
    parser.add_argument("--test", action="store_true", help="Run self-tests")
    parser.add_argument("--json", action="store_true", help="Check JSON-LD files only")
    parser.add_argument("--turtle", action="store_true", help="Check Turtle files only")
    parser.add_argument("--quiet", "-q", action="store_true", help="Only show errors")

    parsed_args = parser.parse_args(args)

    if parsed_args.test:
        success = _run_tests()
        sys.exit(0 if success else 1)

    if not parsed_args.paths:
        parser.print_help()
        sys.exit(1)

    # Determine what to check
    check_json = not parsed_args.turtle or parsed_args.json
    check_turtle = not parsed_args.json or parsed_args.turtle

    # If neither specified explicitly, check both
    if not parsed_args.json and not parsed_args.turtle:
        check_json = True
        check_turtle = True

    ret, results = verify_all_syntax(
        parsed_args.paths,
        root_dir=Path.cwd(),
        check_json=check_json,
        check_turtle=check_turtle,
    )

    # Print results
    for code, msg in results:
        if code == 0:
            if not parsed_args.quiet:
                sys.stdout.write(msg + "\n")
        else:
            sys.stderr.write(msg + "\n")

    sys.exit(ret)


if __name__ == "__main__":
    # Ensure UTF-8 output for emojis, etc.
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")
    main()
