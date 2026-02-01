#!/usr/bin/env python3
"""
Registry-based file resolution using docs/registry.json.

This module provides utilities to discover and resolve ontology files using
the registry.json file as the single source of truth. This replaces the
catalog-based approach with a simpler, faster, and more maintainable solution.

Key Features:
  - Uses docs/registry.json as single source of truth
  - Returns repository-relative paths (strings) by default
  - Supports fixture IRI resolution for test data
  - No filesystem scanning required
"""

import json
import warnings
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple


class RegistryResolver:
    """
    Resolves ontology files using docs/registry.json.

    Usage:
        resolver = RegistryResolver(root_dir="/path/to/repo")
        owl_path = resolver.get_ontology_path("scenario")
        shacl_paths = resolver.get_shacl_paths("scenario")
        domains = resolver.list_domains()
    """

    def __init__(self, root_dir: Path = None):
        """
        Initialize the registry resolver.

        Args:
            root_dir: Root directory of the repository. Defaults to current directory.
        """
        self.root_dir = Path(root_dir or Path.cwd()).resolve()
        self._registry: Dict = {}
        self._fixtures_catalog: Dict[str, str] = {}
        self._iri_to_domain: Dict[str, str] = {}

        self._load_registry()
        self._load_fixtures_catalog()
        self._build_iri_index()

    def _load_registry(self) -> None:
        """Load docs/registry.json."""
        registry_path = self.root_dir / "docs" / "registry.json"
        if not registry_path.exists():
            warnings.warn(f"Registry file not found: {registry_path}")
            return

        try:
            with registry_path.open("r", encoding="utf-8") as f:
                self._registry = json.load(f)
        except Exception as e:
            warnings.warn(f"Could not load registry: {e}")

    def _load_fixtures_catalog(self) -> None:
        """Load tests/fixtures/catalog-v001.xml for fixture IRI resolution."""
        catalog_path = self.root_dir / "tests" / "fixtures" / "catalog-v001.xml"
        if not catalog_path.exists():
            return

        try:
            tree = ET.parse(catalog_path)
            root = tree.getroot()
            ns = {"cat": "urn:oasis:names:tc:entity:xmlns:xml:catalog"}

            for uri_elem in root.findall("cat:uri", ns):
                iri = uri_elem.get("name")
                relative_path = uri_elem.get("uri")
                if iri and relative_path:
                    # Store as relative to tests/fixtures/
                    self._fixtures_catalog[iri] = f"tests/fixtures/{relative_path}"

            # Also try without namespace
            for uri_elem in root.findall("uri"):
                iri = uri_elem.get("name")
                relative_path = uri_elem.get("uri")
                if iri and relative_path:
                    self._fixtures_catalog[iri] = f"tests/fixtures/{relative_path}"

        except Exception as e:
            warnings.warn(f"Could not parse fixtures catalog: {e}")

    def _build_iri_index(self) -> None:
        """Build IRI -> domain mapping from registry."""
        ontologies = self._registry.get("ontologies", {})
        for domain, info in ontologies.items():
            iri = info.get("iri")
            if iri:
                self._iri_to_domain[iri] = domain
                # Also index without trailing version
                base_iri = iri.rstrip("/")
                if base_iri != iri:
                    self._iri_to_domain[base_iri] = domain

    def _get_latest_version_files(self, domain: str) -> Optional[Dict]:
        """Get files dict for the latest version of a domain."""
        ontologies = self._registry.get("ontologies", {})
        if domain not in ontologies:
            return None

        info = ontologies[domain]
        latest = info.get("latest")
        if not latest:
            return None

        versions = info.get("versions", {})
        if latest not in versions:
            return None

        return versions[latest].get("files")

    # =========================================================================
    # Core Methods (return repo-relative paths as strings)
    # =========================================================================

    def list_domains(self) -> List[str]:
        """
        List all ontology domains available in the registry.

        Returns:
            List of domain names sorted alphabetically
        """
        return sorted(self._registry.get("ontologies", {}).keys())

    def get_ontology_path(self, domain: str) -> Optional[str]:
        """
        Get the ontology (.owl.ttl) file path for a domain.

        Args:
            domain: Domain name (e.g., "scenario", "hdmap")

        Returns:
            Repository-relative path to the ontology file, or None if not found
        """
        files = self._get_latest_version_files(domain)
        if not files:
            return None
        return files.get("ontology")

    def get_shacl_paths(self, domain: str) -> List[str]:
        """
        Get all SHACL shapes (.shacl.ttl) file paths for a domain.

        Args:
            domain: Domain name (e.g., "scenario", "survey")

        Returns:
            List of repository-relative paths to SHACL files
        """
        files = self._get_latest_version_files(domain)
        if not files:
            return []

        shacl = files.get("shacl")
        if not shacl:
            return []

        if isinstance(shacl, list):
            return shacl
        return [shacl]

    def get_context_path(self, domain: str) -> Optional[str]:
        """
        Get the JSON-LD context (.context.jsonld) file path for a domain.

        Args:
            domain: Domain name (e.g., "gx")

        Returns:
            Repository-relative path to the context file, or None if not found
        """
        files = self._get_latest_version_files(domain)
        if not files:
            return None
        return files.get("jsonld")

    def get_instance_path(self, domain: str) -> Optional[str]:
        """
        Get the instance file path for a domain.

        Args:
            domain: Domain name (e.g., "scenario")

        Returns:
            Repository-relative path to the instance file, or None if not found
        """
        files = self._get_latest_version_files(domain)
        if not files:
            return None
        return files.get("instance")

    def get_iri(self, domain: str) -> Optional[str]:
        """
        Get the IRI for a domain.

        Args:
            domain: Domain name (e.g., "scenario")

        Returns:
            IRI string, or None if not found
        """
        ontologies = self._registry.get("ontologies", {})
        if domain not in ontologies:
            return None
        return ontologies[domain].get("iri")

    # =========================================================================
    # Bulk Accessors
    # =========================================================================

    def get_all_ontology_paths(self) -> List[str]:
        """
        Get all ontology file paths from the registry.

        Returns:
            List of repository-relative paths to all ontology files
        """
        paths = []
        for domain in self.list_domains():
            path = self.get_ontology_path(domain)
            if path:
                paths.append(path)
        return sorted(paths)

    def get_all_shacl_paths(self) -> List[str]:
        """
        Get all SHACL shape file paths from the registry.

        Returns:
            List of repository-relative paths to all SHACL files
        """
        paths = []
        for domain in self.list_domains():
            paths.extend(self.get_shacl_paths(domain))
        return sorted(set(paths))

    # =========================================================================
    # IRI Resolution
    # =========================================================================

    def resolve_type_to_domain(self, rdf_type: str) -> Optional[str]:
        """
        Map an RDF type IRI to its domain name.

        Args:
            rdf_type: RDF type IRI (e.g., "https://w3id.org/ascs-ev/envited-x/scenario/v5/Scenario")

        Returns:
            Domain name if found, None otherwise
        """
        # Check exact match first
        if rdf_type in self._iri_to_domain:
            return self._iri_to_domain[rdf_type]

        # Check prefix match
        for iri, domain in self._iri_to_domain.items():
            if rdf_type.startswith(iri.rstrip("/") + "/"):
                return domain
            if rdf_type.startswith(iri.rstrip("#") + "#"):
                return domain

        return None

    def resolve_fixture_iri(self, iri: str) -> Optional[str]:
        """
        Resolve a fixture IRI to its local file path.

        Args:
            iri: Fixture IRI (e.g., "did:web:registry.gaia-x.eu:participant:...")

        Returns:
            Repository-relative path to the fixture file, or None if not found
        """
        return self._fixtures_catalog.get(iri)

    # =========================================================================
    # Path Helpers
    # =========================================================================

    def to_absolute(self, rel_path: str) -> Path:
        """
        Convert a repository-relative path to an absolute path.

        Args:
            rel_path: Repository-relative path string

        Returns:
            Absolute Path object
        """
        return self.root_dir / rel_path

    def to_relative(self, abs_path: Path) -> str:
        """
        Convert an absolute path to a repository-relative string.

        Args:
            abs_path: Absolute Path object

        Returns:
            Repository-relative path string
        """
        try:
            return str(abs_path.relative_to(self.root_dir))
        except ValueError:
            return str(abs_path)

    # =========================================================================
    # Discovery Methods
    # =========================================================================

    def discover_required_schemas(
        self, rdf_types: Set[str]
    ) -> Tuple[List[str], List[str]]:
        """
        Discover required ontology and SHACL files based on RDF types.

        Args:
            rdf_types: Set of rdf:type IRIs found in the data

        Returns:
            Tuple of (ontology_paths, shacl_paths) as repository-relative strings
        """
        ontology_paths = []
        shacl_paths = []
        domains_found = set()

        for rdf_type in rdf_types:
            domain = self.resolve_type_to_domain(rdf_type)
            if domain and domain not in domains_found:
                domains_found.add(domain)

                ont_path = self.get_ontology_path(domain)
                if ont_path:
                    ontology_paths.append(ont_path)

                shacl_paths.extend(self.get_shacl_paths(domain))

        return sorted(set(ontology_paths)), sorted(set(shacl_paths))

    def get_base_ontology_paths(self) -> List[str]:
        """
        Get paths to base ontologies (RDF, RDFS, OWL, SKOS).

        These are required for RDFS inference and SHACL validation.

        Returns:
            List of repository-relative paths to base ontology files
        """
        base_files = [
            "imports/rdf/rdf.owl.ttl",
            "imports/rdfs/rdfs.owl.ttl",
            "imports/owl/owl.owl.ttl",
            "imports/skos/skos.owl.ttl",
        ]
        return [f for f in base_files if (self.root_dir / f).exists()]

    # =========================================================================
    # Info Methods
    # =========================================================================

    def get_registry_info(self) -> Dict:
        """
        Get information about the loaded registry.

        Returns:
            Dictionary with registry statistics and info
        """
        return {
            "root_dir": str(self.root_dir),
            "registry_version": self._registry.get("version"),
            "domains_available": len(self.list_domains()),
            "total_ontologies": len(self.get_all_ontology_paths()),
            "total_shacl_files": len(self.get_all_shacl_paths()),
            "fixture_mappings": len(self._fixtures_catalog),
        }


def print_registry_info(resolver: RegistryResolver) -> None:
    """
    Print registry information to console.

    Args:
        resolver: RegistryResolver instance
    """
    info = resolver.get_registry_info()
    print("Registry Resolver Information:")
    print(f"   Root: {info['root_dir']}")
    print(f"   Version: {info['registry_version']}")
    print(f"   Domains Available: {info['domains_available']}")
    print(f"   Total Ontologies: {info['total_ontologies']}")
    print(f"   Total SHACL Files: {info['total_shacl_files']}")
    print(f"   Fixture Mappings: {info['fixture_mappings']}")

    domains = resolver.list_domains()
    if domains:
        print(f"\nAvailable Domains ({len(domains)}):")
        for domain in domains[:10]:
            ont = resolver.get_ontology_path(domain)
            ont_status = "Y" if ont else "N"
            shacl_count = len(resolver.get_shacl_paths(domain))
            shacl_status = f"{shacl_count}" if shacl_count else "N"
            ctx = resolver.get_context_path(domain)
            ctx_status = "Y" if ctx else "N"
            print(
                f"   {domain}: OWL={ont_status} SHACL={shacl_status} Context={ctx_status}"
            )
        if len(domains) > 10:
            print(f"   ... and {len(domains) - 10} more")


if __name__ == "__main__":
    resolver = RegistryResolver()
    print_registry_info(resolver)

    print("\nTesting discovery for 'scenario' domain:")
    ont = resolver.get_ontology_path("scenario")
    shacl = resolver.get_shacl_paths("scenario")
    print(f"   Ontology: {ont}")
    print(f"   SHACL: {shacl}")
