# Gaia-X ontology and SHACL shapes 2210

## Table of Contents
1. [Introduction](#introduction)
2. [Source](#source)
3. [Conversion](#conversion)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Contributing](#contributing)


## Introduction
This repository contains the ontology and shapes for the Gaia-X Trust Framework Model 2210.

## Source
The source of the ontologies and shapes is the gaia-x lab registry:
- Ontology
  - https://registry.lab.gaia-x.eu/v1/api/trusted-schemas-registry/v2/schemas/gax-trust-framework
- SHACL shapes
  - https://registry.lab.gaia-x.eu/v1/api/trusted-shape-registry/v1/shapes/jsonld/trustframework#

Both ontologies and SHACL shapes were copied into the `./input/01_original` directory. The downloaded files are only available in JSON-LD format. 

## Conversion
The files in the `./input/01_original` directory are converted into turtle format with the help of the python based conversion tool stored in `./src/jsonldtottlconverter.py`. The converted files are stored in the root directory of this repository.

### Corrections of the original JSON-LD files
The conversion tool also corrects some issues in the original JSON-LD files and stores them into the directory `./input/02_corrected`.

- change namespace in ontology from `http://w3id.org/gaia-x/gax-trust-framework` to `https://registry.lab.gaia-x.eu/development/api/trusted-shape-registry/v1/shapes/jsonld/trustframework` so it fits to the referenced namespace in the shapes. Otherwise the ontology and the shapes would not have a relation.
- append the suffix `Shape` to certain Shapes where this suffix is missing. This is necessary because of a name clash between ontology and shacl shapes if the names are equal.
- Correction of the `http://www.w3.org/2006/vcard/ns#Address`: The node becomes `AddressShape` and the link to this shape as a node also references the `AddressShape` instead of the `Address` node. 
- Change LegalPerson to LegalParticipant in the ontology since LegalPerson is not existing the shacl shape and [gx wizard](https://wizard.lab.gaia-x.eu/] generates) generates participant credentials as LegalParticipant.

The concrete changes can be made visible by comparing the original and corrected files.

## Installation
A python installation is mandatory to execute the python script. No additional libraries are needed since only standard libraries are used.

## Usage

```bash
cd gx/src
py jsonldtottlconverter.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.