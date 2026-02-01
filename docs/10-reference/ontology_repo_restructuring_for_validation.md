# Strategic Reorganization and Modernization of the GAIA-X4PLC-AAD Ontology Management Architecture

## Executive Summary

The engineering of semantic systems within decentralized data ecosystems—specifically the GAIA-X 4 Product Lifecycle Across Automated Driving (GAIA-X4PLC-AAD)—demands a repository architecture that is not merely a storage location for files, but a functional engine for semantic consistency. The current state of the ontology-management-base repository, while functional for early-stage development, exhibits structural characteristics that will impede scalability, reproducibility, and automated validation as the ecosystem matures. This document analyzes the existing infrastructure and proposes a reorganization plan to address issues such as flat directory structures, manual import management, and fragmented validation scripts.

The proposed architecture facilitates a shift from manual ontology authoring to Model-Driven Engineering (MDE), anchored in three pillars:

1. Structural separation of maintained vs. imported ontologies.
2. Local catalog-mediated resolution using `ontoenv` and XML catalogs.
3. LinkML-driven meta-modeling to generate OWL, SHACL, JSON-LD contexts, and docs from a single source of truth.

---

## 1. Diagnostic Analysis of the Current Repository Architecture

This section dissects structural patterns, workflow limitations, and technical debt that impede scalability and interoperability.

### 1.1 Structural Audit: The Limitations of Flat-Domain Organization

The repository currently uses a flat-domain topology where each domain folder contains ontology files, SHACL shapes, examples, and tests. This approach offers visibility but introduces risks:

#### 1.1.1 Conflation of Source and Distribution

Serialized Turtle files are edited and distributed directly, conflating source and build artifacts. This increases the chance of drift between OWL, SHACL, and documentation.

#### 1.1.2 Scalability of Root-Level Domains

A root-level collection of domains becomes cluttered as the number of domains grows and lacks a standard place for external dependencies.

### 1.2 The Dependency Fragility of Web-Based Imports

Relying on web-based `owl:imports` forces tools to fetch external IRIs at load time, creating network dependencies, potential IRI rot, and offline failures.

### 1.3 Validation and Testing Limitations

Custom validation scripts increase maintenance burden and tests spread across domain folders complicate unified CI test runners.

---

## 2. Architectural Principles for Scalable Semantic Engineering

- Strict separation: `src/` (maintained) vs `imports/` (external, read-only).
- Catalog-mediated resolution: `catalog-v001.xml` maps IRIs -> local files.
- Single source of truth: LinkML YAML generates OWL/SHACL/docs/contexts.

---

## 3. Proposed Repository Layout (Blueprint)

```
ontology-management-base/
├── .github/
├── .ontoenv/
├── config/
│   └── ontoenv.toml
├── imports/        # local copies of external ontologies
├── src/
│   ├── linkml/     # LinkML source
│   └── ontology/   # legacy/manual sources
├── generated/
│   ├── owl/
│   ├── shacl/
│   └── docs/
├── tests/
├── catalog-v001.xml
├── Makefile
└── pyproject.toml
```

│ └── workflows/

├──.ontoenv/ \# (Hidden) ontoenv configuration and cache

├── config/ \# Repository-wide configuration

│ └── ontoenv.toml \# ontoenv definition file

├── imports/ \# External dependencies (ReadOnly)

│ ├── catalog-v001.xml \# Catalog for the imports folder

│ ├── qudt/

│ │ └── qudt.ttl

│ ├── sosa/

│ │ └── sosa.ttl

│ └── external_ontology_n.ttl

├── src/ \# SOURCE OF TRUTH (Editable)

│ ├── linkml/ \# LinkML Schema Definitions

│ │ ├── gaia-x-core.yaml \# Core schema module

│ │ ├── automotive/ \# Automotive domain modules

│ │ │ ├── vehicle.yaml

│ │ │ └── sensors.yaml

│ │ └── types.yaml

│ └── ontology/ \# Legacy/Manual Turtle Sources (if kept)

│ ├── manifest/

│ │ └── manifest-source.ttl

│ └──...

├── generated/ \# BUILD ARTIFACTS (Do not edit manually)

│ ├── owl/ \# Generated OWL ontologies

│ │ ├── catalog-v001.xml \# Master catalog for Protégé

│ │ ├── gaia-x-core.owl.ttl

│ │ └──...

│ ├── shacl/ \# Generated SHACL shapes

│ │ └── gaia-x-core.shacl.ttl

│ └── docs/ \# Generated HTML/MD documentation

├── tests/ \# Integrated Test Suite

│ ├── data/ \# Test instances (Pass/Fail)

│ └── unit/ \# Python test scripts

├── catalog-v001.xml \# Root catalog (redirects to sub-catalogs)

├── Makefile \# Automation entry points

└── pyproject.toml \# Python dependency management

### **3.2 Component Breakdown and Rationale**

#### **3.2.1 src/linkml/ (The New Core)**

This directory houses the LinkML YAML files. Organized modularly, it mirrors the domain logic. Instead of a flat list, domains are grouped. For example, automotive/ might contain vehicle.yaml and sensors.yaml. These files are the _only_ place where schema editing occurs.

| Feature             | Old Structure (Flat Turtle) | New Structure (LinkML YAML) |
| :------------------ | :-------------------------- | :-------------------------- |
| **Edit Location**   | root/domain/\*.ttl          | src/linkml/domain/\*.yaml   |
| **Maintainability** | Low (Duplication)           | High (Inheritance, Mixins)  |
| **Outputs**         | Manual SHACL/OWL            | Auto-generated SHACL/OWL    |

#### **3.2.2 imports/ (The Local Mirror)**

This directory contains physical copies of all external ontologies.

- **Purpose:** Guarantees that if the internet goes down, the project still builds. It serves as an immutable cache of the external world.
- **Management:** This folder is populated and managed by ontoenv. Users generally do not add files here manually; they declare dependencies in the configuration, and ontoenv fetches and places them here.8 This acts similarly to a node_modules folder in JavaScript, but for ontologies.

#### **3.2.3 generated/ (The Output Target)**

A critical change from the current state is that usable artifacts (OWL, SHACL) are moved to generated/.

- **Why?** It prevents confusion about what is source and what is derived.
- **Sub-folders:** Dedicated folders for owl, shacl, jsonld_context, and docs ensure that consumers of the repo (e.g., a software developer needing a SHACL file) know exactly where to look. This standardization simplifies downstream consumption.

#### **3.2.4 config/ and Root Configuration**

The config/ directory holds the ontoenv.toml (or .ontoenv.yaml) file, defining the mapping policies. The root catalog-v001.xml is a "master catalog" that uses \<nextCatalog\> instructions to include the catalogs inside generated/owl/ and imports/, providing a seamless Protégé experience when opening files from the root.

**4\. Implementation Strategy: Local Catalog-Mediated Resolution**

The integration of ontoenv is the linchpin of this reorganization. It transforms the repository from a collection of text files into a managed environment, systematically solving the "Missing Imports" problem.

### **4.1 The Role of ontoenv and the Catalog Mechanism**

ontoenv is a tool designed to manage the "imports closure" of an ontology project.8 It scans the repository for ontology files, extracts their IRIs, and builds a central mapping. It fundamentally replaces the error-prone process of manually editing catalog-v001.xml files.

The XML Catalog standard (catalog-v001.xml) acts as a redirection map. When an ontology tool encounters an import statement, it checks the catalog first.

- **Without Catalog:** Import("<http://example.org/ontology>") \-\> HTTP GET request to <http://example.org/ontology>.
- **With Catalog:** Import("<http://example.org/ontology>") \-\> Lookup in Catalog \-\> Redirect to file://imports/ontology.ttl.

### **4.2 Configuration and Initialization Workflow**

**Step 1: Initialization**

The repository will be initialized using the ontoenv init command. This creates the .ontoenv directory structure which holds internal caches and state.

Bash

ontoenv init \--link-imports

The \--link-imports or equivalent flag (depending on exact version syntax 8) allows ontoenv to create symbolic links or local copies of discovered imports, populating the imports/ directory automatically.

**Step 2: Dependency Declaration**

Instead of hoping Protégé finds an import, we explicitly declare mappings in the ontoenv configuration (typically manifest.yaml or ontoenv.toml depending on implementation specifics). This file acts as the "requirements.txt" for the semantic layer.

_Example Configuration logic (config/ontoenv.toml):_

Ini, TOML

\[dependencies\]  
"<http://www.w3.org/ns/sosa/>" \= "imports/sosa.ttl"  
"<http://qudt.org/2.1/schema/qudt>" \= "imports/qudt.ttl"  
"<https://w3id.org/linkml/types>" \= "imports/linkml_types.ttl"

**Step 3: Refreshing Imports**

When a new dependency is added, the developer runs ontoenv refresh. This command:

1. Fetches the ontology from the specified IRI.
2. Validates the download.
3. Places it in imports/.
4. Updates the imports/catalog-v001.xml file.

### **4.3 The "Cascading Catalog" Architecture**

To support Protégé 2 effectively in a complex folder structure, we will implement a "Cascading Catalog" strategy. This involves chaining multiple catalog files together using the \<nextCatalog\> directive.

| Catalog Level          | Location                       | Responsibility                                                                                                          |
| :--------------------- | :----------------------------- | :---------------------------------------------------------------------------------------------------------------------- |
| **Level 1: Imports**   | imports/catalog-v001.xml       | Maps external IRIs (SOSA, QUDT) to files within the imports/ folder. Generated by ontoenv.                              |
| **Level 2: Generated** | generated/owl/catalog-v001.xml | Maps internal project IRIs (e.g., automotive) to the generated files in generated/owl/. Includes a pointer to Level 1\. |
| **Level 3: Root**      | root/catalog-v001.xml          | The entry point for developers. Simply points to Level 2\.                                                              |

**Catalog File Content Examples:**

**imports/catalog-v001.xml**

XML

\<catalog prefer\="public" xmlns\="urn:oasis:names:tc:entity:xmlns:xml:catalog"\>  
 \<uri name\="<http://www.w3.org/ns/sosa/>" uri\="sosa.ttl"/\>  
 \<uri name\="<http://qudt.org/2.1/schema/qudt>" uri\="qudt.ttl"/\>  
\</catalog\>

**generated/owl/catalog-v001.xml**

XML

\<catalog prefer\="public" xmlns\="urn:oasis:names:tc:entity:xmlns:xml:catalog"\>  
 \<uri name\="<https://w3id.org/gaia-x/automotive>" uri\="automotive.owl.ttl"/\>  
 \<nextCatalog catalog\="../../imports/catalog-v001.xml"/\>  
\</catalog\>

**catalog-v001.xml (Root)**

XML

\<catalog prefer\="public" xmlns\="urn:oasis:names:tc:entity:xmlns:xml:catalog"\>  
 \<nextCatalog catalog\="generated/owl/catalog-v001.xml"/\>  
\</catalog\>

**Operational Benefit:** When a developer opens generated/owl/automotive.owl.ttl in Protégé, Protégé reads the local catalog, sees the nextCatalog reference, loads the imports catalog, and successfully resolves sosa: and qudt: to the local files in imports/. **Zero network requests. Zero "missing import" errors.**

## ---

**5\. Implementation Strategy: LinkML Integration and Modernization**

Preparing for LinkML modeling requires shifting the repository's "center of gravity" from RDF to YAML. This section details how to structure the LinkML schema to support the GAIA-X4PLC-AAD requirements, facilitating the auto-generation of artifacts.

### **5.1 Why LinkML?**

The move to LinkML is not merely a syntactic change; it is a strategic upgrade.

- **Polyglot Modeling:** Write once (YAML), generate everywhere (OWL, SHACL, JSON-Schema, Python).
- **Semantic Validation:** LinkML allows defining constraints (like regex patterns, min/max values) that can be compiled into highly specific SHACL shapes, which are often tedious to write manually.
- **Documentation:** LinkML automatically generates static HTML documentation that is always in sync with the schema, resolving the issue of outdated READMEs.

### **5.2 LinkML Schema Architecture**

The LinkML schema will be split into modules to mirror the domain logic, preventing a monolithic file that is hard to maintain.

**File: src/linkml/gaia_x_core.yaml** (The Entry Point)

YAML

id: <https://w3id.org/gaia-x/core>  
name: gaia-x-core  
imports:  
 \- linkml:types  
 \-./automotive/vehicle \# Local import of sub-module  
 \-./automotive/sensors  
prefixes:  
 gaia: <https://w3id.org/gaia-x/core/>  
 linkml: <https://w3id.org/linkml/>  
 sosa: <http://www.w3.org/ns/sosa/>  
 qudt: <http://qudt.org/2.1/schema/qudt/>  
default_prefix: gaia

classes:  
 \# Base classes for the ecosystem  
 Asset:  
 description: "A generic asset in the GAIA-X ecosystem"  
 slots:  
 \- id  
 \- name  
 \- description

**File: src/linkml/automotive/sensors.yaml** (Domain Module)

YAML

id: <https://w3id.org/gaia-x/automotive/sensors>  
name: automotive-sensors  
prefixes:  
 autosens: <https://w3id.org/gaia-x/automotive/sensors/>  
imports:  
 \-../gaia_x_core \# Import base to inherit Asset

classes:  
 LidarSensor:  
 is_a: Asset  
 mixins:  
 \- sosa:Sensor \# Mapping to external ontology term  
 slots:  
 \- scan_frequency  
 \- range  
 slot_usage:  
 scan_frequency:  
 range: float  
 unit: qudt:Hertz

### **5.3 Artifact Generation Workflow**

The Makefile will control the generation of artifacts. This ensures that the contents of generated/ are always synchronized with src/linkml/.

**Makefile Strategy:**

1. **gen-owl**: Runs linkml-gen-owl.17 This transforms the YAML schema into Turtle format, adding all necessary rdfs:subClassOf and owl:Restriction axioms.
   - _Command:_ gen-owl \--format ttl src/linkml/gaia_x_core.yaml \> generated/owl/gaia_x_core.owl.ttl
   - _Significance:_ This produces the "Reasoning View" of the ontology.
2. **gen-shacl**: Runs linkml-gen-shacl. This produces the validation shapes.
   - _Command:_ gen-shacl src/linkml/gaia_x_core.yaml \> generated/shacl/gaia_x_core.shacl.ttl
   - _Significance:_ This produces the "Validation View," strictly enforcing the constraints defined in YAML.
3. **gen-doc**: Runs linkml-gen-doc to produce static HTML sites describing the classes and slots.

### **5.4 Migration of Legacy Ontologies**

The repository currently contains legacy Turtle files. We cannot simply delete them. The migration strategy involves **bootstrapping** using schema-automator.7

**Migration Steps:**

1. **Ingest:** Run schema-automator import-owl on the existing automotive_simulator_ontology.ttl.
2. **Convert:** This tool parses the OWL axioms and attempts to reconstruct a LinkML YAML class hierarchy.
3. **Refine:** The generated YAML will act as a draft. Engineers must manually review it to ensure that rdfs:domain and rdfs:range constraints were correctly interpreted as LinkML slots.
4. **Replace:** Once the YAML is validated, the original .ttl file is moved to an archive, and the generated/ folder becomes the new home for the Turtle serialization.

## ---

**6\. CI/CD and Automation Pipelines**

The reorganization enables a sophisticated CI/CD pipeline using GitHub Actions. The goal is to enforce quality gates that prevent broken ontologies or invalid shapes from entering the main branch.

### **6.1 Workflow: build-and-test.yml**

This workflow triggers on every Pull Request.

**Job 1: LinkML Validation**

- **Step:** Install LinkML.
- **Step:** Run linkml-lint on src/linkml/. This checks for style violations, missing descriptions, or invalid references.
- **Step:** Run linkml-validate if there are test data files available.

**Job 2: Artifact Generation (Dry Run)**

- **Step:** Execute make all.
- **Step:** Verify that the build succeeds without errors.
- **Step:** (Optional) Check if the generated artifacts differ from what is committed. Ideally, generated artifacts are _not_ committed to the source branch but are built during release, but if they are committed, this step ensures they are up to date.

**Job 3: Ontology Integrity (The ontoenv check)**

- **Step:** Initialize ontoenv.
- **Step:** Run robot verify. using the catalog-v001.xml.
- **Command:**  
  Bash  
  robot verify \--catalog generated/owl/catalog-v001.xml \\  
   \--input generated/owl/gaia_x_core.owl.ttl \\  
   \--queries tests/sparql/consistency.sparql

- **Insight:** This uses the _generated_ catalog to ensure that the ontology being released can successfully resolve all its imports locally in the CI environment. This is the ultimate test of the "Local Catalog-Mediated Resolution" strategy.

### **6.2 Workflow: release.yml**

This workflow triggers when a Release is created.20

- **Step:** Build all artifacts (OWL, SHACL, Docs).
- **Step:** Publish the artifacts. This could mean attaching the .ttl files to the GitHub Release, pushing the Python classes to PyPI (if a python package is configured), or deploying the HTML documentation to GitHub Pages.
- **Step:** The linkml-project-cookiecutter logic suggests auto-generating release notes from PR titles, ensuring full traceability of changes.20

## ---

**7\. Migration Roadmap**

Transitioning from the current state to the proposed architecture requires a phased approach to minimize disruption to ongoing development.

### **Phase 1: Infrastructure Setup (Weeks 1-2)**

1. **Initialize Repository Structure:** Create the src/linkml, imports, generated, and config directories.
2. **Install ontoenv:** Set up the .ontoenv environment and configure ontoenv.toml.
3. **Centralize Imports:** Identify every owl:imports URL in the current .ttl files. Download these files to imports/ and map them in the imports/catalog-v001.xml.
4. **Create Root Catalog:** Create the root catalog-v001.xml to point to the imports.
5. **Verify Protégé Access:** Ensure developers can open existing ontologies without internet access using the new catalog.

### **Phase 2: LinkML Bootstrapping (Weeks 3-5)**

1. **Select Pilot Domain:** Choose a small, stable domain (e.g., manifest or general) for the first conversion.
2. **Convert to YAML:** Use schema-automator to bootstrap the LinkML YAML.
3. **Refactor:** Clean up the YAML. Optimize class names and slot definitions.
4. **Generate Artifacts:** Set up the Makefile to generate the .ttl and .shacl.ttl for this pilot domain into generated/.
5. **Compare:** Compare the generated artifacts with the legacy manual files. Iterate until functional equivalence is achieved.

### **Phase 3: Full Migration and Switchover (Weeks 6-10)**

1. **Migrate Remaining Domains:** Repeat the conversion process for all domains.
2. **Update CI/CD:** Replace the custom Python validation scripts with the LinkML/Robot CI workflow.
3. **Deprecate Root Folders:** Move the legacy root folders (automotive-simulator, etc.) to an archive/ folder or delete them.
4. **Documentation Update:** Update README.md and CONTRIBUTING.md to reflect the new workflow (edit YAML \-\> run make \-\> commit).

## **Conclusion**

The current ontology-management-base repository, while a functional starting point, suffers from a flat, manual, and network-dependent structure that limits its potential as a scalable semantic backbone for GAIA-X4PLC-AAD. By adopting the proposed reorganization—centered on **LinkML** as the source of truth and **ontoenv** for local catalog-mediated resolution—the project will achieve robust reproducibility, automated quality assurance, and a developer experience aligned with modern software engineering standards. The shift to strict separation between maintained source and generated artifacts will eliminate ambiguity, while the local catalog strategy ensures that the ecosystem remains resilient against the volatility of the external web. This architecture paves the way for a highly automated, self-documenting, and interoperable future for the GAIA-X automotive ecosystem.

#### **Works cited**

1. GAIA-X4PLC-AAD/ontology-management-base: Our ... \- GitHub, accessed on January 25, 2026, [https://github.com/GAIA-X4PLC-AAD/ontology-management-base](https://github.com/GAIA-X4PLC-AAD/ontology-management-base)
2. How to use ontology catalog into protege \- owl \- Stack Overflow, accessed on January 25, 2026, [https://stackoverflow.com/questions/79246146/how-to-use-ontology-catalog-into-protege](https://stackoverflow.com/questions/79246146/how-to-use-ontology-catalog-into-protege)
3. How Owl Imports Work \- Protege Wiki, accessed on January 25, 2026, [https://protegewiki.stanford.edu/wiki/How_Owl_Imports_Work](https://protegewiki.stanford.edu/wiki/How_Owl_Imports_Work)
4. standard operating procedures (SOPs) \- OBO Foundry, accessed on January 25, 2026, [http://obofoundry.org/docs/SOP.html](http://obofoundry.org/docs/SOP.html)
5. Principles: Overview \- OBO Foundry, accessed on January 25, 2026, [http://obofoundry.org/principles/fp-000-summary.html](http://obofoundry.org/principles/fp-000-summary.html)
6. How to run a collaborative data modeling project \- linkml documentation, accessed on January 25, 2026, [https://linkml.io/linkml/howtos/collaborative-development.html](https://linkml.io/linkml/howtos/collaborative-development.html)
7. GitHub Organization \- linkml documentation, accessed on January 25, 2026, [https://linkml.io/linkml/developers/organization.html](https://linkml.io/linkml/developers/organization.html)
8. gtfierro/ontoenv-rs: ontoenv is an environment manager for ontology management. It eventually wants to be a package manager for RDF ontologies and graphs. \- GitHub, accessed on January 25, 2026, [https://github.com/gtfierro/ontoenv-rs](https://github.com/gtfierro/ontoenv-rs)
9. Importing Ontologies in P41 \- Protege Wiki, accessed on January 25, 2026, [https://protegewiki.stanford.edu/wiki/Importing_Ontologies_in_P41](https://protegewiki.stanford.edu/wiki/Importing_Ontologies_in_P41)
10. LinkML: An Open Data Modeling Framework \- Oxford Academic, accessed on January 25, 2026, [https://academic.oup.com/gigascience/advance-article-pdf/doi/10.1093/gigascience/giaf152/65854805/giaf152.pdf](https://academic.oup.com/gigascience/advance-article-pdf/doi/10.1093/gigascience/giaf152/65854805/giaf152.pdf)
11. FAQ: Why LinkML, accessed on January 25, 2026, [https://linkml.io/linkml/faq/why-linkml.html](https://linkml.io/linkml/faq/why-linkml.html)
12. LinkML Project Cookiecutter \- GitHub, accessed on January 25, 2026, [https://github.com/linkml/linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter)
13. LinkML Project Cookiecutter, accessed on January 25, 2026, [https://linkml.io/linkml/howtos/linkml-project-cookiecutter.html](https://linkml.io/linkml/howtos/linkml-project-cookiecutter.html)
14. a toolkit for building, maintaining and standardizing biomedical ontologies \- University of Cambridge, accessed on January 25, 2026, [https://www.repository.cam.ac.uk/bitstreams/d47f3037-330f-44f2-9ef8-c391bd278b5a/download](https://www.repository.cam.ac.uk/bitstreams/d47f3037-330f-44f2-9ef8-c391bd278b5a/download)
15. Imports management \- Core Ontology for Biology and Biomedicine \- OBO Foundry, accessed on January 25, 2026, [https://obofoundry.org/COB/odk-workflows/UpdateImports/](https://obofoundry.org/COB/odk-workflows/UpdateImports/)
16. Protege 4.1 XML Catalog Question, accessed on January 25, 2026, [https://protege-user.stanford.narkive.com/Hg9MvfBu/protege-4-1-xml-catalog-question](https://protege-user.stanford.narkive.com/Hg9MvfBu/protege-4-1-xml-catalog-question)
17. OWL \- linkml documentation, accessed on January 25, 2026, [https://linkml.io/linkml/generators/owl.html](https://linkml.io/linkml/generators/owl.html)
18. LinkML-OWL Pizza Tutorial, accessed on January 25, 2026, [https://linkml.io/linkml-owl/tutorial/](https://linkml.io/linkml-owl/tutorial/)
19. Importers — Schema Automator documentation \- LinkML, accessed on January 25, 2026, [https://linkml.io/schema-automator/packages/importers.html](https://linkml.io/schema-automator/packages/importers.html)
20. How to Manage Releases of your LinkML Schema, accessed on January 25, 2026, [https://linkml.io/linkml/developers/manage-releases.html](https://linkml.io/linkml/developers/manage-releases.html)
21. LinkML tutorial for ISMB 2024: slides, accessed on January 25, 2026, [https://linkml.io/linkml-tutorial-2024/LinkML_tutorial_for_ISMB%202024\_%20slides.pdf](https://linkml.io/linkml-tutorial-2024/LinkML_tutorial_for_ISMB%202024_%20slides.pdf)
