#!/usr/bin/env python3
"""
Unit tests for src.tools.utils.registry_resolver catalog resolution.
"""

import json
from pathlib import Path

from src.tools.utils.registry_resolver import RegistryResolver


def _write_registry(root: Path, registry: dict) -> None:
    registry_path = root / "docs" / "registry.json"
    registry_path.parent.mkdir(parents=True, exist_ok=True)
    registry_path.write_text(json.dumps(registry, indent=2))


def _write_imports_catalog(root: Path, content: str) -> None:
    catalog_path = root / "imports" / "catalog-v001.xml"
    catalog_path.parent.mkdir(parents=True, exist_ok=True)
    catalog_path.write_text(content)


def _write_artifacts_catalog(root: Path, content: str) -> None:
    catalog_path = root / "artifacts" / "catalog-v001.xml"
    catalog_path.parent.mkdir(parents=True, exist_ok=True)
    catalog_path.write_text(content)


def test_get_base_ontology_paths_from_imports_catalog(temp_dir):
    registry = {
        "version": "1.0.0",
        "ontologies": {},
    }
    _write_registry(temp_dir, registry)
    _write_artifacts_catalog(
        temp_dir,
        """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE catalog PUBLIC "-//OASIS//DTD Entity Resolution XML Catalog V1.0//EN"
  "http://www.oasis-open.org/committees/entity/release/1.0/catalog.dtd">
<catalog xmlns="urn:oasis:names:tc:entity:xmlns:xml:catalog">
</catalog>
""",
    )

    catalog_content = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE catalog PUBLIC "-//OASIS//DTD Entity Resolution XML Catalog V1.0//EN"
  "http://www.oasis-open.org/committees/entity/release/1.0/catalog.dtd">
<catalog xmlns="urn:oasis:names:tc:entity:xmlns:xml:catalog">
  <uri name="http://example.org/rdf" uri="rdf/rdf.owl.ttl"/>
  <uri name="http://example.org/context" uri="cred/cred.context.jsonld"/>
  <uri name="http://example.org/shapes" uri="sh/sh.shacl.ttl"/>
</catalog>
"""
    _write_imports_catalog(temp_dir, catalog_content)

    resolver = RegistryResolver(temp_dir)
    assert resolver.get_base_ontology_paths() == ["imports/rdf/rdf.owl.ttl"]


def test_get_base_ontology_paths_no_catalog_returns_empty(temp_dir):
    registry = {
        "version": "1.0.0",
        "ontologies": {},
    }
    _write_registry(temp_dir, registry)
    _write_artifacts_catalog(
        temp_dir,
        """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE catalog PUBLIC "-//OASIS//DTD Entity Resolution XML Catalog V1.0//EN"
  "http://www.oasis-open.org/committees/entity/release/1.0/catalog.dtd">
<catalog xmlns="urn:oasis:names:tc:entity:xmlns:xml:catalog">
</catalog>
""",
    )

    resolver = RegistryResolver(temp_dir)
    assert resolver.get_base_ontology_paths() == []


def test_artifacts_catalog_drives_domain_resolution(temp_dir):
    registry = {
        "version": "1.0.0",
        "ontologies": {},
    }
    _write_registry(temp_dir, registry)

    artifacts_catalog = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE catalog PUBLIC "-//OASIS//DTD Entity Resolution XML Catalog V1.0//EN"
  "http://www.oasis-open.org/committees/entity/release/1.0/catalog.dtd">
<catalog xmlns="urn:oasis:names:tc:entity:xmlns:xml:catalog">
  <uri name="http://example.org/demo/v1" uri="demo/demo.owl.ttl"/>
  <uri name="http://example.org/demo/v1/shapes" uri="demo/demo.shacl.ttl"/>
  <uri name="http://example.org/demo/v1/context" uri="demo/demo.context.jsonld"/>
  <uri name="http://example.org/other/v2" uri="other/other.owl.ttl"/>
</catalog>
"""
    _write_artifacts_catalog(temp_dir, artifacts_catalog)

    resolver = RegistryResolver(temp_dir)

    assert resolver.list_domains() == ["demo", "other"]
    assert resolver.get_ontology_path("demo") == "artifacts/demo/demo.owl.ttl"
    assert resolver.get_shacl_paths("demo") == ["artifacts/demo/demo.shacl.ttl"]
    assert resolver.get_context_path("demo") == "artifacts/demo/demo.context.jsonld"
    assert resolver.get_iri("demo") == "http://example.org/demo/v1"
    assert (
        resolver.resolve_type_to_domain("http://example.org/demo/v1/SomeClass")
        == "demo"
    )


def test_base_ontology_filtering_by_iris(temp_dir):
    registry = {
        "version": "1.0.0",
        "ontologies": {},
    }
    _write_registry(temp_dir, registry)
    _write_artifacts_catalog(
        temp_dir,
        """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE catalog PUBLIC "-//OASIS//DTD Entity Resolution XML Catalog V1.0//EN"
  "http://www.oasis-open.org/committees/entity/release/1.0/catalog.dtd">
<catalog xmlns="urn:oasis:names:tc:entity:xmlns:xml:catalog">
</catalog>
""",
    )

    imports_catalog = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE catalog PUBLIC "-//OASIS//DTD Entity Resolution XML Catalog V1.0//EN"
  "http://www.oasis-open.org/committees/entity/release/1.0/catalog.dtd">
<catalog xmlns="urn:oasis:names:tc:entity:xmlns:xml:catalog">
  <uri name="http://www.w3.org/2000/01/rdf-schema#" uri="rdfs/rdfs.owl.ttl"/>
  <uri name="http://www.w3.org/2001/XMLSchema#" uri="xsd/xsd.owl.ttl"/>
  <uri name="http://www.w3.org/2004/02/skos/core#" uri="skos/skos.owl.ttl"/>
</catalog>
"""
    _write_imports_catalog(temp_dir, imports_catalog)

    resolver = RegistryResolver(temp_dir)
    filtered = resolver.get_base_ontology_paths_for_iris(
        {
            "http://www.w3.org/2001/XMLSchema#string",
            "http://www.w3.org/2004/02/skos/core#note",
        }
    )

    assert filtered == ["imports/skos/skos.owl.ttl", "imports/xsd/xsd.owl.ttl"]


def test_base_ontology_filtering_normalizes_http_https(temp_dir):
    registry = {
        "version": "1.0.0",
        "ontologies": {},
    }
    _write_registry(temp_dir, registry)
    _write_artifacts_catalog(
        temp_dir,
        """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE catalog PUBLIC "-//OASIS//DTD Entity Resolution XML Catalog V1.0//EN"
  "http://www.oasis-open.org/committees/entity/release/1.0/catalog.dtd">
<catalog xmlns="urn:oasis:names:tc:entity:xmlns:xml:catalog">
</catalog>
""",
    )

    imports_catalog = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE catalog PUBLIC "-//OASIS//DTD Entity Resolution XML Catalog V1.0//EN"
  "http://www.oasis-open.org/committees/entity/release/1.0/catalog.dtd">
<catalog xmlns="urn:oasis:names:tc:entity:xmlns:xml:catalog">
  <uri name="http://schema.org/" uri="schema/schema.owl.ttl"/>
</catalog>
"""
    _write_imports_catalog(temp_dir, imports_catalog)

    resolver = RegistryResolver(temp_dir)
    filtered = resolver.get_base_ontology_paths_for_iris({"https://schema.org/name"})

    assert filtered == ["imports/schema/schema.owl.ttl"]
