Ontology management
====

## Description

This repository is used to maintain the custom Ontologies and associated SHACL Shapes that are used within the project. It's
also used to ensure a unified process for handling the Ontologies & Shapes.

**Ontologies** are required, when there is a need to introduce a custom type for a Self Description which _must_ be expressed
as an OWL Class. For each Class a **SHACL Shape** _must_ be defined which defines the properties for the class and optional
constraints.

The type is defined using the property `@type` in the `credentialSubject` of a Verifiable Credential, as shown in the following
example:

```json
{
  "credentialSubject": {
    "@context": {
      "example_ns": "http://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#"
    },
    "@id": "did:example:test1",
    "@type": "example_ns:CustomClass"
  }
```

Note: In the following sections the term _type_ has the same meaning as _OWL Class_.

## Repository structure

The repository contains a folder for each Domain in the project which stores Turtle files for the Domain-specific Ontologies and
associated SHACL Shapes.

Example files can be found in the folder `examples/`.

## Process

This section describes the general process to apply changes to the Ontologies & SHACL Shapes.

### General process

1. Checkout the repository
2. Create a local feature branch that will store the changes
3. Perform changes (see "Modeling Guidelines")
4. Push the branch to remote
5. Open a _Pull Request_ and describe the changes according to the provided template which should help the Reviewer to
   understand why the changes are important from you point of view
6. Review process performed by a _Reviewer_
7. (optional) Apply changes recommended by the Reviewer
8. Reviewer merges _Pull Request_ to `main` branch
9. One of the Reviewers adds the changes (SHACL file and/or Ontology file) to the Federated Catalogue via its API

### Creating a new Ontology & Shape

In the case you want to create a new Class which not be suitable for the existing Ontologies, you should create a new Ontology
that contains this class. An Ontology describes a set of classes in a specific subject area and how they are related. A
domain may contain multiple Ontologies.

1. Create a folder for the Domain, if it does not already exist. Consider to update the CODEOWNERS file if applicable (see CODEOWNERS section below)
2. Create a Turtle file for the Ontology
3. Describe the new type as an OWL Class in the Ontology
4. Create a Turtle file for the SHACL Shape
5. Describe a `NodeShape` in the SHACL file that refers to the class created in step 3 and describes its properties and their
   constraints

### Modify an existing Ontology & Shape

In the case you want to create a new Class which fits to any of the existing Ontologies in the Domain, you should add
this class to the existing Ontology.

1. Describe the new type as an OWL Class in the existing Ontology
2. Describe a `NodeShape` in the SHACL file that refers to the class created in step 1 and describes its properties and their
   constraints

### Review process

There should be two reviewers. One for the syntactical part and one for the semantical part.
* Syntactical check (reviewer 1)
  * Check whether modeling guidelines described in this README are followed.
  * Check whether the shacl file can be uploaded to the sd-creation-wizard (https://sd-creation-wizard.gxfs.gx4fm.org/)
* Semantical check (reviewer 2)
  * Check whether the recommended changes make sense (Is there a real need for these changes? Are there probably better solutions?).

### Responsible users for directories

* With github CODEOWNERS concept it is possible to define responsible users for certain directories.
* This is maintained in the CODEOWNERS file in the root directory of this repository.
* It is possible to define a reviewer for the syntactical part as well as the semantical part. 
* See CODEOWNERS file for github documentation and more information.

### Generating VARIABLES.md (overview of used properties in the SHACL files)

TODO: Check if this still will be correct and change if not.
The file VARIABLES.md will be generated automatically when a merge to main is executed. This file is existent in every subdirectory once there is a SHACL file containing properties. This should help to get a fast overview of the properties used in the SHACL files.

NOTE: the VARIABLES.md file should not be changed since it will be overwritten automatically 

## Modeling Guidelines

This section describes that _must_ be followed when applying changes to this repository.

### General

* For _every_ custom class modeled in an Ontology a SHACL Shape must be created that is linked to the class

### Files

* Ontologies are stored in Turtle files having a name in describing the purpose of the Ontology and a suffix `_ontology`.
  Example: `sensor_ontology.ttl`
* SHACL Shapes are stored in Turtle files having the suffix `_shacl`. Example:
  `sensor_shacl.ttl`
* Filename are lowercase and word separated by `_`

### Ontologies

* Class must be a direct subclass of one of the Gaia-X base classes
    * A current limitation in the XFSC Federated Catalogue requires offerings to be a subclass of `gax-core:ServiceOffering`. The
      namespace must be defined in the file header as the following: `@prefix gax-core: <https://w3id.org/gaia-x/core#> .`
* Follow the Guidelines described in [Open Data Support - Designing and developing
  RDF vocabularies](https://data.europa.eu/sites/default/files/d2.1.2_training_module_2.4_designing_and_developing_vocabularies_in_rdf_en_edp.pdf)

### SHACL Shapes

* Shapes have the name of the linked Ontology class and a suffix `Shape`. Example: `ExampleServiceOfferingShape`
* Shapes must be linked with the associated OWL Class via the property `sh:targetClass`
* References to other Self Descriptions are specified by a property having nodeKind `sh:IRI`

### Default namespaces

The following table contains the definitions of namespaces and prefixes that are to be used when referring to them when 
modeling Ontologies or SHACL Shapes. 

| Prefix     | Namespace                                      | Scope (Public or Project) | Documentation (optional) | Description                                                                                     |
|------------|------------------------------------------------|---------------------------|--------------------------|-------------------------------------------------------------------------------------------------|
| xsd        | http://www.w3.org/2001/XMLSchema#              | Public                    |                          | XML Schema Namespace                                                                            |
| sh         | http://www.w3.org/ns/shacl#                    | Public                    |                          | SHACL Namespace                                                                                 |
| gax-core   | https://w3id.org/gaia-x/core#                  | Public                    |                          | Namespace of Gaia-X core Ontology which contains the Gaia-X superclasses (e.g. ServiceOffering) |
| surveyonto | http://semanticweb.org/metadatasurveyontology/ | Project                   |                          | Namespace of Survey Ontology for Bullwhip Effect                                                | 
| plc-aad    | https://www.gaia-x4plcaad.info/common/         | Project                   |                          | Namespace of common classes and properties for the project PLC-AAD                              |


## Further information

### Helpful Plugins
To handle and display rdf-files, especially .ttl files, you can use an IDE with helpful plugins. Following plugins have been experienced as being very helpful:
* VS Code: "Stardog RDF Grammars"
* IntelliJ: "LNKD.tech Editor"

### TODOs / Open Questions

* Questions
    * How many reviewers are required and who's part of the group of reviewers? It must be ensured that every reviewer has deep
      knowledge of the Gaia-X requirements and follows them while reviewing the PRs
    * Who's responsible to add Ontologies & Shapes to the Federated Catalogue?
* Other
    * Define clean guidelines for modeling
