#!/usr/bin/env python3
"""
Properties Updater - Generate ontology property docs and catalog links.

This module extracts SHACL properties and OWL class metadata to build
PROPERTIES.md files in artifacts/{domain}/ and updates documentation
pages that reference these artifacts.

FEATURE SET:
============
1. generate_properties_docs - Create/refresh artifacts/{domain}/PROPERTIES.md
2. update_catalog_table - Refresh docs/ontologies/catalog.md with links
3. update_properties_page - Build docs/ontologies/properties.md via snippets

USAGE:
======
    from src.tools.utils.properties_updater import generate_all

    generate_all()

STANDALONE TESTING:
==================
    python3 -m src.tools.utils.properties_updater [--verbose]

    Options:
      --verbose   Verbose output

DEPENDENCIES:
=============
- rdflib: RDF graph handling

NOTES:
======
- PROPERTIES.md files live with artifacts for each ontology domain.
- Docs consume artifacts PROPERTIES via pymdownx.snippets.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

import rdflib
from rdflib import OWL, RDF, RDFS, URIRef

from src.tools.core.logging import get_logger

logger = get_logger(__name__)

ROOT_DIR = Path(__file__).parent.parent.parent.parent.resolve()
ARTIFACTS_DIR = ROOT_DIR / "artifacts"
DOCS_DIR = ROOT_DIR / "docs"
CATALOG_PATH = DOCS_DIR / "ontologies" / "catalog.md"
PROPERTIES_PAGE = DOCS_DIR / "ontologies" / "properties.md"
REGISTRY_PATH = DOCS_DIR / "registry.json"

REPO_BLOB_BASE = "https://github.com/gaia-x4plc-aad/ontology-management-base/blob/main"

START_MARKER = "<!-- START_REGISTRY_TABLE -->"
END_MARKER = "<!-- END_REGISTRY_TABLE -->"

MAX_MERMAID_CLASSES = 200
MAX_MERMAID_EDGES = 400


@dataclass
class ClassInfo:
    """Container for class metadata extracted from OWL."""

    iri: str
    label: str
    comment: Optional[str]
    parents: List[str]


@dataclass
class ShaclProperty:
    """Container for SHACL property metadata."""

    shape: str
    path: str
    min_count: Optional[str]
    max_count: Optional[str]
    description: Optional[str]
    datatype: Optional[str]
    node_kind: Optional[str]
    filename: str


def parse_graph(file_path: Path, fmt: str) -> rdflib.Graph:
    """
    Parse RDF data into a graph.

    Args:
        file_path: RDF file path
        fmt: RDFLib format string

    Returns:
        Parsed graph
    """
    graph = rdflib.Graph()
    graph.parse(str(file_path), format=fmt)
    return graph


def _best_literal(values: Iterable[rdflib.term.Node]) -> Optional[str]:
    literals = [v for v in values if isinstance(v, rdflib.term.Literal)]
    if not literals:
        return None
    for literal in literals:
        if getattr(literal, "language", None) == "en":
            return str(literal)
    return str(literals[0])


def _display_name(iri: str, label: Optional[str]) -> str:
    if label:
        return label
    if "#" in iri:
        return iri.rsplit("#", 1)[-1]
    if "/" in iri:
        return iri.rstrip("/").rsplit("/", 1)[-1]
    return iri


def extract_class_definitions(owl_file: Path) -> Dict[str, ClassInfo]:
    """
    Extract class definitions from an OWL Turtle file.

    Args:
        owl_file: Path to OWL TTL file

    Returns:
        Mapping of class IRI to ClassInfo
    """
    graph = parse_graph(owl_file, "turtle")
    class_iris = set(graph.subjects(RDF.type, OWL.Class))
    class_iris.update(graph.subjects(RDF.type, RDFS.Class))

    classes: Dict[str, ClassInfo] = {}
    for class_iri in sorted(class_iris, key=lambda x: str(x)):
        if not isinstance(class_iri, URIRef):
            continue
        iri_str = str(class_iri)
        label = _best_literal(graph.objects(class_iri, RDFS.label))
        comment = _best_literal(graph.objects(class_iri, RDFS.comment))

        parent_iris = []
        for parent in graph.objects(class_iri, RDFS.subClassOf):
            if isinstance(parent, URIRef):
                parent_iris.append(str(parent))

        classes[iri_str] = ClassInfo(
            iri=iri_str,
            label=_display_name(iri_str, label),
            comment=comment,
            parents=sorted(set(parent_iris)),
        )

    logger.info("Extracted %d classes from %s", len(classes), owl_file.name)
    return classes


def build_class_hierarchy(
    classes: Dict[str, ClassInfo],
) -> Tuple[List[str], Dict[str, List[str]]]:
    """
    Build a parent->children map and determine root classes.

    Args:
        classes: Map of class IRI to ClassInfo

    Returns:
        Tuple of (roots, children_by_parent)
    """
    children_by_parent: Dict[str, List[str]] = {}
    for class_iri, class_info in classes.items():
        for parent in class_info.parents:
            if parent in classes:
                children_by_parent.setdefault(parent, []).append(class_iri)

    for parent, children in children_by_parent.items():
        children_by_parent[parent] = sorted(
            children, key=lambda iri: classes[iri].label.lower()
        )

    roots = [
        iri
        for iri, class_info in classes.items()
        if not any(parent in classes for parent in class_info.parents)
    ]
    roots.sort(key=lambda iri: classes[iri].label.lower())

    return roots, children_by_parent


def _render_class_tree(
    class_iri: str,
    classes: Dict[str, ClassInfo],
    children_by_parent: Dict[str, List[str]],
    depth: int = 0,
) -> List[str]:
    indent = "  " * depth
    label = classes[class_iri].label
    lines = [f"{indent}- {label} ({classes[class_iri].iri})"]
    for child_iri in children_by_parent.get(class_iri, []):
        lines.extend(
            _render_class_tree(child_iri, classes, children_by_parent, depth + 1)
        )
    return lines


def render_class_hierarchy(
    roots: List[str],
    classes: Dict[str, ClassInfo],
    children_by_parent: Dict[str, List[str]],
) -> str:
    """
    Render class hierarchy as a Markdown bullet list.

    Args:
        roots: Root class IRIs
        classes: Map of class IRI to ClassInfo
        children_by_parent: Parent -> children mapping

    Returns:
        Markdown string
    """
    if not roots:
        return "_No class hierarchy available._"

    lines: List[str] = []
    for root in roots:
        lines.extend(_render_class_tree(root, classes, children_by_parent))
    return "\n".join(lines)


def _mermaid_id(value: str, seen: Dict[str, int]) -> str:
    cleaned = "".join(ch if ch.isalnum() else "_" for ch in value.strip())
    cleaned = cleaned.strip("_") or "Class"
    count = seen.get(cleaned, 0)
    seen[cleaned] = count + 1
    return f"{cleaned}_{count}" if count else cleaned


def render_mermaid_class_diagram(classes: Dict[str, ClassInfo]) -> str:
    """
    Render a Mermaid classDiagram for a subset of classes.

    Args:
        classes: Map of class IRI to ClassInfo

    Returns:
        Mermaid diagram markdown or an explanatory note
    """
    if not classes:
        return "_No class diagram available._"

    total_classes = len(classes)
    if total_classes > MAX_MERMAID_CLASSES:
        return (
            f"_Class diagram omitted for size ({total_classes} classes). "
            "See class hierarchy and definitions below._"
        )

    label_to_id: Dict[str, str] = {}
    seen: Dict[str, int] = {}
    for class_info in sorted(classes.values(), key=lambda c: c.label.lower()):
        label_to_id[class_info.iri] = _mermaid_id(class_info.label, seen)

    lines = ["```mermaid", "classDiagram"]

    for class_info in sorted(classes.values(), key=lambda c: c.label.lower()):
        class_id = label_to_id[class_info.iri]
        lines.append(f"class {class_id}")

    edge_count = 0
    for class_info in classes.values():
        child_id = label_to_id[class_info.iri]
        for parent in class_info.parents:
            if parent not in classes:
                continue
            parent_id = label_to_id[parent]
            lines.append(f"{parent_id} <|-- {child_id}")
            edge_count += 1
            if edge_count >= MAX_MERMAID_EDGES:
                lines.append("%% Truncated edges for brevity")
                lines.append("```")
                return "\n".join(lines)

    lines.append("```")
    return "\n".join(lines)


def _escape_pipes(value: str) -> str:
    return value.replace("|", "\\|")


def render_class_table(classes: Dict[str, ClassInfo]) -> str:
    if not classes:
        return "_No classes found._"

    header = "|Class|IRI|Description|Parents|\n|---|---|---|---|"
    rows = []

    for class_info in sorted(classes.values(), key=lambda c: c.label.lower()):
        parents = ", ".join(
            _display_name(parent, None) for parent in class_info.parents
        )
        row = (
            f"|{_escape_pipes(class_info.label)}|"
            f"{_escape_pipes(class_info.iri)}|"
            f"{_escape_pipes(class_info.comment or '')}|"
            f"{_escape_pipes(parents)}|"
        )
        rows.append(row)

    return "\n".join([header, *rows])


def extract_shacl_properties(graph: rdflib.Graph, filename: str) -> List[ShaclProperty]:
    """
    Extract SHACL properties from a graph.

    Args:
        graph: SHACL graph
        filename: Source filename

    Returns:
        List of ShaclProperty
    """
    query = """
    PREFIX sh: <http://www.w3.org/ns/shacl#>

    SELECT ?shape ?path ?minCount ?maxCount ?description ?datatype ?nodeKind
    WHERE {
      ?shape a sh:NodeShape .
      ?shape sh:property ?property .
      ?property sh:path ?path .
      OPTIONAL { ?property sh:minCount ?minCount }
      OPTIONAL { ?property sh:maxCount ?maxCount }
      OPTIONAL { ?property sh:description ?description }
      OPTIONAL { ?property sh:datatype ?datatype }
      OPTIONAL { ?property sh:nodeKind ?nodeKind }
    }
    """

    results = graph.query(query)
    properties: List[ShaclProperty] = []
    for row in results:
        properties.append(
            ShaclProperty(
                shape=str(row.shape),
                path=str(row.path),
                min_count=str(row.minCount) if row.minCount is not None else None,
                max_count=str(row.maxCount) if row.maxCount is not None else None,
                description=(
                    str(row.description) if row.description is not None else None
                ),
                datatype=str(row.datatype) if row.datatype is not None else None,
                node_kind=str(row.nodeKind) if row.nodeKind is not None else None,
                filename=filename,
            )
        )
    return properties


def extract_prefixes(graph: rdflib.Graph) -> Dict[str, str]:
    prefixes = {}
    for prefix, namespace in graph.namespaces():
        prefixes[str(namespace)] = prefix
    return prefixes


def _replace_with_prefix(uri: str, prefixes: Dict[str, str]) -> Tuple[str, str]:
    for namespace, prefix in prefixes.items():
        if uri.startswith(namespace):
            return prefix, uri.replace(namespace, "")
    return "", uri


def render_properties_table(
    properties: List[ShaclProperty], prefixes: Dict[str, str]
) -> str:
    if not properties:
        return "_No SHACL properties found._"

    header = (
        "|Shape|Property prefix|Property|MinCount|MaxCount|Description|Datatype/NodeKind|Filename|\n"
        "|---|---|---|---|---|---|---|---|"
    )
    rows: List[str] = []

    for prop in properties:
        shape_prefix, shape_name = _replace_with_prefix(prop.shape, prefixes)
        prop_prefix, prop_name = _replace_with_prefix(prop.path, prefixes)
        datatype_or_nodekind = ""
        if prop.datatype:
            datatype_or_nodekind = f"<{prop.datatype}>"
        elif prop.node_kind:
            datatype_or_nodekind = f"<{prop.node_kind}>"

        rows.append(
            "|"
            + "|".join(
                [
                    f"{shape_name}",
                    f"{prop_prefix}",
                    f"{prop_name}",
                    prop.min_count or "",
                    prop.max_count or "",
                    _escape_pipes(prop.description or ""),
                    datatype_or_nodekind,
                    prop.filename,
                ]
            )
            + "|"
        )

    return "\n".join([header, *rows])


def render_properties_markdown(
    domain: str,
    classes: Dict[str, ClassInfo],
    shacl_properties: List[ShaclProperty],
    prefixes: Dict[str, str],
) -> str:
    """
    Render the full PROPERTIES.md content for a domain.

    Args:
        domain: Domain name
        classes: Class definitions
        shacl_properties: SHACL properties list
        prefixes: Prefix mapping

    Returns:
        Markdown string
    """
    roots, children_by_parent = build_class_hierarchy(classes)
    class_hierarchy = render_class_hierarchy(roots, classes, children_by_parent)
    class_table = render_class_table(classes)
    class_diagram = render_mermaid_class_diagram(classes)
    properties_table = render_properties_table(shacl_properties, prefixes)

    prefix_lines = []
    if prefixes:
        prefix_lines = ["## Prefixes", ""] + [
            f"- {prefix}: <{namespace}>"
            for namespace, prefix in sorted(prefixes.items(), key=lambda x: x[1])
        ]

    content_lines = [
        f"## {domain} Properties",
        "",
        "### Class Diagram",
        "",
        class_diagram,
        "",
        "### Class Hierarchy",
        "",
        class_hierarchy,
        "",
        "### Class Definitions",
        "",
        class_table,
        "",
        *prefix_lines,
        "",
        "### SHACL Properties",
        "",
        properties_table,
        "",
    ]

    return "\n".join(content_lines)


def _find_first_file(domain_dir: Path, suffix: str) -> Optional[Path]:
    matches = sorted(domain_dir.glob(f"*{suffix}"))
    return matches[0] if matches else None


def generate_properties_docs() -> None:
    """Generate PROPERTIES.md files for all domains."""
    if not ARTIFACTS_DIR.exists():
        logger.error("Artifacts directory not found: %s", ARTIFACTS_DIR)
        return

    for domain_dir in sorted([d for d in ARTIFACTS_DIR.iterdir() if d.is_dir()]):
        domain = domain_dir.name
        shacl_files = sorted(domain_dir.glob("*.shacl.ttl"))
        if not shacl_files:
            continue

        owl_file = _find_first_file(domain_dir, ".owl.ttl")
        if not owl_file:
            logger.warning("No OWL file found for %s", domain)
            classes: Dict[str, ClassInfo] = {}
        else:
            classes = extract_class_definitions(owl_file)

        all_properties: List[ShaclProperty] = []
        all_prefixes: Dict[str, str] = {}

        for shacl_file in shacl_files:
            graph = parse_graph(shacl_file, "turtle")
            all_properties.extend(extract_shacl_properties(graph, shacl_file.name))
            all_prefixes.update(extract_prefixes(graph))

        properties_content = render_properties_markdown(
            domain, classes, all_properties, all_prefixes
        )

        properties_file = domain_dir / "PROPERTIES.md"
        properties_file.write_text(properties_content, encoding="utf-8")
        logger.info("Updated PROPERTIES.md for %s", domain)


def generate_registry_table(registry: dict) -> str:
    """Generate catalog table with links to raw files and properties anchors."""
    header = (
        "|Domain|Latest|IRI|Ontology|SHACL|Context|Properties|Example Instance|\n"
        "|---|---|---|---|---|---|---|---|"
    )
    rows = []

    for domain, entry in sorted(registry.get("ontologies", {}).items()):
        latest = entry.get("latest")
        latest_entry = entry.get("versions", {}).get(latest, {})
        files = latest_entry.get("files", {})

        iri_link = f"[IRI]({entry.get('iri', '')})" if entry.get("iri") else ""

        def link_or_empty(path_str: Optional[str]) -> str:
            if not path_str:
                return ""
            name = Path(path_str).name
            return f"[{name}]({REPO_BLOB_BASE}/artifacts/{domain}/{name})"

        def list_links(paths: List[str]) -> str:
            if not paths:
                return ""
            links = [
                f"[{Path(path_str).name}]({REPO_BLOB_BASE}/artifacts/{domain}/{Path(path_str).name})"
                for path_str in paths
            ]
            return "<br>".join(links)

        properties_anchor = f"properties.md#{domain}-properties"
        properties_link = (
            f"[{domain} Properties]({properties_anchor})"
            if files.get("properties")
            else ""
        )

        rows.append(
            "|"
            + "|".join(
                [
                    domain,
                    latest or "",
                    iri_link,
                    link_or_empty(files.get("ontology")),
                    list_links(files.get("shacl", [])),
                    link_or_empty(files.get("jsonld")),
                    properties_link,
                    link_or_empty(files.get("instance")),
                ]
            )
            + "|"
        )

    return "\n".join([header, *rows])


def update_catalog_table(catalog_path: Path, table_markdown: str) -> None:
    """Replace registry table in catalog.md with updated content."""
    content = catalog_path.read_text(encoding="utf-8")
    if START_MARKER not in content or END_MARKER not in content:
        raise ValueError("Catalog markers not found in catalog.md")

    before, rest = content.split(START_MARKER, 1)
    _, after = rest.split(END_MARKER, 1)
    updated = f"{before}{START_MARKER}\n{table_markdown}\n{END_MARKER}{after}"

    catalog_path.write_text(updated, encoding="utf-8")
    logger.info("Updated catalog table in %s", catalog_path)


def update_properties_page(registry: dict) -> None:
    """Generate docs/ontologies/properties.md referencing artifacts PROPERTIES."""
    lines = [
        "# Ontology Properties",
        "",
        "This page includes per-domain properties extracted from SHACL shapes.",
        "",
    ]

    for domain in sorted(registry.get("ontologies", {}).keys()):
        properties_path = ARTIFACTS_DIR / domain / "PROPERTIES.md"
        if not properties_path.exists():
            continue
        lines.append(f'--8<-- "artifacts/{domain}/PROPERTIES.md"')
        lines.append("")

    PROPERTIES_PAGE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    logger.info("Updated properties page: %s", PROPERTIES_PAGE)


def load_registry() -> dict:
    """Load docs/registry.json."""
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


def generate_all() -> None:
    """Run all generation steps."""
    generate_properties_docs()
    registry = load_registry()
    update_properties_page(registry)
    table_markdown = generate_registry_table(registry)
    update_catalog_table(CATALOG_PATH, table_markdown)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--verbose", action="store_true", help="Verbose output")
    return parser.parse_args()


def _run_tests() -> bool:
    """Run minimal self-tests."""
    print("Running module self-tests...")
    all_passed = True

    try:
        assert ARTIFACTS_DIR.exists()
        print("PASS: artifacts dir exists")
    except AssertionError:
        print("FAIL: artifacts dir missing")
        all_passed = False

    return all_passed


def main() -> None:
    """CLI entry point."""
    args = _parse_args()
    if args.verbose:
        logger.setLevel("DEBUG")

    generate_all()


if __name__ == "__main__":
    main()
