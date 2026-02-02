#!/usr/bin/env python3
"""
Unit tests for src.tools.validators.shacl.schema_discovery.
"""

import json
from pathlib import Path

from rdflib import RDF, Graph, Literal, URIRef

from src.tools.utils.registry_resolver import RegistryResolver
from src.tools.validators.shacl import schema_discovery


def _write_registry(root: Path) -> None:
    registry_path = root / "docs" / "registry.json"
    registry_path.parent.mkdir(parents=True, exist_ok=True)
    registry_path.write_text(json.dumps({"version": "1.0.0", "ontologies": {}}))


def _write_artifacts_catalog(root: Path, content: str) -> None:
    catalog_path = root / "artifacts" / "catalog-v001.xml"
    catalog_path.parent.mkdir(parents=True, exist_ok=True)
    catalog_path.write_text(content)


def test_extract_rdf_types_predicates_and_datatypes():
    g = Graph()
    s = URIRef("http://example.org/s")
    t = URIRef("http://example.org/T")
    p = URIRef("http://example.org/p")
    g.add((s, RDF.type, t))
    g.add((s, p, Literal("x", datatype=URIRef("http://example.org/dt"))))

    assert schema_discovery.extract_rdf_types(g) == {str(t)}
    assert str(p) in schema_discovery.extract_predicates(g)
    assert "http://example.org/dt" in schema_discovery.extract_datatype_iris(g)


def test_discover_required_schemas_with_catalog(temp_dir: Path):
    _write_registry(temp_dir)
    artifacts_catalog = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE catalog PUBLIC "-//OASIS//DTD Entity Resolution XML Catalog V1.0//EN"
  "http://www.oasis-open.org/committees/entity/release/1.0/catalog.dtd">
<catalog xmlns="urn:oasis:names:tc:entity:xmlns:xml:catalog">
  <uri name="http://example.org/demo/v1" uri="demo/demo.owl.ttl"/>
  <uri name="http://example.org/demo/v1/shapes" uri="demo/demo.shacl.ttl"/>
</catalog>
"""
    _write_artifacts_catalog(temp_dir, artifacts_catalog)

    resolver = RegistryResolver(temp_dir)
    ontology_paths, shacl_paths = schema_discovery.discover_required_schemas(
        {"http://example.org/demo/v1/Thing"}, resolver
    )
    assert ontology_paths == ["artifacts/demo/demo.owl.ttl"]
    assert shacl_paths == ["artifacts/demo/demo.shacl.ttl"]
