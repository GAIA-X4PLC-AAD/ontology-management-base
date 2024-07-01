import rdflib
import os
import shutil
import re
import json
from collections import OrderedDict


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

    # replace the namespace (prefix)
    filedata = filedata.replace("http://w3id.org/gaia-x/gax-trust-framework", "https://registry.lab.gaia-x.eu/development/api/trusted-shape-registry/v1/shapes/jsonld/trustframework")

    # Write the file out again
    with open(filepath, 'w') as file:
        file.write(filedata)
    print(f"  Namespace in file {filepath} was successfully corrected.")


def correct_shape_suffix(filepath):
    with open(filepath, 'r') as file:
        filedata = file.read()

    # Replace the target strings --> append "Shape"
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

    # Replace the sh:node part --> append "Shape"
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


def correct_legal_participant(filepath):
    with open(filepath, 'r') as file:
        filedata = file.read()

    # Replace the target strings since LegalPerson is LegalParticipant in the SHACL shape
    filedata = filedata.replace('#LegalPerson', '#LegalParticipant')

    # Write the file out again
    with open(filepath, 'w') as file:
        file.write(filedata)
    print(f"  LegalPerson to LegalParticipant in file {filepath} were successfully corrected.")


def correct_sub_class_of_attribute(filepath):
    with open(filepath, 'r') as file:
        filedata = file.read()

    # Replace the target strings, for subclass as well as range attributes. Indentation is crucial!
    filedata = filedata.replace('        "@id": "http://w3id.org/gaia-x/core#Participant"',     '        "@id": "https://w3id.org/gaia-x/core#Participant"')
    filedata = filedata.replace('        "@id": "http://w3id.org/gaia-x/core#Resource"',        '        "@id": "https://w3id.org/gaia-x/core#Resource"')
    filedata = filedata.replace('        "@id": "http://w3id.org/gaia-x/core#ServiceOffering"', '        "@id": "https://w3id.org/gaia-x/core#ServiceOffering"')

    # Write the file out again
    with open(filepath, 'w') as file:
        file.write(filedata)
    print(f"  subClassOf attribute file {filepath} were successfully corrected.")


def correct_legal_registration_number(filepath):
    with open(filepath, 'r') as file:
        filedata = file.read()

    # Replace the nested legalRegistrationNumber (sh:node) with a class definition (sh:class) to link via IRI.
    # Note: type is lowercase since gx wizard generates this type lowercase!
    pattern = r'"sh:path": {\s*"@id": "gx:legalRegistrationNumber"\s*},\s*"sh:node": {\s*"@id": "gx:legalRegistrationNumberShape"\s*},\s*"sh:minCount": 1'
    replacement = '"sh:class": {\n            "@id": "gx:legalRegistrationNumber"\n          },\n          "sh:minCount": 1,\n          "sh:nodeKind": {\n            "@id": "sh:IRI"\n          },\n          "sh:path": {\n            "@id": "gx:legalRegistrationNumber"\n          }'
    filedata = re.sub(pattern, replacement, filedata, flags=re.MULTILINE)

    # Write the file out again
    with open(filepath, 'w') as file:
        file.write(filedata)

    print(f"  Legal registration number section in file {filepath} was successfully corrected.")


def correct_missing_legal_registration_number(filepath):
    with open(filepath, 'r') as json_file:
        data = json.load(json_file, object_pairs_hook=OrderedDict)

    # add legalRegistrationNumber to the ontology (since it is missing). Note the lower case type because of gx wizard.
    new_element = {
        "@id": "https://registry.lab.gaia-x.eu/development/api/trusted-shape-registry/v1/shapes/jsonld/trustframework#legalRegistrationNumber",
        "@type": [
            "http://www.w3.org/2002/07/owl#Class"
        ],
        "http://www.w3.org/2000/01/rdf-schema#label": [
            {
                "@language": "en",
                "@value": "Legal Registration Number"
            }
        ]
    }
    data.append(new_element)

    # Write the data back to the file
    with open(filepath, 'w') as json_file:
        json.dump(data, json_file, indent=2, ensure_ascii=False)

    print(f"   Legal registration number in file {filepath} was successfully added.")


def correct_link_from_class_to_node(filepath):
    with open(filepath, 'r') as file:
        filedata = file.read()

        # Replace the sh:class part with sh:node for gx:ServiceOffering
    pattern_service_offering = r'"sh:class": {\s*"@id": "gx:ServiceOffering"\s*},\s*"sh:description": "A resolvable link to the data exchange component that exposes the data resource.",'
    replacement_service_offering = '"sh:node": {\n            "@id": "gx:ServiceOffering"\n          },\n          "sh:description": "A resolvable link to the data exchange component that exposes the data resource.",'
    filedata = re.sub(pattern_service_offering, replacement_service_offering, filedata, flags=re.MULTILINE)

    # Replace the sh:class part with sh:node for gx:LegalParticipant
    pattern_legal_participant = r'"sh:class": {\s*"@id": "gx:LegalParticipant"\s*},'
    replacement_legal_participant = '"sh:node": {\n            "@id": "gx:LegalParticipant"\n          },'
    filedata = re.sub(pattern_legal_participant, replacement_legal_participant, filedata, flags=re.MULTILINE)

    # Write the file out again
    with open(filepath, 'w') as file:
        file.write(filedata)

    print(f"  sh:class to sh:node in file {filepath} was successfully corrected.")


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
process_file(ONTOLOGY_JSON_FILE, [correct_namespace, correct_legal_participant, correct_sub_class_of_attribute,
                                  correct_missing_legal_registration_number])

# process SHACL
process_file(SHACL_JSON_FILE, [correct_shape_suffix, correct_address_shape, correct_legal_registration_number,
                               correct_link_from_class_to_node])


