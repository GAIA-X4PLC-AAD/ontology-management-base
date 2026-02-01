#!/usr/bin/env python3
"""
Registry-Based JSON-LD to SHACL Validation Tool.

Validates JSON-LD instance files against SHACL shapes using registry-based
ontology discovery for faster, more reliable resolution.

Key Features:
  - Registry-based discovery using docs/registry.json
  - Automatic type-based ontology detection
  - Oxigraph performance optimization
  - RDFS inference support
  - Detailed console output for transparency

Usage:
    python3 check_jsonld_against_shacl_schema.py [files/dirs...] [options]

Options:
    --root DIR          Repository root (default: current directory)
    --inference MODE    Inference mode: rdfs|owlrl|none|both (default: rdfs)
    --debug             Enable debug logging
    --logfile FILE      Write detailed logs to file
"""

import sys
from argparse import ArgumentParser
from pathlib import Path
from typing import List

# Import from the new modular structure
from src.tools.validators.shacl.validator import validate_jsonld_files


def collect_jsonld_files(paths: List[str]) -> List[Path]:
    """
    Collect all JSON-LD files from the provided paths.

    Args:
        paths: List of file or directory paths

    Returns:
        List of JSON-LD file paths
    """
    files = []

    for path_str in paths:
        path = Path(path_str).resolve()

        if path.is_file() and path.suffix in {".json", ".jsonld"}:
            files.append(path)
        elif path.is_dir():
            files.extend(path.glob("*.json"))
            files.extend(path.glob("*.jsonld"))

    return sorted(set(files))


def main():
    """Command-line entry point."""
    parser = ArgumentParser(
        description="Validate JSON-LD files against SHACL shapes using registry discovery"
    )
    parser.add_argument(
        "paths", nargs="+", help="JSON-LD files or directories to validate"
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

    args = parser.parse_args()

    # Collect files
    jsonld_files = collect_jsonld_files(args.paths)

    if not jsonld_files:
        print("Error: No JSON-LD files found", file=sys.stderr)
        sys.exit(1)

    # Run validation
    return_code, _ = validate_jsonld_files(
        jsonld_files, args.root.resolve(), args.inference, args.debug, args.logfile
    )

    sys.exit(return_code)


if __name__ == "__main__":
    main()
