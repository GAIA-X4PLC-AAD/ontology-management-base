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

def create_initial_subfolder(subfolder):
    latest_tag = get_latest_tag(subfolder)
    if not latest_tag:
        # Create initial tag if no tags found
        initial_version = "v1.0.0"
        initial_tag = f"{subfolder}_{initial_version}"
        subprocess.run(["git", "tag", initial_tag])
        subprocess.run(["git", "push", "origin", initial_tag])
        latest_tag = initial_tag

    latest_version = latest_tag.split('_v')[-1]
    clean_version = re.sub(r'[^0-9\\.]', '', latest_version)
    version_folder = f"v{clean_version}"

    os.makedirs(os.path.join(subfolder, version_folder), exist_ok=True)
    print(f"Created directory: {os.path.join(subfolder, version_folder)}")

    # Copy only the relevant files to the new version directory
    for file in os.listdir(subfolder):
        if file.endswith(('_shacl.ttl', '_ontology.ttl', '_instance.json')):
            shutil.copy(os.path.join(subfolder, file), os.path.join(subfolder, version_folder))
            print(f"Copied {file} to {os.path.join(subfolder, version_folder)}")

def update_ttl_files(subfolder, version_folder, subfolders):
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
                            latest_tag = get_latest_tag(folder)
                            if latest_tag:
                                version = latest_tag.split('_v')[-1]
                                new_uri = re.sub(r'/(v[0-9]+\\.[0-9]+\\.[0-9]+/)?$', f'/v{version}/', f'https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/{folder}/')
                                line = re.sub(r'<.*>', f'<{new_uri}>', line)
                file.write(line)
        print(f"Updated @prefix in {file_path}")

def update_json_files(subfolder, version_folder, subfolders):
    json_files = [f for f in os.listdir(os.path.join(subfolder, version_folder)) if f.endswith('_instance.json')]
    for json_file in json_files:
        file_path = os.path.join(subfolder, version_folder, json_file)
        with open(file_path, 'r') as file:
            data = json.load(file)
        for folder in subfolders:
            if folder in data.get('@context', {}):
                latest_tag = get_latest_tag(folder)
                if latest_tag:
                    version = latest_tag.split('_v')[-1]
                    data['@context'][folder] = re.sub(r'/(v[0-9]+\\.[0-9]+\\.[0-9]+/)?$', f'/v{version}/', f'https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/{folder}/')
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)
        print(f"Updated @context in {file_path}")

def main():
    with open('subfolders.txt', 'r') as file:
        subfolders = [line.strip() for line in file if line.strip() and line.strip() != 'gx']
    
    for subfolder in subfolders:
        create_initial_subfolder(subfolder)

    for subfolder in subfolders:
        latest_tag = get_latest_tag(subfolder)
        if latest_tag:
            version_folder = f"v{latest_tag.split('_v')[-1]}"
            update_ttl_files(subfolder, version_folder, subfolders)
            update_json_files(subfolder, version_folder, subfolders)

if __name__ == "__main__":
    main()
