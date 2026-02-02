#!/usr/bin/env python3
"""
DEPRECATED: This module has been merged into src.tools.validators.syntax_validator

This file is maintained for backwards compatibility only.
New code should import from src.tools.validators.syntax_validator instead.

Migration:
    # Old import (deprecated)
    from src.tools.validators.verify_json_syntax import check_json_wellformedness

    # New import (preferred)
    from src.tools.validators.syntax_validator import check_json_syntax
"""

import io
import sys
import warnings

# Re-export everything from the new location for backwards compatibility
from src.tools.validators.syntax_validator import check_json_syntax
from src.tools.validators.syntax_validator import (
    check_json_syntax as check_json_wellformedness,
)
from src.tools.validators.syntax_validator import (
    gather_jsonld_files,
    main,
    verify_json_syntax,
)

warnings.warn(
    "src.tools.validators.verify_json_syntax is deprecated, "
    "use src.tools.validators.syntax_validator instead",
    DeprecationWarning,
    stacklevel=2,
)

__all__ = [
    "check_json_wellformedness",
    "check_json_syntax",
    "gather_jsonld_files",
    "verify_json_syntax",
    "main",
]

if __name__ == "__main__":
    # Ensure UTF-8 output for emojis, etc.
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")
    main()
