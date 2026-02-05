#!/usr/bin/env python3
"""
Unit tests for src.tools.core.iri_utils module.
"""

from src.tools.core.iri_utils import (
    extract_prefix_from_context,
    get_local_name,
    get_namespace,
    iri_to_domain_hint,
    is_did_web,
    matches_namespace,
    normalize_iri,
    parse_did_web,
)


class TestGetLocalName:
    """Tests for get_local_name function."""

    def test_extracts_from_hash_uri(self):
        """Should extract local name after # delimiter."""
        result = get_local_name("http://example.org/ontology#MyClass")
        assert result == "MyClass"

    def test_extracts_from_slash_uri(self):
        """Should extract local name after last / delimiter."""
        result = get_local_name("http://example.org/ontology/MyClass")
        assert result == "MyClass"

    def test_lowercase_option(self):
        """Should convert to lowercase when option is True."""
        result = get_local_name("http://example.org/ontology#MyClass", lowercase=True)
        assert result == "myclass"

    def test_preserves_case_by_default(self):
        """Should preserve case by default."""
        result = get_local_name("http://example.org/ontology#MyClass")
        assert result == "MyClass"

    def test_handles_uri_with_multiple_hashes(self):
        """Should use last # as delimiter."""
        result = get_local_name("http://example.org#fragment#LocalName")
        assert result == "LocalName"

    def test_handles_uri_ending_with_slash(self):
        """Should return empty string for URI ending with slash."""
        result = get_local_name("http://example.org/ontology/")
        assert result == ""

    def test_handles_simple_string(self):
        """Should handle string without delimiters."""
        result = get_local_name("JustAName")
        assert result == "JustAName"


class TestGetNamespace:
    """Tests for get_namespace function."""

    def test_extracts_hash_namespace(self):
        """Should extract namespace including # for hash URIs."""
        result = get_namespace("http://example.org/ontology#MyClass")
        assert result == "http://example.org/ontology#"

    def test_extracts_slash_namespace(self):
        """Should extract namespace including / for slash URIs."""
        result = get_namespace("http://example.org/ontology/MyClass")
        assert result == "http://example.org/ontology/"

    def test_handles_uri_with_multiple_slashes(self):
        """Should use last / as delimiter."""
        result = get_namespace("http://example.org/path/to/MyClass")
        assert result == "http://example.org/path/to/"


class TestIsDidWeb:
    """Tests for is_did_web function."""

    def test_returns_true_for_did_web(self):
        """Should return True for did:web: URIs."""
        assert is_did_web("did:web:registry.gaia-x.eu:participant:123")

    def test_returns_false_for_http_uri(self):
        """Should return False for http URIs."""
        assert not is_did_web("http://example.org/resource")

    def test_returns_false_for_https_uri(self):
        """Should return False for https URIs."""
        assert not is_did_web("https://example.org/resource")

    def test_returns_false_for_empty_string(self):
        """Should return False for empty string."""
        assert not is_did_web("")

    def test_returns_false_for_other_did_method(self):
        """Should return False for other DID methods."""
        assert not is_did_web(
            "did:key:z6MkhaXgBZDvotDkL5257faiztiGiC2QtKLGpbnnEGta2doK"
        )


class TestParseDidWeb:
    """Tests for parse_did_web function."""

    def test_parses_full_did_web(self):
        """Should parse full did:web: URI with type and id."""
        result = parse_did_web("did:web:registry.gaia-x.eu:LegalPerson:abc123")

        assert result is not None
        assert result["host"] == "registry.gaia-x.eu"
        assert result["type"] == "LegalPerson"
        assert result["id"] == "abc123"
        assert result["path"] == "LegalPerson:abc123"

    def test_parses_did_web_with_host_only(self):
        """Should parse did:web: with host only."""
        result = parse_did_web("did:web:example.org")

        assert result is not None
        assert result["host"] == "example.org"
        assert result["path"] == ""
        assert result["type"] is None

    def test_returns_none_for_non_did_web(self):
        """Should return None for non did:web: URIs."""
        result = parse_did_web("http://example.org/resource")
        assert result is None

    def test_handles_url_encoded_host(self):
        """Should handle URL-encoded characters in host."""
        result = parse_did_web("did:web:example%2Eorg")
        assert result is not None
        assert result["host"] == "example.org"


class TestNormalizeIri:
    """Tests for normalize_iri function."""

    def test_adds_trailing_slash(self):
        """Should add trailing slash when missing."""
        result = normalize_iri("http://example.org/ontology")
        assert result == "http://example.org/ontology/"

    def test_preserves_existing_trailing_slash(self):
        """Should preserve existing trailing slash."""
        result = normalize_iri("http://example.org/ontology/")
        assert result == "http://example.org/ontology/"

    def test_removes_trailing_slash_when_specified(self):
        """Should remove trailing slash when trailing_slash=False."""
        result = normalize_iri("http://example.org/ontology/", trailing_slash=False)
        assert result == "http://example.org/ontology"

    def test_preserves_hash_uri(self):
        """Should not modify hash URIs."""
        result = normalize_iri("http://example.org/ontology#")
        assert result == "http://example.org/ontology#"


class TestIriToDomainHint:
    """Tests for iri_to_domain_hint function."""

    def test_extracts_domain_from_versioned_uri(self):
        """Should extract domain from versioned ontology URI."""
        result = iri_to_domain_hint("https://w3id.org/ascs-ev/envited-x/scenario/v5/")
        assert result == "scenario"

    def test_extracts_domain_from_simple_uri(self):
        """Should extract last path segment as domain."""
        result = iri_to_domain_hint("https://example.org/ontology/myontology")
        assert result == "myontology"

    def test_handles_uri_with_only_version(self):
        """Should skip version number and get previous segment."""
        result = iri_to_domain_hint("https://example.org/domain/v5")
        assert result == "domain"


class TestMatchesNamespace:
    """Tests for matches_namespace function."""

    def test_matches_hash_namespace(self):
        """Should match URI against hash namespace."""
        assert matches_namespace("http://ex.org/ont#Class", "http://ex.org/ont#")

    def test_matches_slash_namespace(self):
        """Should match URI against slash namespace."""
        assert matches_namespace("http://ex.org/ont/Class", "http://ex.org/ont/")

    def test_matches_namespace_without_terminator(self):
        """Should match when namespace doesn't have trailing # or /."""
        assert matches_namespace("http://ex.org/ont/Class", "http://ex.org/ont")

    def test_no_match_for_different_namespace(self):
        """Should not match when namespaces differ."""
        assert not matches_namespace("http://other.org/Class", "http://ex.org/ont")

    def test_no_partial_match(self):
        """Should not partially match namespace prefixes."""
        assert not matches_namespace(
            "http://ex.org/ontology/Class", "http://ex.org/ont"
        )


class TestExtractPrefixFromContext:
    """Tests for extract_prefix_from_context function."""

    def test_finds_matching_prefix(self):
        """Should find prefix that matches IRI."""
        context = {"gx": "https://w3id.org/gaia-x/", "ex": "http://example.org/"}
        result = extract_prefix_from_context(
            context, "https://w3id.org/gaia-x/LegalPerson"
        )
        assert result == "gx"

    def test_returns_none_when_no_match(self):
        """Should return None when no prefix matches."""
        context = {"gx": "https://w3id.org/gaia-x/"}
        result = extract_prefix_from_context(context, "http://other.org/Resource")
        assert result is None

    def test_handles_empty_context(self):
        """Should return None for empty context."""
        result = extract_prefix_from_context({}, "http://example.org/Resource")
        assert result is None

    def test_ignores_non_string_values(self):
        """Should ignore context entries with non-string values."""
        context = {
            "gx": "https://w3id.org/gaia-x/",
            "@vocab": {"@id": "http://example.org/"},  # non-string value
        }
        result = extract_prefix_from_context(context, "https://w3id.org/gaia-x/Type")
        assert result == "gx"
