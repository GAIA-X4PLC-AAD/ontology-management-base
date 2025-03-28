import os
import re
import json
import shutil
import subprocess

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

def bump_version(version, bump_type):
    major, minor, patch = map(int, version.split('.'))
    if bump_type == "major":
        major += 1
        minor = 0
        patch = 0
    elif bump_type == "minor":
        minor += 1
        patch = 0
    elif bump_type == "patch":
        patch += 1
    return f"{major}.{minor}.{patch}"

def create_version_subfolder(subfolder, bump_type):
    latest_tag = get_latest_tag(subfolder)
    if latest_tag:
        latest_version = latest_tag.split('_v')[-1]
        new_version = bump_version(latest_version, bump_type)
    else:
        new_version = "1.0.0"
    
    new_tag = f"{subfolder}_v{new_version}"
    version_folder = f"v{new_version}"

    if not os.path.exists(os.path.join(subfolder, version_folder)):
        os.makedirs(os.path.join(subfolder, version_folder), exist_ok=True)
        print(f"Created directory: {os.path.join(subfolder, version_folder)}")

        # Copy only the relevant files to the new version directory
        for file in os.listdir(subfolder):
            if file.endswith(('_shacl.ttl', '_ontology.ttl', '_instance.json')):
                shutil.copy(os.path.join(subfolder, file), os.path.join(subfolder, version_folder))
                print(f"Copied {file} to {os.path.join(subfolder, version_folder)}")

    return new_tag, version_folder, new_version

def update_ttl_files(subfolder, version_folder, subfolders, current_version):
    ttl_files = [f for f in os.listdir(os.path.join(subfolder, version_folder)) if f.endswith(('_shacl.ttl', '_ontology.ttl'))]
    for ttl_file in ttl_files:
        file_path = os.path.join(subfolder, version_folder, ttl_file)
        with open(file_path, 'r') as file:
            content = file.readlines()
        with open(file_path, 'w') as file:
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
                            new_uri = re.sub(r'/(v[0-9]+\\.[0-9]+\\.[0-9]+/)?$', f'/v{version}/', f'https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/{folder}/')
                            line = re.sub(r'<.*>', f'<{new_uri}>', line)
                file.write(line)
        print(f"Updated @prefix in {file_path}")

def update_json_files(subfolder, version_folder, subfolders, current_version):
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
                    data['@context'][folder] = re.sub(r'/(v[0-9]+\\.[0-9]+\\.[0-9]+/)?$', f'/v{version}/', f'https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/{folder}/')
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=2)
            print(f"Updated @context in {file_path}")
        except json.JSONDecodeError:
            print(f"Error decoding JSON in {file_path}")

def save_versions(versions):
    with open("versions.txt", "w") as file:
        for version in versions:
            file.write(f"{version[0]} {version[1]} {version[2]}\n")

def main():
    subfolders = os.getenv("subfolders")
    if subfolders:
        subfolders = [sf for sf in subfolders.split() if sf != 'gx']
    else:
        print("No subfolders found in environment variables.")
        return

    bump_type = os.getenv("BUMP_TYPE")
    if not bump_type:
        print("No BUMP_TYPE found in environment variables.")
        return
    
    changed_files = os.getenv("files")
    if changed_files:
        changed_files = changed_files.split()
    else:
        print("No changed files found in environment variables.")
        return

    versions = []
    for subfolder in subfolders:
        if any(file.startswith(f"{subfolder}/") for file in changed_files):
            new_tag, version_folder, new_version = create_version_subfolder(subfolder, bump_type)
            update_ttl_files(subfolder, version_folder, subfolders, new_version)
            update_json_files(subfolder, version_folder, subfolders, new_version)
            versions.append((subfolder, new_tag, version_folder))
    
    save_versions(versions)

if __name__ == "__main__":
    main()
