#!/usr/bin/env python3
"""
Unit tests for src.tools.utils.file_collector module.

Tests file collection utilities including:
- collect_files_by_extension
- collect_turtle_files
- collect_jsonld_files
- collect_files_by_pattern
- collect_ontology_files
- collect_test_files
- collect_ontology_bundles
"""

from pathlib import Path

import pytest  # noqa: F401

from src.tools.utils.file_collector import (
    collect_files_by_extension,
    collect_files_by_pattern,
    collect_jsonld_files,
    collect_ontology_bundles,
    collect_ontology_files,
    collect_test_files,
    collect_turtle_files,
)


class TestCollectFilesByExtension:
    """Tests for collect_files_by_extension function."""

    def test_empty_paths_returns_empty_list(self):
        """Empty input should return empty list."""
        result = collect_files_by_extension([], ".ttl")
        assert result == []

    def test_single_extension_string(self, temp_dir):
        """Test collecting files with a single extension as string."""
        (temp_dir / "file1.ttl").write_text("")
        (temp_dir / "file2.ttl").write_text("")
        (temp_dir / "file3.json").write_text("{}")

        result = collect_files_by_extension([temp_dir], ".ttl", return_pathlib=True)

        assert len(result) == 2
        assert all(f.suffix == ".ttl" for f in result)

    def test_multiple_extensions_set(self, temp_dir):
        """Test collecting files with multiple extensions as set."""
        (temp_dir / "file1.json").write_text("{}")
        (temp_dir / "file2.jsonld").write_text("{}")
        (temp_dir / "file3.ttl").write_text("")

        result = collect_files_by_extension(
            [temp_dir], {".json", ".jsonld"}, return_pathlib=True
        )

        assert len(result) == 2
        assert all(f.suffix in {".json", ".jsonld"} for f in result)

    def test_recursive_directory_walk(self, temp_dir):
        """Test that subdirectories are searched recursively."""
        subdir = temp_dir / "subdir"
        subdir.mkdir()
        (temp_dir / "root.json").write_text("{}")
        (subdir / "nested.json").write_text("{}")

        result = collect_files_by_extension([temp_dir], ".json", return_pathlib=True)

        assert len(result) == 2

    def test_single_file_input(self, temp_dir):
        """Test with a single file as input."""
        file_path = temp_dir / "single.ttl"
        file_path.write_text("")

        result = collect_files_by_extension([file_path], ".ttl", return_pathlib=True)

        assert len(result) == 1
        assert result[0] == file_path

    def test_wrong_extension_ignored(self, temp_dir, capsys):
        """Test that files with wrong extension are ignored with warning."""
        file_path = temp_dir / "wrong.json"
        file_path.write_text("{}")

        result = collect_files_by_extension([file_path], ".ttl", warn_on_invalid=True)

        assert len(result) == 0
        captured = capsys.readouterr()
        assert "Warning" in captured.err

    def test_sort_and_deduplicate(self, temp_dir):
        """Test sorting and deduplication of results."""
        (temp_dir / "b.json").write_text("{}")
        (temp_dir / "a.json").write_text("{}")

        result = collect_files_by_extension(
            [temp_dir, temp_dir],  # Duplicate path
            ".json",
            sort_and_deduplicate=True,
        )

        assert len(result) == 2
        # Should be sorted
        assert "a.json" in str(result[0])

    def test_return_strings_by_default(self, temp_dir):
        """Test that strings are returned by default."""
        (temp_dir / "test.ttl").write_text("")

        result = collect_files_by_extension([temp_dir], ".ttl")

        assert all(isinstance(f, str) for f in result)

    def test_return_pathlib_when_requested(self, temp_dir):
        """Test that Path objects are returned when requested."""
        (temp_dir / "test.ttl").write_text("")

        result = collect_files_by_extension([temp_dir], ".ttl", return_pathlib=True)

        assert all(isinstance(f, Path) for f in result)

    def test_nonexistent_path_warning(self, temp_dir, capsys):
        """Test warning for nonexistent paths."""
        result = collect_files_by_extension(
            [temp_dir / "nonexistent"], ".ttl", warn_on_invalid=True
        )

        assert result == []
        captured = capsys.readouterr()
        assert "Warning" in captured.err


class TestCollectTurtleFiles:
    """Tests for collect_turtle_files convenience function."""

    def test_collects_ttl_files(self, temp_dir):
        """Test that .ttl files are collected."""
        (temp_dir / "ontology.ttl").write_text("")
        (temp_dir / "shapes.shacl.ttl").write_text("")
        (temp_dir / "data.json").write_text("{}")

        result = collect_turtle_files([temp_dir], return_pathlib=True)

        assert len(result) == 2
        assert all(f.suffix == ".ttl" for f in result)


class TestCollectJsonldFiles:
    """Tests for collect_jsonld_files convenience function."""

    def test_collects_json_and_jsonld_files(self, temp_dir):
        """Test that both .json and .jsonld files are collected."""
        (temp_dir / "data.json").write_text("{}")
        (temp_dir / "context.jsonld").write_text("{}")
        (temp_dir / "ontology.ttl").write_text("")

        result = collect_jsonld_files([temp_dir], return_pathlib=True)

        assert len(result) == 2
        assert all(f.suffix in {".json", ".jsonld"} for f in result)


class TestCollectFilesByPattern:
    """Tests for collect_files_by_pattern function."""

    def test_glob_pattern(self, temp_dir):
        """Test glob pattern matching."""
        (temp_dir / "domain.shacl.ttl").write_text("")
        (temp_dir / "domain.owl.ttl").write_text("")
        (temp_dir / "other.ttl").write_text("")

        result = collect_files_by_pattern([temp_dir], "*.shacl.ttl")

        assert len(result) == 1
        assert "shacl" in str(result[0])

    def test_recursive_pattern(self, temp_dir):
        """Test recursive glob pattern."""
        subdir = temp_dir / "subdir"
        subdir.mkdir()
        (temp_dir / "root.json").write_text("{}")
        (subdir / "nested.json").write_text("{}")

        result = collect_files_by_pattern([temp_dir], "**/*.json")

        assert len(result) == 2


class TestCollectOntologyFiles:
    """Tests for collect_ontology_files function."""

    def test_finds_standard_files(self, temp_dir):
        """Test finding files with standard naming convention."""
        domain_dir = temp_dir / "manifest"
        domain_dir.mkdir()
        (domain_dir / "manifest.owl.ttl").write_text("")
        (domain_dir / "manifest.shacl.ttl").write_text("")
        (domain_dir / "manifest.context.jsonld").write_text("{}")

        result = collect_ontology_files(domain_dir)

        assert result["ontology"] is not None
        assert result["shacl"] is not None
        assert len(result["shacl"]) == 1
        assert result["context"] is not None

    def test_multiple_shacl_files(self, temp_dir):
        """Test collecting multiple SHACL files."""
        domain_dir = temp_dir / "domain"
        domain_dir.mkdir()
        (domain_dir / "domain.owl.ttl").write_text("")
        (domain_dir / "domain.shacl.ttl").write_text("")
        (domain_dir / "domain.extra.shacl.ttl").write_text("")

        result = collect_ontology_files(domain_dir)

        assert result["shacl"] is not None
        assert len(result["shacl"]) == 2

    def test_missing_files(self, temp_dir):
        """Test when some files are missing."""
        domain_dir = temp_dir / "incomplete"
        domain_dir.mkdir()
        (domain_dir / "incomplete.owl.ttl").write_text("")

        result = collect_ontology_files(domain_dir)

        assert result["ontology"] is not None
        assert result["shacl"] is None
        assert result["context"] is None


class TestCollectTestFiles:
    """Tests for collect_test_files function."""

    def test_collect_valid_files(self, temp_dir):
        """Test collecting files from valid/ subdirectory."""
        valid_dir = temp_dir / "valid"
        valid_dir.mkdir()
        (valid_dir / "test1.json").write_text("{}")
        (valid_dir / "test2.json").write_text("{}")

        result = collect_test_files(temp_dir, valid=True)

        assert len(result) == 2

    def test_collect_invalid_files(self, temp_dir):
        """Test collecting files from invalid/ subdirectory."""
        invalid_dir = temp_dir / "invalid"
        invalid_dir.mkdir()
        (invalid_dir / "fail1.json").write_text("{}")

        result = collect_test_files(temp_dir, valid=False)

        assert len(result) == 1

    def test_nonexistent_subdir(self, temp_dir):
        """Test when valid/invalid directory doesn't exist."""
        result = collect_test_files(temp_dir, valid=True)

        assert result == []


class TestCollectOntologyBundles:
    """Tests for collect_ontology_bundles function."""

    def test_discovers_bundles(self, temp_dir):
        """Test discovering ontology bundles."""
        domain_dir = temp_dir / "manifest"
        domain_dir.mkdir()
        (domain_dir / "manifest.owl.ttl").write_text("")
        (domain_dir / "manifest.shacl.ttl").write_text("")
        (domain_dir / "manifest.context.jsonld").write_text("{}")

        result = collect_ontology_bundles(temp_dir)

        assert "manifest" in result
        assert result["manifest"]["ontology"] is not None

    def test_skips_dirs_without_owl(self, temp_dir):
        """Test that directories without OWL file are skipped."""
        domain_dir = temp_dir / "incomplete"
        domain_dir.mkdir()
        (domain_dir / "incomplete.shacl.ttl").write_text("")

        result = collect_ontology_bundles(temp_dir)

        assert "incomplete" not in result

    def test_with_tests_dir(self, temp_dir):
        """Test bundle discovery with tests directory."""
        artifacts_dir = temp_dir / "artifacts"
        artifacts_dir.mkdir()
        domain_dir = artifacts_dir / "manifest"
        domain_dir.mkdir()
        (domain_dir / "manifest.owl.ttl").write_text("")

        tests_dir = temp_dir / "tests"
        tests_dir.mkdir()
        valid_dir = tests_dir / "manifest" / "valid"
        valid_dir.mkdir(parents=True)
        (valid_dir / "manifest_instance.json").write_text("{}")

        result = collect_ontology_bundles(artifacts_dir, tests_dir)

        assert "manifest" in result
        assert result["manifest"]["instance"] is not None

    def test_nonexistent_base_dir(self, temp_dir, capsys):
        """Test with nonexistent base directory."""
        result = collect_ontology_bundles(temp_dir / "nonexistent")

        assert result == {}
        captured = capsys.readouterr()
        assert "Warning" in captured.err
