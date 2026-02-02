#!/usr/bin/env python3
"""
Unit tests for coherence_validator behavior.
"""

from pathlib import Path

from src.tools.core.result import ReturnCodes
from src.tools.validators.coherence_validator import (
    extract_ontology_classes,
    extract_shacl_classes_from_file,
    get_local_name,
    validate_artifact_coherence,
)


def _write_registry(root: Path) -> None:
    registry_path = root / "docs" / "registry.json"
    registry_path.parent.mkdir(parents=True, exist_ok=True)
    registry_path.write_text('{"version": "1.0.0", "ontologies": {}}')


def _write_artifacts_catalog(root: Path, content: str) -> None:
    catalog_path = root / "artifacts" / "catalog-v001.xml"
    catalog_path.parent.mkdir(parents=True, exist_ok=True)
    catalog_path.write_text(content)


def test_coherence_fails_when_shacl_missing(temp_dir: Path) -> None:
    _write_registry(temp_dir)

    artifacts_catalog = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE catalog PUBLIC "-//OASIS//DTD Entity Resolution XML Catalog V1.0//EN"
  "http://www.oasis-open.org/committees/entity/release/1.0/catalog.dtd">
<catalog xmlns="urn:oasis:names:tc:entity:xmlns:xml:catalog">
  <uri name="http://example.org/demo/v1" uri="demo/demo.owl.ttl"/>
</catalog>
"""
    _write_artifacts_catalog(temp_dir, artifacts_catalog)

    # No SHACL entries for demo -> should fail
    return_code, message = validate_artifact_coherence("demo", root_dir=temp_dir)

    assert return_code == ReturnCodes.COHERENCE_ERROR
    assert "No SHACL file found" in message


def test_get_local_name_variants():
    assert get_local_name("http://example.org/a#B") == "b"
    assert get_local_name("http://example.org/a/B") == "b"


def test_extract_shacl_classes_from_file(temp_dir: Path):
    ttl = """@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix ex: <http://example.org/> .
ex:Shape a sh:NodeShape ;
  sh:targetClass ex:Thing .
"""
    shacl_file = temp_dir / "shape.shacl.ttl"
    shacl_file.write_text(ttl)
    classes = extract_shacl_classes_from_file(str(shacl_file))
    assert "thing" in classes


def test_extract_ontology_classes(temp_dir: Path):
    ttl = """@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix ex: <http://example.org/> .
ex:Thing a owl:Class .
"""
    owl_file = temp_dir / "demo.owl.ttl"
    owl_file.write_text(ttl)
    classes, labels = extract_ontology_classes(str(owl_file))
    assert "thing" in classes
    assert labels == {}
