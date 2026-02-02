#!/usr/bin/env python3
"""
Core abstractions for the ontology management tools.

This package provides shared types, constants, and result objects used
throughout the validation and processing modules.

Contents:
    - constants: Shared constants (FAST_STORE, etc.)
    - result: ValidationResult dataclass and ReturnCodes enum

Usage:
    from src.tools.core import ValidationResult, ReturnCodes
    from src.tools.core.constants import FAST_STORE
"""

from .constants import FAST_STORE
from .result import ReturnCodes, ValidationResult

__all__ = [
    "FAST_STORE",
    "ReturnCodes",
    "ValidationResult",
]
