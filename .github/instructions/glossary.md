# Glossary

## Domain Terminology

| Term         | Definition                                                                                                 |
| ------------ | ---------------------------------------------------------------------------------------------------------- |
| **Ontology** | A formal specification of concepts and relationships in a domain, expressed in OWL (Web Ontology Language) |
| **SHACL**    | Shapes Constraint Language - W3C standard for validating RDF data against constraints                      |
| **JSON-LD**  | JSON for Linking Data - a JSON-based format for representing RDF data                                      |
| **Turtle**   | Terse RDF Triple Language - a compact text format for RDF                                                  |
| **Domain**   | A specific topic area with its own ontology (e.g., `manifest`, `scenario`, `hdmap`)                        |
| **Instance** | A JSON-LD file containing actual data that conforms to an ontology                                         |
| **Shape**    | A SHACL definition that constrains what valid data looks like                                              |
| **Fixture**  | A mock/sample file used during testing to represent external references                                    |

## File Types

| Extension           | Content                                | Location                           |
| ------------------- | -------------------------------------- | ---------------------------------- |
| `.owl.ttl`          | OWL ontology in Turtle format          | `artifacts/{domain}/`              |
| `.shacl.ttl`        | SHACL shapes in Turtle format          | `artifacts/{domain}/`              |
| `.context.jsonld`   | JSON-LD context file                   | `artifacts/{domain}/`              |
| `.json` / `.jsonld` | JSON-LD instance data                  | `tests/data/{domain}/`             |
| `.expected`         | Expected error output for invalid test | `tests/data/{domain}/invalid/`     |
| `catalog-v001.xml`  | OASIS XML catalog                      | `artifacts/`, `imports/`, `tests/` |

## IRI Patterns

| Pattern                                             | Example                                           | Meaning                                       |
| --------------------------------------------------- | ------------------------------------------------- | --------------------------------------------- |
| `https://w3id.org/ascs-ev/envited-x/{domain}/v{n}/` | `https://w3id.org/ascs-ev/envited-x/scenario/v5/` | Ontology namespace                            |
| `did:web:{host}:{Type}:{id}`                        | `did:web:registry.gaia-x.eu:LegalPerson:abc`      | Decentralized identifier (external reference) |
| `http://www.w3.org/...`                             | `http://www.w3.org/2001/XMLSchema#string`         | W3C standard namespace                        |

## Catalog Terminology

| Term                  | Definition                                                                            |
| --------------------- | ------------------------------------------------------------------------------------- |
| **Catalog**           | An XML file mapping IRIs to local file paths (OASIS standard)                         |
| **Artifacts Catalog** | `artifacts/catalog-v001.xml` - maps ontology IRIs to OWL/SHACL files                  |
| **Imports Catalog**   | `imports/catalog-v001.xml` - maps base ontology IRIs (RDF, RDFS, OWL) to local copies |
| **Tests Catalog**     | `tests/catalog-v001.xml` - lists test data files with metadata                        |
| **Temporary Catalog** | In-memory catalog built for `--path` mode validation                                  |

## Validation Terminology

| Term                       | Definition                                                                   |
| -------------------------- | ---------------------------------------------------------------------------- |
| **Syntax Validation**      | Checking that files are well-formed JSON or Turtle                           |
| **Coherence Validation**   | Checking that SHACL target classes exist in the OWL ontology                 |
| **Conformance Validation** | Checking that data instances satisfy SHACL constraints                       |
| **Inference**              | Deriving implicit triples from explicit ones (e.g., RDFS subclass reasoning) |

## Return Code Categories

| Range     | Category           |
| --------- | ------------------ |
| `0`       | Success            |
| `1`       | General error      |
| `99`      | Dependency error   |
| `100`     | Skipped/not found  |
| `101-102` | Syntax errors      |
| `200-209` | Coherence errors   |
| `210-219` | Conformance errors |

## RDF Terminology

| Term           | Definition                                                                       |
| -------------- | -------------------------------------------------------------------------------- |
| **Triple**     | A statement of (subject, predicate, object)                                      |
| **Graph**      | A collection of triples                                                          |
| **IRI**        | Internationalized Resource Identifier - globally unique identifier               |
| **Blank Node** | An anonymous node in an RDF graph (no IRI)                                       |
| **Literal**    | A data value (string, number, date, etc.)                                        |
| **Prefix**     | A shorthand for an IRI namespace (e.g., `gx:` for `https://w3id.org/gaia-x/...`) |

## Module Terminology

| Term                  | Definition                                                                 |
| --------------------- | -------------------------------------------------------------------------- |
| **file_collector**    | Internal utility for scanning file systems (used by registry_updater only) |
| **registry_updater**  | Module that creates and updates catalog XML files                          |
| **registry_resolver** | Module that reads catalogs and resolves IRIs to paths                      |
| **graph_loader**      | Module that loads RDF files into rdflib Graph objects                      |
| **validator**         | Module that performs a specific type of validation                         |

## ENVITED-X Specific

| Term              | Definition                                                                     |
| ----------------- | ------------------------------------------------------------------------------ |
| **ENVITED-X**     | The parent project/ecosystem this ontology suite belongs to                    |
| **Data Resource** | A dataset described by metadata (from Gaia-X)                                  |
| **Manifest**      | A file listing the contents and metadata of a data package                     |
| **Georeference**  | Geographic coordinate system and location information                          |
| **Gaia-X**        | European data infrastructure initiative; provides base types (`gx:` namespace) |
