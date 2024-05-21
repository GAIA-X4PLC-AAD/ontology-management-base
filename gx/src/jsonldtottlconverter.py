import rdflib
import os
import shutil
import re


SOURCE_FOLDER = os.path.join(os.getcwd(), "../input/01_original")  # folder, where jsonld files are stored in .json format
CORRECTION_FOLDER = os.path.join(os.getcwd(), "../input/02_corrected")  # folder, where corrected jsonld files are stored in .json format
TARGET_FOLDER = os.path.join(os.getcwd(), "../")  # folder, where the resulting .ttl files shall be written to
ONTOLOGY_JSON_FILE = "gx_ontology.json"
SHACL_JSON_FILE = "gx_shacl.json"


def convert(input_filepath, output_filepath):
    graph = rdflib.Graph()
    graph.parse(location=input_filepath, format="json-ld")
    graph.serialize(destination=output_filepath, format="turtle")
    print(f"  File {output_filepath} was successfully converted to turtle.")


def correct_namespace(filepath):
    with open(filepath, 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace("http://w3id.org/gaia-x/gax-trust-framework", "https://registry.lab.gaia-x.eu/development/api/trusted-shape-registry/v1/shapes/jsonld/trustframework")

    # Write the file out again
    with open(filepath, 'w') as file:
        file.write(filedata)
    print(f"  Namespace in file {filepath} was successfully corrected.")


def correct_shape_suffix(filepath):
    with open(filepath, 'r') as file:
        filedata = file.read()

    # Replace the target strings
    filedata = filedata.replace('"@id": "gx:DataResource",', '"@id": "gx:DataResourceShape",', 1)
    filedata = filedata.replace('"@id": "gx:InstantiatedVirtualResource",', '"@id": "gx:InstantiatedVirtualResourceShape",', 1)
    filedata = filedata.replace('"@id": "gx:LegitimateInterest",', '"@id": "gx:LegitimateInterestShape",', 1)
    filedata = filedata.replace('"@id": "gx:ServiceAccessPoint",', '"@id": "gx:ServiceAccessPointShape",', 1)
    filedata = filedata.replace('"@id": "gx:SoftwareResource",', '"@id": "gx:SoftwareResourceShape",', 1)
    filedata = filedata.replace('"@id": "gx:VirtualResource",', '"@id": "gx:VirtualResourceShape",', 1)
    filedata = filedata.replace('"@id": "gx:PhysicalResource",', '"@id": "gx:PhysicalResourceShape",', 1)
    # Write the file out again
    with open(filepath, 'w') as file:
        file.write(filedata)
    print(f"  Shape suffixes in file {filepath} were successfully corrected.")


def correct_address_shape(filepath):
    with open(filepath, 'r') as file:
        filedata = file.read()

    # Replace the sh:node part
    pattern = r'\s*"sh:node": {\s*"@id": "http://www.w3.org/2006/vcard/ns#Address"\s*},'
    replacement = '\n          "sh:node": {\n            "@id": "http://www.w3.org/2006/vcard/ns#AddressShape"\n          },'
    filedata = re.sub(pattern, replacement, filedata, flags=re.MULTILINE)

    # replace the shape definition
    pattern = r'\s*"@id": "http://www.w3.org/2006/vcard/ns#Address",\s*\n\s*"@type": "sh:NodeShape",'
    replacement = '\n      "@id": "http://www.w3.org/2006/vcard/ns#AddressShape",\n      "@type": "sh:NodeShape",'

    filedata = re.sub(pattern, replacement, filedata, flags=re.MULTILINE)

    # Write the file out again
    with open(filepath, 'w') as file:
        file.write(filedata)
    print(f"  Address shape in file {filepath} was successfully corrected.")


def process_file(json_file, correction_functions):
    print("")
    print(f"File {json_file}: start process.")
    input_path = os.path.join(SOURCE_FOLDER, json_file)
    correction_path = os.path.join(CORRECTION_FOLDER, json_file)
    output_path = os.path.join(TARGET_FOLDER, json_file.removesuffix(".json")) + ".ttl"
    shutil.copy2(input_path, correction_path)

    for correction_function in correction_functions:
        correction_function(correction_path)

    convert(correction_path, output_path)
    print(f"File {correction_path} was successfully processed.")


# process ontology
process_file(ONTOLOGY_JSON_FILE, [correct_namespace])

# process SHACL
process_file(SHACL_JSON_FILE, [correct_shape_suffix, correct_address_shape])
