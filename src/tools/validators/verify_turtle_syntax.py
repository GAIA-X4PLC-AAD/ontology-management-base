#!/usr/bin/env python3
"""
DEPRECATED: This module has been merged into src.tools.validators.syntax_validator

This file is maintained for backwards compatibility only.
New code should import from src.tools.validators.syntax_validator instead.

Migration:
    # Old import (deprecated)
    from src.tools.validators.verify_turtle_syntax import check_turtle_wellformedness

    # New import (preferred)
    from src.tools.validators.syntax_validator import check_turtle_syntax
"""

import io
import sys
import warnings

# Re-export everything from the new location for backwards compatibility
from src.tools.validators.syntax_validator import check_turtle_syntax
from src.tools.validators.syntax_validator import (
    check_turtle_syntax as check_turtle_wellformedness,
)
from src.tools.validators.syntax_validator import (
    gather_turtle_files,
    verify_turtle_syntax,
)

warnings.warn(
    "src.tools.validators.verify_turtle_syntax is deprecated, "
    "use src.tools.validators.syntax_validator instead",
    DeprecationWarning,
    stacklevel=2,
)

__all__ = [
    "check_turtle_wellformedness",
    "check_turtle_syntax",
    "gather_turtle_files",
    "verify_turtle_syntax",
]


def main(args=None):
    """CLI entry point - delegates to syntax_validator."""
    import argparse

    from src.tools.validators.syntax_validator import verify_turtle_syntax

    parser = argparse.ArgumentParser(
        description="Verify syntax correctness (well-formedness) of Turtle files."
    )
    parser.add_argument("paths", nargs="+", help="Files or directories to check")
    parsed_args = parser.parse_args(args)

    ret, results = verify_turtle_syntax(parsed_args.paths)

    # Print messages based on return code
    for code, msg in results:
        if code == 0:
            sys.stdout.write(msg + "\n")
        else:
            sys.stderr.write(msg + "\n")

    sys.exit(ret)


if __name__ == "__main__":
    # Ensure UTF-8 output for emojis, etc.
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")
    main()
