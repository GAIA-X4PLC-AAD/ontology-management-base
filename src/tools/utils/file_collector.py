#!/usr/bin/env python3
"""
Centralized file collection utilities.

This module provides a unified interface for collecting files by extension
from a mix of file paths and directories. It consolidates the functionality
previously scattered across multiple modules.
"""

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
                sys.stderr.write(f"⚠️ Ignoring file with wrong extension: {path}\n")
        elif path.is_dir():
            # Walk directory recursively
            for file_path in path.rglob("*"):
                if file_path.is_file() and file_path.suffix in ext_set:
                    files.append(file_path if return_pathlib else str(file_path))
        elif warn_on_invalid:
            sys.stderr.write(f"⚠️ Ignoring invalid path or unsupported file: {path}\n")

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
