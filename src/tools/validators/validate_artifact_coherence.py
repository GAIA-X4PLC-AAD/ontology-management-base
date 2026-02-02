#!/usr/bin/env python3
"""
DEPRECATED: This module has been refactored to src.tools.validators.coherence_validator

This file is maintained for backwards compatibility only.
New code should import from src.tools.validators.coherence_validator instead.

Migration:
    # Old import (deprecated)
    from src.tools.validators.validate_artifact_coherence import validate_artifact_coherence

    # New import (preferred)
    from src.tools.validators.coherence_validator import validate_artifact_coherence
"""

import io
import sys
import warnings

# Re-export namespace for users who imported it
from rdflib import Namespace

# Re-export everything from the new location for backwards compatibility
from src.tools.validators.coherence_validator import (
    EXPECTED_TARGETCLASS_FAILURES,
    extract_classes_from_graph,
    extract_ontology_classes,
    extract_shacl_classes,
    extract_shacl_classes_from_file,
    get_base_ontology_classes,
    get_local_name,
    main,
    validate_artifact_coherence,
)

warnings.warn(
    "src.tools.validators.validate_artifact_coherence is deprecated, "
    "use src.tools.validators.coherence_validator instead",
    DeprecationWarning,
    stacklevel=2,
)

SH = Namespace("http://www.w3.org/ns/shacl#")

__all__ = [
    "SH",
    "EXPECTED_TARGETCLASS_FAILURES",
    "get_local_name",
    "extract_classes_from_graph",
    "extract_shacl_classes_from_file",
    "extract_shacl_classes",
    "extract_ontology_classes",
    "get_base_ontology_classes",
    "validate_artifact_coherence",
    "main",
]

if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")
    main()
