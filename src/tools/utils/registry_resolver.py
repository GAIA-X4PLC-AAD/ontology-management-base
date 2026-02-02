#!/usr/bin/env python3
"""
Registry-based resolution for ontology and SHACL file paths.

The RegistryResolver loads the registry.json configuration file and provides
methods to resolve:
- Ontology domains to their OWL file paths
- RDF types to the domains they belong to
- SHACL shapes for a given domain
- Fixture IRIs to concrete URIs

This is a domain-agnostic utility used primarily by the SHACL validation
pipeline (see src.tools.validators.shacl) but designed to be reusable by
any component that needs registry-based path resolution.

Key Features:
  - Uses docs/registry.json as single source of truth
  - Returns repository-relative paths (strings) by default
  - Supports fixture IRI resolution for test data
  - No filesystem scanning required

Usage:
    from src.tools.utils import RegistryResolver

    resolver = RegistryResolver()
    owl_path = resolver.get_ontology_path("general")
    shacl_paths = resolver.get_shacl_paths("general")

    # Discover required schemas based on RDF types
    rdf_types = {"https://w3id.org/ascs-ev/envited-x/scenario/v5/Scenario"}
    ontology_paths, shacl_paths = resolver.discover_required_schemas(rdf_types)

See also:
    - docs/registry.json: Registry configuration file
    - src.tools.validators.shacl: Main consumer of this utility
"""

import json
import warnings
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple


class RegistryResolver:
    """
    Resolves ontology files using docs/registry.json.
    Loads fixture mappings from unified test catalog (tests/catalog-v001.xml).

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
        self._catalog: Dict[str, Dict] = {}  # Full catalog (test-data + fixtures)
        self._fixtures_catalog: Dict[str, str] = {}  # Legacy: fixture IRIs only
        self._iri_to_domain: Dict[str, str] = {}

        self._load_registry()
        self._load_catalog()  # Replaces _load_fixtures_catalog
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

    def _load_catalog(self) -> None:
        """
        Load unified test catalog for test data discovery and fixture resolution.

        Loads all catalog entries including test-data, fixtures, and other categories.
        Maintains backward compatibility with _fixtures_catalog for fixture IRI resolution.
        """
        catalog_path = self.root_dir / "tests" / "catalog-v001.xml"

        # Fallback to legacy fixtures catalog if unified doesn't exist
        if not catalog_path.exists():
            catalog_path = self.root_dir / "tests" / "fixtures" / "catalog-v001.xml"

        if not catalog_path.exists():
            return

        try:
            tree = ET.parse(catalog_path)
            root = tree.getroot()
            ns = {"cat": "urn:oasis:names:tc:entity:xmlns:xml:catalog"}

            # Parse with namespace first
            for uri_elem in root.findall("cat:uri", ns):
                test_id = uri_elem.get("name")
                path = uri_elem.get("uri")
                domain = uri_elem.get("domain")
                test_type = uri_elem.get("test-type")
                category = uri_elem.get("category")

                if test_id and path:
                    self._catalog[test_id] = {
                        "path": path,
                        "domain": domain,
                        "test_type": test_type,
                        "category": category,
                    }

                    # Maintain legacy fixtures catalog for IRI resolution
                    if category == "fixture":
                        self._fixtures_catalog[test_id] = path

            # Try without namespace if nothing found
            if not self._catalog:
                for uri_elem in root.findall("uri"):
                    test_id = uri_elem.get("name")
                    path = uri_elem.get("uri")
                    domain = uri_elem.get("domain")
                    test_type = uri_elem.get("test-type")
                    category = uri_elem.get("category")

                    if test_id and path:
                        self._catalog[test_id] = {
                            "path": path,
                            "domain": domain,
                            "test_type": test_type,
                            "category": category,
                        }

                        # Legacy fixture handling
                        if not category or category == "fixture":
                            if not path.startswith("tests/"):
                                path = f"tests/fixtures/{path}"
                            self._fixtures_catalog[test_id] = path

        except Exception as e:
            warnings.warn(f"Could not parse test catalog: {e}")

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

    def get_base_ontology_paths(self) -> List[str]:
        """
        Get paths to base ontologies required for RDFS inference.

        Base ontologies (RDF, RDFS, OWL, SKOS, etc.) are registered in
        the imports/ directory and listed in the registry's base_ontologies section.

        Returns:
            List of repository-relative paths to base ontology files
        """
        base_ontologies = self._registry.get("base_ontologies", [])
        # Return sorted and deduplicated list
        return sorted(set(base_ontologies))

    # =========================================================================
    # Test Catalog Methods
    # =========================================================================

    def get_test_files(
        self, domain: str, test_type: str = None, category: str = "test-data"
    ) -> List[Path]:
        """
        Get test files for a specific domain from the catalog.

        Args:
            domain: Domain name (e.g., "scenario", "manifest")
            test_type: Optional filter: "valid", "invalid", "custom", or None for all
            category: Category filter: "test-data" (default), "fixture", etc.

        Returns:
            List of absolute paths to test files
        """
        test_files = []

        for test_id, metadata in self._catalog.items():
            if (
                metadata.get("category") == category
                and metadata.get("domain") == domain
            ):
                if test_type is None or metadata.get("test_type") == test_type:
                    file_path = self.root_dir / metadata["path"]
                    if file_path.exists():
                        test_files.append(file_path)

        return sorted(test_files)

    def get_test_domains(self, category: str = "test-data") -> List[str]:
        """
        Get list of all test domains in the catalog.

        Args:
            category: Category filter (default: "test-data")

        Returns:
            Sorted list of domain names
        """
        domains = set()
        for metadata in self._catalog.values():
            if metadata.get("category") == category:
                domain = metadata.get("domain")
                if domain:
                    domains.add(domain)
        return sorted(domains)

    def is_catalog_loaded(self) -> bool:
        """
        Check if catalog is loaded and has entries.

        Returns:
            True if catalog has entries, False otherwise
        """
        return len(self._catalog) > 0

    def add_temporary_test_entries(
        self, domain: str, file_paths: List[Path], test_type: str = "valid"
    ) -> None:
        """
        Add temporary catalog entries for custom file paths.

        Useful for validating arbitrary files using catalog infrastructure.

        Args:
            domain: Temporary domain name to use
            file_paths: List of file paths to add to catalog
            test_type: Test type identifier (default: "valid")
        """
        for i, file_path in enumerate(file_paths):
            file_path = Path(file_path)
            if not file_path.is_absolute():
                file_path = (self.root_dir / file_path).resolve()

            # Create relative path from root
            try:
                rel_path = file_path.relative_to(self.root_dir)
            except ValueError:
                # File is outside repo, use absolute path
                rel_path = file_path

            test_id = f"temporary:{domain}:file{i:03d}"
            self._catalog[test_id] = {
                "path": str(rel_path),
                "domain": domain,
                "test_type": test_type,
                "category": "test-data",
            }

    def create_temporary_domain(self, paths: List[str]) -> Optional[str]:
        """
        Create a temporary domain from file paths for validation.

        Collects JSON-LD files from paths and adds them as temporary catalog entries.

        Args:
            paths: List of file or directory paths

        Returns:
            Temporary domain name, or None if no files found
        """
        import hashlib

        from src.tools.validators.validate_data_conformance import collect_jsonld_files

        # Generate unique domain name from paths
        path_hash = hashlib.md5("|".join(sorted(paths)).encode()).hexdigest()[:8]
        temp_domain = f"custom-path-{path_hash}"

        # Collect all JSON-LD files from provided paths
        jsonld_files = collect_jsonld_files(paths)

        if not jsonld_files:
            return None

        # Convert to Path objects
        file_paths = [Path(f) for f in jsonld_files]

        # Add temporary entries to catalog
        self.add_temporary_test_entries(temp_domain, file_paths, test_type="valid")

        print(
            f"📋 Created temporary domain '{temp_domain}' with {len(file_paths)} file(s)",
            flush=True,
        )

        return temp_domain

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
