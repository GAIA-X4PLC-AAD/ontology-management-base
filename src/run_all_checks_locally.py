import io
import os
import sys

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

# Explicitly excluded folders
EXCLUDED_FOLDERS = {"src", "base-ontologies"}
EXPECTED_TARGETCLASS_FAILURES = {"gx"}  # ontologies allowed to fail this check


def get_ontology_dirs():
    """Return non-hidden directories in ROOT_DIR that are not explicitly excluded, sorted alphabetically."""
    return sorted(
        [
            folder
            for folder in os.listdir(ROOT_DIR)
            if os.path.isdir(os.path.join(ROOT_DIR, folder))
            and folder not in EXCLUDED_FOLDERS
            and not folder.startswith(".")
        ]
    )


ONTOLOGY_DIRS = get_ontology_dirs()


def check_syntax_all() -> int:
    """Check the syntax of all Turtle (.ttl) and JSON-LD (.json) files."""
    print("\n=== Checking JSON-LD syntax ===", flush=True)
    overall_ret = 0

    json_ret, json_results = validate_jsonld_files(ONTOLOGY_DIRS)
    for code, msg in json_results:
        if code == 0:
            print(msg)
        else:
            print(msg, file=sys.stderr)
        overall_ret |= code

    print("\n=== Checking TTL syntax ===", flush=True)
    ttl_ret, ttl_results = validate_turtle_files(ONTOLOGY_DIRS)
    for code, msg in ttl_results:
        if code == 0:
            print(msg)
        else:
            print(msg, file=sys.stderr)
        overall_ret |= code

    print("📌 Completed TTL and JSON syntax tests", flush=True)
    return overall_ret


def check_jsonld_against_shacl_all() -> int:
    """Validate JSON-LD files against SHACL schemas for each ontology folder."""
    print("\n=== Checking JSON-LD against SHACL ===", flush=True)
    overall_ret = 0

    for ontology in ONTOLOGY_DIRS:
        print(
            f"\n🔍 Starting JSON-LD SHACL validation for folder: {ontology}", flush=True
        )
        # Fix: Pass explicitly relative path starting with ./
        ontology_dict = build_dict_for_ontologies(
            ROOT_DIR, [os.path.join(".", ontology)]
        )

        if not ontology_dict:
            print(
                f"Error code 100: No valid files found in folder '{ontology}'.",
                file=sys.stderr,
                flush=True,
            )
            overall_ret |= 100
            continue

        returncode, output = validate_jsonld_against_shacl(
            ROOT_DIR, ontology_dict, debug=False, inference_mode="rdfs"
        )

        if output:
            target = sys.stdout if returncode == 0 else sys.stderr
            print(output, file=target, flush=True)

        if returncode != 0:
            print(
                f"\n❌ Error during JSON-LD SHACL validation for folder '{ontology}'.",
                file=sys.stderr,
                flush=True,
            )
            overall_ret |= returncode
        else:
            print(f"✅ {ontology} conforms to SHACL constraints.", flush=True)

        print(
            f"📌 Completed JSON-LD SHACL validation for folder: {ontology}", flush=True
        )

    return overall_ret


def check_failing_tests_all() -> int:
    """Run failing test cases and compare output to expected results."""
    print("\n=== Running failing tests ===", flush=True)
    overall_ret = 0

    for ontology in ONTOLOGY_DIRS:
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
            # Fix: Manually construct ./ relative path to avoid normpath stripping it
            rel_path = os.path.relpath(os.path.join(test_folder, test), ROOT_DIR)
            test_path = f".{os.sep}{rel_path}"
            expected_output_path = os.path.splitext(test_path)[0] + ".expected"

            if not os.path.exists(expected_output_path):
                print(
                    f"⚠️ No expected output file found: {expected_output_path}",
                    file=sys.stderr,
                    flush=True,
                )
                overall_ret |= 1
                continue

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
                        f"\n❌ Error during comparison for {test_path}.",
                        file=sys.stderr,
                        flush=True,
                    )
                    overall_ret |= 1
            else:
                print(
                    f"\n❌ Test {test_path} did not return expected error code 210 (got {returncode}).",
                    file=sys.stderr,
                    flush=True,
                )
                overall_ret |= returncode or 1

    return overall_ret


def check_target_classes_all() -> int:
    """Validate if all target classes in the SHACL shapes exist in the ontology."""
    print("\n=== Checking target classes against OWL classes ===", flush=True)
    overall_ret = 0

    for ontology in ONTOLOGY_DIRS:
        # Fix: Use relative path ./ontology for consistency
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
                f"\n❌ Error {returncode} during target class validation for {ontology}.",
                file=sys.stderr,
                flush=True,
            )
            overall_ret |= returncode
        else:
            print(f"✅ Target classes are correctly defined in {ontology}.", flush=True)

    return overall_ret


def main():
    """Run all validation checks sequentially, aborting on the first failure phase."""
    print("Detected ontology directories:", flush=True)
    for directory in ONTOLOGY_DIRS:
        print(f" - {directory}", flush=True)

    print("\n🚀 Running all ontology validation checks...", flush=True)

    # Sequence of checks; script will exit if any check returns a non-zero code.
    check_phases = [
        ("Syntax", check_syntax_all),
        ("JSON-LD SHACL", check_jsonld_against_shacl_all),
        ("Failing Tests", check_failing_tests_all),
        ("Target Classes", check_target_classes_all),
    ]

    for name, phase_func in check_phases:
        rc = phase_func()
        if rc != 0:
            print(
                f"\n❌ {name} phase failed (code {rc}). Aborting.",
                file=sys.stderr,
                flush=True,
            )
            sys.exit(rc)

    print("\n✅ All checks completed successfully!", flush=True)


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")
    main()
