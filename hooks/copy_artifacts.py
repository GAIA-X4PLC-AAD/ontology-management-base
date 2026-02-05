#!/usr/bin/env python3
"""
MkDocs Hook: Link Artifacts

Updates class page navigation and link paths before build.
Artifacts are referenced via raw GitHub URLs in generated docs.

NOTES:
- No file copying or symlinks (use raw URLs instead)
- Excludes gx/ domain (redirects to official Gaia-X documentation)
"""

from pathlib import Path

# Domains that redirect to external documentation
EXTERNAL_DOMAINS = {"gx"}


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


def on_post_build(config, **kwargs):
    """
    MkDocs hook called after build completes.
    """
    pass
