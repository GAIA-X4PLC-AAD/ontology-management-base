import io
import os
import sys
import unicodedata

from check_jsonld_against_shacl_schema import validate_jsonld_against_shacl
from check_target_classes_against_owl_classes import (
    validate_target_classes_against_owl_classes,
)

# Import the refactored core functions directly
from check_ttl_syntax import check_ttl_syntax

# Define the root directory of the repository and the source folder for scripts
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(ROOT_DIR, "src")

# Explicitly excluded folders
EXCLUDED_FOLDERS = {"src", "base-ontologies"}


def get_ontology_dirs():
    """Return non-hidden directories in ROOT_DIR that are not explicitly excluded."""
    return [
        folder
        for folder in os.listdir(ROOT_DIR)
        if os.path.isdir(os.path.join(ROOT_DIR, folder))
        and folder not in EXCLUDED_FOLDERS
        and not folder.startswith(".")
    ]


ONTOLOGY_DIRS = get_ontology_dirs()
print(f"Detected ontology directories: {ONTOLOGY_DIRS}", flush=True)
print("\n🚀 Running all ontology validation checks...", flush=True)


def check_ttl_syntax_all():
    """Check the syntax of all Turtle (.ttl) files in each ontology folder."""
    print("\n=== Checking TTL syntax ===", flush=True)
    for ontology in ONTOLOGY_DIRS:
        folder_path = os.path.join(ROOT_DIR, ontology)
        print(f"\n🔍 Starting TTL syntax tests for folder: {ontology}", flush=True)
        ttl_files = [
            os.path.join(folder_path, f)
            for f in os.listdir(folder_path)
            if f.endswith(".ttl")
        ]
        if not ttl_files:
            print(f"⚠️  No .ttl files found in folder: {ontology}", flush=True)
            continue

        for ttl_file in ttl_files:
            print(f"🔍 Checking syntax of {ttl_file}...", flush=True)
            returncode, output = check_ttl_syntax(ttl_file)
            if returncode != 0:
                print(
                    f"\n❌ Error during TTL syntax check for {ttl_file}:\n{output}",
                    file=sys.stderr,
                    flush=True,
                )

                sys.exit(returncode)
            else:
                print(f"✅ {ttl_file} passed syntax check.", flush=True)
        print(f"📌 Completed TTL syntax tests for folder: {ontology}", flush=True)


def check_jsonld_against_shacl_all():
    """Validate JSON-LD files against SHACL schemas for each ontology folder."""
    print("\n=== Checking JSON-LD against SHACL ===", flush=True)
    for ontology in ONTOLOGY_DIRS:
        folder_path = os.path.join(ROOT_DIR, ontology)
        print(
            f"\n🔍 Starting JSON-LD SHACL validation for folder: {ontology}", flush=True
        )
        returncode, output = validate_jsonld_against_shacl([folder_path], debug=False)
        if returncode != 0:
            print(
                f"\n❌ Error during JSON-LD SHACL validation for {folder_path}:\n{output}",
                file=sys.stderr,
                flush=True,
            )

            sys.exit(returncode)
        else:
            print(f"✅ {ontology} conforms to SHACL constraints.", flush=True)
        print(
            f"📌 Completed JSON-LD SHACL validation for folder: {ontology}", flush=True
        )


def normalize_text(text: str) -> str:
    # Normalize unicode characters (NFC form)
    normalized = unicodedata.normalize("NFC", text)
    # Normalize line endings to '\n'
    normalized = normalized.replace("\r\n", "\n").replace("\r", "\n")
    # Strip trailing and leading whitespace from each line and join
    lines = [line.strip() for line in normalized.split("\n")]
    return "\n".join(lines).strip()


def check_failing_tests_all():
    """
    Run failing test cases in the tests/ subfolder of each ontology and compare output to expected results.
    The expected output file is determined by stripping the '.json' extension from the test file name
    and appending '.expected'.
    """
    print("\n=== Running failing tests ===", flush=True)
    for ontology in ONTOLOGY_DIRS:
        folder_path = os.path.join(ROOT_DIR, ontology)
        test_folder = os.path.join(folder_path, "tests")
        if not os.path.exists(test_folder):
            print(
                f"⚠️  No tests folder found in {ontology}, skipping failing tests.",
                flush=True,
            )
            continue

        print(f"\n🔍 Running failing tests in folder: {ontology}", flush=True)
        fail_tests = sorted(
            f
            for f in os.listdir(test_folder)
            if f.startswith("fail") and f.endswith(".json")
        )
        if not fail_tests:
            print(f"⚠️  No failing test files found in {ontology}.", flush=True)
            continue

        for test in fail_tests:
            test_path = os.path.join(test_folder, test)
            expected_output_filename = os.path.splitext(test)[0] + ".expected"
            expected_output_path = os.path.join(test_folder, expected_output_filename)

            if os.path.exists(expected_output_path):
                with open(expected_output_path, "r", encoding="utf-8") as f:
                    expected_output = f.read().strip()
            else:
                print(
                    f"⚠️ No expected output file found: {expected_output_path}",
                    file=sys.stderr,
                    flush=True,
                )

                sys.exit(1)

            print(
                f"🔍 Running failing test: {test_path} in folder: {ontology}",
                flush=True,
            )

            returncode, output = validate_jsonld_against_shacl([test_path], debug=False)

            if returncode == 210:
                # Normalize output and expected output for comparison
                output_norm = normalize_text(
                    (output.split("=")[0].strip() + "=" + output.split("=")[-1].strip())
                )
                expected_norm = normalize_text(
                    (
                        expected_output.split("=")[0].strip()
                        + "="
                        + expected_output.split("=")[-1].strip()
                    )
                )

                if output_norm.strip() == expected_norm.strip():
                    print(
                        f"✅ Test {test} in folder {ontology} failed as expected.",
                        flush=True,
                    )
                else:
                    print(
                        f"\n❌ Error during comparison of expected vs. result for {test_path}:\n"
                        f"Validation output:\n{output}\n\nExpected output file:\n{expected_output}\n",
                        file=sys.stderr,
                        flush=True,
                    )

                    sys.exit(1)
            else:
                print(
                    f"\n❌ Error during failing test validation for {test_path}:\n"
                    f"Errorcode: {returncode}\n",
                    file=sys.stderr,
                    flush=True,
                )

                sys.exit(returncode)

        print(f"📌 Completed failing tests for folder: {ontology}", flush=True)


def check_target_classes_all():
    """Validate if all target classes in the SHACL shapes exist in the ontology."""
    print("\n=== Checking target classes against OWL classes ===", flush=True)
    for ontology in ONTOLOGY_DIRS:
        folder_path = os.path.join(ROOT_DIR, ontology)
        print(f"\n🔍 Checking target classes in folder: {ontology}", flush=True)
        returncode, output = validate_target_classes_against_owl_classes(folder_path)
        if returncode != 0:
            print(
                f"\n❌ Error {returncode} during target class validation for {ontology}:\n{output}",
                file=sys.stderr,
                flush=True,
            )

            sys.exit(returncode)
        else:
            print(f"✅ Target classes are correctly defined in {ontology}.", flush=True)
        print(
            f"📌 Completed target class validation for folder: {ontology}", flush=True
        )


def main():
    """Run all validation checks sequentially, aborting on the first failure."""
    check_ttl_syntax_all()
    check_jsonld_against_shacl_all()
    check_failing_tests_all()
    check_target_classes_all()
    print("\n✅ All checks completed successfully!", flush=True)


if __name__ == "__main__":
    # Set the encoding for stdout to UTF-8
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

    main()
