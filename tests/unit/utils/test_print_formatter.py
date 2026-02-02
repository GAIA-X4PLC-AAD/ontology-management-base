#!/usr/bin/env python3
"""
Unit tests for src.tools.utils.print_formatter.
"""

from io import StringIO
from pathlib import Path

from rdflib import RDF, Graph, Literal, Namespace

from src.tools.utils import print_formatter


def test_normalize_path_for_display(temp_dir: Path):
    path = temp_dir / "nested" / "file.ttl"
    path.parent.mkdir(parents=True)
    path.write_text("")
    normalized = print_formatter.normalize_path_for_display(path, temp_dir)
    assert normalized == "nested/file.ttl"


def test_normalize_text_scrubs_bnode():
    text = "N1234567890abcdef1234567890abcdef"
    normalized = print_formatter.normalize_text(text)
    assert "[BNODE]" in normalized or normalized == ""


def test_format_artifact_coherence_result_contains_header():
    out = print_formatter.format_artifact_coherence_result(
        "artifacts/demo/demo.owl.ttl",
        3,
        2,
        {"a"},
        set(),
        set(),
        set(),
    )
    assert "VALIDATION SUMMARY" in out
    assert "Ontology File" in out


def test_format_data_conformance_result_success():
    buffer = StringIO()
    print_formatter.format_data_conformance_result(
        True, onto_files=["file.json"], report_graph=None, file=buffer
    )
    output = buffer.getvalue()
    assert "SHACL validation passed" in output


def test_format_data_conformance_result_with_errors():
    buffer = StringIO()
    SH = Namespace("http://www.w3.org/ns/shacl#")
    g = Graph()
    from rdflib import URIRef

    result = URIRef("urn:res1")
    g.add((result, RDF.type, SH.ValidationResult))
    g.add((result, SH.resultMessage, Literal("bad")))
    print_formatter.format_data_conformance_result(
        False, onto_files=["file.json"], report_graph=g, file=buffer
    )
    output = buffer.getvalue()
    assert "SHACL validation failed" in output
