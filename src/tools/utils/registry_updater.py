#!/usr/bin/env python3
"""
Registry Update Script for Ontology Management Base.

This script generates/updates:
  1. docs/registry.json - Maps maintained ontology domains (artifacts only)
  2. artifacts/catalog-v001.xml - OASIS XML Catalog for domain ontologies
  3. imports/catalog-v001.xml - OASIS XML Catalog for base ontologies
  4. tests/catalog-v001.xml - Unified test catalog (test data + fixtures)
  5. config/ontoenv.toml - Ontology environment config (derived from catalogs)

Usage:
    python -m src.tools.utils.registry_updater [--release-tag TAG] [--dry-run]
"""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Union
from urllib.parse import urlparse
from xml.dom import minidom
from xml.etree import ElementTree as ET

# TOML reader (stdlib in Python 3.11+)
try:
    import tomllib
except ImportError:  # pragma: no cover - fallback for older Pythons
    import tomli as tomllib

# Import RDFLib
import rdflib
from rdflib import OWL, RDF, URIRef
from rdflib.namespace import RDFS, SKOS

# Import from core
from src.tools.core.constants import FAST_STORE
from src.tools.core.logging import get_logger
from src.tools.utils.file_collector import (
    collect_jsonld_files,
    collect_ontology_bundles,
)

logger = get_logger(__name__)

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
ONTOENV_PATH = ROOT_DIR / "config" / "ontoenv.toml"

REGISTRY_VERSION = "2.1.0"

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
        logger.warning("Could not parse %s: %s", file_path.name, e)
        return None


def extract_iri_from_graph(g: rdflib.Graph) -> Optional[str]:
    """
    Robustly identify the Ontology IRI from a graph.
    DETERMINISTIC: Sorts candidates and picks the shortest one to avoid
    picking sub-modules (like prov-links) over the main ontology (prov).
    """
    candidates = []

    # 1. Look for owl:Ontology
    for s in g.subjects(RDF.type, OWL.Ontology):
        if isinstance(s, URIRef):
            candidates.append(str(s))

    if candidates:
        # Sort by length first (shortest first), then alphabetically
        # This ensures 'http://www.w3.org/ns/prov#' (len 24) wins over
        # 'http://www.w3.org/ns/prov-links#' (len 30)
        candidates.sort(key=lambda x: (len(x), x))
        return candidates[0]

    # 2. Look for skos:ConceptScheme (fallback)
    for s in g.subjects(RDF.type, SKOS.ConceptScheme):
        if isinstance(s, URIRef):
            return str(s)

    # 3. No IRI found
    return None


def clean_iri(iri: str) -> str:
    """
    Cleans an IRI by removing file extensions if they are part of the URL.
    Fixes: https://w3id.org/gaia-x/development#gaia-x.owl.ttl -> .../development#
    """
    if not iri:
        return iri

    lower_iri = iri.lower()
    if "#" in iri:
        base, fragment = iri.split("#", 1)
        fragment_lower = fragment.lower()
        for ext in [".ttl", ".owl", ".rdf", ".jsonld", ".json"]:
            if fragment_lower.endswith(ext):
                return f"{base}#"
        return iri

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


def _normalize_version_info(value: str) -> str:
    cleaned = value.replace("Version ", "").strip()
    return cleaned if cleaned.startswith("v") else f"v{cleaned}"


def _extract_label_from_graph(g: rdflib.Graph, subject_iri: str) -> Optional[str]:
    labels = list(g.objects(URIRef(subject_iri), RDFS.label))
    if not labels:
        return None
    for label in labels:
        if getattr(label, "language", None) == "en":
            return str(label)
    return str(labels[0])


def extract_ontology_info(owl_file: Path) -> Dict[str, Optional[str]]:
    """Extract version info, namespace, and IRIs from an ontology file."""
    g = parse_graph(owl_file)
    raw_iri = extract_iri_from_graph(g) if g else None

    if not raw_iri and owl_file.name in KNOWN_IRIS:
        raw_iri = KNOWN_IRIS[owl_file.name]

    cleaned_iri = clean_iri(raw_iri) if raw_iri else None
    namespace = determine_namespace_from_iri(cleaned_iri) if cleaned_iri else "unknown"

    version_info = None
    version_iri = None
    label = None

    if g and raw_iri:
        for obj in g.objects(URIRef(raw_iri), OWL.versionIRI):
            version_iri = clean_iri(str(obj))
            break

        for obj in g.objects(URIRef(raw_iri), OWL.versionInfo):
            version_info = _normalize_version_info(str(obj))
            break

        label = _extract_label_from_graph(g, raw_iri)

    return {
        "version": version_info,
        "versionInfo": version_info,
        "versionIri": version_iri,
        "namespace": namespace,
        "iri": cleaned_iri,
        "label": label,
    }


def extract_dependency_info(owl_file: Path) -> Dict[str, Optional[str]]:
    """Extract base ontology dependency info (IRI + label)."""
    g = parse_graph(owl_file)
    raw_iri = extract_iri_from_graph(g) if g else None

    if not raw_iri and owl_file.name in KNOWN_IRIS:
        raw_iri = KNOWN_IRIS[owl_file.name]

    cleaned_iri = clean_iri(raw_iri) if raw_iri else None
    label = _extract_label_from_graph(g, raw_iri) if g and raw_iri else None

    return {
        "iri": cleaned_iri,
        "label": label,
    }


def to_relative_str(
    path: Union[Path, List[Path]], start: Path = ROOT_DIR
) -> Union[str, List[str], None]:
    """Convert path(s) to POSIX-style relative path strings."""
    if path is None:
        return None
    if isinstance(path, list):
        return [p.relative_to(start).as_posix() for p in path]
    return path.relative_to(start).as_posix()


def to_posix_relative(file_path: Path, base_path: Path) -> str:
    """
    Convert a file path to a POSIX-style relative path string.

    Uses pathlib for cross-platform compatibility. The result uses forward
    slashes regardless of the OS, which is required for XML catalogs.

    Args:
        file_path: Absolute path to the file
        base_path: Base directory to compute relative path from

    Returns:
        POSIX-style relative path string (e.g., "domain/file.ttl")
    """
    return file_path.relative_to(base_path).as_posix()


def update_registry(release_tag: str, ontologies: Dict[str, dict]) -> dict:
    existing = load_existing_registry()
    old_registry_content = {k: v for k, v in existing.items() if k != "generated"}

    registry = {
        "version": REGISTRY_VERSION,
        "latestRelease": release_tag,
        "ontologies": {},
    }

    for domain, files in sorted(ontologies.items()):
        owl_path = files["ontology"]
        info = extract_ontology_info(owl_path)

        if not info["iri"]:
            logger.warning(
                "Skipping %s: No valid IRI found in %s", domain, owl_path.name
            )
            continue

        if not info["versionInfo"]:
            logger.warning(
                "Skipping %s: owl:versionInfo missing in %s", domain, owl_path.name
            )
            continue

        if not info["versionIri"]:
            logger.warning(
                "owl:versionIRI missing in %s; using ontology IRI as version IRI",
                owl_path.name,
            )
            info["versionIri"] = info["iri"]

        onto_entry = {
            "namespace": info["namespace"],
            "iri": info["iri"],
            "latest": info["versionInfo"],
            "versions": {},
        }

        json_files = {
            "ontology": to_relative_str(files["ontology"]),
            "shacl": to_relative_str(files["shacl"]),
            "jsonld": to_relative_str(files["jsonld"]),
            "properties": to_relative_str(files["properties"]),
            "instance": to_relative_str(files["instance"]),
        }

        onto_entry["versions"][info["versionInfo"]] = {
            "releaseTag": release_tag,
            "versionInfo": info["versionInfo"],
            "versionIri": info["versionIri"],
            "files": {k: v for k, v in json_files.items() if v is not None},
        }

        registry["ontologies"][domain] = onto_entry

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


def _normalize_line_endings(content: str) -> str:
    """Normalize line endings to LF for consistent comparison."""
    return content.replace("\r\n", "\n").replace("\r", "\n")


def write_registry(registry: dict) -> None:
    """Write registry to file only if content has changed."""
    REGISTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    new_content = json.dumps(registry, indent=2, sort_keys=False) + "\n"

    # Check if content has changed (normalize line endings for cross-platform)
    if REGISTRY_PATH.exists():
        existing_content = REGISTRY_PATH.read_text(encoding="utf-8")
        if _normalize_line_endings(existing_content) == _normalize_line_endings(
            new_content
        ):
            logger.info("Registry unchanged: %s", REGISTRY_PATH.as_posix())
            return

    with REGISTRY_PATH.open("w", encoding="utf-8", newline="\n") as f:
        f.write(new_content)
    logger.info("Registry updated: %s", REGISTRY_PATH.as_posix())


def extract_shacl_iri(shacl_file: Path) -> Optional[str]:
    g = parse_graph(shacl_file)
    if g:
        iri = extract_iri_from_graph(g)
        return clean_iri(iri) if iri else None
    return None


def build_shapes_iri(ontology_iri: str) -> str:
    """Build a SHACL namespace IRI from an ontology namespace IRI."""
    if ontology_iri.endswith("#"):
        return f"{ontology_iri}shapes"
    return f"{ontology_iri.rstrip('/')}/shapes"


def build_context_iri(ontology_iri: str) -> str:
    """Build a JSON-LD context IRI from an ontology namespace IRI."""
    if ontology_iri.endswith("#"):
        return f"{ontology_iri}context"
    return f"{ontology_iri.rstrip('/')}/context"


def generate_xml_catalog(
    ontologies: Dict[str, dict], registry: dict, target_catalog_path: Path
) -> str:
    catalog = ET.Element("catalog", xmlns="urn:oasis:names:tc:entity:xmlns:xml:catalog")
    catalog.append(
        ET.Comment(f" Auto-generated catalog for {target_catalog_path.parent.name} ")
    )

    uri_mappings = []
    catalog_base = target_catalog_path.parent

    for domain in sorted(ontologies.keys()):
        files = ontologies[domain]

        # Ontology file
        owl_path = files.get("ontology")
        if not owl_path:
            continue

        # Prefer extracting directly from the ontology file so we still emit
        # catalog entries when docs/registry metadata is incomplete.
        info = extract_ontology_info(Path(owl_path))
        iri = info.get("iri")
        if not iri and domain in registry.get("ontologies", {}):
            iri = registry["ontologies"][domain].get("iri")

        if not iri:
            logger.warning("No ontology IRI found for domain '%s', skipping", domain)
            continue

        rel_path = to_posix_relative(Path(owl_path), catalog_base)
        uri_mappings.append((iri, rel_path))

        # SHACL files
        shacl_paths = files.get("shacl")
        if shacl_paths:
            is_single_shacl = len(shacl_paths) == 1
            for shacl_path in shacl_paths:
                shacl_iri = extract_shacl_iri(shacl_path)
                if not shacl_iri and is_single_shacl:
                    shacl_iri = build_shapes_iri(iri)
                if not shacl_iri:
                    logger.warning(
                        "No SHACL IRI found in %s, skipping", Path(shacl_path).name
                    )
                    continue
                rel = to_posix_relative(Path(shacl_path), catalog_base)
                uri_mappings.append((shacl_iri, rel))

        # JSON-LD context file
        jsonld_path = files.get("jsonld")
        if jsonld_path:
            context_iri = build_context_iri(iri)
            rel = to_posix_relative(Path(jsonld_path), catalog_base)
            uri_mappings.append((context_iri, rel))

    uri_mappings.sort(key=lambda x: x[0])
    for iri, path in uri_mappings:
        uri_elem = ET.SubElement(catalog, "uri")
        uri_elem.set("name", iri)
        uri_elem.set("uri", path)

    return pretty_print_xml(catalog)


def generate_imports_catalog(
    base_ontologies: Dict[str, dict], target_catalog_path: Path
) -> str:
    """
    Generate XML catalog for base/imported ontologies (rdf, rdfs, owl, etc.).

    Unlike generate_xml_catalog, this function extracts IRIs directly from
    the ontology files rather than looking them up in the registry.
    It also includes .context.jsonld files if present.

    Args:
        base_ontologies: Dictionary of domain -> file paths from collect_ontology_bundles
        target_catalog_path: Path to the target catalog file

    Returns:
        Pretty-printed XML catalog string
    """
    catalog = ET.Element("catalog", xmlns="urn:oasis:names:tc:entity:xmlns:xml:catalog")
    catalog.append(
        ET.Comment(f" Auto-generated catalog for {target_catalog_path.parent.name} ")
    )

    uri_mappings = []
    catalog_base = target_catalog_path.parent

    for domain in sorted(base_ontologies.keys()):
        files = base_ontologies[domain]
        owl_path = files.get("ontology")

        if not owl_path:
            continue

        # Extract IRI directly from the ontology file
        info = extract_dependency_info(owl_path)
        iri = info.get("iri")

        if not iri:
            logger.warning("No IRI found in %s, skipping", Path(owl_path).name)
            continue

        # Add ontology file
        rel_path = to_posix_relative(Path(owl_path), catalog_base)
        uri_mappings.append((iri, rel_path))

        # Add JSON-LD context file if present
        jsonld_path = files.get("jsonld")
        if jsonld_path:
            context_iri = build_context_iri(iri)
            rel = to_posix_relative(Path(jsonld_path), catalog_base)
            uri_mappings.append((context_iri, rel))

    uri_mappings.sort(key=lambda x: x[0])
    for iri, path in uri_mappings:
        uri_elem = ET.SubElement(catalog, "uri")
        uri_elem.set("name", iri)
        uri_elem.set("uri", path)

    return pretty_print_xml(catalog)


def pretty_print_xml(element: ET.Element) -> str:
    """
    Pretty-print an XML element with proper indentation.

    Note: We intentionally omit the DOCTYPE declaration because our catalogs
    use custom attributes (domain, test-type, category) that are not defined
    in the OASIS XML Catalog 1.0 DTD, which would cause validation errors.
    """
    xml_str = ET.tostring(element, encoding="unicode")
    dom = minidom.parseString(xml_str)
    pretty_xml = dom.toprettyxml(indent="  ")
    lines = [line for line in pretty_xml.split("\n") if line.strip()]
    result_lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    for line in lines:
        if not line.startswith("<?xml"):
            result_lines.append(line)
    return "\n".join(result_lines) + "\n"


def write_file(content: str, path: Path) -> None:
    """Write content to file only if it has changed."""
    path.parent.mkdir(parents=True, exist_ok=True)

    # Check if content has changed (normalize line endings for cross-platform)
    if path.exists():
        existing_content = path.read_text(encoding="utf-8")
        if _normalize_line_endings(existing_content) == _normalize_line_endings(
            content
        ):
            logger.info("Unchanged: %s", path.as_posix())
            return

    with path.open("w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    logger.info("Generated: %s", path.as_posix())


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
            # Normalize to forward slashes for cross-platform catalog compatibility
            rel_path_str = str(rel_path).replace("\\", "/")

            def add_entry(tid, cat="test-data"):
                test_data[tid] = {
                    "path": rel_path_str,
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


def _read_pyproject_metadata() -> Dict[str, Optional[str]]:
    pyproject_path = ROOT_DIR / "pyproject.toml"
    if not pyproject_path.exists():
        return {"name": None, "version": None}
    try:
        with pyproject_path.open("rb") as f:
            data = tomllib.load(f)
        project = data.get("project", {})
        return {"name": project.get("name"), "version": project.get("version")}
    except Exception:
        return {"name": None, "version": None}


def _default_release_tag() -> str:
    meta = _read_pyproject_metadata()
    version = meta.get("version")
    if version:
        return f"v{version}"
    return "v0.1.0"


def _toml_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ").strip()


def generate_ontoenv(
    base_ontologies: Dict[str, dict], project_name: str, project_version: str
) -> str:
    lines = []
    lines.append("# Auto-generated by registry_updater.py. Do not edit by hand.")
    lines.append("# Source of truth: imports/catalog-v001.xml and ontology metadata.")
    lines.append("")
    lines.append("[tool.ontoenv]")
    lines.append(f'name = "{_toml_escape(project_name)}"')
    lines.append(f'version = "{_toml_escape(project_version)}"')
    lines.append("")

    for domain in sorted(base_ontologies.keys()):
        files = base_ontologies[domain]
        owl_path = files.get("ontology")
        if not owl_path:
            continue
        info = extract_dependency_info(owl_path)
        if not info["iri"]:
            logger.warning("No valid IRI found for dependency %s", domain)
            continue

        lines.append(f"[dependencies.{domain}]")
        lines.append(f'uri = "{_toml_escape(info["iri"])}"')
        lines.append(f'local = "{_toml_escape(to_relative_str(owl_path))}"')
        if info["label"]:
            lines.append(f'description = "{_toml_escape(info["label"])}"')
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--release-tag", "-r", default=None)
    parser.add_argument("--dry-run", "-n", action="store_true")
    args = parser.parse_args()

    release_tag = args.release_tag or _default_release_tag()
    meta = _read_pyproject_metadata()
    project_name = meta.get("name") or "ontology-management-base"
    project_version = meta.get("version") or release_tag.lstrip("v")

    logger.info("Using RDF store: %s", FAST_STORE)
    logger.info("Release tag: %s", release_tag)

    logger.info("Scanning artifacts/...")
    domain_ontologies = collect_ontology_bundles(ARTIFACTS_DIR, TESTS_DATA_DIR)

    logger.info("Scanning imports/...")
    base_ontologies = collect_ontology_bundles(IMPORTS_DIR)

    logger.info(
        "Updating registry.json (processing %d domains)...", len(domain_ontologies)
    )
    registry = update_registry(release_tag, domain_ontologies)

    logger.info("Generating XML catalogs...")
    artifacts_xml = generate_xml_catalog(
        domain_ontologies, registry, ARTIFACTS_CATALOG_PATH
    )
    imports_xml = generate_imports_catalog(base_ontologies, IMPORTS_CATALOG_PATH)

    logger.info("Generating ontoenv.toml...")
    ontoenv_toml = generate_ontoenv(base_ontologies, project_name, project_version)

    logger.info("Discovering test data & fixtures...")
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
        write_file(ontoenv_toml, ONTOENV_PATH)
        write_file(test_catalog_xml, TEST_CATALOG_PATH)
        print("\n✅ Update complete!")


if __name__ == "__main__":
    main()
