#!/usr/bin/env python3
"""
DEPRECATED: This module has been refactored to src.tools.validators.conformance_validator

This file is maintained for backwards compatibility only.
New code should import from src.tools.validators.conformance_validator instead.

Migration:
    # Old import (deprecated)
    from src.tools.validators.validate_data_conformance import collect_jsonld_files

    # New import (preferred)
    from src.tools.validators.conformance_validator import collect_jsonld_files
"""

import sys
import warnings
from argparse import ArgumentParser
from pathlib import Path

# Re-export everything from the new location for backwards compatibility
from src.tools.validators.conformance_validator import (
    collect_jsonld_files,
    validate_data_conformance,
    validate_files,
)

# Also re-export from shacl.validator for full backwards compatibility
from src.tools.validators.shacl.validator import (  # noqa: F401
    validate_data_conformance as _validate,
)

warnings.warn(
    "src.tools.validators.validate_data_conformance is deprecated, "
    "use src.tools.validators.conformance_validator instead",
    DeprecationWarning,
    stacklevel=2,
)

__all__ = [
    "collect_jsonld_files",
    "validate_data_conformance",
    "validate_files",
    "main",
]


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
    return_code, _ = validate_data_conformance(
        jsonld_files, args.root.resolve(), args.inference, args.debug, args.logfile
    )

    sys.exit(return_code)


if __name__ == "__main__":
    main()
