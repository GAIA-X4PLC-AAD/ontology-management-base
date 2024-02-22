# Ontology management

## Description

This repository is used to maintain the custom Ontologies and associated SHACL Shapes that are used within a specific Scope (Base-X). It's
also used to ensure a unified process for handling the Ontologies & Shapes.

**Ontologies** are required, when there is a need to introduce a custom type for a Self Description which should be expressed
as an OWL Class. For each Class a **SHACL Shape** _must_ be defined, which defines the properties for the class and optional
constraints.

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
8. Reviewer merges _Pull Request_ to `main` branch and adds the changes (SHACL file and/or Ontology file) to the Federated Catalogue via its API (supported by Github Action)

### Review process responsibilities

* With github CODEOWNERS concept it is possible to define responsible users for certain directories.
* This is maintained in the CODEOWNERS file in the root directory of this repository.
* See CODEOWNERS file for github documentation and more information.
* Two reviewers should be defined. One for the syntactical part and one for the semantical part.
  * Syntactical check (reviewer 1)
    * Check whether modeling guidelines described in this README are followed.
    * Check whether the shacl file fulfills the rules of the SHACL format.
  * Semantical check (reviewer 2)
    * Check whether the recommended changes make sense (Is there a real need for these changes? Are there probably better solutions?).

### Generating VARIABLES.md (overview of used properties in the SHACL files)

The file VARIABLES.md will be generated automatically when a merge to main is executed. This file is existent in every subdirectory once there is a SHACL file containing properties. This should help to get a fast overview of the properties used in the SHACL files.

NOTE: the VARIABLES.md file should not be changed since it will be overwritten automatically. For further information, see "GITHUB_ACTIONS.md" file in the root directory.

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
* Follow the Guidelines described in [Open Data Support - Designing and developing
  RDF vocabularies](https://data.europa.eu/sites/default/files/d2.1.2_training_module_2.4_designing_and_developing_vocabularies_in_rdf_en_edp.pdf)

### SHACL Shapes

* Shapes have the name of the linked Ontology class and a suffix `Shape`. Example: `ExampleServiceOfferingShape`
* Shapes must be linked with the associated OWL Class via the property `sh:targetClass`
* References to other Self Descriptions are specified by a property having nodeKind `sh:IRI`

## Further information

### Helpful Plugins

To handle and display rdf-files, especially .ttl files, you can use an IDE with plugins. Following plugins have been experienced as being very helpful:

* VS Code: "Stardog RDF Grammars"
* IntelliJ: "LNKD.tech Editor"
