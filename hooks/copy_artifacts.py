#!/usr/bin/env python3
"""
MkDocs Hook: Copy Artifacts

Copies ontology artifact files (.ttl) to docs/artifacts/ during build,
making them accessible for client-side parsing and visualization.

NOTES:
- Excludes gx/ domain (redirects to official Gaia-X documentation)
- Only copies .owl.ttl and .shacl.ttl files
- Creates directory structure matching artifacts/
"""

import shutil
from pathlib import Path

# Domains that redirect to external documentation
EXTERNAL_DOMAINS = {"gx"}


def on_pre_build(config, **kwargs):
    """
    MkDocs hook called before build starts.

    Copies artifact TTL files to docs/artifacts/ for client-side access.
    """
    docs_dir = Path(config["docs_dir"])
    artifacts_src = docs_dir.parent / "artifacts"
    artifacts_dst = docs_dir / "artifacts"

    if not artifacts_src.exists():
        print(f"[copy_artifacts] Warning: {artifacts_src} not found")
        return

    # Clean existing artifacts in docs
    if artifacts_dst.exists():
        shutil.rmtree(artifacts_dst)

    # Copy TTL files for each domain (excluding external domains)
    copied_count = 0
    for domain_dir in artifacts_src.iterdir():
        if not domain_dir.is_dir():
            continue

        domain_name = domain_dir.name
        if domain_name in EXTERNAL_DOMAINS:
            print(f"[copy_artifacts] Skipping external domain: {domain_name}")
            continue

        # Find TTL files in domain
        ttl_files = list(domain_dir.glob("*.ttl"))
        if not ttl_files:
            continue

        # Create destination directory
        dst_domain_dir = artifacts_dst / domain_name
        dst_domain_dir.mkdir(parents=True, exist_ok=True)

        # Copy TTL files
        for ttl_file in ttl_files:
            dst_file = dst_domain_dir / ttl_file.name
            shutil.copy2(ttl_file, dst_file)
            copied_count += 1

    print(f"[copy_artifacts] Copied {copied_count} TTL files to docs/artifacts/")


def on_post_build(config, **kwargs):
    """
    MkDocs hook called after build completes.

    Cleans up artifacts from docs/ to keep source clean.
    """
    # Don't clean up - the files are needed in the built site
    # The docs/artifacts/ folder is in .gitignore anyway
    pass
