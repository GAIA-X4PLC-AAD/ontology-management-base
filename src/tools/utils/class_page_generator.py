#!/usr/bin/env python3
"""
Class Page Generator - Generate per-class documentation pages with visualizations.

Creates individual documentation pages for each OWL class, featuring:
    - Interactive WebVOWL visualization
- Inheritance tree (parents and children)
- Slots table with cardinality, range, and inheritance provenance
- Usages table (where this class is referenced)
- Cross-domain navigation links

FEATURE SET:
============
1. generate_class_pages - Create docs/ontologies/classes/{domain}/{class}.md
2. build_class_index - Build cross-domain class lookup for usages
3. generate_gx_redirect - Create redirect page for gx domain

USAGE:
======
    from src.tools.utils.class_page_generator import generate_all_class_pages

    generate_all_class_pages()

STANDALONE TESTING:
==================
    python3 -m src.tools.utils.class_page_generator [--verbose] [--domain DOMAIN]

DEPENDENCIES:
=============
- rdflib: RDF graph handling

NOTES:
======
- gx domain redirects to official Gaia-X docs
- Cross-domain references link to appropriate pages
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Set
from urllib.parse import quote

import rdflib
from rdflib import OWL, RDF, RDFS, URIRef

from src.tools.core.logging import get_logger

logger = get_logger(__name__)

ROOT_DIR = Path(__file__).parent.parent.parent.parent.resolve()
ARTIFACTS_DIR = ROOT_DIR / "artifacts"
DOCS_DIR = ROOT_DIR / "docs"
CLASSES_DIR = DOCS_DIR / "ontologies" / "classes"
MKDOCS_YML = ROOT_DIR / "mkdocs.yml"

# External domains with their documentation URLs
EXTERNAL_DOMAINS = {
    "gx": {
        "name": "Gaia-X",
        "url": "https://docs.gaia-x.eu/ontology/development/",
        "class_url": "https://docs.gaia-x.eu/ontology/development/classes/{class}/",
    }
}

# Standard ontology prefixes to exclude from local generation
STANDARD_PREFIXES = {
    "http://www.w3.org/",
    "http://xmlns.com/foaf/",
    "http://purl.org/dc/",
}

WEBVOWL_BASE_URL = "https://service.tib.eu/webvowl/#iri="


def _load_site_url() -> Optional[str]:
    if not MKDOCS_YML.exists():
        return None
    for line in MKDOCS_YML.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("site_url:"):
            return stripped.split("site_url:", 1)[1].strip()
    return None


SITE_URL = os.environ.get("DOCS_SITE_URL") or _load_site_url()
ARTIFACTS_SITE_BASE_URL = f"{SITE_URL.rstrip('/')}/artifacts" if SITE_URL else None


def _is_local_site() -> bool:
    if not SITE_URL:
        return False
    lowered = SITE_URL.lower()
    return "127.0.0.1" in lowered or "localhost" in lowered


@dataclass
class ClassInfo:
    """Container for class metadata."""

    iri: str
    label: str
    comment: Optional[str]
    domain: str
    parents: List[str] = field(default_factory=list)
    children: List[str] = field(default_factory=list)
    properties: List["PropertyInfo"] = field(default_factory=list)
    usages: List["UsageInfo"] = field(default_factory=list)


@dataclass
class PropertyInfo:
    """Container for property metadata."""

    path: str
    name: str
    min_count: Optional[str]
    max_count: Optional[str]
    description: Optional[str]
    datatype: Optional[str]
    class_ref: Optional[str]  # sh:class - object property target
    node_ref: Optional[str]  # sh:node - nested shape
    provenance: str  # "direct" or parent class IRI


@dataclass
class UsageInfo:
    """Container for usage/reverse reference."""

    source_class: str
    source_domain: str
    property_path: str
    property_name: str


def local_name(iri: str) -> str:
    """Extract local name from IRI."""
    if "#" in iri:
        return iri.rsplit("#", 1)[-1]
    if "/" in iri:
        return iri.rstrip("/").rsplit("/", 1)[-1]
    return iri


def build_raw_owl_url(
    domain: str, version_info: str, filename: Optional[str] = None
) -> str:
    """Build an absolute URL for an OWL file (used by WebVOWL)."""
    owl_name = filename or f"{domain}.owl.ttl"
    if ARTIFACTS_SITE_BASE_URL:
        return f"{ARTIFACTS_SITE_BASE_URL}/{domain}/{version_info}/{owl_name}"
    return (
        "https://raw.githubusercontent.com/gaia-x4plc-aad/"
        f"ontology-management-base/main/artifacts/{domain}/{owl_name}"
    )


def build_webvowl_url(owl_url: str) -> str:
    """Build a WebVOWL viewer URL for an OWL file."""
    return f"{WEBVOWL_BASE_URL}{quote(owl_url, safe='')}"


def safe_filename(name: str) -> str:
    """Convert name to safe filename."""
    return re.sub(r"[^a-zA-Z0-9_-]", "_", name)


def _anchor_id(value: str) -> str:
    cleaned = "".join(ch if ch.isalnum() or ch in "-_" else "-" for ch in value)
    cleaned = cleaned.strip("-_").lower()
    return cleaned or "property"


def _build_class_url(domain: str, class_name: str) -> Optional[str]:
    if not SITE_URL:
        return None
    base = SITE_URL.rstrip("/")
    filename = safe_filename(class_name)
    return f"{base}/ontologies/classes/{domain}/{filename}/"


def _normalize_version_info(value: str) -> str:
    cleaned = value.replace("Version ", "").strip()
    if not cleaned:
        return "unknown"
    return cleaned if cleaned.startswith("v") else f"v{cleaned}"


def _extract_version_info(owl_graph: rdflib.Graph) -> str:
    ontology = next(owl_graph.subjects(RDF.type, OWL.Ontology), None)
    if ontology is None:
        return "unknown"

    version_info = owl_graph.value(ontology, OWL.versionInfo)
    if version_info is not None:
        return _normalize_version_info(str(version_info))

    version_iri = owl_graph.value(ontology, OWL.versionIRI)
    version_iri_str = None
    if isinstance(version_iri, URIRef):
        version_iri_str = str(version_iri)
    elif isinstance(ontology, URIRef):
        version_iri_str = str(ontology)

    if version_iri_str:
        matches = re.findall(r"/(v\\d+(?:\\.\\d+)*)/?", version_iri_str)
        if matches:
            return _normalize_version_info(matches[-1])

    return "unknown"


def extract_domain_from_iri(iri: str) -> Optional[str]:
    """Extract domain name from IRI."""
    # Match patterns like /manifest/v5/ or /scenario/v5/
    match = re.search(r"/([a-z-]+)/v\d+/?", iri, re.IGNORECASE)
    if match:
        return match.group(1)

    # Check for gx
    if "gaia-x" in iri.lower() or "/gx/" in iri or "/gx#" in iri:
        return "gx"

    return None


def is_external_iri(iri: str) -> bool:
    """Check if IRI belongs to external/standard ontology."""
    for prefix in STANDARD_PREFIXES:
        if iri.startswith(prefix):
            return True

    domain = extract_domain_from_iri(iri)
    return domain in EXTERNAL_DOMAINS


def parse_owl_file(owl_file: Path) -> rdflib.Graph:
    """Parse OWL Turtle file."""
    graph = rdflib.Graph()
    graph.parse(str(owl_file), format="turtle")
    return graph


def parse_shacl_file(shacl_file: Path) -> rdflib.Graph:
    """Parse SHACL Turtle file."""
    graph = rdflib.Graph()
    graph.parse(str(shacl_file), format="turtle")
    return graph


def extract_classes(owl_graph: rdflib.Graph, domain: str) -> Dict[str, ClassInfo]:
    """
    Extract class definitions from OWL graph.

    Args:
        owl_graph: Parsed OWL graph
        domain: Domain name

    Returns:
        Mapping of class IRI to ClassInfo
    """
    classes: Dict[str, ClassInfo] = {}

    # Find all owl:Class and rdfs:Class
    class_iris: Set[URIRef] = set()
    for class_type in [OWL.Class, RDFS.Class]:
        for s in owl_graph.subjects(RDF.type, class_type):
            if isinstance(s, URIRef):
                class_iris.add(s)

    for class_iri in class_iris:
        iri_str = str(class_iri)

        # Get label
        label = None
        for lbl in owl_graph.objects(class_iri, RDFS.label):
            if hasattr(lbl, "language") and lbl.language == "en":
                label = str(lbl)
                break
            label = str(lbl)
        if not label:
            label = local_name(iri_str)

        # Get comment
        comment = None
        for cmt in owl_graph.objects(class_iri, RDFS.comment):
            if hasattr(cmt, "language") and cmt.language == "en":
                comment = str(cmt)
                break
            comment = str(cmt)

        # Get parents
        parents = []
        for parent in owl_graph.objects(class_iri, RDFS.subClassOf):
            if isinstance(parent, URIRef):
                parents.append(str(parent))

        classes[iri_str] = ClassInfo(
            iri=iri_str,
            label=label,
            comment=comment,
            domain=domain,
            parents=sorted(set(parents)),
        )

    # Build children relationships
    for class_iri, class_info in classes.items():
        for parent_iri in class_info.parents:
            if parent_iri in classes:
                classes[parent_iri].children.append(class_iri)

    # Sort children
    for class_info in classes.values():
        class_info.children.sort(key=lambda x: local_name(x).lower())

    logger.info("Extracted %d classes from %s domain", len(classes), domain)
    return classes


def extract_properties(
    shacl_graph: rdflib.Graph, classes: Dict[str, ClassInfo]
) -> None:
    """
    Extract SHACL properties and attach to class objects.

    Modifies classes in place to add properties.

    Args:
        shacl_graph: Parsed SHACL graph
        classes: Class mapping to update
    """
    query = """
    PREFIX sh: <http://www.w3.org/ns/shacl#>

    SELECT ?shape ?targetClass ?path ?name ?minCount ?maxCount ?description
           ?datatype ?nodeKind ?classRef ?nodeRef
    WHERE {
      ?shape a sh:NodeShape .
      ?shape sh:property ?property .
      ?property sh:path ?path .
      OPTIONAL { ?shape sh:targetClass ?targetClass }
      OPTIONAL { ?property sh:name ?name }
      OPTIONAL { ?property sh:minCount ?minCount }
      OPTIONAL { ?property sh:maxCount ?maxCount }
      OPTIONAL { ?property sh:description ?description }
      OPTIONAL { ?property sh:datatype ?datatype }
      OPTIONAL { ?property sh:nodeKind ?nodeKind }
      OPTIONAL { ?property sh:class ?classRef }
      OPTIONAL { ?property sh:node ?nodeRef }
    }
    """

    results = shacl_graph.query(query)

    # Group properties by target class
    shape_to_class: Dict[str, str] = {}
    for row in results:
        if row.targetClass:
            shape_to_class[str(row.shape)] = str(row.targetClass)

    for row in results:
        # Determine target class
        target_class = None
        if row.targetClass:
            target_class = str(row.targetClass)
        elif str(row.shape) in shape_to_class:
            target_class = shape_to_class[str(row.shape)]

        if not target_class or target_class not in classes:
            continue

        prop_info = PropertyInfo(
            path=str(row.path),
            name=str(row.name) if row.name else local_name(str(row.path)),
            min_count=str(row.minCount) if row.minCount else None,
            max_count=str(row.maxCount) if row.maxCount else None,
            description=str(row.description) if row.description else None,
            datatype=str(row.datatype) if row.datatype else None,
            class_ref=str(row.classRef) if row.classRef else None,
            node_ref=str(row.nodeRef) if row.nodeRef else None,
            provenance="direct",
        )

        classes[target_class].properties.append(prop_info)

    logger.debug("Extracted properties for %d classes", len(classes))


def build_usages_index(
    all_classes: Dict[str, Dict[str, ClassInfo]],
) -> Dict[str, List[UsageInfo]]:
    """
    Build reverse reference index across all domains.

    Args:
        all_classes: Mapping of domain -> (class IRI -> ClassInfo)

    Returns:
        Mapping of class IRI -> list of UsageInfo where it's referenced
    """
    usages: Dict[str, List[UsageInfo]] = {}

    for domain, classes in all_classes.items():
        for class_iri, class_info in classes.items():
            for prop in class_info.properties:
                # Check if property references another class
                target = prop.class_ref or prop.node_ref
                if target:
                    if target not in usages:
                        usages[target] = []
                    usages[target].append(
                        UsageInfo(
                            source_class=class_iri,
                            source_domain=domain,
                            property_path=prop.path,
                            property_name=prop.name,
                        )
                    )

    return usages


def apply_inherited_properties(classes: Dict[str, ClassInfo]) -> None:
    """
    Expand class properties with inherited slots from ancestor classes.

    Adds inherited properties with provenance set to the ancestor class IRI.
    """
    direct_props = {iri: list(info.properties) for iri, info in classes.items()}

    def add_props_from(
        ancestor_iri: str,
        seen_paths: Set[str],
        target: List[PropertyInfo],
    ) -> None:
        for prop in direct_props.get(ancestor_iri, []):
            if prop.path in seen_paths:
                continue
            seen_paths.add(prop.path)
            target.append(
                PropertyInfo(
                    path=prop.path,
                    name=prop.name,
                    min_count=prop.min_count,
                    max_count=prop.max_count,
                    description=prop.description,
                    datatype=prop.datatype,
                    class_ref=prop.class_ref,
                    node_ref=prop.node_ref,
                    provenance=ancestor_iri,
                )
            )

    def walk_ancestors(
        class_iri: str,
        seen_paths: Set[str],
        target: List[PropertyInfo],
        visited: Set[str],
    ) -> None:
        for parent in classes[class_iri].parents:
            if parent not in classes or parent in visited:
                continue
            visited.add(parent)
            add_props_from(parent, seen_paths, target)
            walk_ancestors(parent, seen_paths, target, visited)

    for class_iri, class_info in classes.items():
        inherited: List[PropertyInfo] = []
        seen_paths = {prop.path for prop in direct_props.get(class_iri, [])}
        walk_ancestors(class_iri, seen_paths, inherited, set())
        class_info.properties = direct_props.get(class_iri, []) + inherited


def collect_property_paths(classes: Dict[str, ClassInfo]) -> Set[str]:
    """Collect SHACL property paths defined for a domain."""
    paths: Set[str] = set()
    for class_info in classes.values():
        for prop in class_info.properties:
            paths.add(prop.path)
    return paths


def _get_class_info(
    class_iri: str, all_classes: Dict[str, Dict[str, ClassInfo]]
) -> Optional[ClassInfo]:
    domain = extract_domain_from_iri(class_iri)
    if domain and domain in all_classes and class_iri in all_classes[domain]:
        return all_classes[domain][class_iri]
    return None


def _format_inheritance_link(
    class_iri: str,
    current_domain: str,
    all_classes: Dict[str, Dict[str, ClassInfo]],
) -> str:
    class_name = local_name(class_iri)
    domain = extract_domain_from_iri(class_iri)

    if domain in EXTERNAL_DOMAINS:
        ext = EXTERNAL_DOMAINS[domain]
        url = ext["class_url"].format(**{"class": class_name})
        return f"[{class_name}]({url}){{ target=_blank }}"

    if domain == current_domain:
        return f"[{class_name}]({safe_filename(class_name)}.md)"

    if domain and domain in all_classes and class_iri in all_classes[domain]:
        return f"[{class_name}](../{domain}/{safe_filename(class_name)}.md)"

    return class_name


def _build_ancestry_paths(
    class_iri: str, all_classes: Dict[str, Dict[str, ClassInfo]]
) -> List[List[str]]:
    info = _get_class_info(class_iri, all_classes)
    if not info or not info.parents:
        return [[class_iri]]

    paths: List[List[str]] = []
    for parent in info.parents:
        parent_info = _get_class_info(parent, all_classes)
        if parent_info is None:
            paths.append([parent, class_iri])
            continue
        for path in _build_ancestry_paths(parent, all_classes):
            paths.append(path + [class_iri])

    return paths


def _render_descendants(
    class_iri: str,
    depth: int,
    current_domain: str,
    all_classes: Dict[str, Dict[str, ClassInfo]],
) -> List[str]:
    indent = "  " * depth
    lines = [
        f"{indent}- {_format_inheritance_link(class_iri, current_domain, all_classes)}"
    ]
    info = _get_class_info(class_iri, all_classes)
    if info:
        for child in info.children:
            lines.extend(
                _render_descendants(child, depth + 1, current_domain, all_classes)
            )
    return lines


def _render_inheritance_tree(
    class_info: ClassInfo, all_classes: Dict[str, Dict[str, ClassInfo]]
) -> List[str]:
    paths = _build_ancestry_paths(class_info.iri, all_classes)
    if not paths:
        return ["_No inheritance available._"]

    lines: List[str] = []
    for path in paths:
        for depth, iri in enumerate(path):
            indent = "  " * depth
            lines.append(
                f"{indent}- {_format_inheritance_link(iri, class_info.domain, all_classes)}"
            )
            if iri == class_info.iri:
                for child in class_info.children:
                    lines.extend(
                        _render_descendants(
                            child, depth + 1, class_info.domain, all_classes
                        )
                    )
    return lines


def _render_inheritance_mermaid(
    class_info: ClassInfo, all_classes: Dict[str, Dict[str, ClassInfo]]
) -> List[str]:
    paths = _build_ancestry_paths(class_info.iri, all_classes)
    if not paths:
        return ["_No inheritance diagram available._"]

    edges = set()
    nodes = set()

    for path in paths:
        nodes.update(path)
        for idx in range(len(path) - 1):
            parent = path[idx]
            child = path[idx + 1]
            edges.add((parent, child))

    nodes.add(class_info.iri)
    for child in class_info.children:
        edges.add((class_info.iri, child))
        nodes.add(class_info.iri)
        nodes.add(child)

    id_map: Dict[str, str] = {}
    seen: Dict[str, int] = {}
    for iri in sorted(nodes):
        label = local_name(iri)
        base = re.sub(r"[^a-zA-Z0-9_]", "_", label) or "Class"
        count = seen.get(base, 0)
        seen[base] = count + 1
        id_map[iri] = f"{base}_{count}" if count else base

    lines = ["```mermaid", "graph TD"]
    for iri in sorted(nodes):
        label = local_name(iri)
        lines.append(f'{id_map[iri]}["{label}"]')

    for parent, child in sorted(edges):
        lines.append(f"{id_map[parent]} --> {id_map[child]}")

    for iri in sorted(nodes):
        domain = extract_domain_from_iri(iri)
        class_name = local_name(iri)
        url = None
        if domain in EXTERNAL_DOMAINS:
            url = EXTERNAL_DOMAINS[domain]["class_url"].format(**{"class": class_name})
        elif domain:
            url = _build_class_url(domain, class_name)
        if url:
            lines.append(f'click {id_map[iri]} "{url}"')

    lines.append("```")
    return lines


def render_class_page(
    class_info: ClassInfo,
    all_classes: Dict[str, Dict[str, ClassInfo]],
    usages_index: Dict[str, List[UsageInfo]],
    version_info: str,
    property_paths_by_domain: Dict[str, Set[str]],
) -> str:
    """
    Render a complete class documentation page.

    Args:
        class_info: Class to document
        all_classes: All classes across domains for cross-linking
        usages_index: Reverse reference index
        property_paths_by_domain: Domain -> set of SHACL property paths

    Returns:
        Markdown content
    """
    domain = class_info.domain
    lines = [
        f"# {class_info.label}",
        "",
        f"**IRI:** `{class_info.iri}`",
        "",
    ]

    # Description
    if class_info.comment:
        lines.extend([class_info.comment, ""])

    # Interactive visualization (WebVOWL) or local static diagram
    lines.append("## Class Diagram")
    lines.append("")
    if _is_local_site():
        lines.extend(_render_inheritance_mermaid(class_info, all_classes))
        lines.append("")
    else:
        owl_url = build_raw_owl_url(domain, version_info)
        webvowl_url = build_webvowl_url(owl_url)
        lines.extend(
            [
                '<div class="ontology-webvowl">',
                f'  <iframe src="{webvowl_url}" title="WebVOWL: {domain}" loading="lazy"></iframe>',
                "</div>",
                "",
                f"[Open in WebVOWL]({webvowl_url}){{ target=_blank }}",
                "",
            ]
        )

    # Inheritance
    lines.extend(
        [
            "## Inheritance",
            "",
            *_render_inheritance_tree(class_info, all_classes),
            "",
        ]
    )

    # Slots (properties)
    if class_info.properties:
        lines.extend(
            [
                "## Slots",
                "",
                "| Name | Cardinality and Range | Description | Inheritance |",
                "|------|-----------------------|-------------|-------------|",
            ]
        )

        for prop in sorted(class_info.properties, key=lambda p: p.name.lower()):
            cardinality = _format_cardinality(prop.min_count, prop.max_count)
            prop_type = _format_property_type(prop, all_classes)
            desc = (prop.description or "").replace("\n", " ").replace("|", "\\|")
            has_type = prop_type and prop_type != "-"
            card_range = f"{cardinality}<br>{prop_type}" if has_type else cardinality

            provenance = (
                "direct"
                if prop.provenance == "direct"
                else _format_class_link(prop.provenance, all_classes)
            )

            prop_label = prop.name
            if prop.path.startswith("http"):
                prop_domain = extract_domain_from_iri(prop.path)
                if (
                    prop_domain
                    and prop_domain in property_paths_by_domain
                    and prop.path in property_paths_by_domain[prop_domain]
                ):
                    anchor = f"prop-{_anchor_id(prop.path)}"
                    prop_label = (
                        f"[{prop.name}](../../properties/{prop_domain}.md#{anchor})"
                    )
                else:
                    prop_label = f"[{prop.name}]({prop.path}){{ target=_blank }}"

            lines.append(f"| {prop_label} | {card_range} | {desc} | {provenance} |")

        lines.append("")

    # Usages
    usages = usages_index.get(class_info.iri, [])
    if usages:
        lines.extend(
            [
                "## Usages",
                "",
                "This class is referenced by:",
                "",
                "| Class | Property | Domain |",
                "|-------|----------|--------|",
            ]
        )

        for usage in sorted(
            usages, key=lambda u: (u.source_domain, local_name(u.source_class))
        ):
            source_name = local_name(usage.source_class)
            if usage.source_domain == domain:
                source_link = f"[{source_name}]({safe_filename(source_name)}.md)"
            elif usage.source_domain in EXTERNAL_DOMAINS:
                ext = EXTERNAL_DOMAINS[usage.source_domain]
                url = ext["class_url"].format(**{"class": source_name})
                source_link = f"[{source_name}]({url}){{ target=_blank }}"
            else:
                source_link = f"[{source_name}](../{usage.source_domain}/{safe_filename(source_name)}.md)"

            lines.append(
                f"| {source_link} | {usage.property_name} | {usage.source_domain} |"
            )

        lines.append("")

    # Source files
    link_prefix = f"../../../artifacts/{domain}/{version_info}"
    source_lines = _build_source_lines(domain, link_prefix)
    lines.extend(["## Source", ""])
    if source_lines:
        lines.extend(source_lines)
    else:
        lines.append("- (No source artifacts found)")
    lines.append("")

    return "\n".join(lines)


def _format_cardinality(min_count: Optional[str], max_count: Optional[str]) -> str:
    """Format cardinality string."""
    min_val = min_count or "0"
    max_val = max_count or "*"
    if min_val == max_val:
        return min_val
    return f"{min_val}..{max_val}"


def _format_property_type(
    prop: PropertyInfo, all_classes: Dict[str, Dict[str, ClassInfo]]
) -> str:
    """Format property type with links."""
    if prop.datatype:
        # XSD datatype
        return f"`{local_name(prop.datatype)}`"

    if prop.class_ref:
        return _format_class_link(prop.class_ref, all_classes)

    if prop.node_ref:
        return _format_class_link(prop.node_ref, all_classes)

    return "-"


def _format_class_link(
    class_iri: str, all_classes: Dict[str, Dict[str, ClassInfo]]
) -> str:
    """Format a class reference as a link."""
    class_name = local_name(class_iri)
    domain = extract_domain_from_iri(class_iri)

    if domain in EXTERNAL_DOMAINS:
        ext = EXTERNAL_DOMAINS[domain]
        url = ext["class_url"].format(**{"class": class_name})
        return f"[{class_name}]({url}){{ target=_blank }}"

    if domain and domain in all_classes and class_iri in all_classes[domain]:
        return f"[{class_name}](../{domain}/{safe_filename(class_name)}.md)"

    return class_name


def generate_domain_index(
    domain: str, classes: Dict[str, ClassInfo], version_info: str
) -> str:
    """Generate index page for a domain's classes."""
    lines = [
        f"# {domain} Classes",
        "",
        f"This domain defines {len(classes)} classes.",
        "",
        "## Class List",
        "",
        "| Class | Description |",
        "|-------|-------------|",
    ]

    for class_info in sorted(classes.values(), key=lambda c: c.label.lower()):
        class_name = local_name(class_info.iri)
        desc = (class_info.comment or "").replace("\n", " ").replace("|", "\\|")
        if len(desc) > 80:
            desc = desc[:77] + "..."
        lines.append(
            f"| [{class_info.label}]({safe_filename(class_name)}.md) | {desc} |"
        )

    artifacts_prefix = f"../../../artifacts/{domain}/{version_info}"
    domain_dir = ARTIFACTS_DIR / domain
    lines.extend(["", "## Artifacts", ""])
    if domain_dir.exists():
        owl_files = sorted(domain_dir.glob("*.owl.ttl"))
        shacl_files = sorted(domain_dir.glob("*.shacl.ttl"))
        context_files = sorted(domain_dir.glob("*.context.jsonld"))

        for owl_file in owl_files:
            lines.append(
                f"- OWL: [{owl_file.name}]({artifacts_prefix}/{owl_file.name})"
            )
        for shacl_file in shacl_files:
            lines.append(
                f"- SHACL: [{shacl_file.name}]({artifacts_prefix}/{shacl_file.name})"
            )
        for context_file in context_files:
            lines.append(
                f"- Context: [{context_file.name}]({artifacts_prefix}/{context_file.name})"
            )
    else:
        lines.append("- (No artifacts found)")
    lines.append("")

    return "\n".join(lines)


def generate_gx_redirect_page() -> str:
    """Generate redirect page for gx domain."""
    ext = EXTERNAL_DOMAINS["gx"]
    return f"""# Gaia-X Ontology

The Gaia-X ontology is maintained by the Gaia-X community. This project extends
and references the official Gaia-X types.

## Official Documentation

For complete class definitions, interactive visualizations, and the latest
specifications, please visit the official documentation:

**[{ext['url']}]({ext['url']}){{ .md-button .md-button--primary target=_blank }}**

## Common Classes Referenced

The following Gaia-X classes are commonly referenced by ENVITED-X ontologies:

- [LegalPerson]({ext['class_url'].format(**{'class': 'LegalPerson'})}){{ target=_blank }}
- [ServiceOffering]({ext['class_url'].format(**{'class': 'ServiceOffering'})}){{ target=_blank }}
- [DataResource]({ext['class_url'].format(**{'class': 'DataResource'})}){{ target=_blank }}
- [Participant]({ext['class_url'].format(**{'class': 'Participant'})}){{ target=_blank }}
"""


def _build_source_lines(domain: str, link_prefix: str) -> List[str]:
    """
    Build Source section links based on actual artifact files.

    Args:
        domain: Ontology domain name
        link_prefix: Relative link prefix to artifacts directory

    Returns:
        List of markdown list items for source files
    """
    domain_dir = ARTIFACTS_DIR / domain
    lines: List[str] = []

    if not domain_dir.exists():
        return lines

    standard_owl = domain_dir / f"{domain}.owl.ttl"
    owl_files = (
        [standard_owl]
        if standard_owl.exists()
        else sorted(domain_dir.glob("*.owl.ttl"))
    )

    shacl_files = sorted(domain_dir.glob("*.shacl.ttl"))
    context_files = sorted(domain_dir.glob("*.context.jsonld"))

    for owl_file in owl_files:
        lines.append(f"- OWL: [`{owl_file.name}`]({link_prefix}/{owl_file.name})")

    for shacl_file in shacl_files:
        lines.append(f"- SHACL: [`{shacl_file.name}`]({link_prefix}/{shacl_file.name})")

    for context_file in context_files:
        lines.append(
            f"- Context: [`{context_file.name}`]({link_prefix}/{context_file.name})"
        )

    return lines


def generate_classes_index(all_domains: List[str]) -> str:
    """Generate main classes index page."""
    lines = [
        "# Ontology Classes",
        "",
        "Browse classes by domain:",
        "",
    ]

    for domain in sorted(all_domains):
        if domain in EXTERNAL_DOMAINS:
            ext = EXTERNAL_DOMAINS[domain]
            lines.append(
                f"- **[{domain}]({domain}/index.md)** - {ext['name']} (external)"
            )
        else:
            lines.append(f"- **[{domain}]({domain}/index.md)**")

    lines.extend(
        [
            "",
            "## Interactive Visualization",
            "",
            "Each class page includes an interactive diagram showing:",
            "",
            "- Class inheritance relationships",
            "- Object property connections",
            "- Cross-domain references",
            "",
            "Click on any node to see details, or double-click to navigate to that class page.",
            "",
        ]
    )

    return "\n".join(lines)


def generate_all_class_pages(domains: Optional[List[str]] = None) -> None:
    """
    Generate class pages for all (or specified) domains.

    Args:
        domains: Optional list of domains to process. If None, process all.
    """
    if not ARTIFACTS_DIR.exists():
        logger.error("Artifacts directory not found: %s", ARTIFACTS_DIR)
        return

    # Discover domains
    available_domains = []
    for domain_dir in sorted(ARTIFACTS_DIR.iterdir()):
        if not domain_dir.is_dir():
            continue
        owl_file = domain_dir / f"{domain_dir.name}.owl.ttl"
        if owl_file.exists():
            available_domains.append(domain_dir.name)

    if domains:
        available_domains = [d for d in available_domains if d in domains]

    logger.info("Processing %d domains: %s", len(available_domains), available_domains)

    # First pass: extract all classes
    all_classes: Dict[str, Dict[str, ClassInfo]] = {}
    domain_versions: Dict[str, str] = {}

    for domain in available_domains:
        if domain in EXTERNAL_DOMAINS:
            continue  # Skip external domains

        domain_dir = ARTIFACTS_DIR / domain
        owl_file = domain_dir / f"{domain}.owl.ttl"
        shacl_file = domain_dir / f"{domain}.shacl.ttl"

        if not owl_file.exists():
            logger.warning("OWL file not found: %s", owl_file)
            continue

        # Parse and extract
        owl_graph = parse_owl_file(owl_file)
        version_info = _extract_version_info(owl_graph)
        domain_versions[domain] = version_info
        classes = extract_classes(owl_graph, domain)

        if shacl_file.exists():
            shacl_graph = parse_shacl_file(shacl_file)
            extract_properties(shacl_graph, classes)

        all_classes[domain] = classes

    # Build usages index from direct properties only
    usages_index = build_usages_index(all_classes)
    property_paths_by_domain = {
        domain: collect_property_paths(classes)
        for domain, classes in all_classes.items()
    }

    # Expand properties with inheritance for rendering
    for classes in all_classes.values():
        apply_inherited_properties(classes)

    # Create output directory
    if CLASSES_DIR.exists():
        shutil.rmtree(CLASSES_DIR)
    CLASSES_DIR.mkdir(parents=True, exist_ok=True)

    # Generate pages for each domain
    all_domain_names = list(all_classes.keys()) + list(EXTERNAL_DOMAINS.keys())

    for domain, classes in all_classes.items():
        domain_dir = CLASSES_DIR / domain
        domain_dir.mkdir(exist_ok=True)

        # Generate index
        index_content = generate_domain_index(
            domain, classes, domain_versions.get(domain, "unknown")
        )
        (domain_dir / "index.md").write_text(index_content)

        # Generate class pages
        for class_iri, class_info in classes.items():
            class_name = local_name(class_iri)
            filename = f"{safe_filename(class_name)}.md"
            content = render_class_page(
                class_info,
                all_classes,
                usages_index,
                domain_versions.get(domain, "unknown"),
                property_paths_by_domain,
            )
            (domain_dir / filename).write_text(content)

        logger.info("Generated %d class pages for %s", len(classes), domain)

    # Generate gx redirect
    gx_dir = CLASSES_DIR / "gx"
    gx_dir.mkdir(exist_ok=True)
    (gx_dir / "index.md").write_text(generate_gx_redirect_page())
    logger.info("Generated gx redirect page")

    # Generate main index
    (CLASSES_DIR / "index.md").write_text(generate_classes_index(all_domain_names))
    logger.info("Generated classes index")


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    parser.add_argument(
        "--domain",
        "-d",
        nargs="+",
        help="Specific domains to process (default: all)",
    )

    args = parser.parse_args()

    if args.verbose:
        import logging

        logging.getLogger().setLevel(logging.DEBUG)

    generate_all_class_pages(args.domain)
    print("Class page generation complete!")


if __name__ == "__main__":
    main()
