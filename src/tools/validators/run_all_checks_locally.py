import argparse
import io
import os
import sys
from pathlib import Path
from typing import List

from src.tools.utils.check_parse_jsonld import validate_jsonld_files
from src.tools.utils.check_parse_turtle import validate_turtle_files
from src.tools.utils.print_formatting import normalize_text
from src.tools.validators.check_jsonld_against_shacl_schema import collect_jsonld_files
from src.tools.validators.check_target_classes_against_owl_classes import (
    validate_target_classes_against_owl_classes,
)
from src.tools.validators.shacl.validator import (
    validate_jsonld_files as validate_jsonld_with_shacl,
)

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


def get_artifacts_for_domain(domain: str) -> dict:
    """
    Get artifact paths for a given domain in the new structure.
    New structure: artifacts/{domain}/{domain}.owl.ttl
    Returns dict with paths to ontology, shacl, and test files.
    """
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

    # Collect all directories to check in new structure: artifacts/{domain}/
    dirs_to_check = []
    for domain in ontology_domains:
        artifact_dir = os.path.join(ARTIFACTS_DIR, domain)
        if os.path.isdir(artifact_dir):
            dirs_to_check.append(artifact_dir)
        valid_dir = os.path.join(TESTS_DATA_DIR, domain, "valid")
        if os.path.isdir(valid_dir):
            dirs_to_check.append(valid_dir)

    print("\n=== Checking JSON-LD syntax ===", flush=True)
    json_ret, json_results = validate_jsonld_files(dirs_to_check)
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
    ttl_ret, ttl_results = validate_turtle_files(ttl_dirs)
    for code, msg in ttl_results:
        if code == 0:
            print(msg)
        else:
            print(msg, file=sys.stderr)
            return code

    print("📌 Completed TTL and JSON syntax tests", flush=True)
    return 0


def check_jsonld_against_shacl_all(ontology_domains: List[str]) -> int:
    """Validate JSON-LD files against SHACL schemas using catalog-based discovery."""
    if not ontology_domains:
        return 0
    print("\n=== Checking JSON-LD against SHACL ===", flush=True)

    for domain in ontology_domains:
        artifacts = get_artifacts_for_domain(domain)
        valid_dir = artifacts["valid_instances_dir"]

        if not valid_dir:
            print(
                f"⚠️ No valid instances directory found for '{domain}'. Skipping.",
                flush=True,
            )
            continue

        print(
            f"\n🔍 Starting JSON-LD SHACL validation for domain: {domain}", flush=True
        )

        # Collect JSON-LD files from the valid instances directory
        jsonld_files = collect_jsonld_files([valid_dir])

        if not jsonld_files:
            print(f"⚠️ No JSON-LD files found in '{domain}'. Skipping.", flush=True)
            continue

        # Use new catalog-based validator
        returncode, output = validate_jsonld_with_shacl(
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


def check_failing_tests_all(ontology_domains: List[str]) -> int:
    """Run failing test cases from tests/data/{domain}/invalid/ directories."""
    if not ontology_domains:
        return 0
    print("\n=== Running failing tests ===", flush=True)

    for domain in ontology_domains:
        artifacts = get_artifacts_for_domain(domain)
        test_folder = artifacts["invalid_tests_dir"]

        if not test_folder:
            continue

        print(f"\n🔍 Running failing tests for domain: {domain}", flush=True)
        fail_tests = sorted(
            f
            for f in os.listdir(test_folder)
            if f.startswith("fail") and f.endswith(".json")
        )

        for test in fail_tests:
            test_abs_path = os.path.join(test_folder, test)
            rel_path = os.path.relpath(test_abs_path, ROOT_DIR)
            test_path = f".{os.sep}{rel_path}"
            expected_output_path = os.path.splitext(test_abs_path)[0] + ".expected"

            if not os.path.exists(expected_output_path):
                print(
                    f"⚠️ No expected output file found: {expected_output_path}",
                    file=sys.stderr,
                    flush=True,
                )
                return 1

            with open(expected_output_path, "r", encoding="utf-8") as f:
                expected_output = f.read().strip()

            print(f"🔍 Running failing test: {test_path}", flush=True)

            # Collect failing test file
            jsonld_files = collect_jsonld_files([test_abs_path])

            # Use new catalog-based validator
            returncode, output = validate_jsonld_with_shacl(
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
                        f"✅ Test {test} for domain {domain} failed as expected.",
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


def check_target_classes_all(ontology_domains: List[str]) -> int:
    """Validate target classes against OWL for each domain."""
    if not ontology_domains:
        return 0
    print("\n=== Checking target classes against OWL classes ===", flush=True)

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
        returncode, output = validate_target_classes_against_owl_classes(
            domain, ARTIFACTS_DIR, None, IMPORTS_DIR
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
    parser = argparse.ArgumentParser(description="Run ontology validation checks.")
    parser.add_argument(
        "--check",
        type=str,
        choices=["all", "syntax", "target-classes", "shacl", "failing-tests"],
        default="all",
        help="Specific check to run (default: all)",
    )
    # UPDATED: Accept multiple domains or none
    parser.add_argument(
        "--folder",
        "--domain",
        type=str,
        nargs="*",
        default=None,
        dest="domain",
        help="Specific ontology domains to run checks on (space separated).",
    )
    args = parser.parse_args()

    # 4. Determine Target Domains
    if args.domain is not None:
        # User provided specific domains
        ontology_domains = [
            d for d in args.domain if os.path.isdir(os.path.join(TESTS_DATA_DIR, d))
        ]

        if not ontology_domains and len(args.domain) > 0:
            print(f"⚠️ None of the provided domains exist in tests/data/: {args.domain}")
            print("Skipping checks.")
            sys.exit(0)
    else:
        # Automatic discovery (default behavior)
        ontology_domains = get_ontology_domains()

    if not ontology_domains:
        print("No ontology domains to check. Exiting.")
        sys.exit(0)

    print(f"Detected ontology domains: {ontology_domains}", flush=True)

    # 5. Define the Mapping
    check_map = {
        "syntax": [("Syntax", lambda: check_syntax_all(ontology_domains))],
        "target-classes": [
            ("Target Classes", lambda: check_target_classes_all(ontology_domains))
        ],
        "shacl": [
            ("JSON-LD SHACL", lambda: check_jsonld_against_shacl_all(ontology_domains))
        ],
        "failing-tests": [
            ("Failing Tests", lambda: check_failing_tests_all(ontology_domains))
        ],
    }

    if args.check == "all":
        checks_to_run = (
            check_map["syntax"]
            + check_map["target-classes"]
            + check_map["shacl"]
            + check_map["failing-tests"]
        )
    else:
        checks_to_run = check_map[args.check]

    print(f"\n🚀 Running check mode: {args.check.upper()} ...", flush=True)

    for name, phase_func in checks_to_run:
        rc = phase_func()
        if rc != 0:
            print(
                f"\n❌ {name} phase failed (code {rc}). Aborting.",
                file=sys.stderr,
                flush=True,
            )
            sys.exit(rc)

    print(f"\n✅ {args.check.upper()} checks completed successfully!", flush=True)


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")
    main()
