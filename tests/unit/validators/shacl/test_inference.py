#!/usr/bin/env python3
"""
Unit tests for src.tools.validators.shacl.inference.
"""

from rdflib import RDF, RDFS, Graph, Namespace

from src.tools.validators.shacl.inference import apply_rdfs_inference


def test_apply_rdfs_inference_subclass_and_domain():
    ex = Namespace("http://example.org/")
    data = Graph()
    ont = Graph()

    data.add((ex.instance, ex.prop, ex.obj))
    data.add((ex.instance, RDF.type, ex.Sub))

    ont.add((ex.Sub, RDFS.subClassOf, ex.Super))
    ont.add((ex.prop, RDFS.domain, ex.DomainClass))

    combined, inferred = apply_rdfs_inference(data, ont)
    assert (ex.instance, RDF.type, ex.Super) in combined
    assert (ex.instance, RDF.type, ex.DomainClass) in combined
    assert inferred >= 1
