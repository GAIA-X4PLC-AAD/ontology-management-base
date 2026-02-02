#!/usr/bin/env python3
"""
Registry Update Script for Ontology Management Base.

This script generates/updates:
  1. docs/registry.json - Maps ontology domains to their artifact locations
  2. artifacts/catalog-v001.xml - OASIS XML Catalog for ontology resolution
  3. tests/catalog-v001.xml - Unified test catalog (test data + fixtures)

Usage:
    python -m src.tools.utils.registry_updater [--release-tag TAG]

The script scans artifacts/ to discover ontologies and their files,
and tests/fixtures/ to discover test fixture references, then updates
the registry and catalogs with current metadata.

After restructuring, artifacts are organized as:
    artifacts/{ontology}/{ontology}.owl.ttl
    artifacts/{ontology}/{ontology}.shacl.ttl
    artifacts/{ontology}/{ontology}.context.jsonld
    artifacts/{ontology}/PROPERTIES.md

Test fixtures are organized as:
    tests/fixtures/{fixture_name}.json (with @id field for IRI mapping)
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Optional
from xml.dom import minidom
from xml.etree import ElementTree as ET

# Constants
# Navigate from src/tools/utils/registry_updater.py up 4 levels to repo root
ROOT_DIR = Path(__file__).parent.parent.parent.parent.resolve()
ARTIFACTS_DIR = ROOT_DIR / "artifacts"
TESTS_DATA_DIR = ROOT_DIR / "tests" / "data"
FIXTURES_DIR = ROOT_DIR / "tests" / "fixtures"
IMPORTS_DIR = ROOT_DIR / "imports"
REGISTRY_PATH = ROOT_DIR / "docs" / "registry.json"
CATALOG_PATH = ROOT_DIR / "artifacts" / "catalog-v001.xml"
TEST_CATALOG_PATH = ROOT_DIR / "tests" / "catalog-v001.xml"
IMPORTS_CATALOG_PATH = ROOT_DIR / "imports" / "catalog-v001.xml"

REGISTRY_VERSION = "2.0.0"  # Bumped for new structure


def discover_ontologies() -> Dict[str, dict]:
    """
    Discover ontology domains by scanning the artifacts directory.

    New structure (post-restructuring):
        artifacts/
        ├── {ontology}/
        │   ├── {ontology}.owl.ttl
        │   ├── {ontology}.shacl.ttl (optional)
        │   ├── {ontology}.context.jsonld (optional)
        │   └── PROPERTIES.md (auto-generated)

    Returns a dict mapping domain names to their file paths.
    """
    ontologies = {}

    if not ARTIFACTS_DIR.exists():
        print(
            f"Warning: artifacts directory not found: {ARTIFACTS_DIR}", file=sys.stderr
        )
        return ontologies

    # Find all ontology directories (artifacts/<ontology>/)
    for ont_dir in sorted(ARTIFACTS_DIR.iterdir()):
        if not ont_dir.is_dir():
            continue

        domain = ont_dir.name

        # Look for ontology file: artifacts/<ontology>/<ontology>.owl.ttl
        owl_file = ont_dir / f"{domain}.owl.ttl"
        if not owl_file.exists():
            continue

        # Find SHACL files: artifacts/<ontology>/*.shacl.ttl
        # Support multiple SHACL files per domain (e.g., survey)
        shacl_files = sorted(ont_dir.glob("*.shacl.ttl"))

        # Find JSON-LD context: artifacts/<ontology>/<ontology>.context.jsonld
        jsonld_file = ont_dir / f"{domain}.context.jsonld"

        # Find properties documentation: artifacts/<ontology>/PROPERTIES.md
        properties_file = ont_dir / "PROPERTIES.md"

        # Find instance file(s) from tests
        valid_dir = TESTS_DATA_DIR / domain / "valid"
        instance_file = None
        if valid_dir.exists():
            # Look for primary instance file
            for pattern in [f"{domain}_instance.json", "*_instance.json"]:
                matches = list(valid_dir.glob(pattern))
                if matches:
                    instance_file = matches[0]
                    break

        ontologies[domain] = {
            "ontology": str(owl_file.relative_to(ROOT_DIR)),
            "shacl": (
                [str(f.relative_to(ROOT_DIR)) for f in shacl_files]
                if shacl_files
                else None
            ),
            "jsonld": (
                str(jsonld_file.relative_to(ROOT_DIR)) if jsonld_file.exists() else None
            ),
            "properties": (
                str(properties_file.relative_to(ROOT_DIR))
                if properties_file.exists()
                else None
            ),
            "instance": (
                str(instance_file.relative_to(ROOT_DIR)) if instance_file else None
            ),
        }

    return ontologies


def extract_ontology_info(owl_file: Path) -> Dict[str, Optional[str]]:
    """
    Extract semantic version and namespace from ontology file.

    Handles special cases:
      - gx: Uses prefix-based IRI without version in @prefix
      - openlabel: Uses @base with ASAM URL instead of w3id.org

    Returns dict with:
        - version: e.g., "v2", "v1.0.0"
        - namespace: e.g., "gaia-x4plcaad" or "ascs-ev/envited-x"
        - iri: full ontology IRI if found
    """
    try:
        content = owl_file.read_text(encoding="utf-8")

        version = None
        namespace = None
        iri = None

        # Special case 1: openlabel - Extract from @base directive
        # Pattern: @base <https://openlabel.asam.net/V1-0-0/ontologies/> .
        if not iri:
            base_pattern = r"@base\s+<(https?://openlabel\.asam\.net/[^>]+)>"
            match = re.search(base_pattern, content)
            if match:
                iri = match.group(1).rstrip(
                    "/"
                )  # Remove trailing slash for consistency
                namespace = "asam-openlabel"

        # Special case 2: gx - Extract from @prefix declaration (ONLY for gx.owl.ttl)
        # Many ontologies use gx: prefix, so we must check the filename to avoid false matches
        # Pattern: @prefix gx: <https://w3id.org/gaia-x/development/> .
        if not iri and owl_file.name == "gx.owl.ttl":
            gx_prefix_pattern = (
                r"@prefix\s+gx:\s+<(https?://w3id\.org/gaia-x/development/)>"
            )
            match = re.search(gx_prefix_pattern, content)
            if match:
                iri = match.group(1).rstrip("/")  # Remove trailing slash
                namespace = "gaia-x"

        # Standard case: Look for ontology IRI patterns with version and namespace
        # e.g., https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2
        # e.g., https://w3id.org/ascs-ev/envited-x/core/v1.0
        # e.g., https://w3id.org/gaia-x4plcaad/ontologies/description/v1
        if not iri:
            # Pattern matches w3id.org IRIs that contain version numbers (v followed by digits)
            iri_pattern = r"<(https?://w3id\.org/([^/]+)/.*?v[\d.]+)"
            match = re.search(iri_pattern, content)
            if match:
                iri = match.group(1)
                # Extract namespace (e.g., "gaia-x4plcaad" or "ascs-ev")
                namespace_part = match.group(2)
                namespace = namespace_part

        # Also look for owl:versionInfo
        version_pattern = r'owl:versionInfo\s+"v?([\d.]+)"'
        match = re.search(version_pattern, content)
        if match:
            ver = match.group(1)
            # Normalize to vN format
            version = f"v{ver.split('.')[0]}"
        elif iri:
            # Extract version from IRI
            v_match = re.search(r"/v([\d.]+)(?:/|>)", iri)
            if v_match:
                version = f"v{v_match.group(1).split('.')[0]}"

        # Default to v1 if no version found
        if not version:
            version = "v1"
        if not namespace:
            namespace = "unknown"

        return {
            "version": version,
            "namespace": namespace,
            "iri": iri,
        }
    except Exception as e:
        print(f"Warning: Error extracting info from {owl_file}: {e}", file=sys.stderr)
        return {
            "version": "v1",
            "namespace": "unknown",
            "iri": None,
        }


def load_existing_registry() -> dict:
    """Load existing registry or return empty structure."""
    if REGISTRY_PATH.exists():
        try:
            with REGISTRY_PATH.open("r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass

    return {
        "version": REGISTRY_VERSION,
        "generated": None,
        "latestRelease": None,
        "namespaces": {
            "gaia-x4plcaad": "https://w3id.org/gaia-x4plcaad/ontologies/",
            "ascs-ev": "https://w3id.org/ascs-ev/",
        },
        "ontologies": {},
    }


def update_registry(
    release_tag: str, ontologies: Dict[str, dict], base_ontologies: list[str] = None
) -> dict:
    """
    Update registry with new release information.
    Preserves historical versions while adding new mappings.

    Args:
        release_tag: Git release tag
        ontologies: Dict of discovered ontologies
        base_ontologies: List of base ontology paths from imports/
    """
    registry = load_existing_registry()

    # Store old registry state (excluding generated timestamp) to detect changes
    old_registry_content = {k: v for k, v in registry.items() if k != "generated"}

    # Update metadata
    registry["version"] = REGISTRY_VERSION
    # Note: generated timestamp will be updated later only if there are changes
    registry["latestRelease"] = release_tag

    # Add base ontologies if provided
    if base_ontologies is not None:
        registry["base_ontologies"] = base_ontologies

    # Update each ontology
    for domain, files in ontologies.items():
        # Extract ontology info
        owl_path = ROOT_DIR / files["ontology"]
        info = extract_ontology_info(owl_path)

        if domain not in registry["ontologies"]:
            registry["ontologies"][domain] = {
                "namespace": info["namespace"],
                "iri": info["iri"],
                "latest": None,
                "versions": {},
            }

        onto_entry = registry["ontologies"][domain]

        # Update with latest info
        onto_entry["namespace"] = info["namespace"]
        if info["iri"]:
            onto_entry["iri"] = info["iri"]

        version = info["version"]

        # Update latest version
        onto_entry["latest"] = version

        # Add or update version entry
        onto_entry["versions"][version] = {
            "releaseTag": release_tag,
            "files": {
                "ontology": files["ontology"],
                "shacl": files["shacl"],
                "jsonld": files["jsonld"],
                "properties": files["properties"],
                "instance": files["instance"],
            },
        }

    # Check if registry content has changed (excluding generated timestamp)
    new_registry_content = {k: v for k, v in registry.items() if k != "generated"}

    # Only update timestamp if there are actual content changes
    if new_registry_content != old_registry_content:
        registry["generated"] = datetime.now(timezone.utc).isoformat()
    # else: keep the old timestamp

    return registry


def write_registry(registry: dict) -> None:
    """Write registry to file."""
    # Ensure docs directory exists
    REGISTRY_PATH.parent.mkdir(parents=True, exist_ok=True)

    with REGISTRY_PATH.open("w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2, sort_keys=False)
        f.write("\n")

    print(f"✅ Registry updated: {REGISTRY_PATH}")

    # Print summary
    ontologies = registry.get("ontologies", {})
    print(f"   Total ontologies: {len(ontologies)}")
    if ontologies:
        print("   Ontologies:")
        for domain in sorted(ontologies.keys()):
            ver = ontologies[domain].get("latest", "v?")
            ns = ontologies[domain].get("namespace", "?")
            print(f"     - {domain}: {ver} ({ns})")


def extract_shacl_iri(shacl_file: Path) -> Optional[str]:
    """
    Extract SHACL shapes graph IRI from SHACL file.

    Looks for pattern:
      <https://w3id.org/.../v5/shapes/> a owl:Ontology ;
      or with rdf:type:
      <https://w3id.org/.../v5/shapes/>
          rdf:type owl:Ontology ;

    Returns the IRI or None if not found.
    """
    try:
        content = shacl_file.read_text(encoding="utf-8")
        # Match SHACL shapes IRI pattern (ends with /shapes/ or /shapes)
        # Allow for whitespace including newlines and both 'a' and 'rdf:type'
        match = re.search(
            r"<(https?://[^>]+/shapes/??)>\s+(?:a|rdf:type)\s+owl:Ontology",
            content,
            re.DOTALL,
        )
        if match:
            return match.group(1)
    except Exception:
        pass
    return None


def generate_catalog(ontologies: Dict[str, dict], registry: dict) -> str:
    """
    Generate OASIS XML Catalog for ontology resolution.

    Maps THREE types of IRIs to local files:
      1. Ontology IRIs → {ontology}.owl.ttl
      2. SHACL shapes IRIs → {ontology}.shacl.ttl (if exists)
      3. Context IRIs → {ontology}.context.jsonld (if exists)

    Enables Protégé/OWLAPI to resolve ontologies locally during reasoning.
    URI entries are sorted alphabetically by name= for consistency.

    Returns the formatted XML string.
    """
    # Create root catalog element
    catalog = ET.Element("catalog", xmlns="urn:oasis:names:tc:entity:xmlns:xml:catalog")

    # Add header comment
    comment = ET.Comment(
        "OASIS XML Catalog for Local Ontology Resolution\n"
        "    Maps maintained ontology IRIs to local artifact files\n"
        "    Includes ontologies, SHACL shapes, and JSON-LD contexts\n"
        "    Auto-generated by utils/registry_updater.py - do not edit manually"
    )
    catalog.append(comment)

    # Collect all URI mappings first (as tuples of name, uri_path)
    uri_mappings = []

    # Add URI mappings for each ontology
    for domain in sorted(ontologies.keys()):
        onto_entry = registry["ontologies"][domain]
        iri = onto_entry.get("iri")

        if not iri:
            continue

        onto_dir = domain

        # 1. Map Ontology IRI → OWL file
        owl_filename = f"{domain}.owl.ttl"
        owl_relative_path = f"{onto_dir}/{owl_filename}"
        uri_mappings.append((iri, owl_relative_path))

        # 2. Map SHACL Shapes IRIs → SHACL files (if exist)
        # Support multiple SHACL files per domain
        shacl_paths = ontologies[domain].get("shacl")
        if shacl_paths:
            # Handle both single file and list of files
            if not isinstance(shacl_paths, list):
                shacl_paths = [shacl_paths]

            for shacl_path in shacl_paths:
                # Extract SHACL IRI from file
                shacl_file = ROOT_DIR / shacl_path
                shacl_iri = extract_shacl_iri(shacl_file)

                if shacl_iri:
                    shacl_filename = shacl_file.name
                    shacl_relative_path = f"{onto_dir}/{shacl_filename}"
                    uri_mappings.append((shacl_iri, shacl_relative_path))

        # 3. Map Context IRI → JSON-LD context file (if exists)
        jsonld_path = ontologies[domain].get("jsonld")
        if jsonld_path:
            # Generate context IRI from ontology IRI with /context suffix
            context_iri = f"{iri}/context"
            jsonld_filename = f"{domain}.context.jsonld"
            jsonld_relative_path = f"{onto_dir}/{jsonld_filename}"
            uri_mappings.append((context_iri, jsonld_relative_path))

    # Sort URI mappings alphabetically by name (IRI)
    uri_mappings.sort(key=lambda x: x[0])

    # Add sorted URI elements to catalog
    for iri, uri_path in uri_mappings:
        uri_elem = ET.SubElement(catalog, "uri")
        uri_elem.set("name", iri)
        uri_elem.set("uri", uri_path)

    # Format XML with proper indentation and declaration
    xml_str = ET.tostring(catalog, encoding="unicode")

    # Parse and pretty-print
    dom = minidom.parseString(xml_str)
    pretty_xml = dom.toprettyxml(indent="  ", encoding="UTF-8")

    # Decode and remove extra blank lines
    pretty_str = (
        pretty_xml.decode("utf-8") if isinstance(pretty_xml, bytes) else pretty_xml
    )

    # Add XML declaration and DOCTYPE
    xml_lines = pretty_str.split("\n")
    result_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<!DOCTYPE catalog PUBLIC "-//OASIS//DTD Entity Resolution XML Catalog V1.0//EN"',
        '  "http://www.oasis-open.org/committees/entity/release/1.0/catalog.dtd">',
    ]

    # Add the catalog element (skip the duplicate XML declaration from minidom)
    for line in xml_lines:
        if line.startswith("<?xml") or line.startswith("<!DOCTYPE"):
            continue
        if line.strip():
            result_lines.append(line)

    return "\n".join(result_lines) + "\n"


def write_catalog(catalog_xml: str) -> None:
    """Write XML catalog to file."""
    # Ensure artifacts directory exists
    CATALOG_PATH.parent.mkdir(parents=True, exist_ok=True)

    with CATALOG_PATH.open("w", encoding="utf-8") as f:
        f.write(catalog_xml)

    print(f"✅ Catalog generated: {CATALOG_PATH}")


def discover_fixtures() -> Dict[str, str]:
    """
    Discover fixture files and extract their IRIs.

    Scans tests/fixtures/ for JSON-LD files and extracts the @id field
    from each file to create IRI → filename mappings.

    Returns:
        Dict mapping fixture IRI to relative filename
    """
    fixtures = {}

    if not FIXTURES_DIR.exists():
        print(f"⚠️  Warning: fixtures directory not found: {FIXTURES_DIR}")
        return fixtures

    # Find all JSON files in fixtures directory
    for fixture_file in sorted(FIXTURES_DIR.glob("*.json")):
        try:
            with fixture_file.open("r", encoding="utf-8") as f:
                data = json.load(f)

            # Extract @id field
            iri = data.get("@id")
            if iri:
                # Store relative filename (just the basename)
                fixtures[iri] = fixture_file.name
            else:
                print(f"⚠️  Warning: No @id found in {fixture_file.name}")

        except Exception as e:
            print(f"⚠️  Warning: Could not parse {fixture_file.name}: {e}")

    return fixtures


def discover_base_ontologies() -> list[str]:
    """
    Discover base ontologies from imports/catalog-v001.xml.

    Reads the imports catalog to find all registered base ontologies
    (RDF, RDFS, OWL, SKOS, etc.) and returns their file paths.

    Returns:
        List of repository-relative paths to base ontology files
    """
    base_ontologies = []

    if not IMPORTS_CATALOG_PATH.exists():
        print(f"⚠️  Warning: imports catalog not found: {IMPORTS_CATALOG_PATH}")
        return base_ontologies

    try:
        tree = ET.parse(IMPORTS_CATALOG_PATH)
        root = tree.getroot()
        ns = {"cat": "urn:oasis:names:tc:entity:xmlns:xml:catalog"}

        # Extract all URI mappings from the catalog
        for uri_elem in root.findall("cat:uri", ns):
            relative_path = uri_elem.get("uri")
            if relative_path:
                # Convert to repository-relative path
                repo_relative = f"imports/{relative_path}"
                # Verify file exists
                if (ROOT_DIR / repo_relative).exists():
                    base_ontologies.append(repo_relative)

        # Also try without namespace prefix (for backward compatibility)
        if not base_ontologies:
            for uri_elem in root.findall("uri"):
                relative_path = uri_elem.get("uri")
                if relative_path:
                    repo_relative = f"imports/{relative_path}"
                    if (ROOT_DIR / repo_relative).exists():
                        base_ontologies.append(repo_relative)

    except Exception as e:
        print(f"⚠️  Warning: Could not parse imports catalog: {e}")

    return sorted(base_ontologies)


def discover_test_data() -> Dict[str, dict]:
    """
    Discover test data files and extract their metadata.

    Scans tests/data/ for JSON-LD files organized as:
      tests/data/{domain}/{valid|invalid}/*.json

    Supports both flat structure and @graph structure:
      - Flat: Single entity with @id at root level
      - @graph: Multiple entities in @graph array, plus optional document @id

    For @graph files, creates catalog entries for:
      - Each entity within the @graph array (by their @id)
      - The document itself (by root @id, if present)

    Returns:
        Dict mapping test @id to metadata (path, domain, test_type)
    """
    test_data = {}

    if not TESTS_DATA_DIR.exists():
        print(f"⚠️  Warning: tests/data directory not found: {TESTS_DATA_DIR}")
        return test_data

    # Find all JSON files in test data directory
    for test_file in sorted(TESTS_DATA_DIR.rglob("*.json")):
        try:
            with test_file.open("r", encoding="utf-8") as f:
                data = json.load(f)

            # Extract metadata from path
            parts = test_file.parts
            data_idx = parts.index("data")
            domain = parts[data_idx + 1]
            test_type = parts[data_idx + 2]  # "valid" or "invalid"

            # Store relative to repo root
            rel_path = test_file.relative_to(ROOT_DIR)

            # Check if file uses @graph structure (named graph with multiple entities)
            if "@graph" in data and isinstance(data["@graph"], list):
                entity_count = 0

                # Index each entity in the graph by its @id
                for entity in data["@graph"]:
                    entity_id = entity.get("@id")
                    if entity_id:
                        test_data[entity_id] = {
                            "path": str(rel_path),
                            "domain": domain,
                            "test_type": test_type,
                            "category": "test-data",
                        }
                        entity_count += 1

                # Also index the document/graph itself if it has a root @id
                doc_id = data.get("@id")
                if doc_id:
                    test_data[doc_id] = {
                        "path": str(rel_path),
                        "domain": domain,
                        "test_type": test_type,
                        "category": "test-data",
                    }
                    entity_count += 1

                if entity_count == 0:
                    print(
                        f"⚠️  Warning: @graph present but no @id found in {test_file.name}"
                    )
            else:
                # Flat structure - single entity with @id at root
                test_id = data.get("@id")
                if not test_id:
                    print(f"⚠️  Warning: No @id found in {test_file.name}")
                    continue

                test_data[test_id] = {
                    "path": str(rel_path),
                    "domain": domain,
                    "test_type": test_type,
                    "category": "test-data",
                }

        except Exception as e:
            print(f"⚠️  Warning: Could not parse {test_file.name}: {e}")

    return test_data


def generate_test_catalog(test_data: Dict[str, dict], fixtures: Dict[str, str]) -> str:
    """
    Generate unified test catalog including both test data and fixtures.

    Args:
        test_data: Dict mapping test @id to metadata
        fixtures: Dict mapping fixture @id to relative filename

    Returns:
        The formatted XML string
    """
    # Create root catalog element
    catalog = ET.Element("catalog", xmlns="urn:oasis:names:tc:entity:xmlns:xml:catalog")

    # Add header comment
    comment = ET.Comment(
        "\n"
        "    Unified Test Catalog for Ontology Management Base\n"
        "    \n"
        "    This catalog maps test instance did:web IRIs to local files.\n"
        "    Includes both test data (valid/invalid) and test fixtures.\n"
        "    \n"
        "    Structure:\n"
        "    - Test Data: tests/data/{domain}/{valid|invalid}/*.json\n"
        "    - Test Fixtures: tests/fixtures/*.json\n"
        "    \n"
        "    Auto-generated by registry_updater.py - do not edit manually\n"
        "  "
    )
    catalog.append(comment)

    # Collect all entries
    entries = []

    # Add fixtures
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

    # Add test data
    for test_id, metadata in test_data.items():
        entries.append(
            {
                "id": test_id,
                "uri": metadata["path"],
                "domain": metadata["domain"],
                "test-type": metadata["test_type"],
                "category": metadata["category"],
            }
        )

    # Sort entries by ID for consistency
    entries.sort(key=lambda x: x["id"])

    # Add URI elements with metadata
    for entry in entries:
        uri_elem = ET.SubElement(catalog, "uri")
        uri_elem.set("name", entry["id"])
        uri_elem.set("uri", entry["uri"])
        uri_elem.set("domain", entry["domain"])
        uri_elem.set("test-type", entry["test-type"])
        uri_elem.set("category", entry["category"])

    # Format XML with proper indentation
    xml_str = ET.tostring(catalog, encoding="unicode")
    dom = minidom.parseString(xml_str)
    pretty_xml = dom.toprettyxml(indent="  ")

    # Clean up extra whitespace and build final output
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


def write_test_catalog(catalog_xml: str) -> None:
    """Write unified test catalog to file."""
    TEST_CATALOG_PATH.parent.mkdir(parents=True, exist_ok=True)

    with TEST_CATALOG_PATH.open("w", encoding="utf-8") as f:
        f.write(catalog_xml)

    print(f"✅ Test catalog generated: {TEST_CATALOG_PATH}")


def main():
    parser = argparse.ArgumentParser(
        description="Update ontology registry and catalog for w3id resolution and artifact discovery."
    )
    parser.add_argument(
        "--release-tag",
        "-r",
        default="main",
        help="Git release tag (e.g., v0.0.5). Default: main",
    )
    parser.add_argument(
        "--dry-run",
        "-n",
        action="store_true",
        help="Print registry and catalog without writing.",
    )

    args = parser.parse_args()

    # Discover ontologies
    print("🔍 Discovering ontologies from artifacts/...")
    ontologies = discover_ontologies()

    if not ontologies:
        print("❌ Error: No ontologies found in artifacts/", file=sys.stderr)
        sys.exit(1)

    print(
        f"✅ Found {len(ontologies)} ontologies: {', '.join(sorted(ontologies.keys()))}"
    )

    # Discover base ontologies from imports catalog
    print("🔍 Discovering base ontologies from imports/catalog-v001.xml...")
    base_ontologies = discover_base_ontologies()
    print(f"✅ Found {len(base_ontologies)} base ontologies")

    # Update registry
    print(f"📝 Updating registry with release tag: {args.release_tag}")
    registry = update_registry(args.release_tag, ontologies, base_ontologies)

    # Generate catalog
    print("📋 Generating XML catalog for ontology resolution...")
    catalog_xml = generate_catalog(ontologies, registry)

    # Discover test data
    print("🔍 Discovering test data from tests/data/...")
    test_data = discover_test_data()
    print(f"✅ Found {len(test_data)} test data files")

    # Discover fixtures
    print("🔍 Discovering test fixtures from tests/fixtures/...")
    fixtures = discover_fixtures()
    print(
        f"✅ Found {len(fixtures)} fixtures: {', '.join(sorted(Path(f).stem for f in fixtures.values()))}"
    )

    # Generate unified test catalog
    print("📋 Generating unified test catalog (data + fixtures)...")
    test_catalog_xml = generate_test_catalog(test_data, fixtures)

    if args.dry_run:
        print("\n--- Registry (dry run) ---")
        print(json.dumps(registry, indent=2))
        print("\n--- Catalog (dry run) ---")
        print(catalog_xml)
        print("\n--- Test Catalog (dry run) ---")
        print(test_catalog_xml[:1000] + "...")
    else:
        write_registry(registry)
        write_catalog(catalog_xml)
        write_test_catalog(test_catalog_xml)
        print("\n✅ Update complete!")


if __name__ == "__main__":
    main()
