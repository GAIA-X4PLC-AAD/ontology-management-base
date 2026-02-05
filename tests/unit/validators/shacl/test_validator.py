#!/usr/bin/env python3
"""
Unit tests for src.tools.validators.shacl.validator.
"""

from pathlib import Path

from rdflib import RDF, RDFS, Graph, Namespace

from src.tools.validators.shacl.validator import ShaclValidator


def _make_validator(tmp: Path) -> ShaclValidator:
    # Minimal catalog files so RegistryResolver initializes without warnings
    (tmp / "docs").mkdir(parents=True, exist_ok=True)
    (tmp / "docs" / "registry.json").write_text('{"version":"1.0.0","ontologies":{}}')
    (tmp / "artifacts").mkdir(parents=True, exist_ok=True)
    (tmp / "artifacts" / "catalog-v001.xml").write_text(
        """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE catalog PUBLIC "-//OASIS//DTD Entity Resolution XML Catalog V1.0//EN"
  "http://www.oasis-open.org/committees/entity/release/1.0/catalog.dtd">
<catalog xmlns="urn:oasis:names:tc:entity:xmlns:xml:catalog"></catalog>
"""
    )
    return ShaclValidator(tmp, inference_mode="none", verbose=False)


def test_apply_inference_none_includes_ontology(tmp_path: Path):
    ex = Namespace("http://example.org/")
    validator = _make_validator(tmp_path)

    data = Graph()
    ont = Graph()
    data.add((ex.a, RDF.type, ex.Type))
    ont.add((ex.Type, RDFS.subClassOf, ex.Super))

    combined, inferred = validator._apply_inference(data, ont)
    assert inferred == 0
    assert (ex.Type, RDFS.subClassOf, ex.Super) in combined


def test_apply_inference_rdfs_adds_inferred(tmp_path: Path):
    ex = Namespace("http://example.org/")
    validator = _make_validator(tmp_path)
    validator.inference_mode = "rdfs"

    data = Graph()
    ont = Graph()
    data.add((ex.a, RDF.type, ex.Sub))
    ont.add((ex.Sub, RDFS.subClassOf, ex.Super))

    combined, inferred = validator._apply_inference(data, ont)
    assert (ex.a, RDF.type, ex.Super) in combined
    assert inferred >= 1
