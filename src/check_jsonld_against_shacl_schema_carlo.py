import sys
import glob
import os
import json
from rdflib import Graph, URIRef, Namespace
from pyshacl import validate

def resolve_prefixed_type(json_type, context):
    """Converts a prefixed type like 'hdmap:HdMap' to a full IRI and normalizes it."""
    if ":" in json_type:
        prefix, suffix = json_type.split(":", 1)
        base_iri = context.get(prefix, "").rstrip("/")
        if base_iri:
            return f"{base_iri}/{suffix}"
    return json_type

def load_shacl_files(root_dir):
    """Loads all SHACL files and extracts shape mappings based on sh:targetClass."""
    shacl_graph = Graph()
    shape_mappings = {}

    shacl_files = glob.glob(f'{root_dir}/**/*_shacl.ttl', recursive=True)
    for shacl_file in shacl_files:
        shacl_graph.parse(shacl_file, format='turtle')

    SH = Namespace("http://www.w3.org/ns/shacl#")
    for s, _, o in shacl_graph.triples((None, SH.targetClass, None)):
        shape_mappings.setdefault(str(o), []).append(str(s))

    print(f"✅ Loaded {len(shacl_files)} SHACL files, found {len(shape_mappings)} ontology classes with shapes.")
    return shacl_graph, shape_mappings

def extract_references(instance_file, json_data):
    """Extracts referenced files and their sh:conformsTo values."""
    reference_files = []
    conforms_to_shapes = []

    for key, value in json_data.items():
        if isinstance(value, dict) and value.get("@type") == "manifest:Link":
            file_metadata = value.get("manifest:fileMetaData", {})
            if isinstance(file_metadata, dict) and "sh:conformsTo" in file_metadata:
                ref_path = file_metadata.get("manifest:uri", {}).get("@value", file_metadata.get("manifest:uri"))
                if not ref_path:
                    continue

                reference_file_path = os.path.normpath(os.path.join(os.path.dirname(instance_file), ref_path))
                if not os.path.exists(reference_file_path):
                    print(f"⚠️ Warning: Referenced file {reference_file_path} does not exist.")
                    continue

                reference_files.append(reference_file_path)

                conforms_to = file_metadata.get("sh:conformsTo", [])
                if isinstance(conforms_to, dict):
                    conforms_to = [conforms_to]

                for conforms_entry in conforms_to:
                    conforms_id = conforms_entry.get("@id")
                    if conforms_id:
                        conforms_to_shapes.append(conforms_id)

    print(f"🔗 Found {len(reference_files)} referenced files: {reference_files}")
    print(f"🔍 Extracted `sh:conformsTo` shapes: {conforms_to_shapes}")

    return reference_files, conforms_to_shapes

def validate_jsonld(shacl_graph, file_path, additional_files=None, conforms_to_shapes=None, processed_files=None):
    """Validates a JSON-LD file against SHACL shapes, ensuring reference files are included."""
    if processed_files is None:
        processed_files = set()

    if file_path in processed_files:
        return []
    processed_files.add(file_path)

    failed_validations = []
    data_graph = Graph()

    # Load the main JSON-LD instance file
    try:
        data_graph.parse(file_path, format="json-ld")
        print(f"📄 Loaded instance file: {file_path}")
    except Exception as e:
        print(f"❌ Error parsing JSON-LD file {file_path}: {e}")
        return [(False, file_path, f"Parsing error: {e}")]

    # Load additional referenced JSON-LD files
    if additional_files:
        for ref_file in additional_files:
            if os.path.exists(ref_file) and ref_file not in processed_files:
                try:
                    data_graph.parse(ref_file, format="json-ld")
                    processed_files.add(ref_file)
                    print(f"✅ Merged reference file into validation graph: {ref_file}")
                except Exception as e:
                    print(f"❌ Error parsing reference file {ref_file}: {e}")

    # Debug: Check the RDF Graph after merging references
    print("🔎 RDF Graph Before Validation (first 1000 chars):")
    print(data_graph.serialize(format="turtle")[:1000])

    # Debug: Check applied SHACL shapes
    print("🔎 Checking applied SHACL shapes:")
    for s, p, o in shacl_graph.triples((None, URIRef("http://www.w3.org/ns/shacl#targetClass"), None)):
        print(f"   - Shape: {s} applies to {o}")

    # Ensure `sh:conformsTo` constraints are applied correctly
    if conforms_to_shapes:
        print("🔍 Validating reference files explicitly with extracted `sh:conformsTo` shapes...")
        for shape in conforms_to_shapes:
            if (URIRef(shape), None, None) in shacl_graph:
                print(f"✅ `{shape}` is correctly applied in the SHACL validation.")
            else:
                print(f"❌ ERROR: `{shape}` is MISSING in the SHACL validation!")

    # Run SHACL Validation
    print(f'🔍 Validating {file_path} and its references...')
    conforms, _, v_text = validate(
        data_graph,
        shacl_graph=shacl_graph,
        inference='rdfs',
        debug=False,
        advanced=True
    )

    if not conforms:
        failed_validations.append((conforms, file_path, v_text))

    return failed_validations

def main():
    if len(sys.argv) < 2:
        print('Usage: python validate_jsonld_shacl.py <directory or file> [additional files...]')
        sys.exit(1)

    paths = sys.argv[1:]
    print('🔍 Loading SHACL shapes...')
    shacl_graph, shape_mappings = load_shacl_files('.')

    instance_files = []
    processed_files = set()

    for path in paths:
        if os.path.isdir(path):
            instance_files.extend(glob.glob(f'{path}/*_instance.json'))
        elif os.path.isfile(path) and path.endswith("_instance.json"):
            instance_files.append(path)

    failed_validations = []

    for instance_file in instance_files:
        print(f'📂 Processing: {instance_file}')

        with open(instance_file, 'r') as f:
            json_data = json.load(f)

        reference_files, conforms_to_shapes = extract_references(instance_file, json_data)

        # Step 1: Validate the main instance file
        failed_validations.extend(validate_jsonld(shacl_graph, instance_file, reference_files, None, processed_files))

        # Step 2: Explicitly validate referenced files with extracted `sh:conformsTo`
        for ref_file in reference_files:
            failed_validations.extend(validate_jsonld(shacl_graph, ref_file, None, conforms_to_shapes, processed_files))

    print("\n##### VALIDATION RESULTS #####\n")

    for _, _, v_text in failed_validations:
        print("$$_$$")
        print(v_text)

    if not failed_validations:
        print("✅ All files passed validation!")

if __name__ == "__main__":
    main()
