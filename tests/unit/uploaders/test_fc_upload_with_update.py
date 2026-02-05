#!/usr/bin/env python3
"""
Unit tests for src.tools.uploaders.fc_upload_with_update.
"""

from pathlib import Path

import rdflib

from src.tools.uploaders import fc_upload_with_update as uploader


def test_extract_ontology_name():
    g = rdflib.Graph()
    onto = rdflib.URIRef("http://example.org/demo/v1")
    g.add((onto, rdflib.RDF.type, rdflib.OWL.Ontology))
    assert uploader.extract_ontology_name(g) == str(onto)


def test_extract_shape_target_classes():
    ttl = """@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix ex: <http://example.org/> .

ex:Shape a sh:NodeShape ;
  sh:targetClass ex:Thing .
"""
    g = rdflib.Graph()
    g.parse(data=ttl, format="turtle")
    targets = uploader.extract_shape_target_classes(g)
    assert targets == ["http://example.org/Thing"]


def test_all_classes_exist_in_ontology():
    ont = rdflib.Graph()
    klass = rdflib.URIRef("http://example.org/Thing")
    ont.add((klass, rdflib.RDF.type, rdflib.OWL.Class))
    assert uploader.all_classes_exist_in_ontology(ont, [str(klass)]) is True


def test_find_corresponding_shapes_from_filesystem(temp_dir: Path):
    ontology = """@prefix owl: <http://www.w3.org/2002/07/owl#> .
<http://example.org/demo/v1> a owl:Ontology .
<http://example.org/Thing> a owl:Class .
"""
    shape = """@prefix sh: <http://www.w3.org/ns/shacl#> .
<http://example.org/Shape> a sh:NodeShape ;
  sh:targetClass <http://example.org/Thing> .
"""
    (temp_dir / "demo.owl.ttl").write_text(ontology)
    (temp_dir / "demo.shacl.ttl").write_text(shape)

    g = rdflib.Graph()
    g.parse(str(temp_dir / "demo.owl.ttl"), format="turtle")
    shapes, name = uploader.find_corresponding_shapes_from_filesystem(
        str(temp_dir), g, False
    )
    assert name == "http://example.org/demo/v1"
    assert "demo.shacl.ttl" in shapes
