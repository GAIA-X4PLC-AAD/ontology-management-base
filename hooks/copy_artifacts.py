#!/usr/bin/env python3
"""
MkDocs Hook: Prepare Documentation Artifacts

Updates class page navigation and copies ontology artifacts into docs
so they can be referenced locally during MkDocs builds.

NOTES:
- Artifacts are copied into docs/artifacts/<domain>/<versionInfo>/
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

import rdflib
from rdflib import OWL, RDF, URIRef

ROOT_DIR = Path(__file__).parent.parent.resolve()
ARTIFACTS_DIR = ROOT_DIR / "artifacts"
TESTS_DATA_DIR = ROOT_DIR / "tests" / "data"
DOCS_DIR = ROOT_DIR / "docs"
DOCS_ARTIFACTS_DIR = DOCS_DIR / "artifacts"
DOCS_SITE_URL = os.environ.get("DOCS_SITE_URL")


def _normalize_version_info(value: str) -> str:
    cleaned = value.replace("Version ", "").strip()
    if not cleaned:
        return "unknown"
    return cleaned if cleaned.startswith("v") else f"v{cleaned}"


def _safe_path_segment(value: str) -> str:
    return re.sub(r"[^a-zA-Z0-9._-]", "_", value.strip()) or "unknown"


def _extract_version_info(owl_file: Path) -> str:
    graph = rdflib.Graph()
    graph.parse(str(owl_file), format="turtle")

    ontology = next(graph.subjects(RDF.type, OWL.Ontology), None)
    if ontology is None:
        return "unknown"

    version_info = graph.value(ontology, OWL.versionInfo)
    if version_info is not None:
        return _safe_path_segment(_normalize_version_info(str(version_info)))

    version_iri = graph.value(ontology, OWL.versionIRI)
    version_iri_str = None
    if isinstance(version_iri, URIRef):
        version_iri_str = str(version_iri)
    elif isinstance(ontology, URIRef):
        version_iri_str = str(ontology)

    if version_iri_str:
        matches = re.findall(r"/(v\\d+(?:\\.\\d+)*)/?", version_iri_str)
        if matches:
            return _safe_path_segment(_normalize_version_info(matches[-1]))

    return "unknown"


def _find_instance_file(domain: str) -> Path | None:
    valid_dir = TESTS_DATA_DIR / domain / "valid"
    if not valid_dir.exists():
        return None

    for pattern in [f"{domain}_instance.json", "*_instance.json"]:
        matches = sorted(valid_dir.glob(pattern))
        if matches:
            return matches[0]

    return None


def _copy_domain_artifacts(domain_dir: Path) -> None:
    domain = domain_dir.name
    owl_file = domain_dir / f"{domain}.owl.ttl"
    if not owl_file.exists():
        return

    version_info = _extract_version_info(owl_file)
    target_dir = DOCS_ARTIFACTS_DIR / domain / version_info
    target_dir.mkdir(parents=True, exist_ok=True)

    for file_path in sorted(domain_dir.iterdir()):
        if file_path.is_file():
            shutil.copy2(file_path, target_dir / file_path.name)

    instance_file = _find_instance_file(domain)
    if instance_file:
        shutil.copy2(instance_file, target_dir / instance_file.name)


def _run_docs_generators() -> None:
    """
    Run documentation generators before building docs.

    DOCS_SITE_URL is optional and overrides the base URL used for local diagrams.
    """
    subprocess.run(
        [sys.executable, "-m", "src.tools.utils.properties_updater"], check=True
    )
    subprocess.run(
        [sys.executable, "-m", "src.tools.utils.class_page_generator"], check=True
    )


def _build_class_page_nav(docs_dir: Path) -> dict:
    """
    Build navigation entries for generated class pages.

    Returns:
        Mapping of domain -> list of nav items (Overview + class pages)
    """
    classes_root = docs_dir / "ontologies" / "classes"
    if not classes_root.exists():
        return {}

    domain_nav: dict = {}
    for domain_dir in sorted(classes_root.iterdir()):
        if not domain_dir.is_dir():
            continue

        class_files = sorted(
            [p for p in domain_dir.glob("*.md") if p.name != "index.md"]
        )
        if not class_files:
            continue

        domain_name = domain_dir.name
        overview_path = f"ontologies/classes/{domain_name}/index.md"

        entries = [{"Overview": overview_path}]
        for class_file in class_files:
            class_name = class_file.stem
            class_path = f"ontologies/classes/{domain_name}/{class_file.name}"
            entries.append({class_name: class_path})

        domain_nav[domain_name] = entries

    return domain_nav


def on_config(config):
    """
    MkDocs hook called after configuration is loaded.

    Ensures class pages are included in nav so the sidebar appears on them.
    """
    docs_dir = Path(config.get("docs_dir", "docs"))
    domain_nav = _build_class_page_nav(docs_dir)
    if not domain_nav:
        return config

    nav = config.get("nav", [])
    for entry in nav:
        if not isinstance(entry, dict) or "Ontologies" not in entry:
            continue

        ontologies_section = entry["Ontologies"]
        for item in ontologies_section:
            if not isinstance(item, dict) or "Class Explorer" not in item:
                continue

            class_explorer_section = item["Class Explorer"]
            updated_section = []
            for class_entry in class_explorer_section:
                if not isinstance(class_entry, dict):
                    updated_section.append(class_entry)
                    continue

                name, path_or_children = next(iter(class_entry.items()))
                if (
                    name in domain_nav
                    and isinstance(path_or_children, str)
                    and path_or_children.endswith("/index.md")
                ):
                    updated_section.append({name: domain_nav[name]})
                else:
                    updated_section.append(class_entry)

            item["Class Explorer"] = updated_section
            break

        break

    config["nav"] = nav
    return config


def on_pre_build(config, **kwargs):
    """
    MkDocs hook called before build.

    Copies artifacts into docs/ so they can be linked locally.
    """
    _run_docs_generators()

    if not ARTIFACTS_DIR.exists():
        return

    if DOCS_ARTIFACTS_DIR.exists():
        shutil.rmtree(DOCS_ARTIFACTS_DIR)
    DOCS_ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

    for domain_dir in sorted(ARTIFACTS_DIR.iterdir()):
        if not domain_dir.is_dir():
            continue
        _copy_domain_artifacts(domain_dir)


def on_post_build(config, **kwargs):
    """
    MkDocs hook called after build completes.
    """
    pass
