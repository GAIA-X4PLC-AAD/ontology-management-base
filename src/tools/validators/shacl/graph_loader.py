#!/usr/bin/env python3
"""
DEPRECATED: This module has been moved to src.tools.utils.graph_loader

This file is maintained for backwards compatibility only.
New code should import from src.tools.utils.graph_loader instead.

Migration:
    # Old import (deprecated)
    from src.tools.validators.shacl.graph_loader import load_jsonld_files

    # New import (preferred)
    from src.tools.utils.graph_loader import load_jsonld_files
"""

import warnings

# Re-export everything from the new location for backwards compatibility
from src.tools.utils.graph_loader import (
    FAST_STORE,
    extract_external_iris,
    load_fixtures_for_iris,
    load_graph,
    load_graphs,
    load_jsonld_files,
    load_jsonld_with_context,
    load_turtle_files,
)

warnings.warn(
    "src.tools.validators.shacl.graph_loader is deprecated, "
    "use src.tools.utils.graph_loader instead",
    DeprecationWarning,
    stacklevel=2,
)

__all__ = [
    "FAST_STORE",
    "load_graph",
    "load_graphs",
    "load_jsonld_files",
    "load_turtle_files",
    "load_jsonld_with_context",
    "load_fixtures_for_iris",
    "extract_external_iris",
]
