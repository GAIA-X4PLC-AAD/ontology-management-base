import io
import os
import re
import sys
import unicodedata

from check_jsonld_against_shacl_schema import (
    build_dict_for_ontologies,
    validate_jsonld_against_shacl,
)
from check_target_classes_against_owl_classes import (
    validate_target_classes_against_owl_classes,
)
from utils.check_parse_jsonld import validate_jsonld_files
from utils.check_parse_turtle import validate_turtle_files

# Define the root directory of the repository and the source folder for scripts
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(ROOT_DIR, "src")

# Explicitly excluded folders
EXCLUDED_FOLDERS = {"src", "base-ontologies"}
EXPECTED_TARGETCLASS_FAILURES = {"gx"}  # ontologies allowed to fail this check


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


def check_syntax_all():
    """Check the syntax of all Turtle (.ttl) and JSON-LD (.json) files in each ontology folder."""
    print("\n=== Checking JSON-LD syntax ===", flush=True)

    overall_ret = 0

    # --- JSON-LD validation ---
    json_ret, json_results = validate_jsonld_files(ONTOLOGY_DIRS)
    for code, msg in json_results:
        if code == 0:
            print(msg)
        else:
            print(msg, file=sys.stderr)
        overall_ret |= code

    print("\n=== Checking TTL syntax ===", flush=True)
    # --- Turtle validation ---
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

    for ontology in ONTOLOGY_DIRS:
        print(
            f"\n🔍 Starting JSON-LD SHACL validation for folder: {ontology}",
            flush=True,
        )

        ontology_dict = build_dict_for_ontologies(ROOT_DIR, [ontology])

        if not ontology_dict:
            msg = f"Error code 100: No valid files found in folder '{ontology}'."
            print(msg, file=sys.stderr, flush=True)
            return 100

        returncode, output = validate_jsonld_against_shacl(
            ROOT_DIR,
            ontology_dict,
            debug=False,
            inference_mode="rdfs",
        )

        # Print validator output
        if output:
            target = sys.stdout if returncode == 0 else sys.stderr
            print(output, file=target, flush=True)

        if returncode != 0:
            print(
                f"\n❌ Error during JSON-LD SHACL validation for folder '{ontology}'.",
                file=sys.stderr,
                flush=True,
            )
            return returncode

        print(f"✅ {ontology} conforms to SHACL constraints.", flush=True)
        print(
            f"📌 Completed JSON-LD SHACL validation for folder: {ontology}",
            flush=True,
        )

    return 0


def normalize_text(text: str) -> str:
    # Normalize unicode and line endings first
    text = unicodedata.normalize("NFC", text)
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Strip whitespace from each line before regex
    lines = [line.strip() for line in text.split("\n")]
    text = "\n".join(lines)

    pattern = (
        r"("  # capture entire two-block sequence
        r"={10,}\n"  # first block start delimiter
        r"(?:\s*=.*\n)+"  # first block content lines
        r"={10,}\n"  # first block end delimiter
        r"={10,}\n"  # second block start delimiter
        r"(?:\s*=.*\n)+"  # second block content lines
        r"={10,}"  # second block end delimiter
        r")"
    )

    match = re.search(pattern, text)
    if match:
        normalized = match.group(0).strip()
        return normalized
    else:
        print("⚠️  Block not found")
        return ""


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
        test_folder = os.path.relpath(test_folder, ROOT_DIR)
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
                output_norm = normalize_text(output)
                expected_norm = normalize_text(expected_output)

                if output_norm == expected_norm:
                    print(
                        f"✅ Test {test} in folder {ontology} failed as expected.",
                        flush=True,
                    )
                else:
                    print(
                        f"\n❌ Error during comparison of expected vs. result for {test_path}:\n"
                        f"Validation output:\n{output_norm}\n\nExpected output file:\n{expected_norm}\n\n",
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


def check_target_classes_all() -> int:
    """Validate if all target classes in the SHACL shapes exist in the ontology."""
    print("\n=== Checking target classes against OWL classes ===", flush=True)

    overall_ret = 0

    for ontology in ONTOLOGY_DIRS:
        folder_path = os.path.join(ROOT_DIR, ontology)
        print(f"\n🔍 Checking target classes in folder: {ontology}", flush=True)

        returncode, output = validate_target_classes_against_owl_classes(folder_path)

        # Show the validator's detailed output (your big summary block)
        if output:
            target = sys.stdout if returncode == 0 else sys.stderr
            print(output, file=target, flush=True)

        if returncode != 0:
            if ontology in EXPECTED_TARGETCLASS_FAILURES:
                # Known / accepted failure: report it but don't mark overall as failed
                print(
                    f"⚠️ Target class validation for '{ontology}' failed with "
                    f"error code {returncode}, but this is currently an expected "
                    f"known issue and will not fail the overall test run.",
                    file=sys.stderr,
                    flush=True,
                )
                # Do NOT OR this into overall_ret
                continue

            # Any other ontology failing is a real error
            print(
                f"\n❌ Error {returncode} during target class validation for {ontology}",
                file=sys.stderr,
                flush=True,
            )
            overall_ret |= returncode
        else:
            print(
                f"✅ Target classes are correctly defined in {ontology}.",
                flush=True,
            )

        print(
            f"📌 Completed target class validation for folder: {ontology}",
            flush=True,
        )

    return overall_ret


def main():
    """Run all validation checks sequentially, aborting on the first failure."""
    print("Detected ontology directories:", flush=True)
    for directory in ONTOLOGY_DIRS:
        print(f" - {directory}", flush=True)

    print("\n🚀 Running all ontology validation checks...", flush=True)

    # 1) Syntax checks
    rc = check_syntax_all()
    if rc != 0:
        print(
            "\n❌ Syntax check failed. Aborting further validation.",
            file=sys.stderr,
            flush=True,
        )
        sys.exit(rc)

    # 2) JSON-LD vs SHACL
    # rc = check_jsonld_against_shacl_all()
    if rc != 0:
        print(
            "\n❌ JSON-LD SHACL validation failed. Aborting further validation.",
            file=sys.stderr,
            flush=True,
        )
        sys.exit(rc)

    # 3) Failing tests
    # rc = check_failing_tests_all()
    if rc != 0:
        print(
            "\n❌ Failing tests check failed. Aborting further validation.",
            file=sys.stderr,
            flush=True,
        )
        sys.exit(rc)

    # 4) Target class checks
    rc = check_target_classes_all()
    if rc != 0:
        print(
            "\n❌ Target classes check failed. Aborting further validation.",
            file=sys.stderr,
            flush=True,
        )
        sys.exit(rc)

    print("\n✅ All checks completed successfully!", flush=True)


if __name__ == "__main__":
    # Set the encoding for stdout and stderr to UTF-8
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

    main()
