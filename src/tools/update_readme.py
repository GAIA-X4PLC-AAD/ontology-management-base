import os
import xml.etree.ElementTree as ET

# CONFIGURATION
XML_FILE = "artifacts/catalog-v001.xml"
README_FILE = "README.md"
START_MARKER = ""
END_MARKER = ""


def generate_table():
    tree = ET.parse(XML_FILE)
    root = tree.getroot()

    # Define namespace map (from your XML)
    ns = {"c": "urn:oasis:names:tc:entity:xmlns:xml:catalog"}

    table_lines = [
        "| Ontology / Resource IRI | Local Artifact File |",
        "| :--- | :--- |",
    ]

    for uri_elem in root.findall("c:uri", ns):
        name = uri_elem.get("name")
        uri = uri_elem.get("uri")

        # Build the link relative to root (prepending artifacts/)
        local_link = f"[{(uri)}]({os.path.join('artifacts', uri)})"
        table_lines.append(f"| `{name}` | {local_link} |")

    return "\n".join(table_lines)


def update_readme():
    new_table = generate_table()

    with open(README_FILE, "r") as f:
        content = f.read()

    # Check if markers exist
    if START_MARKER not in content or END_MARKER not in content:
        print("Error: Markers not found in README.md")
        return

    # Replace content between markers
    start_index = content.find(START_MARKER) + len(START_MARKER)
    end_index = content.find(END_MARKER)

    new_content = content[:start_index] + "\n" + new_table + "\n" + content[end_index:]

    with open(README_FILE, "w") as f:
        f.write(new_content)
    print("README updated successfully.")


if __name__ == "__main__":
    update_readme()
