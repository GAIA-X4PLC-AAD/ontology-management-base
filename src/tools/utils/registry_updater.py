#!/usr/bin/env python3
"""
Registry Update Script for Ontology Management Base.

This script generates/updates:
  1. docs/registry.json - Maps ALL ontology domains (artifacts + imports) to files
  2. artifacts/catalog-v001.xml - OASIS XML Catalog for domain ontologies
  3. imports/catalog-v001.xml - OASIS XML Catalog for base ontologies
  4. tests/catalog-v001.xml - Unified test catalog (test data + fixtures)

Usage:
    python -m src.tools.utils.registry_updater [--release-tag TAG] [--dry-run]
"""

import argparse
import json
import os
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Union
from urllib.parse import urlparse
from xml.dom import minidom
from xml.etree import ElementTree as ET

# Import RDFLib
import rdflib
from rdflib import OWL, RDF, URIRef
from rdflib.namespace import SKOS

# Try to use Oxigraph for speed
try:
    import oxrdflib  # noqa: F401

    FAST_STORE = "oxigraph"
except ImportError:
    FAST_STORE = "default"

# Import centralized file collector
from src.tools.utils.file_collector import (
    collect_jsonld_files,
    collect_ontology_bundles,
)

# Constants
ROOT_DIR = Path(__file__).parent.parent.parent.parent.resolve()
ARTIFACTS_DIR = ROOT_DIR / "artifacts"
TESTS_DATA_DIR = ROOT_DIR / "tests" / "data"
FIXTURES_DIR = ROOT_DIR / "tests" / "fixtures"
IMPORTS_DIR = ROOT_DIR / "imports"

REGISTRY_PATH = ROOT_DIR / "docs" / "registry.json"
ARTIFACTS_CATALOG_PATH = ARTIFACTS_DIR / "catalog-v001.xml"
IMPORTS_CATALOG_PATH = IMPORTS_DIR / "catalog-v001.xml"
TEST_CATALOG_PATH = ROOT_DIR / "tests" / "catalog-v001.xml"

REGISTRY_VERSION = "2.0.0"

# Known IRIs for standard ontologies that might fail auto-detection
KNOWN_IRIS = {
    "xsd.owl.ttl": "http://www.w3.org/2001/XMLSchema#",
    "rdf.owl.ttl": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs.owl.ttl": "http://www.w3.org/2000/01/rdf-schema#",
    "owl.owl.ttl": "http://www.w3.org/2002/07/owl#",
    "sh.owl.ttl": "http://www.w3.org/ns/shacl#",
    "skos.owl.ttl": "http://www.w3.org/2004/02/skos/core#",
    "dcterms.owl.ttl": "http://purl.org/dc/terms/",
    "dc.owl.ttl": "http://purl.org/dc/elements/1.1/",
    "foaf.owl.ttl": "http://xmlns.com/foaf/0.1/",
    "prov.owl.ttl": "http://www.w3.org/ns/prov#",
    "dcat.owl.ttl": "http://www.w3.org/ns/dcat#",
    "schema.owl.ttl": "http://schema.org/",
    "cred.owl.ttl": "https://www.w3.org/2018/credentials#",
}


def parse_graph(file_path: Path) -> Optional[rdflib.Graph]:
    """Helper to parse an RDF file efficiently."""
    g = rdflib.Graph(store=FAST_STORE)
    try:
        suffix = file_path.suffix.lower()
        if suffix == ".ttl":
            fmt = "turtle"
        elif suffix in [".jsonld", ".json"]:
            fmt = "json-ld"
        elif suffix in [".rdf", ".xml"]:
            fmt = "xml"
        else:
            fmt = rdflib.util.guess_format(str(file_path)) or "turtle"

        g.parse(str(file_path), format=fmt)
        return g
    except Exception as e:
        print(f"⚠️  Warning: Could not parse {file_path.name}: {e}", file=sys.stderr)
        return None


def extract_iri_from_graph(g: rdflib.Graph) -> Optional[str]:
    """Robustly identify the Ontology IRI from a graph."""
    # 1. Look for owl:Ontology
    for s in g.subjects(RDF.type, OWL.Ontology):
        if isinstance(s, URIRef):
            return str(s)

    # 2. Look for skos:ConceptScheme
    for s in g.subjects(RDF.type, SKOS.ConceptScheme):
        if isinstance(s, URIRef):
            return str(s)

    # 3. Statistical Heuristic (last resort)
    namespaces = []
    for s in g.subjects():
        if isinstance(s, URIRef):
            uri = str(s)
            if "#" in uri:
                ns = uri.rsplit("#", 1)[0] + "#"
            else:
                ns = uri.rsplit("/", 1)[0] + "/"
            namespaces.append(ns)

    if namespaces:
        most_common = Counter(namespaces).most_common(1)
        if most_common:
            candidate = most_common[0][0]
            if len(candidate) > 7:
                return candidate

    return None


def clean_iri(iri: str) -> str:
    """
    Cleans an IRI by removing file extensions if they are part of the URL.
    Fixes: https://w3id.org/gaia-x/development/gaia-x.owl.ttl -> .../development/
    """
    if not iri:
        return iri

    lower_iri = iri.lower()
    for ext in [".ttl", ".owl", ".rdf", ".jsonld", ".json"]:
        if lower_iri.endswith(ext):
            return iri.rsplit("/", 1)[0] + "/"

    return iri


def determine_namespace_from_iri(iri: str) -> str:
    """Deduce a 'namespace' string from the IRI."""
    try:
        parsed = urlparse(iri)
        domain = parsed.netloc.lower()
        path_parts = [p for p in parsed.path.split("/") if p]

        if "w3id.org" in domain and path_parts:
            return path_parts[0]
        if "purl.org" in domain and path_parts:
            if path_parts[0] == "dc":
                return "dc"
            return path_parts[0]

        domain_parts = domain.split(".")
        if len(domain_parts) >= 2:
            return domain_parts[-2]

        return "external"
    except Exception:
        return "unknown"


def extract_ontology_info(owl_file: Path) -> Dict[str, Optional[str]]:
    """Extract semantic version, namespace, and IRI from ontology file."""

    # 0. Check KNOWN_IRIS fallback first
    if owl_file.name in KNOWN_IRIS:
        iri = KNOWN_IRIS[owl_file.name]
        g = None
    else:
        g = parse_graph(owl_file)
        iri = extract_iri_from_graph(g) if g else None

    # 1. Clean the IRI
    if iri:
        iri = clean_iri(iri)

    version = None
    namespace = "unknown"

    if iri:
        namespace = determine_namespace_from_iri(iri)

        if g:
            # Try owl:versionIRI
            for obj in g.objects(URIRef(iri), OWL.versionIRI):
                version = str(obj).split("/")[-1]
                break

            # Try owl:versionInfo
            if not version:
                for obj in g.objects(URIRef(iri), OWL.versionInfo):
                    v_str = str(obj).replace("Version ", "").strip()
                    version = v_str if v_str.startswith("v") else f"v{v_str}"
                    break

        if not version:
            import re

            match = re.search(r"/v([\d.]+)(?:/|$|#)", iri)
            if match:
                version = f"v{match.group(1)}"

        if not version:
            version = "v1"

    return {
        "version": version,
        "namespace": namespace,
        "iri": iri,
    }


def to_relative_str(
    path: Union[Path, List[Path]], start: Path = ROOT_DIR
) -> Union[str, List[str], None]:
    if path is None:
        return None
    if isinstance(path, list):
        return [str(p.relative_to(start)) for p in path]
    return str(path.relative_to(start))


def update_registry(release_tag: str, ontologies: Dict[str, dict]) -> dict:
    registry = load_existing_registry()
    old_registry_content = {k: v for k, v in registry.items() if k != "generated"}

    registry["version"] = REGISTRY_VERSION
    registry["latestRelease"] = release_tag

    if "base_ontologies" in registry:
        del registry["base_ontologies"]

    for domain, files in ontologies.items():
        owl_path = files["ontology"]
        info = extract_ontology_info(owl_path)

        if not info["iri"]:
            print(
                f"⚠️  Skipping {domain}: No valid IRI found in {owl_path.name}",
                file=sys.stderr,
            )
            continue

        if domain not in registry["ontologies"]:
            registry["ontologies"][domain] = {
                "namespace": info["namespace"],
                "iri": info["iri"],
                "latest": None,
                "versions": {},
            }

        onto_entry = registry["ontologies"][domain]
        onto_entry["namespace"] = info["namespace"]
        onto_entry["iri"] = info["iri"]

        version = info["version"]
        onto_entry["latest"] = version

        json_files = {
            "ontology": to_relative_str(files["ontology"]),
            "shacl": to_relative_str(files["shacl"]),
            "jsonld": to_relative_str(files["jsonld"]),
            "properties": to_relative_str(files["properties"]),
            "instance": to_relative_str(files["instance"]),
        }

        onto_entry["versions"][version] = {
            "releaseTag": release_tag,
            "files": {k: v for k, v in json_files.items() if v is not None},
        }

    new_registry_content = {k: v for k, v in registry.items() if k != "generated"}
    if new_registry_content != old_registry_content:
        registry["generated"] = datetime.now(timezone.utc).isoformat()

    return registry


def load_existing_registry() -> dict:
    if REGISTRY_PATH.exists():
        try:
            with REGISTRY_PATH.open("r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    return {"version": REGISTRY_VERSION, "ontologies": {}}


def write_registry(registry: dict) -> None:
    REGISTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    with REGISTRY_PATH.open("w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2, sort_keys=False)
        f.write("\n")
    print(f"✅ Registry updated: {REGISTRY_PATH}")


def extract_shacl_iri(shacl_file: Path) -> Optional[str]:
    g = parse_graph(shacl_file)
    if g:
        iri = extract_iri_from_graph(g)
        return clean_iri(iri) if iri else None
    return None


def generate_xml_catalog(
    ontologies: Dict[str, dict], registry: dict, target_catalog_path: Path
) -> str:
    catalog = ET.Element("catalog", xmlns="urn:oasis:names:tc:entity:xmlns:xml:catalog")
    catalog.append(
        ET.Comment(f" Auto-generated catalog for {target_catalog_path.parent.name} ")
    )

    uri_mappings = []

    for domain in sorted(ontologies.keys()):
        if domain not in registry["ontologies"]:
            continue

        iri = registry["ontologies"][domain].get("iri")
        if not iri:
            continue

        files = ontologies[domain]

        try:
            rel_path = os.path.relpath(files["ontology"], target_catalog_path.parent)
            uri_mappings.append((iri, rel_path))
        except ValueError:
            pass

        shacl_paths = files.get("shacl")
        if shacl_paths:
            for shacl_path in shacl_paths:
                shacl_iri = extract_shacl_iri(shacl_path)
                if shacl_iri:
                    try:
                        rel = os.path.relpath(shacl_path, target_catalog_path.parent)
                        uri_mappings.append((shacl_iri, rel))
                    except ValueError:
                        pass

        jsonld_path = files.get("jsonld")
        if jsonld_path:
            # FIX: Ensure we don't create double slashes by rstrip('/')
            context_iri = f"{iri.rstrip('/')}/context"
            try:
                rel = os.path.relpath(jsonld_path, target_catalog_path.parent)
                uri_mappings.append((context_iri, rel))
            except ValueError:
                pass

    uri_mappings.sort(key=lambda x: x[0])
    for iri, path in uri_mappings:
        uri_elem = ET.SubElement(catalog, "uri")
        uri_elem.set("name", iri)
        uri_elem.set("uri", path)

    return pretty_print_xml(catalog)


def pretty_print_xml(element: ET.Element) -> str:
    xml_str = ET.tostring(element, encoding="unicode")
    dom = minidom.parseString(xml_str)
    pretty_xml = dom.toprettyxml(indent="  ")
    lines = [line for line in pretty_xml.split("\n") if line.strip()]
    result_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<!DOCTYPE catalog PUBLIC "-//OASIS//DTD Entity Resolution XML Catalog V1.0//EN"',
        '  "http://www.oasis-open.org/committees/entity/release/1.0/catalog.dtd">',
    ]
    for line in lines:
        if not line.startswith("<?xml"):
            result_lines.append(line)
    return "\n".join(result_lines) + "\n"


def write_file(content: str, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Generated: {path}")


def discover_test_data() -> Dict[str, dict]:
    test_data = {}
    if not TESTS_DATA_DIR.exists():
        return test_data
    files = collect_jsonld_files(
        [TESTS_DATA_DIR], return_pathlib=True, warn_on_invalid=False
    )
    for test_file in files:
        try:
            with test_file.open("r", encoding="utf-8") as f:
                data = json.load(f)

            parts = test_file.parts
            try:
                data_idx = parts.index("data")
                domain = parts[data_idx + 1]
                test_type = parts[data_idx + 2]
            except (ValueError, IndexError):
                continue
            rel_path = test_file.relative_to(ROOT_DIR)

            def add_entry(tid, cat="test-data"):
                test_data[tid] = {
                    "path": str(rel_path),
                    "domain": domain,
                    "test_type": test_type,
                    "category": cat,
                }

            if "@graph" in data and isinstance(data["@graph"], list):
                for entity in data["@graph"]:
                    if entity.get("@id"):
                        add_entry(entity.get("@id"))
                if data.get("@id"):
                    add_entry(data.get("@id"))
            elif data.get("@id"):
                add_entry(data.get("@id"))
        except Exception:
            pass
    return test_data


def discover_fixtures() -> Dict[str, str]:
    fixtures = {}
    if not FIXTURES_DIR.exists():
        return fixtures
    files = collect_jsonld_files(
        [FIXTURES_DIR], return_pathlib=True, warn_on_invalid=False
    )
    for fixture_file in files:
        try:
            with fixture_file.open("r", encoding="utf-8") as f:
                data = json.load(f)
            iri = data.get("@id")
            if iri:
                fixtures[iri] = fixture_file.name
        except Exception:
            pass
    return fixtures


def generate_test_catalog(test_data: Dict[str, dict], fixtures: Dict[str, str]) -> str:
    catalog = ET.Element("catalog", xmlns="urn:oasis:names:tc:entity:xmlns:xml:catalog")
    catalog.append(ET.Comment("Unified Test Catalog"))
    entries = []
    for iri, filename in fixtures.items():
        entries.append(
            {
                "id": iri,
                "uri": f"tests/fixtures/{filename}",
                "domain": "fixture",
                "test-type": "fixture",
                "category": "fixture",
            }
        )
    for test_id, meta in test_data.items():
        entries.append(
            {
                "id": test_id,
                "uri": meta["path"],
                "domain": meta["domain"],
                "test-type": meta["test_type"],
                "category": meta["category"],
            }
        )
    entries.sort(key=lambda x: x["id"])
    for entry in entries:
        uri_elem = ET.SubElement(catalog, "uri")
        uri_elem.set("name", entry["id"])
        uri_elem.set("uri", entry["uri"])
        uri_elem.set("domain", entry["domain"])
        uri_elem.set("test-type", entry["test-type"])
        uri_elem.set("category", entry["category"])
    return pretty_print_xml(catalog)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--release-tag", "-r", default="main")
    parser.add_argument("--dry-run", "-n", action="store_true")
    args = parser.parse_args()

    print(f"🔧 Using RDF store: {FAST_STORE}")

    print("🔍 Scanning artifacts/...")
    domain_ontologies = collect_ontology_bundles(ARTIFACTS_DIR, TESTS_DATA_DIR)

    print("🔍 Scanning imports/...")
    base_ontologies = collect_ontology_bundles(IMPORTS_DIR)

    all_ontologies = {**domain_ontologies, **base_ontologies}

    print(f"📝 Updating registry.json (processing {len(all_ontologies)} domains)...")
    registry = update_registry(args.release_tag, all_ontologies)

    print("📋 Generating XML catalogs...")
    artifacts_xml = generate_xml_catalog(
        domain_ontologies, registry, ARTIFACTS_CATALOG_PATH
    )
    imports_xml = generate_xml_catalog(base_ontologies, registry, IMPORTS_CATALOG_PATH)

    print("🔍 Discovering test data & fixtures...")
    test_data = discover_test_data()
    fixtures = discover_fixtures()
    test_catalog_xml = generate_test_catalog(test_data, fixtures)

    if args.dry_run:
        print(json.dumps(registry, indent=2))
        print(artifacts_xml)
        print(imports_xml)
        print(test_catalog_xml[:500] + "...")
    else:
        write_registry(registry)
        write_file(artifacts_xml, ARTIFACTS_CATALOG_PATH)
        write_file(imports_xml, IMPORTS_CATALOG_PATH)
        write_file(test_catalog_xml, TEST_CATALOG_PATH)
        print("\n✅ Update complete!")


if __name__ == "__main__":
    main()
