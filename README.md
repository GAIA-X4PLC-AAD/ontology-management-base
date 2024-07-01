# Ontology management

## Purpose

This repository is used to maintain the custom Ontologies and associated SHACL Shapes that are used within a specific Scope. It's also used to ensure a unified process for handling the Ontologies & Shapes.

**Ontologies** are required, when there is a need to introduce a custom type for a Self Description which should be expressed
as an OWL class. For each class a **SHACL Shape** _must_ be defined, which defines the properties for the class and optional
constraints.

## Repository structure

The repository contains a folder for each domain in the project which stores Turtle files for the domain-specific Ontologies and
associated SHACL Shapes.

Example files can be found in the folder [example](https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/example) in the this repository.

## Process

This section describes the general process to apply changes to the Ontologies & SHACL Shapes.

### General process

1. Checkout the repository
2. Create a local feature branch that will store the changes
3. Perform changes (see [Modeling Guidelines](#modeling-guidelines), [Creating a new Ontology & Shape](#creating-a-new-ontology--shape) or [Modify an existing Ontology & Shape](#modify-an-existing-ontology--shape))
4. Push the branch to remote
5. Check the [CI pipeline](#ci-pipeline) status.
6. Open a _Pull Request_ and describe the changes according to the provided template which should help the Reviewer to
   understand why the changes are important from you point of view
7. [Review process](#review-process-responsibilities) performed by Reviewers
8. (optional) Apply changes recommended by the Reviewer
9. Reviewer merges _Pull Request_ to `main` branch and adds the changes (SHACL file and/or Ontology file) to the Federated Catalogue via its API (supported by Github Action)

### Creating a new Ontology & Shape

In the case you want to create a new Class which is not suitable for the existing Ontologies, you should create a new Ontology
that contains this class. An Ontology describes a set of classes in a specific subject area and how they are related. A domain may contain multiple Ontologies.

1. Create a folder for the Domain, if it does not already exist. 
2. Create a Turtle file for the Ontology
3. Describe the new type as an OWL Class in the Ontology
4. Create a Turtle file for the SHACL Shape
5. Describe a `NodeShape` in the SHACL file that refers to the class created in step 3 and describes its properties and their
   constraints
6. Add a new entry to the CODEOWNERS file in the root directory of this repository and specify the owners for the new directory (see [Review process](#review-process-responsibilities) section below).

### Modify an existing Ontology & Shape

In the case you want to create a new Class which fits to any of the existing Ontologies in the Domain, you should add
this class to the existing Ontology.

1. Describe the new type as an OWL Class in the existing Ontology
2. Describe a `NodeShape` in the SHACL file that refers to the class created in step 1 and describes its properties and their
   constraints

### Review process responsibilities

* With github CODEOWNERS concept it is possible to define responsible users for certain directories.
* This is maintained in the CODEOWNERS file in the root directory of this repository.
* See CODEOWNERS file for github documentation and more information.
* Two reviewers should be defined. One for the syntactical part and one for the semantical part.
  * Syntactical check (reviewer 1)
    * Check whether modeling guidelines described in this README are followed.
    * Check the [CI pipeline](#ci-pipeline) status.
  * Semantical check (reviewer 2)
    * Check whether the recommended changes make sense (Is there a real need for these changes? Are there probably better solutions?).
* After the review is done, the reviewer assigns the PR back to the author for incorporation.
* After incorporation is done, the author assigns the PR back to the reviewer for final review (and so forth).

## Modeling Guidelines

This section describes guidelines that _must_ be followed when applying changes to this repository.

### General

* For _every_ custom class modeled in an Ontology a SHACL Shape must be created that is linked to the class. In addition to that there must be an example on an instance of a SHACL Shape.  

### Directories & files

* Each domain has its own directory in the root of the repository.
* Folders and filename are lowercase and words are separated by `-` (except the `_` as separator for the suffix, see below).
* The name of the directory must match the prefix defined in the Ontology and SHACL files.
* Ontologies are stored in Turtle files having a name in describing the purpose of the Ontology and a suffix `_ontology`.
  Example: `sensor_ontology.ttl`
* SHACL Shapes are stored in Turtle files having the suffix `_shacl`. Example:
  `sensor_shacl.ttl`
* The example instance of a SHACL Shape is stored in json-ld format in a json file with the suffix `_instance`. Example: `sensor_instance.json`. The content stored in the json file is also called _claims_.
  * The [SD-Creation-Wizard](https://sd-creation-wizard.gxfs.gx4fm.org/) can be used to generate the example instance of a SHACL Shape. 

### Ontologies

* Class must be a subclass of one of the Gaia-X base classes
* The name of the class must be in PascalCase. Example: `Sensor`
* The attributes of the class must be in camelCase. Example: `sensorType`
* The prefix of the ontology must match the prefix defined in the SHACL Shape.

### SHACL Shapes

* The name of the shape must be in PascalCase. Example: `SensorShape`
* The attributes of the shape must be in camelCase. Example: `sensorType`
* Shapes have the name of the linked Ontology class and a suffix `Shape`. Example: `SensorShape`
* Shapes must be linked with the associated OWL Class via the property `sh:targetClass`
* References to other Self Descriptions are specified by a property having `sh:nodeKind sh:IRI`
* The prefix of the SHACL Shape must match the prefix defined in the ontology.
* Every Shape linking to an ontology must **nest** the `general` Shape. Example:
  * Add prefix 
    ```turtle
    @prefix general:https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/general/ .
    ```
  * Nest the `GeneralShape` as a node. Replace `<your_prefix>` with the prefix of the ontology
    ```turtle
    sh:property [ sh:maxCount 1 ;
                sh:minCount 1 ;
                sh:node general:GeneralShape ;
                # some other attributes
                sh:path <your_prefix>:general ],
    ```

## CI pipeline

The CI/CD pipeline is defined in the `.github/workflows` directory. The pipeline is triggered on every push to the repository as defined in the workflow. The result can be seen in the `Actions` tab in the github repository.

### Steps
 
#### Generate VARIABLES.md (overview of used properties in the SHACL files)
The file VARIABLES.md will be generated automatically when a push to a non-main branch is executed. This file is existent in every subdirectory once there is a SHACL file containing properties. This should help to get a fast overview of the properties used in the SHACL files.

>NOTE: the VARIABLES.md file should not be changed since it will be overwritten automatically. 

#### Check syntax of Turtle files
The pipeline checks the syntax of the Turtle files (`*.ttl`) by loading a RDF graph. If the Turtle file is not correct the pipeline fails with a detailed error message.

#### Check if `_instance.json` file is conform to the SHACL Shape(s)
The pipeline checks if the `_instance.json` file is conform to the SHACL Shape(s) defined in the corresponding SHACL file. For this all `*_shacl.ttl` files in this repository are collected to be able to check against a schema not defined in the current SHACL Shape. If the instance is not conform the pipeline fails with a detailed error message.

### Run the pipeline scripts locally
```bash
# prepare venv (optional)
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv) $ python3 -m pip install --upgrade pip
(.venv) $ python3 -m pip install -r src/requirements_ci.txt
# execute check from CI
python3 src/check_ttl_syntax.py <path_to_ttl_file>
python3 src/check_jsonld_against_shacl_schema.py <directory name>
```
Example:
```bash
python3 src/check_ttl_syntax.py scenario/scenario_ontology.ttl
python3 src/check_jsonld_against_shacl_schema.py scenario
```

>You might use `py` or `python` instead of `python3` depending on your system.

## Further information

### Related repository
* [gaia-x-compliant-claims-example](https://github.com/GAIA-X4PLC-AAD/gaia-x-compliant-claims-example)
  * This repository contains an overview of how to instantiate the Gaia-X trust framework classes to create Gaia-X compliant claims.

### Helpful Plugins

To handle and display rdf-files, especially .ttl files, you can use an IDE with plugins. Following plugins have been experienced as being very helpful:

* VS Code: "Stardog RDF Grammars"
* IntelliJ: "LNKD.tech Editor"

### Known issues
#### Issues with [SD-Creation-Wizard](https://sd-creation-wizard.gxfs.gx4fm.org/)
* The wizard does not support the creation of a SHACL Shape with a nested external Shape, e. g. `GeneralShape` in `SensorShape`. To do this you have to temporarily copy the `GeneralShape` into the `SensorShape` file. This applies to all external Shapes which are not defined in the file which is loaded into the wizard.
* The wizard may generate a non conform `_instance` file when having optional structures which have mandatory attributes. 
  Example: `relatedData` in `GeneralShape`:
  ```turtle
        [ sh:node general:LinkShape ;
            sh:description "Reference to optional related assets" ;
            skos:example "at hd map, link to optional surface map" ;
            sh:name "relatedData" ;
            sh:order 2 ;
            sh:path general:relatedData ];
  ```
  If `relatedData` is not filled in the wizard, following block will be generated:
  ```json
      "general:relatedData": {
        "@type": "general:Link"
      }
  ```
  This is obviously not conform since the mandatory files `url` and `type` of `LinkShape` are missing. This [bug](https://gitlab.eclipse.org/eclipse/xfsc/self-description-tooling/sd-creation-wizard-frontend/-/issues/41) will be fixed in the future.
  > Feel free to contribute to the wizard to fix this or other issues in the gitlab repositories [backend](https://gitlab.eclipse.org/eclipse/xfsc/self-description-tooling/sd-creation-wizard-api) or [frontend](https://gitlab.eclipse.org/eclipse/xfsc/self-description-tooling/sd-creation-wizard-frontend).