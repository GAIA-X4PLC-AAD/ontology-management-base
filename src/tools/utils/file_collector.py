#!/usr/bin/env python3
"""
File Collector - Centralized File Discovery Utilities

FEATURE SET:
============
1. collect_files_by_extension - Generic pattern-based file collection
2. collect_turtle_files - Collect all .ttl files from paths
3. collect_jsonld_files - Collect all .json/.jsonld files from paths
4. collect_ontology_bundles - Discover complete ontology bundles
5. collect_files_by_pattern - Glob pattern-based collection
6. collect_ontology_files - Get {ontology, shacl, context} paths for a domain
7. collect_test_files - Collect test files from valid/invalid subdirs

USAGE:
======
    from src.tools.utils.file_collector import (
        collect_jsonld_files,
        collect_turtle_files,
        collect_ontology_bundles,
    )

    # Collect JSON-LD files from multiple paths
    files = collect_jsonld_files(["data/", "examples/"])

    # Collect Turtle files
    ttl_files = collect_turtle_files(["artifacts/"])

    # Discover ontology bundles
    bundles = collect_ontology_bundles(Path("artifacts/"))

STANDALONE TESTING:
==================
    python3 -m src.tools.utils.file_collector [--test] [--verbose] [paths...]

DEPENDENCIES:
=============
- pathlib: For path operations (stdlib)
- No external dependencies - this module is intentionally pure

NOTES:
======
- This module has NO internal src.tools imports to avoid circular dependencies
- All file discovery logic should be centralized here
- Other modules should delegate file discovery to these functions
"""

import argparse
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set, Union


def collect_files_by_extension(
    paths: List[Union[str, Path]],
    extensions: Union[str, Set[str]],
    warn_on_invalid: bool = True,
    return_pathlib: bool = False,
    sort_and_deduplicate: bool = False,
) -> List[Union[str, Path]]:
    """
    Collect all files with specified extensions from the given paths.

    This function walks through directories recursively and collects files
    matching the specified extensions. It can handle both individual files
    and directories.

    Args:
        paths: List of file or directory paths to search
        extensions: File extension(s) to collect (e.g., ".ttl" or {".json", ".jsonld"})
                    Extensions should include the dot prefix
        warn_on_invalid: If True, write warnings to stderr for invalid paths
        return_pathlib: If True, return Path objects; if False, return strings
        sort_and_deduplicate: If True, sort and remove duplicates from results

    Returns:
        List of file paths matching the specified extensions

    Examples:
        # Collect Turtle files
        files = collect_files_by_extension(["artifacts/"], ".ttl")

        # Collect JSON-LD files
        files = collect_files_by_extension(
            ["data/", "examples/"],
            {".json", ".jsonld"},
            return_pathlib=True,
            sort_and_deduplicate=True
        )
    """
    # Normalize extensions to a set
    if isinstance(extensions, str):
        ext_set = {extensions}
    else:
        ext_set = set(extensions)

    # Ensure all extensions start with a dot
    ext_set = {ext if ext.startswith(".") else f".{ext}" for ext in ext_set}

    files = []

    for path_input in paths:
        path = Path(path_input).resolve() if isinstance(path_input, str) else path_input

        if path.is_file():
            # Check if file has the right extension
            if path.suffix in ext_set:
                files.append(path if return_pathlib else str(path))
            elif warn_on_invalid:
                sys.stderr.write(
                    f"Warning: Ignoring file with wrong extension: {path}\n"
                )
        elif path.is_dir():
            # Walk directory recursively
            for file_path in path.rglob("*"):
                if file_path.is_file() and file_path.suffix in ext_set:
                    files.append(file_path if return_pathlib else str(file_path))
        elif warn_on_invalid:
            sys.stderr.write(
                f"Warning: Ignoring invalid path or unsupported file: {path}\n"
            )

    # Sort and deduplicate if requested
    if sort_and_deduplicate:
        files = sorted(set(files))

    return files


def collect_turtle_files(
    paths: List[Union[str, Path]],
    warn_on_invalid: bool = True,
    return_pathlib: bool = False,
) -> List[Union[str, Path]]:
    """
    Collect all Turtle (.ttl) files from the given paths.

    Args:
        paths: List of file or directory paths to search
        warn_on_invalid: If True, write warnings to stderr for invalid paths
        return_pathlib: If True, return Path objects; if False, return strings

    Returns:
        List of Turtle file paths
    """
    return collect_files_by_extension(
        paths, ".ttl", warn_on_invalid=warn_on_invalid, return_pathlib=return_pathlib
    )


def collect_jsonld_files(
    paths: List[Union[str, Path]],
    warn_on_invalid: bool = True,
    return_pathlib: bool = False,
    sort_and_deduplicate: bool = False,
) -> List[Union[str, Path]]:
    """
    Collect all JSON-LD (.json, .jsonld) files from the given paths.

    Args:
        paths: List of file or directory paths to search
        warn_on_invalid: If True, write warnings to stderr for invalid paths
        return_pathlib: If True, return Path objects; if False, return strings
        sort_and_deduplicate: If True, sort and remove duplicates

    Returns:
        List of JSON-LD file paths
    """
    return collect_files_by_extension(
        paths,
        {".json", ".jsonld"},
        warn_on_invalid=warn_on_invalid,
        return_pathlib=return_pathlib,
        sort_and_deduplicate=sort_and_deduplicate,
    )


def collect_files_by_pattern(
    paths: List[Union[str, Path]],
    pattern: str,
    return_pathlib: bool = False,
) -> List[Union[str, Path]]:
    """
    Generic pattern-based file collection using glob patterns.

    Args:
        paths: List of directory paths to search
        pattern: Glob pattern to match (e.g., "*.shacl.ttl", "**/*.json")
        return_pathlib: If True, return Path objects; if False, return strings

    Returns:
        List of matching file paths
    """
    files = []

    for path_input in paths:
        path = Path(path_input).resolve() if isinstance(path_input, str) else path_input

        if path.is_dir():
            for file_path in path.glob(pattern):
                if file_path.is_file():
                    files.append(file_path if return_pathlib else str(file_path))
        elif path.is_file() and path.match(pattern):
            files.append(path if return_pathlib else str(path))

    return sorted(set(files))


def collect_ontology_files(domain_dir: Path) -> Dict[str, Optional[Path]]:
    """
    Discover ontology files for a domain directory.

    Returns {ontology, shacl, context} paths for a domain following the
    standard naming convention: {domain}.owl.ttl, {domain}.shacl.ttl,
    {domain}.context.jsonld

    Args:
        domain_dir: Path to domain directory (e.g., artifacts/manifest/)

    Returns:
        Dictionary with keys: ontology, shacl (list), context
        Values are Path objects or None if not found
    """
    domain = domain_dir.name

    # Standard file patterns
    ontology_file = domain_dir / f"{domain}.owl.ttl"
    context_file = domain_dir / f"{domain}.context.jsonld"

    # SHACL files can be multiple: domain.shacl.ttl and domain.*.shacl.ttl
    shacl_files = sorted(domain_dir.glob("*.shacl.ttl"))

    return {
        "ontology": ontology_file if ontology_file.exists() else None,
        "shacl": shacl_files if shacl_files else None,
        "context": context_file if context_file.exists() else None,
    }


def collect_test_files(
    test_dir: Path,
    valid: bool = True,
    extensions: Set[str] = None,
) -> List[Path]:
    """
    Collect test files from valid/ or invalid/ subdirectories.

    Args:
        test_dir: Path to test domain directory (e.g., tests/data/manifest/)
        valid: If True, collect from valid/, otherwise from invalid/
        extensions: File extensions to collect (default: {".json", ".jsonld"})

    Returns:
        List of test file paths
    """
    if extensions is None:
        extensions = {".json", ".jsonld"}

    subdir = "valid" if valid else "invalid"
    target_dir = test_dir / subdir

    if not target_dir.exists():
        return []

    return collect_files_by_extension(
        [target_dir],
        extensions,
        warn_on_invalid=False,
        return_pathlib=True,
        sort_and_deduplicate=True,
    )


def collect_ontology_bundles(
    base_dir: Path, tests_dir: Optional[Path] = None
) -> Dict[str, Dict[str, Union[Path, List[Path], None]]]:
    """
    Discover ontology bundles (Ontology, SHACL, Context, Tests) in a directory.

    Assumes the standard project structure:
      {base_dir}/{domain}/{domain}.owl.ttl
      {base_dir}/{domain}/*.shacl.ttl
      {base_dir}/{domain}/{domain}.context.jsonld
      {tests_dir}/{domain}/valid/*_instance.json (optional)

    Args:
        base_dir: Directory containing domain subdirectories (e.g., artifacts/ or imports/)
        tests_dir: Optional directory containing test data (e.g., tests/data/)

    Returns:
        Dictionary mapping domain names to a bundle of absolute Path objects:
        {
            "domain": {
                "ontology": Path(...),
                "shacl": [Path(...), ...],
                "jsonld": Path(...) or None,
                "properties": Path(...) or None,
                "instance": Path(...) or None
            }
        }
    """
    bundles = {}

    if not base_dir.exists():
        sys.stderr.write(f"Warning: Directory not found: {base_dir}\n")
        return bundles

    # Iterate over domain directories
    for ont_dir in sorted(base_dir.iterdir()):
        if not ont_dir.is_dir():
            continue

        domain = ont_dir.name

        # 1. Ontology File: {domain}.owl.ttl
        owl_file = ont_dir / f"{domain}.owl.ttl"
        if not owl_file.exists():
            continue

        # 2. SHACL Files: *.shacl.ttl
        shacl_files = sorted(ont_dir.glob("*.shacl.ttl"))

        # 3. JSON-LD Context
        jsonld_file = ont_dir / f"{domain}.context.jsonld"

        # 4. Properties Documentation
        properties_file = ont_dir / "PROPERTIES.md"

        # 5. Instance File (from tests directory if provided)
        instance_file = None
        if tests_dir and tests_dir.exists():
            valid_dir = tests_dir / domain / "valid"
            if valid_dir.exists():
                # Look for standard instance patterns
                for pattern in [f"{domain}_instance.json", "*_instance.json"]:
                    matches = list(valid_dir.glob(pattern))
                    if matches:
                        instance_file = matches[0]
                        break

        bundles[domain] = {
            "ontology": owl_file.resolve(),
            "shacl": [f.resolve() for f in shacl_files] if shacl_files else None,
            "jsonld": jsonld_file.resolve() if jsonld_file.exists() else None,
            "properties": (
                properties_file.resolve() if properties_file.exists() else None
            ),
            "instance": instance_file.resolve() if instance_file else None,
        }

    return bundles


def _run_tests() -> bool:
    """Run self-tests for the module."""
    import tempfile

    print("Running file_collector self-tests...")
    all_passed = True

    # Test 1: collect_files_by_extension with empty list
    result = collect_files_by_extension([], ".ttl")
    if result != []:
        print("FAIL: Empty input should return empty list")
        all_passed = False
    else:
        print("PASS: Empty input handling")

    # Test 2: Create temp files and collect them
    with tempfile.TemporaryDirectory() as tmpdir:
        tmppath = Path(tmpdir)

        # Create test files
        (tmppath / "test1.json").write_text("{}")
        (tmppath / "test2.jsonld").write_text("{}")
        (tmppath / "test3.ttl").write_text("")
        (tmppath / "subdir").mkdir()
        (tmppath / "subdir" / "nested.json").write_text("{}")

        # Test JSON-LD collection
        jsonld_files = collect_jsonld_files([tmppath], return_pathlib=True)
        if len(jsonld_files) != 3:
            print(f"FAIL: Expected 3 JSON-LD files, got {len(jsonld_files)}")
            all_passed = False
        else:
            print("PASS: JSON-LD file collection")

        # Test Turtle collection
        turtle_files = collect_turtle_files([tmppath], return_pathlib=True)
        if len(turtle_files) != 1:
            print(f"FAIL: Expected 1 Turtle file, got {len(turtle_files)}")
            all_passed = False
        else:
            print("PASS: Turtle file collection")

        # Test sort and deduplicate
        jsonld_sorted = collect_jsonld_files(
            [tmppath, tmppath],
            return_pathlib=True,
            sort_and_deduplicate=True,
        )
        if len(jsonld_sorted) != 3:
            print(f"FAIL: Deduplication failed, got {len(jsonld_sorted)}")
            all_passed = False
        else:
            print("PASS: Sort and deduplicate")

        # Test pattern-based collection
        pattern_files = collect_files_by_pattern([tmppath], "**/*.json")
        if len(pattern_files) != 2:
            print(f"FAIL: Expected 2 .json files, got {len(pattern_files)}")
            all_passed = False
        else:
            print("PASS: Pattern-based collection")

    if all_passed:
        print("\nAll tests passed!")
    else:
        print("\nSome tests failed!")

    return all_passed


def main():
    """CLI entry point for file_collector."""
    parser = argparse.ArgumentParser(
        description="Collect files by extension from paths"
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="Paths to search (files or directories)",
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="Run self-tests",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Verbose output",
    )
    parser.add_argument(
        "--extension",
        "-e",
        default=".json",
        help="Extension to collect (default: .json)",
    )
    parser.add_argument(
        "--jsonld",
        action="store_true",
        help="Collect JSON-LD files (.json, .jsonld)",
    )
    parser.add_argument(
        "--turtle",
        action="store_true",
        help="Collect Turtle files (.ttl)",
    )

    args = parser.parse_args()

    if args.test:
        success = _run_tests()
        sys.exit(0 if success else 1)

    if not args.paths:
        parser.print_help()
        sys.exit(1)

    # Collect files based on options
    if args.jsonld:
        files = collect_jsonld_files(args.paths, sort_and_deduplicate=True)
    elif args.turtle:
        files = collect_turtle_files(args.paths)
    else:
        files = collect_files_by_extension(
            args.paths,
            args.extension,
            sort_and_deduplicate=True,
        )

    # Print results
    if args.verbose:
        print(f"Found {len(files)} file(s):")

    for f in files:
        print(f)


if __name__ == "__main__":
    main()
