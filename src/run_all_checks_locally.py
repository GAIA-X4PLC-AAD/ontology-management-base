import argparse
import io
import os
import sys
from typing import List

from check_jsonld_against_shacl_schema import (
    build_dict_for_ontologies,
    validate_jsonld_against_shacl,
)
from check_target_classes_against_owl_classes import (
    validate_target_classes_against_owl_classes,
)
from utils.check_parse_jsonld import validate_jsonld_files
from utils.check_parse_turtle import validate_turtle_files
from utils.print_formatting import normalize_text

# Define the root directory of the repository and the source folder for scripts
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(ROOT_DIR, "src")


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


# 1. Start with valid repository folders that are NOT ontologies
EXCLUDED_FOLDERS = {
    "src",
    "base-ontologies",
    "base-references",
    "service-characteristics",
    ".git",
    ".github",
    ".idea",
    ".vscode",
}

# 2. Add dynamic folders from .gitignore
EXCLUDED_FOLDERS.update(parse_gitignore_patterns(ROOT_DIR))

EXPECTED_TARGETCLASS_FAILURES = set()


def get_ontology_dirs():
    """Return non-hidden directories in ROOT_DIR that are not explicitly excluded."""
    return sorted(
        [
            folder
            for folder in os.listdir(ROOT_DIR)
            if os.path.isdir(os.path.join(ROOT_DIR, folder))
            and folder not in EXCLUDED_FOLDERS
            and not folder.startswith(".")
        ]
    )


def check_syntax_all(ontology_dirs: List[str]) -> int:
    """Check the syntax of all Turtle (.ttl) and JSON-LD (.json) files."""
    if not ontology_dirs:
        return 0
    print("\n=== Checking JSON-LD syntax ===", flush=True)
    json_ret, json_results = validate_jsonld_files(ontology_dirs)
    for code, msg in json_results:
        if code == 0:
            print(msg)
        else:
            print(msg, file=sys.stderr)
            return code

    print("\n=== Checking TTL syntax ===", flush=True)
    ttl_ret, ttl_results = validate_turtle_files(ontology_dirs)
    for code, msg in ttl_results:
        if code == 0:
            print(msg)
        else:
            print(msg, file=sys.stderr)
            return code

    print("📌 Completed TTL and JSON syntax tests", flush=True)
    return 0


def check_jsonld_against_shacl_all(ontology_dirs: List[str]) -> int:
    """Validate JSON-LD files against SHACL schemas."""
    if not ontology_dirs:
        return 0
    print("\n=== Checking JSON-LD against SHACL ===", flush=True)

    for ontology in ontology_dirs:
        print(
            f"\n🔍 Starting JSON-LD SHACL validation for folder: {ontology}", flush=True
        )
        ontology_dict = build_dict_for_ontologies(
            ROOT_DIR, [os.path.join(".", ontology)]
        )

        if not ontology_dict:
            # If a folder exists but has no files, strictly speaking it's not a failure,
            # but we warn.
            print(
                f"⚠️ No validateable files found in '{ontology}'. Skipping.", flush=True
            )
            continue

        returncode, output = validate_jsonld_against_shacl(
            ROOT_DIR, ontology_dict, debug=False, inference_mode="rdfs"
        )

        if output:
            target = sys.stdout if returncode == 0 else sys.stderr
            print(output, file=target, flush=True)

        if returncode != 0:
            print(
                f"\n❌ Error during JSON-LD SHACL validation for folder '{ontology}'. Aborting.",
                file=sys.stderr,
                flush=True,
            )
            return returncode
        else:
            print(f"✅ {ontology} conforms to SHACL constraints.", flush=True)

    return 0


def check_failing_tests_all(ontology_dirs: List[str]) -> int:
    """Run failing test cases."""
    if not ontology_dirs:
        return 0
    print("\n=== Running failing tests ===", flush=True)

    for ontology in ontology_dirs:
        folder_path = os.path.join(ROOT_DIR, ontology)
        test_folder = os.path.join(folder_path, "tests")
        if not os.path.exists(test_folder):
            continue

        print(f"\n🔍 Running failing tests in folder: {ontology}", flush=True)
        fail_tests = sorted(
            f
            for f in os.listdir(test_folder)
            if f.startswith("fail") and f.endswith(".json")
        )

        for test in fail_tests:
            rel_path = os.path.relpath(os.path.join(test_folder, test), ROOT_DIR)
            test_path = f".{os.sep}{rel_path}"
            expected_output_path = os.path.splitext(test_path)[0] + ".expected"

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
            ontology_dict = build_dict_for_ontologies(ROOT_DIR, [test_path])
            returncode, output = validate_jsonld_against_shacl(
                ROOT_DIR, ontology_dict, debug=False
            )

            if returncode == 210:
                output_norm = normalize_text(output)
                expected_norm = normalize_text(expected_output)

                if output_norm == expected_norm:
                    print(
                        f"✅ Test {test} in folder {ontology} failed as expected.",
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


def check_target_classes_all(ontology_dirs: List[str]) -> int:
    """Validate target classes against OWL."""
    if not ontology_dirs:
        return 0
    print("\n=== Checking target classes against OWL classes ===", flush=True)

    for ontology in ontology_dirs:
        folder_path = os.path.join(".", ontology)
        print(f"\n🔍 Checking target classes in folder: {ontology}", flush=True)
        returncode, output = validate_target_classes_against_owl_classes(folder_path)

        if output:
            target = sys.stdout if returncode == 0 else sys.stderr
            print(output, file=target, flush=True)

        if returncode != 0:
            if ontology in EXPECTED_TARGETCLASS_FAILURES:
                print(
                    f"⚠️ Expected target class failure for '{ontology}' (ignored).",
                    flush=True,
                )
                continue
            print(
                f"\n❌ Error {returncode} during target class validation for {ontology}. Aborting.",
                file=sys.stderr,
                flush=True,
            )
            return returncode
        else:
            print(f"✅ Target classes are correctly defined in {ontology}.", flush=True)

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
    # UPDATED: Accept multiple folders or none
    parser.add_argument(
        "--folder",
        type=str,
        nargs="*",
        default=None,
        help="Specific folders to run checks on (space separated).",
    )
    args = parser.parse_args()

    # 4. Determine Target Directories
    if args.folder is not None:
        # User provided specific folders.
        # Filter out invalid or deleted directories to prevent runtime errors.
        ontology_dirs = [
            f for f in args.folder if os.path.isdir(os.path.join(ROOT_DIR, f))
        ]

        if not ontology_dirs and len(args.folder) > 0:
            # User provided folders, but none exist (deleted?)
            print(
                f"⚠️ None of the provided folders exist (files might have been deleted): {args.folder}"
            )
            print("Skipping checks.")
            sys.exit(0)
    else:
        # Automatic discovery (default behavior)
        ontology_dirs = get_ontology_dirs()

    if not ontology_dirs:
        print("No directories to check. Exiting.")
        sys.exit(0)

    print(f"Detected ontology directories: {ontology_dirs}", flush=True)

    # 5. Define the Mapping
    # Lambda captures the list of dirs
    check_map = {
        "syntax": [("Syntax", lambda: check_syntax_all(ontology_dirs))],
        "target-classes": [
            ("Target Classes", lambda: check_target_classes_all(ontology_dirs))
        ],
        "shacl": [
            ("JSON-LD SHACL", lambda: check_jsonld_against_shacl_all(ontology_dirs))
        ],
        "failing-tests": [
            ("Failing Tests", lambda: check_failing_tests_all(ontology_dirs))
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
