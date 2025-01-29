import os
import re
import json
import subprocess

# Funktion, um den neuesten Tag eines Subfolders zu erhalten
def get_latest_tag(subfolder):
    result = subprocess.run(
        ["git", "ls-remote", "--tags", "origin"],
        capture_output=True,
        text=True
    )
    tags = result.stdout.splitlines()
    latest_tag = ""
    for tag in tags:
        if f"refs/tags/{subfolder}_v" in tag:
            tag_name = re.search(f"{subfolder}_v[0-9]*\\.[0-9]*\\.[0-9]*$", tag)
            if tag_name:
                latest_tag = tag_name.group(0)
    return latest_tag

# Funktion, um zu überprüfen, ob der Versionsordner und die erforderlichen Dateien existieren
def check_version_subfolder(subfolder, version):
    version_folder = f"v{version}"
    folder_path = os.path.join(subfolder, version_folder)
    if not os.path.exists(folder_path):
        print(f"Error: Version folder {folder_path} does not exist.")
        return False

    required_files = [f"{subfolder}_shacl.ttl", f"{subfolder}_ontology.ttl", f"{subfolder}_instance.json"]
    for file in required_files:
        if not os.path.exists(os.path.join(folder_path, file)):
            print(f"Error: Required file {file} does not exist in {folder_path}.")
            return False

    return True

# Funktion, um die TTL-Dateien zu überprüfen
def check_ttl_files(subfolder, version_folder, subfolders, current_version):
    ttl_files = [f for f in os.listdir(os.path.join(subfolder, version_folder)) if f.endswith(('_shacl.ttl', '_ontology.ttl'))]
    for ttl_file in ttl_files:
        file_path = os.path.join(subfolder, version_folder, ttl_file)
        with open(file_path, 'r') as file:
            content = file.readlines()
        for line in content:
            if line.startswith('@prefix'):
                for folder in subfolders:
                    if folder in line:
                        if folder == subfolder:
                            version = current_version
                        else:
                            latest_tag = get_latest_tag(folder)
                            if latest_tag:
                                version = latest_tag.split('_v')[-1]
                        expected_uri = re.sub(r'/(v[0-9]+\\.[0-9]+\\.[0-9]+/)?$', f'/v{version}/', f'https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/{folder}/')
                        if not re.search(f'<{expected_uri}>', line):
                            print(f"Error: @prefix in {file_path} does not match expected URI {expected_uri}.")
                            return False
    return True

# Funktion, um die JSON-Dateien zu überprüfen
def check_json_files(subfolder, version_folder, subfolders, current_version):
    json_files = [f for f in os.listdir(os.path.join(subfolder, version_folder)) if f.endswith('_instance.json')]
    for json_file in json_files:
        file_path = os.path.join(subfolder, version_folder, json_file)
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
            for folder in subfolders:
                if folder in data.get('@context', {}):
                    if folder == subfolder:
                        version = current_version
                    else:
                        latest_tag = get_latest_tag(folder)
                        if latest_tag:
                            version = latest_tag.split('_v')[-1]
                    expected_uri = re.sub(r'/(v[0-9]+\\.[0-9]+\\.[0-9]+/)?$', f'/v{version}/', f'https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/{folder}/')
                    if data['@context'][folder] != expected_uri:
                        print(f"Error: @context in {file_path} does not match expected URI {expected_uri}.")
                        return False
        except json.JSONDecodeError:
            print(f"Error decoding JSON in {file_path}")
            return False
    return True

def main():
    # Subfolders aus den Umgebungsvariablen abrufen
    subfolders = os.getenv("subfolders")
    if subfolders:
        subfolders = [sf for sf in subfolders.split() if sf != 'gx']
    else:
        print("No subfolders found in environment variables.")
        return

    # Bump-Typ aus den Umgebungsvariablen abrufen
    bump_type = os.getenv("BUMP_TYPE")
    if not bump_type:
        print("No BUMP_TYPE found in environment variables.")
        return
    
    # Geänderte Dateien aus den Umgebungsvariablen abrufen
    changed_files = os.getenv("files")
    if changed_files:
        changed_files = changed_files.split()
    else:
        print("No changed files found in environment variables.")
        return

    # Überprüfen, ob Änderungen in mehreren Subfolders vorgenommen wurden
    changed_subfolders = set()
    for subfolder in subfolders:
        if any(file.startswith(f"{subfolder}/") for file in changed_files):
            changed_subfolders.add(subfolder)
    
    if len(changed_subfolders) > 1:
        print("Error: Changes span multiple subfolders. Only one subfolder can be modified per pull request.")
        return

    for subfolder in changed_subfolders:
        latest_tag = get_latest_tag(subfolder)
        if latest_tag:
            latest_version = latest_tag.split('_v')[-1]
            new_version = bump_version(latest_version, bump_type)
        else:
            new_version = "1.0.0"
        
        version_folder = f"v{new_version}"
        if not check_version_subfolder(subfolder, new_version):
            return
        
        if not check_ttl_files(subfolder, version_folder, subfolders, new_version):
            return
        
        if not check_json_files(subfolder, version_folder, subfolders, new_version):
            return

    print("All checks passed successfully.")

if __name__ == "__main__":
    main()
