#!/usr/bin/env python3
"""
Unit tests for src.tools.utils.registry_updater.
"""

from pathlib import Path

import rdflib

from src.tools.utils import registry_updater


def test_clean_iri_strips_extension():
    iri = "https://example.org/onto/file.owl.ttl"
    cleaned = registry_updater.clean_iri(iri)
    assert cleaned.endswith("/")


def test_determine_namespace_from_iri():
    iri = "https://w3id.org/ascs-ev/envited-x/hdmap/v5"
    assert registry_updater.determine_namespace_from_iri(iri) == "ascs-ev"


def test_extract_iri_from_graph_prefers_ontology():
    g = rdflib.Graph()
    onto = rdflib.URIRef("http://example.org/onto/v1")
    g.add((onto, rdflib.RDF.type, rdflib.OWL.Ontology))
    assert registry_updater.extract_iri_from_graph(g) == str(onto)


def test_generate_xml_catalog_includes_entries(temp_dir: Path):
    # Create minimal ontology file
    ontology_file = temp_dir / "demo.owl.ttl"
    ontology_file.write_text(
        "@prefix owl: <http://www.w3.org/2002/07/owl#> .\n"
        "<http://example.org/demo/v1> a owl:Ontology .\n"
    )

    # Create minimal shacl file with owl:Ontology
    shacl_file = temp_dir / "demo.shacl.ttl"
    shacl_file.write_text(
        "@prefix owl: <http://www.w3.org/2002/07/owl#> .\n"
        "<http://example.org/demo/v1/shapes> a owl:Ontology .\n"
    )

    context_file = temp_dir / "demo.context.jsonld"
    context_file.write_text("{}")

    ontologies = {
        "demo": {
            "ontology": ontology_file,
            "shacl": [shacl_file],
            "jsonld": context_file,
            "properties": None,
            "instance": None,
        }
    }
    registry = {
        "ontologies": {
            "demo": {
                "iri": "http://example.org/demo/v1",
                "latest": "v1",
                "versions": {"v1": {"files": {}}},
            }
        }
    }

    xml = registry_updater.generate_xml_catalog(
        ontologies, registry, temp_dir / "catalog-v001.xml"
    )
    assert "http://example.org/demo/v1" in xml
    assert "http://example.org/demo/v1/shapes" in xml
    assert "http://example.org/demo/v1/context" in xml
