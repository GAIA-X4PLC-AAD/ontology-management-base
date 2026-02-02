#!/usr/bin/env python3
"""
Validation Suite for Ontology Management Base

This script provides a unified interface for running various validation checks
on ontology artifacts, SHACL shapes, and test data.

USAGE MODES:
===========

1. CATALOG-BASED VALIDATION (Domain Mode)
   Uses the test catalog (tests/catalog-v001.xml) to discover and validate files.

   Examples:
   - Validate all domains:
     python3 -m src.tools.validators.validation_suite --run all

   - Check syntax for specific domain(s):
     python3 -m src.tools.validators.validation_suite --run check-syntax --domain manifest
     python3 -m src.tools.validators.validation_suite --run check-syntax --domain manifest scenario

   - Check artifact coherence for domain(s):
     python3 -m src.tools.validators.validation_suite --run check-artifact-coherence --domain hdmap

   - Validate data conformance for domain(s):
     python3 -m src.tools.validators.validation_suite --run check-data-conformance --domain manifest


2. FILE-BASED VALIDATION (Path Mode)
   Validates arbitrary files or directories without requiring catalog entries.

   Examples:
   - Check syntax of specific file(s):
     python3 -m src.tools.validators.validation_suite --run check-syntax --path myfile.json
     python3 -m src.tools.validators.validation_suite --run check-syntax --path file1.json file2.ttl

   - Check syntax of directory:
     python3 -m src.tools.validators.validation_suite --run check-syntax --path /path/to/directory/

   - Validate data conformance for specific files:
     python3 -m src.tools.validators.validation_suite --run check-data-conformance --path tests/data/manifest/valid/

   - Check artifact coherence for custom ontology (requires naming convention):
     python3 -m src.tools.validators.validation_suite --run check-artifact-coherence --path /my/ontology/ --domain custom-name


VALIDATION MODES:
================

--run all                        Run all validation checks (syntax, coherence, conformance, failing tests)
--run check-syntax               Check JSON-LD and Turtle syntax only
--run check-artifact-coherence   Validate SHACL target classes against OWL class definitions
--run check-data-conformance     Validate JSON-LD data against SHACL constraints
--run check-failing-tests        Run tests expected to fail with specific error messages


OPTIONS:
========

--domain DOMAIN [DOMAIN ...]     Specify domain name(s) from catalog (e.g., "manifest", "scenario")
--path PATH [PATH ...]           Specify file(s) or directory path(s) to validate
--no-catalog                     Disable catalog-based discovery (file system only)


NOTES:
======

- When using --domain, the validator uses catalog entries and standard directory structure
- When using --path, the validator works with arbitrary files/directories
- --domain and --path can be combined for some validation modes
- All file paths in output are shown relative to repository root for privacy/portability
- Syntax checks validate well-formedness only (not semantic correctness)
- Conformance checks require SHACL shapes to be discoverable via catalog or naming conventions
"""

import argparse
import io
import os
import sys
from pathlib import Path
from typing import List

from src.tools.utils.print_formatter import normalize_text
from src.tools.utils.registry_resolver import RegistryResolver
from src.tools.validators.shacl.validator import (
    validate_data_conformance as validate_data_conformance,
)
from src.tools.validators.validate_artifact_coherence import (
    validate_artifact_coherence,
)
from src.tools.validators.validate_data_conformance import collect_jsonld_files
from src.tools.validators.verify_json_syntax import (
    check_json_wellformedness,
    verify_json_syntax,
)
from src.tools.validators.verify_turtle_syntax import verify_turtle_syntax

# Define the root directory of the repository
# Navigate up from src/tools/validators to the repo root
ROOT_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)
SRC_DIR = os.path.join(ROOT_DIR, "src")
ARTIFACTS_DIR = os.path.join(ROOT_DIR, "artifacts")
TESTS_DATA_DIR = os.path.join(ROOT_DIR, "tests", "data")
IMPORTS_DIR = os.path.join(ROOT_DIR, "imports")


def parse_gitignore_patterns(root_dir):
    """
    Parses .gitignore to find folders that should be ignored.
    Returns a set of folder names.
    """
    gitignore_path = os.path.join(root_dir, ".gitignore")
    ignored_folders = set()

    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                clean_name = line.strip("/")
                if line.endswith("/") or os.path.isdir(
                    os.path.join(root_dir, clean_name)
                ):
                    ignored_folders.add(clean_name)
    return ignored_folders


# Add dynamic folders from .gitignore
GITIGNORE_FOLDERS = parse_gitignore_patterns(ROOT_DIR)

EXPECTED_TARGETCLASS_FAILURES = set()


def get_ontology_domains():
    """
    Return ontology domain names by scanning tests/data/ directory.
    Each subdirectory in tests/data/ represents an ontology domain.
    """
    if not os.path.isdir(TESTS_DATA_DIR):
        return []

    return sorted(
        [
            folder
            for folder in os.listdir(TESTS_DATA_DIR)
            if os.path.isdir(os.path.join(TESTS_DATA_DIR, folder))
            and not folder.startswith(".")
        ]
    )


def get_artifacts_for_domain(domain: str, use_catalog: bool = True) -> dict:
    """
    Get artifact paths for a given domain using catalog/registry.

    Args:
        domain: Domain name (e.g., "scenario", "manifest")
        use_catalog: If True, use registry/catalog; if False, use file discovery

    Returns:
        Dict with paths to ontology, shacl, and test directories
    """
    from src.tools.utils.registry_resolver import RegistryResolver

    if use_catalog:
        # Use registry for ontology and SHACL paths
        resolver = RegistryResolver(ROOT_DIR)
        ontology_path = resolver.get_ontology_path(domain)
        shacl_paths = resolver.get_shacl_paths(domain)

        ontology_file = os.path.join(ROOT_DIR, ontology_path) if ontology_path else None
        shacl_file = os.path.join(ROOT_DIR, shacl_paths[0]) if shacl_paths else None

        # Test paths are now handled by RegistryResolver
        # Return None for backward compatibility
        return {
            "domain": domain,
            "ontology": ontology_file,
            "shacl": shacl_file,
            "valid_instances_dir": None,  # Use RegistryResolver instead
            "invalid_tests_dir": None,  # Use RegistryResolver instead
        }
    else:
        # Fallback to file-based discovery
        ontology_file = os.path.join(ARTIFACTS_DIR, domain, f"{domain}.owl.ttl")
        shacl_file = os.path.join(ARTIFACTS_DIR, domain, f"{domain}.shacl.ttl")
        valid_instances_dir = os.path.join(TESTS_DATA_DIR, domain, "valid")
        invalid_tests_dir = os.path.join(TESTS_DATA_DIR, domain, "invalid")

        return {
            "domain": domain,
            "ontology": ontology_file if os.path.exists(ontology_file) else None,
            "shacl": shacl_file if os.path.exists(shacl_file) else None,
            "valid_instances_dir": (
                valid_instances_dir if os.path.isdir(valid_instances_dir) else None
            ),
            "invalid_tests_dir": (
                invalid_tests_dir if os.path.isdir(invalid_tests_dir) else None
            ),
        }


def check_syntax_all(ontology_domains: List[str]) -> int:
    """Check the syntax of all Turtle (.ttl) and JSON-LD (.json) files."""
    if not ontology_domains:
        return 0

    # Convert ROOT_DIR to Path for use with normalization
    ROOT_DIR_PATH = Path(ROOT_DIR)

    # Use catalog-based discovery for comprehensive JSON-LD file collection
    catalog_resolver = RegistryResolver(ROOT_DIR)

    print("\n=== Checking JSON-LD syntax ===", flush=True)

    if catalog_resolver.is_catalog_loaded():
        # Catalog-based approach: Get ALL JSON-LD files from catalog
        json_files_to_check = []

        # Get all entries from catalog (test-data, fixtures, etc.)
        for test_id, metadata in catalog_resolver._catalog.items():
            file_path = ROOT_DIR_PATH / metadata["path"]
            if file_path.suffix in [".json", ".jsonld"] and file_path.exists():
                json_files_to_check.append(str(file_path))

        # Also check for any JSON-LD files in artifacts that might not be cataloged
        for domain in ontology_domains:
            artifact_dir = os.path.join(ARTIFACTS_DIR, domain)
            if os.path.isdir(artifact_dir):
                for file in os.listdir(artifact_dir):
                    if file.endswith((".json", ".jsonld")):
                        file_path = os.path.join(artifact_dir, file)
                        if file_path not in json_files_to_check:
                            json_files_to_check.append(file_path)

        # Check each file individually
        json_results = []
        for json_file in sorted(json_files_to_check):
            code, msg = check_json_wellformedness(json_file, ROOT_DIR_PATH)
            json_results.append((code, msg))
            if code != 0:
                print(msg, file=sys.stderr)
                return code
            print(msg)
    else:
        # Fallback: directory-based approach
        dirs_to_check = []
        for domain in ontology_domains:
            artifact_dir = os.path.join(ARTIFACTS_DIR, domain)
            if os.path.isdir(artifact_dir):
                dirs_to_check.append(artifact_dir)
            valid_dir = os.path.join(TESTS_DATA_DIR, domain, "valid")
            if os.path.isdir(valid_dir):
                dirs_to_check.append(valid_dir)
            invalid_dir = os.path.join(TESTS_DATA_DIR, domain, "invalid")
            if os.path.isdir(invalid_dir):
                dirs_to_check.append(invalid_dir)

        # Add fixtures directory
        fixtures_dir = os.path.join(ROOT_DIR, "tests", "fixtures")
        if os.path.isdir(fixtures_dir):
            dirs_to_check.append(fixtures_dir)

        json_ret, json_results = verify_json_syntax(dirs_to_check, ROOT_DIR_PATH)
        for code, msg in json_results:
            if code == 0:
                print(msg)
            else:
                print(msg, file=sys.stderr)
                return code

    print("\n=== Checking TTL syntax ===", flush=True)
    # Check TTL files in all domain directories
    ttl_dirs = [
        os.path.join(ARTIFACTS_DIR, domain)
        for domain in ontology_domains
        if os.path.isdir(os.path.join(ARTIFACTS_DIR, domain))
    ]
    ttl_ret, ttl_results = verify_turtle_syntax(ttl_dirs, ROOT_DIR_PATH)
    for code, msg in ttl_results:
        if code == 0:
            print(msg)
        else:
            print(msg, file=sys.stderr)
            return code

    print("📌 Completed TTL and JSON syntax tests", flush=True)
    return 0


def validate_data_conformance_all(
    ontology_domains: List[str], use_catalog: bool = True
) -> int:
    """
    Validate JSON-LD files against SHACL schemas.

    Args:
        ontology_domains: List of domain names to test
        use_catalog: If True, use catalog-based discovery; if False, use file discovery
    """
    if not ontology_domains:
        return 0
    print("\n=== Checking JSON-LD against SHACL ===", flush=True)

    # Try catalog-based discovery first
    catalog_resolver = RegistryResolver(ROOT_DIR) if use_catalog else None

    if catalog_resolver and catalog_resolver.is_catalog_loaded():
        print("📋 Using catalog-based test discovery\n", flush=True)

    for domain in ontology_domains:
        print(
            f"\n🔍 Starting JSON-LD SHACL validation for domain: {domain}", flush=True
        )

        # Hybrid discovery: Try catalog first, fall back to file discovery
        if catalog_resolver and catalog_resolver.is_catalog_loaded():
            jsonld_files = catalog_resolver.get_test_files(domain, test_type="valid")
            if jsonld_files:
                print(
                    f"   Found {len(jsonld_files)} test files from catalog", flush=True
                )
        else:
            # Fallback to file-based discovery
            artifacts = get_artifacts_for_domain(domain)
            valid_dir = artifacts["valid_instances_dir"]

            if not valid_dir:
                print(
                    f"⚠️ No valid instances directory found for '{domain}'. Skipping.",
                    flush=True,
                )
                continue

            jsonld_files = collect_jsonld_files([valid_dir])

        if not jsonld_files:
            print(f"⚠️ No JSON-LD files found in '{domain}'. Skipping.", flush=True)
            continue

        # Use new catalog-based validator
        returncode, output = validate_data_conformance(
            jsonld_files,
            Path(ROOT_DIR),
            inference_mode="rdfs",
            debug=False,
            logfile=None,
        )

        if returncode != 0:
            print(
                f"\n❌ Error during JSON-LD SHACL validation for domain '{domain}'. Aborting.",
                file=sys.stderr,
                flush=True,
            )
            return returncode
        else:
            print(f"\n✅ {domain} conforms to SHACL constraints.", flush=True)

    return 0


def check_failing_tests_all(
    ontology_domains: List[str], use_catalog: bool = True
) -> int:
    """
    Run failing test cases from tests/data/{domain}/invalid/ directories.

    Args:
        ontology_domains: List of domain names to test
        use_catalog: If True, use catalog-based discovery; if False, use file discovery
    """
    if not ontology_domains:
        return 0
    print("\n=== Running failing tests ===", flush=True)

    # Try catalog-based discovery first
    catalog_resolver = RegistryResolver(ROOT_DIR) if use_catalog else None

    if catalog_resolver and catalog_resolver.is_catalog_loaded():
        print("📋 Using catalog-based test discovery\n", flush=True)

    for domain in ontology_domains:
        print(f"\n🔍 Running failing tests for domain: {domain}", flush=True)

        # Hybrid discovery: Try catalog first, fall back to file discovery
        if catalog_resolver and catalog_resolver.is_catalog_loaded():
            invalid_test_files = catalog_resolver.get_test_files(
                domain, test_type="invalid"
            )
            if not invalid_test_files:
                continue
        else:
            # Fallback to file-based discovery
            artifacts = get_artifacts_for_domain(domain)
            test_folder = artifacts["invalid_tests_dir"]

            if not test_folder:
                continue

            fail_tests = sorted(
                f
                for f in os.listdir(test_folder)
                if f.startswith("fail") and f.endswith(".json")
            )
            invalid_test_files = [Path(test_folder) / f for f in fail_tests]

        for test_abs_path in invalid_test_files:
            test_abs_path = Path(test_abs_path)
            rel_path = os.path.relpath(test_abs_path, ROOT_DIR)
            test_path = f".{os.sep}{rel_path}"
            expected_output_path = test_abs_path.with_suffix("").with_suffix(
                ".expected"
            )

            if not expected_output_path.exists():
                print(
                    f"⚠️ No expected output file found: {expected_output_path}",
                    file=sys.stderr,
                    flush=True,
                )
                return 1

            expected_output = expected_output_path.read_text(encoding="utf-8").strip()

            print(f"🔍 Running failing test: {test_path}", flush=True)

            # Collect failing test file
            jsonld_files = collect_jsonld_files([str(test_abs_path)])

            # Use new catalog-based validator
            returncode, output = validate_data_conformance(
                jsonld_files,
                Path(ROOT_DIR),
                inference_mode="rdfs",
                debug=False,
                logfile=None,
            )

            if returncode == 210:
                output_norm = normalize_text(output)
                expected_norm = normalize_text(expected_output)

                if output_norm == expected_norm:
                    print(
                        f"✅ Test {test_path} for domain {domain} failed as expected.",
                        flush=True,
                    )
                else:
                    print(
                        f"\n❌ Error: Output discrepancy for {test_path}. Aborting.",
                        file=sys.stderr,
                        flush=True,
                    )
                    return 1
            else:
                print(
                    f"\n❌ Test {test_path} did not return code 210 (got {returncode}). Aborting.",
                    file=sys.stderr,
                    flush=True,
                )
                return returncode or 1

    return 0


def validate_artifact_coherence_all(ontology_domains: List[str]) -> int:
    """Validate target classes against OWL for each domain."""
    if not ontology_domains:
        return 0
    print("\n=== Checking target classes against OWL classes ===", flush=True)

    # Convert ROOT_DIR to Path for use with normalization
    ROOT_DIR_PATH = Path(ROOT_DIR)

    for domain in ontology_domains:
        print(f"\n🔍 Checking target classes for domain: {domain}", flush=True)

        # New structure: artifacts/{domain}/{domain}.owl.ttl
        ontology_file = os.path.join(ARTIFACTS_DIR, domain, f"{domain}.owl.ttl")
        shacl_file = os.path.join(ARTIFACTS_DIR, domain, f"{domain}.shacl.ttl")

        if not os.path.exists(ontology_file):
            print(f"⚠️ No ontology file found for '{domain}'. Skipping.", flush=True)
            continue

        if not os.path.exists(shacl_file):
            print(f"⚠️ No SHACL file found for '{domain}'. Skipping.", flush=True)
            continue

        # Call the updated validator with the new structure
        # Pass domain name and artifacts directory
        returncode, output = validate_artifact_coherence(
            domain, ARTIFACTS_DIR, None, IMPORTS_DIR, ROOT_DIR_PATH
        )

        if output:
            target = sys.stdout if returncode == 0 else sys.stderr
            print(output, file=target, flush=True)

        if returncode != 0:
            if domain in EXPECTED_TARGETCLASS_FAILURES:
                print(
                    f"⚠️ Expected target class failure for '{domain}' (ignored).",
                    flush=True,
                )
                continue
            print(
                f"\n❌ Error {returncode} during target class validation for {domain}. Aborting.",
                file=sys.stderr,
                flush=True,
            )
            return returncode
        else:
            print(f"✅ Target classes are correctly defined for {domain}.", flush=True)

    return 0


# --- CLI / Main Logic ---
def main():
    """Run validation checks based on arguments."""

    # 1. Enforce Python 3.12+
    if sys.version_info < (3, 12):
        print(
            f"❌ Error: This project requires Python 3.12+. You are running {sys.version.split()[0]}.",
            file=sys.stderr,
        )
        sys.exit(1)

    # 2. Enforce Virtual Environment
    in_venv = (
        (sys.prefix != sys.base_prefix)
        or ("CONDA_DEFAULT_ENV" in os.environ)
        or ("GITHUB_ACTIONS" in os.environ)
    )

    if not in_venv:
        print(
            "❌ Error: You are NOT running inside a virtual environment.",
            file=sys.stderr,
        )
        sys.exit(1)

    # 3. Argument Parsing
    parser = argparse.ArgumentParser(
        description="Run ontology validation checks.",
        epilog="Use --help for detailed usage examples. See module docstring for comprehensive documentation.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--run",
        type=str,
        choices=[
            "all",
            "check-syntax",
            "check-artifact-coherence",
            "check-data-conformance",
            "check-failing-tests",
        ],
        default="all",
        help="Validation mode to run (default: all)",
    )
    parser.add_argument(
        "--domain",
        type=str,
        nargs="+",
        default=None,
        metavar="DOMAIN",
        help="Domain name(s) from catalog (e.g., manifest, scenario). Uses catalog structure and test data.",
    )
    parser.add_argument(
        "--path",
        type=str,
        nargs="+",
        default=None,
        metavar="PATH",
        help="File or directory path(s) to validate. Works with arbitrary files outside standard structure.",
    )
    parser.add_argument(
        "--folder",
        type=str,
        nargs="+",
        default=None,
        dest="folder_deprecated",
        help=argparse.SUPPRESS,  # Hidden deprecated option
    )
    parser.add_argument(
        "--no-catalog",
        action="store_true",
        help="Disable catalog-based discovery (use file system only)",
    )
    args = parser.parse_args()

    # Handle deprecated --folder option
    if args.folder_deprecated:
        print(
            "⚠️  Warning: --folder is deprecated. Use --domain for catalog domains or --path for file paths.",
            file=sys.stderr,
        )
        if not args.domain and not args.path:
            # Try to determine if these are domains or paths
            if all(not os.path.exists(f) for f in args.folder_deprecated):
                # Looks like domain names
                args.domain = args.folder_deprecated
                print(
                    f"   Interpreting as --domain {' '.join(args.domain)}",
                    file=sys.stderr,
                )
            else:
                # Looks like paths
                args.path = args.folder_deprecated
                print(
                    f"   Interpreting as --path {' '.join(args.path)}", file=sys.stderr
                )

    # 4. Determine Operation Mode
    use_catalog = not args.no_catalog

    # PATH MODE: User specified file/directory paths
    # Create temporary catalog domain for these paths
    if args.path:
        print("🔍 Path mode: Validating specified paths", flush=True)
        # Validate that paths exist
        valid_paths = []
        for p in args.path:
            if os.path.exists(p):
                valid_paths.append(p)
            else:
                print(f"⚠️  Warning: Path does not exist: {p}", file=sys.stderr)

        if not valid_paths:
            print("❌ Error: No valid paths provided.", file=sys.stderr)
            sys.exit(1)

        # Create catalog resolver and temporary domain
        catalog_resolver = RegistryResolver(ROOT_DIR)
        temp_domain = catalog_resolver.create_temporary_domain(valid_paths)

        if not temp_domain:
            print(
                "❌ Error: No JSON-LD files found in provided paths.", file=sys.stderr
            )
            sys.exit(1)

        # Use temporary domain like a regular catalog domain
        ontology_domains = [temp_domain]
        paths_to_check = valid_paths  # Keep for potential direct file operations

    # DOMAIN MODE: User specified catalog domains
    elif args.domain is not None:
        print(f"🔍 Domain mode: Using catalog for domain(s): {args.domain}", flush=True)
        # User provided specific domains
        ontology_domains = [
            d for d in args.domain if os.path.isdir(os.path.join(TESTS_DATA_DIR, d))
        ]

        if not ontology_domains and len(args.domain) > 0:
            print(f"⚠️ None of the provided domains exist in tests/data/: {args.domain}")
            print("Available domains:", get_ontology_domains())
            sys.exit(1)

        paths_to_check = None
        print(f"Detected ontology domains: {ontology_domains}", flush=True)

    # AUTO MODE: Discover all domains from catalog
    else:
        print("🔍 Auto mode: Discovering all domains from catalog", flush=True)
        ontology_domains = get_ontology_domains()
        paths_to_check = None

        if not ontology_domains:
            print("No ontology domains to check. Exiting.")
            sys.exit(0)

        print(f"Detected ontology domains: {ontology_domains}", flush=True)

    # 5. Define validation checks based on mode (PATH vs DOMAIN)
    if args.path:
        # PATH MODE: Use temporary catalog domain
        # Artifact coherence and failing tests require standard structure
        if args.run in ["check-artifact-coherence", "check-failing-tests"]:
            print(
                f"❌ Error: {args.run} is not supported in path mode.", file=sys.stderr
            )
            print(
                "   These checks require catalog structure and domain information.",
                file=sys.stderr,
            )
            print(
                "   Use --domain instead of --path for these checks.", file=sys.stderr
            )
            sys.exit(1)

        # Store catalog_resolver for use in nested functions
        _path_catalog_resolver = catalog_resolver  # Capture from outer scope

        # Helper function for syntax checking in path mode
        def check_syntax_path_mode():
            """Check syntax using catalog for JSON-LD and direct check for TTL."""
            ROOT_DIR_PATH = Path(ROOT_DIR)

            # Check JSON-LD files via catalog (already in temporary domain)
            print("\n=== Checking JSON-LD syntax ===", flush=True)
            jsonld_files = _path_catalog_resolver.get_test_files(ontology_domains[0])

            if jsonld_files:
                for json_file in sorted(jsonld_files):
                    code, msg = check_json_wellformedness(str(json_file), ROOT_DIR_PATH)
                    if code == 0:
                        print(msg)
                    else:
                        print(msg, file=sys.stderr)
                        return code
            else:
                print("⚠️ No JSON-LD files found in provided paths.")

            # Check TTL files directly
            print("\n=== Checking TTL syntax ===", flush=True)
            ttl_ret, ttl_results = verify_turtle_syntax(paths_to_check, ROOT_DIR_PATH)
            for code, msg in ttl_results:
                if code == 0:
                    print(msg)
                elif "No Turtle files found" not in msg:
                    print(msg, file=sys.stderr)
                    return code

            print("📌 Completed syntax tests", flush=True)
            return 0

        # Helper function for data conformance in path mode
        def check_data_conformance_path_mode():
            """Check data conformance using temporary catalog domain."""
            print("\n=== Checking JSON-LD against SHACL ===", flush=True)

            # Get JSON-LD files from temporary catalog
            jsonld_files = _path_catalog_resolver.get_test_files(ontology_domains[0])

            if not jsonld_files:
                print("⚠️ No JSON-LD files found in provided paths.", flush=True)
                return 0

            print(f"Found {len(jsonld_files)} JSON-LD file(s) to validate", flush=True)

            # Use validator directly with files from temporary catalog
            returncode, output = validate_data_conformance(
                [str(f) for f in jsonld_files],
                Path(ROOT_DIR),
                inference_mode="rdfs",
                debug=False,
                logfile=None,
            )

            if returncode != 0:
                print(
                    "\n❌ Error during JSON-LD SHACL validation. Aborting.",
                    file=sys.stderr,
                    flush=True,
                )
                return returncode
            else:
                print("\n✅ All files conform to SHACL constraints.", flush=True)

            return 0

        check_map = {
            "check-syntax": [("Check Syntax", check_syntax_path_mode)],
            "check-data-conformance": [
                (
                    "Check Data Conformance",
                    check_data_conformance_path_mode,
                )
            ],
        }

        if args.run == "all":
            print(
                "ℹ️  Path mode: Running syntax and conformance checks only.", flush=True
            )
            checks_to_run = (
                check_map["check-syntax"] + check_map["check-data-conformance"]
            )
        else:
            checks_to_run = check_map[args.run]

    else:
        # DOMAIN MODE: Validate using catalog structure
        check_map = {
            "check-syntax": [
                ("Check Syntax", lambda: check_syntax_all(ontology_domains))
            ],
            "check-artifact-coherence": [
                (
                    "Check Artifact Coherence",
                    lambda: validate_artifact_coherence_all(ontology_domains),
                )
            ],
            "check-data-conformance": [
                (
                    "Check Data Conformance",
                    lambda: validate_data_conformance_all(
                        ontology_domains, use_catalog
                    ),
                )
            ],
            "check-failing-tests": [
                (
                    "Check Failing Tests",
                    lambda: check_failing_tests_all(ontology_domains, use_catalog),
                )
            ],
        }

        if args.run == "all":
            checks_to_run = (
                check_map["check-syntax"]
                + check_map["check-artifact-coherence"]
                + check_map["check-data-conformance"]
                + check_map["check-failing-tests"]
            )
        else:
            checks_to_run = check_map[args.run]

    print(f"\n🚀 Running check mode: {args.run.upper()} ...", flush=True)

    for name, phase_func in checks_to_run:
        rc = phase_func()
        if rc != 0:
            print(
                f"\n❌ {name} phase failed (code {rc}). Aborting.",
                file=sys.stderr,
                flush=True,
            )
            sys.exit(rc)

    print(f"\n✅ {args.run.upper()} checks completed successfully!", flush=True)


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")
    main()
