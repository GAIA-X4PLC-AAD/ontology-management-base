#!/usr/bin/env python3
"""
Unit tests for src.tools.core.constants.
"""

from src.tools.core import constants


def test_fast_store_value():
    assert constants.FAST_STORE in ("oxigraph", "default")


def test_extensions_values():
    assert constants.Extensions.TURTLE == ".ttl"
    assert ".json" in constants.Extensions.JSONLD
    assert constants.Extensions.OWL.endswith(".owl.ttl")
    assert constants.Extensions.SHACL.endswith(".shacl.ttl")
    assert constants.Extensions.CONTEXT.endswith(".context.jsonld")


def test_namespaces_values():
    assert constants.Namespaces.RDF.startswith("http://")
    assert constants.Namespaces.RDFS.startswith("http://")
    assert constants.Namespaces.OWL.startswith("http://")
    assert constants.Namespaces.XSD.startswith("http://")
    assert constants.Namespaces.SHACL.startswith("http://")
    assert constants.Namespaces.SKOS.startswith("http://")
