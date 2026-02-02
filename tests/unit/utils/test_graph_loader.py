#!/usr/bin/env python3
"""
Unit tests for src.tools.utils.graph_loader.
"""

import json
from pathlib import Path

from rdflib import Graph

from src.tools.utils import graph_loader
from src.tools.utils.registry_resolver import RegistryResolver


def test_load_graph_auto_detects_jsonld(temp_dir: Path):
    jsonld_file = temp_dir / "data.jsonld"
    jsonld_file.write_text(
        json.dumps(
            {
                "@context": {"ex": "http://example.org/"},
                "@id": "ex:a",
                "ex:prop": "value",
            }
        )
    )

    g = graph_loader.load_graph(jsonld_file)
    assert isinstance(g, Graph)
    assert len(g) >= 1


def test_load_graphs_combines_files(temp_dir: Path):
    a = temp_dir / "a.ttl"
    b = temp_dir / "b.ttl"
    a.write_text(
        "<http://example.org/a> <http://example.org/p> <http://example.org/o> ."
    )
    b.write_text(
        "<http://example.org/b> <http://example.org/p> <http://example.org/o> ."
    )

    g = graph_loader.load_graphs([a, b])
    assert len(g) == 2


def test_load_jsonld_files_extracts_prefixes(temp_dir: Path):
    jsonld_file = temp_dir / "data.json"
    jsonld_file.write_text(
        json.dumps(
            {
                "@context": {"ex": "http://example.org/"},
                "@id": "ex:thing",
            }
        )
    )

    g, prefixes = graph_loader.load_jsonld_files([jsonld_file], temp_dir)
    assert len(g) >= 1
    assert prefixes.get("ex") == "http://example.org/"


def test_load_turtle_files(temp_dir: Path):
    ttl_file = temp_dir / "data.ttl"
    ttl_file.write_text(
        "<http://example.org/a> <http://example.org/p> <http://example.org/o> ."
    )

    g = graph_loader.load_turtle_files([ttl_file], temp_dir)
    assert len(g) == 1


def test_extract_external_iris_detects_did_web(temp_dir: Path):
    ttl_file = temp_dir / "data.ttl"
    ttl_file.write_text(
        "<did:web:test.example:thing> <http://example.org/p> <did:web:test.example:obj> ."
    )
    g = Graph()
    g.parse(str(ttl_file), format="turtle")
    iris = graph_loader.extract_external_iris(g)
    assert "did:web:test.example:thing" in iris
    assert "did:web:test.example:obj" in iris


def test_load_fixtures_for_iris(temp_dir: Path):
    # Create minimal registry and catalog
    (temp_dir / "docs").mkdir()
    (temp_dir / "docs" / "registry.json").write_text(
        '{"version":"1.0.0","ontologies":{}}'
    )

    (temp_dir / "tests").mkdir()
    catalog = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE catalog PUBLIC "-//OASIS//DTD Entity Resolution XML Catalog V1.0//EN"
  "http://www.oasis-open.org/committees/entity/release/1.0/catalog.dtd">
<catalog xmlns="urn:oasis:names:tc:entity:xmlns:xml:catalog">
  <uri name="did:web:test.fixture:entity" uri="tests/fixtures/entity.json" domain="fixture" test-type="fixture" category="fixture"/>
</catalog>
"""
    (temp_dir / "tests" / "catalog-v001.xml").write_text(catalog)
    fixtures_dir = temp_dir / "tests" / "fixtures"
    fixtures_dir.mkdir()
    fixture_file = fixtures_dir / "entity.json"
    fixture_file.write_text(json.dumps({"@id": "did:web:test.fixture:entity"}))

    resolver = RegistryResolver(temp_dir)
    g = Graph()
    loaded = graph_loader.load_fixtures_for_iris(
        {"did:web:test.fixture:entity"}, resolver, g, temp_dir
    )
    assert loaded == 1
    assert len(g) >= 1
