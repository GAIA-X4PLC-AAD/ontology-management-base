import os
import subprocess
import sys

# Define the root directory of the repository
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(ROOT_DIR, "src")

# Exclude non-ontology folders
EXCLUDED_FOLDERS = {"src", ".git", ".github", ".playground", ".venv"}

def get_ontology_dirs():
    """Dynamically detects ontology directories by scanning the repository structure."""
    return [
        folder for folder in os.listdir(ROOT_DIR)
        if os.path.isdir(os.path.join(ROOT_DIR, folder)) and folder not in EXCLUDED_FOLDERS
    ]

# Automatically detected ontology directories
ONTOLOGY_DIRS = get_ontology_dirs()

print(f"📂 Detected ontology directories: {ONTOLOGY_DIRS}")

def run_command(command, description):
    """Runs a shell command and logs the output."""
    print(f"\n🔍 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during {description}:\n{e.stderr}", file=sys.stderr)
        sys.exit(1)


def check_ttl_syntax():
    """Check syntax of all Turtle (.ttl) files in the repository and catch syntax errors."""
    print("\n=== Checking TTL syntax in all ontology folders ===")
    
    for ontology in ONTOLOGY_DIRS:
        ttl_files = [
            os.path.join(ontology, f) for f in os.listdir(ontology)
            if f.endswith(".ttl")
        ]

        for ttl_file in ttl_files:
            print(f"\n🔍 Checking syntax of {ttl_file}...")

            result = subprocess.run(
                [sys.executable, os.path.join(SRC_DIR, "check_ttl_syntax.py"), ttl_file],
                capture_output=True,
                text=True
            )

            stdout_output = result.stdout.strip()
            stderr_output = result.stderr.strip()
            full_output = stdout_output + "\n" + stderr_output

            # Log full output for debugging
            print(full_output)

            if result.returncode != 0 or "Syntax Error" in full_output:
                print(f"❌ Syntax error detected in {ttl_file}!")
                sys.exit(1)  # Fail the script if a syntax error is detected
            else:
                print(f"✅ {ttl_file} syntax is correct.")


def check_jsonld_against_shacl():
    """Check all JSON-LD instance files against their SHACL schemas and verify SHACL validation results."""
    print("\n=== Checking JSON-LD files against SHACL schemas ===")
    for ontology in ONTOLOGY_DIRS:
        print(f"\n🔍 Validating JSON-LD in {ontology} against SHACL...")
        
        result = subprocess.run(
            [sys.executable, os.path.join(SRC_DIR, "check_jsonld_against_shacl_schema.py"), ontology],
            capture_output=True,
            text=True
        )

        # Capture stdout and stderr separately
        stdout_output = result.stdout.strip()
        stderr_output = result.stderr.strip()
        full_output = stdout_output + "\n" + stderr_output

        # Log the raw validation output for debugging
        print(full_output)

        # Explicitly check for "Conforms: False" in the validation output
        if "Conforms: False" in full_output:
            print(f"❌ Validation failed for {ontology}, but was expected. Please check the SHACL rules.")
            sys.exit(1)  # Fail the script if a validation issue was found
        else:
            print(f"✅ {ontology} conforms to SHACL constraints.")


def check_failing_tests():
    """Run failing test cases in each ontology's tests/ folder and compare with expected failure messages."""
    print("\n=== Running failing test cases ===")
    for ontology in ONTOLOGY_DIRS:
        test_folder = os.path.join(ontology, "tests")
        if not os.path.exists(test_folder):
            continue  # Skip if no tests exist

        fail_tests = [
            f for f in os.listdir(test_folder) if f.startswith("fail") and f.endswith(".json")
        ]

        for test in fail_tests:
            test_path = os.path.join(test_folder, test)
            expected_output_path = test_path.replace(".json", ".expected")

            print(f"\n🛠 Running failing test: {test}")
            result = subprocess.run(
                [sys.executable, os.path.join(SRC_DIR, "check_jsonld_against_shacl_schema.py"), test_path],
                capture_output=True,
                text=True
            )

            # Capture actual SHACL validation output
            actual_output = result.stderr.strip() if result.returncode != 0 else result.stdout.strip()

            # Look for explicit "Conforms: False" in output
            if "Conforms: False" not in actual_output:
                print(f"❌ Test {test} should fail, but SHACL validation reported success!")
                sys.exit(1)

            # Compare actual vs expected failure messages
            if os.path.exists(expected_output_path):
                with open(expected_output_path, "r") as expected_file:
                    expected_output = expected_file.read().strip()

                if expected_output in actual_output:
                    print(f"✅ Test {test} failed as expected.")
                else:
                    print(f"❌ Test {test} failed, but output does not match expected.")
                    print(f"Expected:\n{expected_output}\n\nActual:\n{actual_output}")
                    sys.exit(1)
            else:
                print(f"⚠️ No expected output file found for {test}. Please add one.")
                print(f"Actual output:\n{actual_output}")


def main():
    """Main execution function for running all checks."""
    print("\n🚀 Running all ontology validation checks...")

    check_ttl_syntax()
    check_jsonld_against_shacl()
    check_failing_tests()

    print("\n✅ All checks completed successfully!")

if __name__ == "__main__":
    main()
