import os
import subprocess

# Funktion, um den neuesten Tag eines Subfolders zu erhalten
def get_latest_tag(folder):
    result = subprocess.run(
        ["git", "tag", "-l", f"{folder}_v*"],
        capture_output=True,
        text=True
    )
    tags = result.stdout.strip().split("\n")
    tags.sort()
    return tags[-1] if tags else None

# Funktion, um einen Versionsordner zu erstellen und ein Release zu erzeugen
def create_version_subfolder(subfolder, new_tag, version_folder):
    os.makedirs(os.path.join(subfolder, version_folder), exist_ok=True)
    print(f"Created directory: {os.path.join(subfolder, version_folder)}")

    os.chdir(subfolder)
    subprocess.run(["git", "tag", "-a", new_tag, "-m", f"Release for {subfolder} version {new_tag.split('_v')[-1]}"])
    subprocess.run(["git", "push", "origin", new_tag])
    subprocess.run(["zip", "-r", f"{subfolder}_{new_tag.split('_v')[-1]}.zip", version_folder])
    subprocess.run(["gh", "release", "create", new_tag, f"{subfolder}_{new_tag.split('_v')[-1]}.zip", "--title", new_tag, "--notes", f"Automated release for {subfolder} version {new_tag.split('_v')[-1]}"])
    os.chdir("..")

def main():
    if not os.path.exists("versions.txt"):
        print("No versions.txt file found.")
        return

    with open("versions.txt", "r") as file:
        versions = [line.strip().split() for line in file.readlines()]

    for subfolder, new_tag, version_folder in versions:
        create_version_subfolder(subfolder, new_tag, version_folder)

if __name__ == "__main__":
    main()
