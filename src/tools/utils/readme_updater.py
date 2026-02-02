import os
import xml.etree.ElementTree as ET

# CONFIGURATION
XML_FILE = "artifacts/catalog-v001.xml"
README_FILE = "README.md"
START_MARKER = "<!-- START_CATALOG_TABLE -->"
END_MARKER = "<!-- END_CATALOG_TABLE -->"


def generate_table():
    tree = ET.parse(XML_FILE)
    root = tree.getroot()

    # Define namespace map (from your XML)
    ns = {"c": "urn:oasis:names:tc:entity:xmlns:xml:catalog"}

    table_lines = [
        "| Ontology / Resource IRI | Local Artifact File |",
        "| :--- | :--- |",
    ]

    # 1. Collect all entries into a list of tuples or dictionaries
    entries = []
    for uri_elem in root.findall("c:uri", ns):
        name = uri_elem.get("name")
        uri = uri_elem.get("uri")
        if name and uri:  # Basic safety check
            entries.append((name, uri))

    # 2. Sort the list alphabetically by the first element (name)
    #    key=lambda x: x[0].lower() ensures case-insensitive sorting
    entries.sort(key=lambda x: x[0].lower())

    # 3. Build the table rows from the sorted list
    for name, uri in entries:
        # Build the link relative to root (prepending artifacts/)
        local_link = f"[{(uri)}]({os.path.join('artifacts', uri)})"
        table_lines.append(f"| `{name}` | {local_link} |")

    return "\n".join(table_lines)


def update_readme():
    if not os.path.exists(XML_FILE):
        print(f"Error: XML file not found at {XML_FILE}")
        return

    if not os.path.exists(README_FILE):
        print(f"Error: README file not found at {README_FILE}")
        return

    new_table = generate_table()

    with open(README_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Find marker positions
    start_pos = content.find(START_MARKER)
    end_pos = content.find(END_MARKER)

    if start_pos == -1 or end_pos == -1:
        print("Error: Markers not found in README.md")
        return

    # Validate marker order
    if start_pos >= end_pos:
        print("Error: Markers are in incorrect order")
        return

    # Calculate insertion positions
    start_index = start_pos + len(START_MARKER)
    end_index = end_pos

    # Build new content
    new_content = content[:start_index] + "\n" + new_table + "\n" + content[end_index:]

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("README updated successfully.")


if __name__ == "__main__":
    update_readme()
