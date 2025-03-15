import os
import re
import subprocess
import sys

# Define the root directory of the repository
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(ROOT_DIR, "src")

# Explicitly excluded folders
EXCLUDED_FOLDERS = {"src"}


def get_ontology_dirs():
    """Detect ontology directories, excluding explicitly named and hidden folders."""
    return [
        folder
        for folder in os.listdir(ROOT_DIR)
        if os.path.isdir(os.path.join(ROOT_DIR, folder))
        and folder not in EXCLUDED_FOLDERS  # Exclude explicitly listed folders
        and not folder.startswith(".")  # Exclude all hidden folders
    ]


ONTOLOGY_DIRS = get_ontology_dirs()
print(f"📂 Detected ontology directories: {ONTOLOGY_DIRS}")


def normalize_text(text):
    """
    Normalize text while preserving important punctuation for SHACL validation comparison.
    """
    text = text.strip().lower()  # Convert to lowercase for case-insensitive comparison
    text = re.sub(r"\s+", " ", text)  # Normalize excessive whitespace
    text = re.sub(
        r"([^\w\s:/.-])", "", text
    )  # Preserve colons, slashes, periods, and dashes
    return text


def extract_validation_result(output):
    """Extracts the SHACL validation summary, ensuring 'Conforms: False' is captured."""
    match = re.search(
        r"Validation Report\s+Conforms:\s+(True|False)", output, re.IGNORECASE
    )
    conforms_status = match.group(0) if match else "Conforms: Unknown"

    violations = "\n".join(
        line for line in output.split("\n") if "constraint violation" in line.lower()
    )

    return f"{conforms_status}\n{violations}"


def run_command(command, description):
    """Runs a shell command, captures and normalizes output, ensuring correct SHACL validation detection."""
    print(f"\n🔍 {description}...")

    try:
        result = subprocess.run(
            command, shell=False, capture_output=True, text=True, check=True
        )
        full_output = result.stdout.strip() + "\n" + result.stderr.strip()

        print("\n🔎 Raw SHACL Validation Output:\n" + full_output)  # 🔍 Debugging step

        extracted_output = extract_validation_result(full_output)
        normalized_output = normalize_text(extracted_output)

        print(
            "\n🔎 Extracted & Normalized Output:\n" + normalized_output
        )  # 🔍 Debugging step

        return result.returncode, normalized_output
    except subprocess.CalledProcessError as e:
        error_output = e.stdout.strip() + "\n" + e.stderr.strip()
        print(f"❌ Error during {description}:\n{error_output}", file=sys.stderr)
        sys.exit(1)


def ensure_shacl_failure(test_name, actual_output):
    """Ensures SHACL validation correctly reports 'Conforms: False' for failing test cases."""
    if "conforms: false" not in actual_output:
        print(
            f"❌ Test {test_name} should fail, but SHACL validation reported success!"
        )
        print(f"\n🔎 DEBUG: Extracted Validation Output:\n{actual_output}")
        sys.exit(1)


def check_ttl_syntax():
    """Check syntax of all Turtle (.ttl) files in the repository and catch syntax errors."""
    print("\n=== Checking TTL syntax in all ontology folders ===")

    for ontology in ONTOLOGY_DIRS:
        ttl_files = [
            os.path.join(ontology, f)
            for f in os.listdir(ontology)
            if f.endswith(".ttl")
        ]

        for ttl_file in ttl_files:
            print(f"\n🔍 Checking syntax of {ttl_file}...")
            returncode, _ = run_command(
                [
                    sys.executable,
                    os.path.join(SRC_DIR, "check_ttl_syntax.py"),
                    ttl_file,
                ],
                f"Checking TTL syntax in {ttl_file}",
            )

            if returncode != 0:
                print(f"❌ Syntax error detected in {ttl_file}!")
                sys.exit(1)
            else:
                print(f"✅ {ttl_file} syntax is correct.")


def check_jsonld_against_shacl():
    """Check all JSON-LD instance files against their SHACL schemas and verify SHACL validation results."""
    print("\n=== Checking JSON-LD files against SHACL schemas ===")

    for ontology in ONTOLOGY_DIRS:
        print(f"\n🔍 Validating JSON-LD in {ontology} against SHACL...")
        returncode, output = run_command(
            [
                sys.executable,
                os.path.join(SRC_DIR, "check_jsonld_against_shacl_schema.py"),
                ontology,
            ],
            f"Validating {ontology} JSON-LD against SHACL",
        )

        if "conforms: false" in output:
            print(f"❌ Validation failed for {ontology}, please check SHACL rules.")
            sys.exit(1)
        else:
            print(f"✅ {ontology} conforms to SHACL constraints.")


def check_failing_tests():
    """Run failing test cases in each ontology's tests/ folder and compare with expected failure messages."""
    print("\n=== Running failing test cases ===")
    validated_references = set()

    for ontology in ONTOLOGY_DIRS:
        test_folder = os.path.join(ontology, "tests")
        if not os.path.exists(test_folder):
            continue

        fail_tests = [
            f
            for f in os.listdir(test_folder)
            if f.startswith("fail") and f.endswith(".json")
        ]
        instance_files = [f for f in fail_tests if "_instance.json" in f]
        reference_files = [f for f in fail_tests if "_reference.json" in f]

        for test in instance_files:
            test_path = os.path.join(test_folder, test)
            expected_output_path = test_path.replace(".json", ".expected")

            reference_path = test.replace("_instance.json", "_reference.json")
            reference_path_full = os.path.join(test_folder, reference_path)

            validation_args = [test_path]
            if reference_path in reference_files:
                validation_args.append(reference_path_full)
                validated_references.add(reference_path_full)

            print(f"\n🛠 Running failing test: {test}")
            returncode, actual_output = run_command(
                [
                    sys.executable,
                    os.path.join(SRC_DIR, "check_jsonld_against_shacl_schema.py"),
                ]
                + validation_args,
                f"Validating failing test: {test}",
            )

            ensure_shacl_failure(test, actual_output)

            if os.path.exists(expected_output_path):
                with open(expected_output_path, "r") as expected_file:
                    expected_output = normalize_text(expected_file.read().strip())

                if expected_output in actual_output:
                    print(f"✅ Test {test} produced the expected failure message.")
                else:
                    print(f"❌ Test {test} failed, but output does not match expected.")
                    print("\n🔎 DEBUG: Expected vs. Actual SHACL Validation Output")
                    print(f"\n🔹 Expected Output:\n{expected_output}")
                    print(f"\n🔹 Actual Output:\n{actual_output}")

                    diff_lines = [
                        f"- {line}"
                        for line in expected_output.split("\n")
                        if line not in actual_output.split("\n")
                    ]
                    extra_lines = [
                        f"+ {line}"
                        for line in actual_output.split("\n")
                        if line not in expected_output.split("\n")
                    ]

                    print(
                        "\n🔎 Differences Detected:\n"
                        + "\n".join(diff_lines + extra_lines)
                    )
                    sys.exit(1)
            else:
                print(
                    f"⚠️ No expected output file found for {test}. Creating placeholder."
                )
                with open(expected_output_path, "w") as placeholder:
                    placeholder.write(actual_output)
                print(
                    f"📄 Created {expected_output_path} with actual validation output."
                )


def main():
    """Main execution function for running all checks."""
    print("\n🚀 Running all ontology validation checks...")
    check_ttl_syntax()
    check_jsonld_against_shacl()
    check_failing_tests()
    print("\n✅ All checks completed successfully!")


if __name__ == "__main__":
    main()
