#!/usr/bin/env python3
"""
Shared pytest fixtures for ontology management tests.

This module provides reusable fixtures for testing the ontology validation
and management tools. All fixtures are automatically available to tests
in the tests/ directory.

FIXTURE CATEGORIES:
==================
1. Path fixtures - root_dir, temp_dir, etc.
2. Sample data fixtures - minimal ontology, SHACL, instance files
3. Invalid data fixtures - malformed files for error testing
4. Infrastructure fixtures - resolver, graphs, catalogs

USAGE:
======
    def test_something(root_dir, sample_ontology):
        # root_dir and sample_ontology are automatically injected
        pass
"""

import json
from pathlib import Path
from typing import Dict

import pytest
from rdflib import Graph

# =============================================================================
# Path Fixtures
# =============================================================================


@pytest.fixture
def root_dir() -> Path:
    """Repository root directory."""
    return Path(__file__).parent.parent.resolve()


@pytest.fixture
def temp_dir(tmp_path) -> Path:
    """
    Temporary directory for test artifacts.

    This is automatically cleaned up after each test.
    """
    return tmp_path


@pytest.fixture
def artifacts_dir(root_dir) -> Path:
    """Artifacts directory containing ontology bundles."""
    return root_dir / "artifacts"


@pytest.fixture
def imports_dir(root_dir) -> Path:
    """Imports directory containing base ontologies."""
    return root_dir / "imports"


@pytest.fixture
def test_data_dir(root_dir) -> Path:
    """Test data directory with valid/invalid instances."""
    return root_dir / "tests" / "data"


# =============================================================================
# Minimal Sample Data Fixtures
# =============================================================================


MINIMAL_OWL_ONTOLOGY = """@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix : <http://test.example.org/minimal/v1/> .

<http://test.example.org/minimal/v1> a owl:Ontology ;
    owl:versionInfo "1.0.0" .

:TestClass a owl:Class ;
    rdfs:label "Test Class" .

:testProperty a owl:DatatypeProperty ;
    rdfs:domain :TestClass ;
    rdfs:range xsd:string .
"""


MINIMAL_SHACL_SHAPES = """@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix : <http://test.example.org/minimal/v1/> .

:TestClassShape a sh:NodeShape ;
    sh:targetClass :TestClass ;
    sh:property [
        sh:path :testProperty ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:datatype xsd:string ;
        sh:message "testProperty is required and must be a string" ;
    ] .
"""


MINIMAL_CONTEXT = {"@context": {"@vocab": "http://test.example.org/minimal/v1/"}}


MINIMAL_VALID_INSTANCE = {
    "@context": {"@vocab": "http://test.example.org/minimal/v1/"},
    "@id": "did:test:valid-instance-001",
    "@type": "TestClass",
    "testProperty": "valid test value",
}


MINIMAL_INVALID_INSTANCE = {
    "@context": {"@vocab": "http://test.example.org/minimal/v1/"},
    "@id": "did:test:invalid-instance-001",
    "@type": "TestClass",
    # Missing required testProperty - will trigger SHACL violation
}


@pytest.fixture
def sample_ontology(temp_dir) -> Path:
    """Creates minimal OWL ontology file."""
    ontology_file = temp_dir / "minimal.owl.ttl"
    ontology_file.write_text(MINIMAL_OWL_ONTOLOGY)
    return ontology_file


@pytest.fixture
def sample_shacl(temp_dir) -> Path:
    """Creates minimal SHACL shapes file."""
    shacl_file = temp_dir / "minimal.shacl.ttl"
    shacl_file.write_text(MINIMAL_SHACL_SHAPES)
    return shacl_file


@pytest.fixture
def sample_context(temp_dir) -> Path:
    """Creates minimal JSON-LD context file."""
    context_file = temp_dir / "minimal.context.jsonld"
    context_file.write_text(json.dumps(MINIMAL_CONTEXT, indent=2))
    return context_file


@pytest.fixture
def sample_instance(temp_dir) -> Path:
    """Creates valid JSON-LD instance file."""
    instance_file = temp_dir / "valid_instance.json"
    instance_file.write_text(json.dumps(MINIMAL_VALID_INSTANCE, indent=2))
    return instance_file


@pytest.fixture
def invalid_instance(temp_dir) -> Path:
    """Creates invalid JSON-LD instance (SHACL violation)."""
    instance_file = temp_dir / "invalid_instance.json"
    instance_file.write_text(json.dumps(MINIMAL_INVALID_INSTANCE, indent=2))
    return instance_file


@pytest.fixture
def sample_domain_bundle(temp_dir) -> Dict[str, Path]:
    """
    Complete test domain bundle: OWL + SHACL + context + instance.

    Returns a dictionary with paths to all files.
    """
    domain_dir = temp_dir / "minimal"
    domain_dir.mkdir(parents=True, exist_ok=True)

    # Create ontology
    ontology_file = domain_dir / "minimal.owl.ttl"
    ontology_file.write_text(MINIMAL_OWL_ONTOLOGY)

    # Create SHACL shapes
    shacl_file = domain_dir / "minimal.shacl.ttl"
    shacl_file.write_text(MINIMAL_SHACL_SHAPES)

    # Create context
    context_file = domain_dir / "minimal.context.jsonld"
    context_file.write_text(json.dumps(MINIMAL_CONTEXT, indent=2))

    # Create valid instance
    instance_file = domain_dir / "minimal_instance.json"
    instance_file.write_text(json.dumps(MINIMAL_VALID_INSTANCE, indent=2))

    return {
        "domain": "minimal",
        "dir": domain_dir,
        "ontology": ontology_file,
        "shacl": shacl_file,
        "context": context_file,
        "instance": instance_file,
    }


# =============================================================================
# Edge Case Fixtures
# =============================================================================


@pytest.fixture
def multi_type_instance(temp_dir) -> Path:
    """Instance with @types from 2+ different domains."""
    instance = {
        "@context": [
            {"@vocab": "http://test.example.org/domain1/v1/"},
            {"d2": "http://test.example.org/domain2/v1/"},
        ],
        "@id": "did:test:multi-type-001",
        "@type": ["TestClass", "d2:OtherClass"],
        "testProperty": "value",
    }
    instance_file = temp_dir / "multi_type_instance.json"
    instance_file.write_text(json.dumps(instance, indent=2))
    return instance_file


@pytest.fixture
def no_type_instance(temp_dir) -> Path:
    """Instance with @id but no @type (edge case)."""
    instance = {
        "@context": {"@vocab": "http://test.example.org/minimal/v1/"},
        "@id": "did:test:no-type-001",
        "testProperty": "value without type",
    }
    instance_file = temp_dir / "no_type_instance.json"
    instance_file.write_text(json.dumps(instance, indent=2))
    return instance_file


@pytest.fixture
def malformed_json(temp_dir) -> Path:
    """Invalid JSON for syntax validation testing."""
    bad_file = temp_dir / "malformed.json"
    bad_file.write_text('{"key": "value", missing_quote: true}')
    return bad_file


@pytest.fixture
def malformed_turtle(temp_dir) -> Path:
    """Invalid Turtle for syntax validation testing."""
    bad_file = temp_dir / "malformed.ttl"
    bad_file.write_text(
        """@prefix ex: <http://example.org/> .
ex:subject ex:predicate "unclosed string .
"""
    )
    return bad_file


@pytest.fixture
def empty_json(temp_dir) -> Path:
    """Empty JSON object file."""
    empty_file = temp_dir / "empty.json"
    empty_file.write_text("{}")
    return empty_file


@pytest.fixture
def empty_turtle(temp_dir) -> Path:
    """Empty Turtle file (valid but no triples)."""
    empty_file = temp_dir / "empty.ttl"
    empty_file.write_text("# Empty turtle file\n")
    return empty_file


# =============================================================================
# Infrastructure Fixtures
# =============================================================================


@pytest.fixture
def empty_graph() -> Graph:
    """Empty RDF graph for testing."""
    return Graph()


@pytest.fixture
def sample_graph(sample_ontology) -> Graph:
    """Graph loaded with sample ontology."""
    g = Graph()
    g.parse(str(sample_ontology), format="turtle")
    return g


@pytest.fixture
def registry_resolver(root_dir):
    """Configured RegistryResolver instance."""
    from src.tools.utils.registry_resolver import RegistryResolver

    return RegistryResolver(root_dir)


@pytest.fixture
def manifest_graph(root_dir) -> Graph:
    """Loaded manifest ontology graph (if exists)."""
    manifest_owl = root_dir / "artifacts" / "manifest" / "manifest.owl.ttl"
    g = Graph()
    if manifest_owl.exists():
        g.parse(str(manifest_owl), format="turtle")
    return g


# =============================================================================
# Catalog/Registry Fixtures
# =============================================================================


@pytest.fixture
def temp_catalog(temp_dir) -> Path:
    """Creates temporary XML catalog file."""
    catalog_content = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE catalog PUBLIC "-//OASIS//DTD Entity Resolution XML Catalog V1.0//EN"
  "http://www.oasis-open.org/committees/entity/release/1.0/catalog.dtd">
<catalog xmlns="urn:oasis:names:tc:entity:xmlns:xml:catalog">
    <uri name="did:test:minimal:test_valid_instance"
         uri="minimal/valid_instance.json"
         domain="minimal"
         test-type="valid"
         category="test-data"/>
</catalog>
"""
    catalog_file = temp_dir / "catalog-v001.xml"
    catalog_file.write_text(catalog_content)
    return catalog_file


@pytest.fixture
def mock_registry(temp_dir) -> Dict:
    """Creates mock registry.json structure."""
    registry = {
        "version": "1.0.0",
        "ontologies": {
            "minimal": {
                "iri": "http://test.example.org/minimal/v1/",
                "latest": "v1",
                "versions": {
                    "v1": {
                        "files": {
                            "ontology": "artifacts/minimal/minimal.owl.ttl",
                            "shacl": "artifacts/minimal/minimal.shacl.ttl",
                            "jsonld": "artifacts/minimal/minimal.context.jsonld",
                        }
                    }
                },
            }
        },
        "base_ontologies": [],
    }

    registry_file = temp_dir / "docs" / "registry.json"
    registry_file.parent.mkdir(parents=True, exist_ok=True)
    registry_file.write_text(json.dumps(registry, indent=2))

    return registry


# =============================================================================
# Test Data Discovery Fixtures
# =============================================================================


@pytest.fixture
def manifest_test_files(test_data_dir) -> list:
    """List of manifest test files (if they exist)."""
    manifest_dir = test_data_dir / "manifest" / "valid"
    if manifest_dir.exists():
        return sorted(manifest_dir.glob("*.json"))
    return []


@pytest.fixture
def scenario_test_files(test_data_dir) -> list:
    """List of scenario test files (if they exist)."""
    scenario_dir = test_data_dir / "scenario" / "valid"
    if scenario_dir.exists():
        return sorted(scenario_dir.glob("*.json"))
    return []


# =============================================================================
# Helper Fixtures
# =============================================================================


@pytest.fixture
def json_files_in_temp(temp_dir) -> callable:
    """
    Factory fixture that creates multiple JSON files in temp dir.

    Usage:
        files = json_files_in_temp([
            {"name": "file1.json", "content": {"key": "value"}},
            {"name": "file2.json", "content": {"other": "data"}},
        ])
    """

    def _create_files(file_specs: list) -> list:
        created = []
        for spec in file_specs:
            file_path = temp_dir / spec["name"]
            file_path.write_text(json.dumps(spec["content"], indent=2))
            created.append(file_path)
        return created

    return _create_files


@pytest.fixture
def turtle_files_in_temp(temp_dir) -> callable:
    """
    Factory fixture that creates multiple Turtle files in temp dir.

    Usage:
        files = turtle_files_in_temp([
            {"name": "file1.ttl", "content": "@prefix ..."},
            {"name": "file2.ttl", "content": "@prefix ..."},
        ])
    """

    def _create_files(file_specs: list) -> list:
        created = []
        for spec in file_specs:
            file_path = temp_dir / spec["name"]
            file_path.write_text(spec["content"])
            created.append(file_path)
        return created

    return _create_files
