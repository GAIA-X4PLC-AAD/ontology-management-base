#!/usr/bin/env python3
"""
IRI Utils - IRI String Manipulation Utilities

Provides centralized functions for parsing, extracting, and manipulating
IRI (Internationalized Resource Identifier) strings. This module handles
pure string operations only - graph-based operations belong in graph_loader.py.

FEATURE SET:
============
1. get_local_name - Extract local name from URI (after # or last /)
2. get_namespace - Extract namespace from URI (before # or last /)
3. is_did_web - Check if IRI is a did:web: decentralized identifier
4. parse_did_web - Parse did:web: IRI into components
5. normalize_iri - Normalize IRI for comparison (trailing slash handling)
6. iri_to_domain - Extract domain hint from ontology IRI

USAGE:
======
    from src.tools.core.iri_utils import get_local_name, is_did_web

    # Extract local name
    name = get_local_name("http://example.org/ontology#MyClass")
    # Returns: "MyClass"

    # Check for did:web: IRI
    if is_did_web("did:web:registry.gaia-x.eu:participant:123"):
        components = parse_did_web(iri)

STANDALONE TESTING:
==================
    python3 -m src.tools.core.iri_utils [--test]

    Options:
      --test      Run self-tests

DEPENDENCIES:
=============
- re (stdlib)
- urllib.parse (stdlib)

NOTES:
======
- This module has NO internal src.tools imports (core layer)
- Graph-based IRI extraction (from triples) is in graph_loader.py
- Case-insensitive comparison should use get_local_name().lower()
"""

import argparse
import re
import sys
from typing import Dict, Optional
from urllib.parse import unquote


def get_local_name(uri: str, lowercase: bool = False) -> str:
    """
    Extract the local name from a URI.

    Takes the part after `#` or the last `/`.

    Args:
        uri: Full URI string
        lowercase: If True, convert result to lowercase

    Returns:
        Local name portion of the URI

    Examples:
        >>> get_local_name("http://example.org/ontology#MyClass")
        'MyClass'
        >>> get_local_name("http://example.org/ontology/MyClass")
        'MyClass'
        >>> get_local_name("http://example.org/ontology#MyClass", lowercase=True)
        'myclass'
    """
    if "#" in uri:
        local = uri.rsplit("#", 1)[1]
    else:
        local = uri.rsplit("/", 1)[-1]

    return local.lower() if lowercase else local


def get_namespace(uri: str) -> str:
    """
    Extract the namespace from a URI.

    Takes the part before and including `#` or the last `/`.

    Args:
        uri: Full URI string

    Returns:
        Namespace portion of the URI (includes trailing # or /)

    Examples:
        >>> get_namespace("http://example.org/ontology#MyClass")
        'http://example.org/ontology#'
        >>> get_namespace("http://example.org/ontology/MyClass")
        'http://example.org/ontology/'
    """
    if "#" in uri:
        return uri.rsplit("#", 1)[0] + "#"
    else:
        return uri.rsplit("/", 1)[0] + "/"


def is_did_web(iri: str) -> bool:
    """
    Check if an IRI is a did:web: decentralized identifier.

    Args:
        iri: IRI string to check

    Returns:
        True if IRI starts with "did:web:", False otherwise

    Example:
        >>> is_did_web("did:web:registry.gaia-x.eu:participant:123")
        True
        >>> is_did_web("http://example.org/resource")
        False
    """
    return iri.startswith("did:web:")


def parse_did_web(iri: str) -> Optional[Dict[str, str]]:
    """
    Parse a did:web: IRI into its components.

    did:web: format: did:web:<host>:<path-segments>

    Args:
        iri: did:web: IRI string

    Returns:
        Dictionary with keys: host, path, type, id
        Or None if not a valid did:web: IRI

    Example:
        >>> parse_did_web("did:web:registry.gaia-x.eu:LegalPerson:abc123")
        {'host': 'registry.gaia-x.eu', 'path': 'LegalPerson:abc123',
         'type': 'LegalPerson', 'id': 'abc123'}
    """
    if not is_did_web(iri):
        return None

    # Remove "did:web:" prefix
    remainder = iri[8:]

    # Split into parts (: separated in did:web)
    parts = remainder.split(":")

    if len(parts) < 1:
        return None

    host = unquote(parts[0])
    path = ":".join(parts[1:]) if len(parts) > 1 else ""

    # Try to extract type and id from path
    path_parts = parts[1:] if len(parts) > 1 else []
    type_name = path_parts[0] if len(path_parts) > 0 else None
    resource_id = path_parts[-1] if len(path_parts) > 1 else None

    return {
        "host": host,
        "path": path,
        "type": type_name,
        "id": resource_id,
    }


def normalize_iri(iri: str, trailing_slash: bool = True) -> str:
    """
    Normalize an IRI for comparison.

    Args:
        iri: IRI string to normalize
        trailing_slash: If True, ensure trailing slash; if False, remove it

    Returns:
        Normalized IRI string

    Examples:
        >>> normalize_iri("http://example.org/ontology")
        'http://example.org/ontology/'
        >>> normalize_iri("http://example.org/ontology/", trailing_slash=False)
        'http://example.org/ontology'
    """
    # Don't modify hash-based URIs
    if "#" in iri:
        return iri

    if trailing_slash:
        return iri if iri.endswith("/") else iri + "/"
    else:
        return iri.rstrip("/")


def iri_to_domain_hint(iri: str) -> Optional[str]:
    """
    Extract a domain hint from an ontology IRI.

    Attempts to find the domain name from typical ontology IRI patterns.

    Args:
        iri: Ontology IRI

    Returns:
        Possible domain name, or None if not determinable

    Examples:
        >>> iri_to_domain_hint("https://w3id.org/ascs-ev/envited-x/scenario/v5/")
        'scenario'
        >>> iri_to_domain_hint("https://w3id.org/gaia-x/development/")
        'gx'
    """
    # Remove trailing slash/hash for parsing
    clean = iri.rstrip("/#")

    # Pattern: .../domain/vN/ or .../domain/
    # Match version pattern
    version_match = re.search(r"/([^/]+)/v\d+/?$", iri)
    if version_match:
        return version_match.group(1)

    # Match last path segment
    parts = clean.split("/")
    if parts:
        last = parts[-1]
        # Skip version numbers
        if not re.match(r"^v\d+$", last):
            return last

    return None


def matches_namespace(iri: str, namespace: str) -> bool:
    """
    Check if an IRI belongs to a namespace.

    Handles both hash (#) and slash (/) namespaces.

    Args:
        iri: IRI to check
        namespace: Namespace IRI (with or without trailing # or /)

    Returns:
        True if IRI belongs to the namespace

    Examples:
        >>> matches_namespace("http://ex.org/ont#Class", "http://ex.org/ont#")
        True
        >>> matches_namespace("http://ex.org/ont/Class", "http://ex.org/ont/")
        True
        >>> matches_namespace("http://ex.org/ont/Class", "http://ex.org/ont")
        True
    """
    # Normalize namespace
    base = namespace.rstrip("/#")

    return iri.startswith(base + "/") or iri.startswith(base + "#")


def extract_prefix_from_context(context: dict, iri: str) -> Optional[str]:
    """
    Find the prefix that matches an IRI from a JSON-LD @context.

    Args:
        context: JSON-LD @context dictionary
        iri: IRI to find prefix for

    Returns:
        Prefix string or None if not found

    Example:
        >>> ctx = {"gx": "https://w3id.org/gaia-x/"}
        >>> extract_prefix_from_context(ctx, "https://w3id.org/gaia-x/LegalPerson")
        'gx'
    """
    for prefix, namespace in context.items():
        if isinstance(namespace, str) and matches_namespace(iri, namespace):
            return prefix
    return None


def _run_tests() -> bool:
    """Run self-tests for the module."""
    print("Running iri_utils self-tests...")
    all_passed = True

    # Test 1: get_local_name with hash
    try:
        result = get_local_name("http://example.org/ontology#MyClass")
        assert result == "MyClass", f"Expected 'MyClass', got '{result}'"
        print("PASS: get_local_name with hash")
    except AssertionError as e:
        print(f"FAIL: get_local_name with hash - {e}")
        all_passed = False

    # Test 2: get_local_name with slash
    try:
        result = get_local_name("http://example.org/ontology/MyClass")
        assert result == "MyClass", f"Expected 'MyClass', got '{result}'"
        print("PASS: get_local_name with slash")
    except AssertionError as e:
        print(f"FAIL: get_local_name with slash - {e}")
        all_passed = False

    # Test 3: get_local_name lowercase
    try:
        result = get_local_name("http://example.org/ontology#MyClass", lowercase=True)
        assert result == "myclass", f"Expected 'myclass', got '{result}'"
        print("PASS: get_local_name lowercase")
    except AssertionError as e:
        print(f"FAIL: get_local_name lowercase - {e}")
        all_passed = False

    # Test 4: get_namespace with hash
    try:
        result = get_namespace("http://example.org/ontology#MyClass")
        assert result == "http://example.org/ontology#"
        print("PASS: get_namespace with hash")
    except AssertionError as e:
        print(f"FAIL: get_namespace with hash - {e}")
        all_passed = False

    # Test 5: get_namespace with slash
    try:
        result = get_namespace("http://example.org/ontology/MyClass")
        assert result == "http://example.org/ontology/"
        print("PASS: get_namespace with slash")
    except AssertionError as e:
        print(f"FAIL: get_namespace with slash - {e}")
        all_passed = False

    # Test 6: is_did_web positive
    try:
        result = is_did_web("did:web:registry.gaia-x.eu:participant:123")
        assert result is True
        print("PASS: is_did_web positive")
    except AssertionError as e:
        print(f"FAIL: is_did_web positive - {e}")
        all_passed = False

    # Test 7: is_did_web negative
    try:
        result = is_did_web("http://example.org/resource")
        assert result is False
        print("PASS: is_did_web negative")
    except AssertionError as e:
        print(f"FAIL: is_did_web negative - {e}")
        all_passed = False

    # Test 8: parse_did_web
    try:
        result = parse_did_web("did:web:registry.gaia-x.eu:LegalPerson:abc123")
        assert result is not None
        assert result["host"] == "registry.gaia-x.eu"
        assert result["type"] == "LegalPerson"
        assert result["id"] == "abc123"
        print("PASS: parse_did_web")
    except AssertionError as e:
        print(f"FAIL: parse_did_web - {e}")
        all_passed = False

    # Test 9: normalize_iri add trailing slash
    try:
        result = normalize_iri("http://example.org/ontology")
        assert result == "http://example.org/ontology/"
        print("PASS: normalize_iri add trailing slash")
    except AssertionError as e:
        print(f"FAIL: normalize_iri add trailing slash - {e}")
        all_passed = False

    # Test 10: normalize_iri remove trailing slash
    try:
        result = normalize_iri("http://example.org/ontology/", trailing_slash=False)
        assert result == "http://example.org/ontology"
        print("PASS: normalize_iri remove trailing slash")
    except AssertionError as e:
        print(f"FAIL: normalize_iri remove trailing slash - {e}")
        all_passed = False

    # Test 11: iri_to_domain_hint
    try:
        result = iri_to_domain_hint("https://w3id.org/ascs-ev/envited-x/scenario/v5/")
        assert result == "scenario", f"Expected 'scenario', got '{result}'"
        print("PASS: iri_to_domain_hint")
    except AssertionError as e:
        print(f"FAIL: iri_to_domain_hint - {e}")
        all_passed = False

    # Test 12: matches_namespace
    try:
        assert matches_namespace("http://ex.org/ont#Class", "http://ex.org/ont#")
        assert matches_namespace("http://ex.org/ont/Class", "http://ex.org/ont/")
        assert matches_namespace("http://ex.org/ont/Class", "http://ex.org/ont")
        assert not matches_namespace("http://other.org/Class", "http://ex.org/ont")
        print("PASS: matches_namespace")
    except AssertionError as e:
        print(f"FAIL: matches_namespace - {e}")
        all_passed = False

    print()
    if all_passed:
        print("All tests passed!")
    else:
        print("Some tests FAILED!")

    return all_passed


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--test", action="store_true", help="Run self-tests")
    parser.add_argument("iri", nargs="?", help="IRI to parse")

    args = parser.parse_args()

    if args.test:
        success = _run_tests()
        sys.exit(0 if success else 1)

    if args.iri:
        print(f"IRI: {args.iri}")
        print(f"  Local name: {get_local_name(args.iri)}")
        print(f"  Namespace: {get_namespace(args.iri)}")
        print(f"  Is did:web: {is_did_web(args.iri)}")
        if is_did_web(args.iri):
            parsed = parse_did_web(args.iri)
            print(f"  Parsed: {parsed}")
        print(f"  Domain hint: {iri_to_domain_hint(args.iri)}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
