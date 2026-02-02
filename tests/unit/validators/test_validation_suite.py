#!/usr/bin/env python3
"""
Unit tests for src.tools.validators.validation_suite.
"""

from pathlib import Path

from src.tools.validators import validation_suite


def test_parse_gitignore_patterns(temp_dir: Path):
    gitignore = temp_dir / ".gitignore"
    gitignore.write_text(
        "\n".join(
            [
                "# comment",
                "dist/",
                "build/",
                "file.txt",
            ]
        )
    )
    # Create directories so they are detected
    (temp_dir / "dist").mkdir()
    (temp_dir / "build").mkdir()
    ignored = validation_suite.parse_gitignore_patterns(temp_dir)
    assert "dist" in ignored
    assert "build" in ignored
    assert "file.txt" not in ignored
