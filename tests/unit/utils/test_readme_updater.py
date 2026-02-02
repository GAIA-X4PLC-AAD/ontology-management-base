#!/usr/bin/env python3
"""
Unit tests for src.tools.utils.readme_updater.
"""

from pathlib import Path

from src.tools.utils import readme_updater


def test_generate_table_sorted(monkeypatch, temp_dir: Path):
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE catalog PUBLIC "-//OASIS//DTD Entity Resolution XML Catalog V1.0//EN"
  "http://www.oasis-open.org/committees/entity/release/1.0/catalog.dtd">
<catalog xmlns="urn:oasis:names:tc:entity:xmlns:xml:catalog">
  <uri name="b" uri="b.owl.ttl"/>
  <uri name="a" uri="a.owl.ttl"/>
</catalog>
"""
    xml_path = temp_dir / "catalog-v001.xml"
    xml_path.write_text(xml)
    monkeypatch.setattr(readme_updater, "XML_FILE", str(xml_path))

    table = readme_updater.generate_table()
    assert "`a`" in table.splitlines()[2]


def test_update_readme_inserts_table(monkeypatch, temp_dir: Path):
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE catalog PUBLIC "-//OASIS//DTD Entity Resolution XML Catalog V1.0//EN"
  "http://www.oasis-open.org/committees/entity/release/1.0/catalog.dtd">
<catalog xmlns="urn:oasis:names:tc:entity:xmlns:xml:catalog">
  <uri name="a" uri="a.owl.ttl"/>
</catalog>
"""
    xml_path = temp_dir / "catalog-v001.xml"
    xml_path.write_text(xml)

    readme_path = temp_dir / "README.md"
    readme_path.write_text(
        "Header\n<!-- START_CATALOG_TABLE -->\nold\n<!-- END_CATALOG_TABLE -->\nFooter"
    )

    monkeypatch.setattr(readme_updater, "XML_FILE", str(xml_path))
    monkeypatch.setattr(readme_updater, "README_FILE", str(readme_path))

    readme_updater.update_readme()
    content = readme_path.read_text()
    assert "| `a` |" in content
