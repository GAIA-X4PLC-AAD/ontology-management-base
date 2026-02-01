You are absolutely right. I missed detailing the **Resolution Registry** strategy in the previous file. That is the critical link that makes the "Smart Resolver" work.

Here is the complete, merged architecture document. It now includes:

1. **The Folder Structure** (with strict separation).  
2. **The Git Submodule Strategy** (inside imports/).  
3. **The Registry Strategy** (the registry.json \+ w3id integration).  
4. **The Migration Checklist**.

You can save this as ARCHITECTURE\_MASTERPLAN.md.

# ---

**GAIA-X4PLC-AAD Ontology Architecture & Migration Masterplan**

**Status:** Implementation Ready

**Goal:** Transition to a LinkML-driven, catalog-mediated architecture with automated w3id resolution.

## ---

**1\. The Target Directory Structure**

This layout enforces a clean separation between "What we write" (src), "What we depend on" (imports), and "What we build" (generated).

Plaintext

ontology-management-base/  
├── .github/  
│   └── workflows/           \# CI Pipelines (release.yml, ci.yml)  
├── config/  
│   └── ontoenv.toml         \# Dependency declarations for ontoenv  
├── imports/                 \# \[DEPENDENCIES\] External Ontologies & Submodules  
│   ├── catalog-v001.xml     \# Auto-generated index of all imports  
│   ├── sosa.ttl             \# Downloaded by ontoenv  
│   └── common-defs/         \# \<--- GIT SUBMODULES go here  
├── src/  
│   ├── linkml/              \# \[SEMANTIC SOURCE\] The Source of Truth  
│   │   ├── envited-x.yaml  
│   │   ├── manifest.yaml  
│   │   └── modules/         \# Reusable LinkML fragments  
│   └── tools/               \# \[PYTHON SOURCE\] Validation & Utility scripts  
│       ├── \_\_init\_\_.py      \# Makes this a package  
│       ├── validators/      \# e.g., check\_jsonld...py  
│       └── uploaders/       \# e.g., fc\_upload.py  
├── scripts/                 \# \[AUTOMATION\] CI/CD Glue scripts  
│   ├── update\_registry.py   \# \<--- Updates registry.json  
│   └── clean\_build.sh  
├── tests/  
│   ├── fixtures/            \# \[SHARED DATA\] Old 'base-references'  
│   │   ├── envited-x\_manifest\_reference.json  
│   │   └── context.jsonld  
│   ├── data/                \# \[TEST CASES\] Organized by Domain  
│   │   ├── envited-x/  
│   │   │   ├── valid/       \# Working examples  
│   │   │   └── invalid/     \# Fail-tests  
│   │   └── manifest/  
│   └── unit/                \# Python unit tests for src/tools  
├── generated/               \# \[ARTIFACTS\] Read-Only Build Outputs  
│   ├── owl/                 \# .ttl files for Protege/Release  
│   ├── shacl/               \# .shacl.ttl files for validation  
│   └── docs/                \# HTML documentation  
├── docs/                    \# \[GITHUB PAGES\]  
│   └── index.html           \# \<--- The Smart Resolver Script  
├── registry.json            \# \[DATABASE\] The Version Map for w3id  
├── Makefile                 \# Build command center  
└── pyproject.toml           \# Python dependencies (linkml, ontoenv)

## ---

**2\. Component Placement Strategy**

### **2.1 External Dependencies (imports/)**

* **Purpose:** Stores specific versions of external ontologies to ensure offline reproducibility.  
* **Git Submodules:** If you rely on shared repositories, add them here.  
  * *Command:* git submodule add https://github.com/org/repo.git imports/repo  
* **OntoEnv:** The ontoenv tool will manage catalog-v001.xml in this folder, mapping logical URIs (like http://www.w3.org/ns/sosa/) to these physical files.

### **2.2 Source Code (src/)**

* **src/linkml/:** The new home for ontology definitions (.yaml).  
* **src/tools/:** Python logic (validation, API uploads). It is a structured Python package.

### **2.3 The Smart Registry (registry.json)**

* **Purpose:** This file acts as the "Traffic Controller" for w3id.org. It maps abstract URIs and Versions to concrete GitHub paths.  
* **Managed By:** It is **auto-updated** by the CI pipeline (scripts/update\_registry.py) whenever a release is made.  
* **Structure:**  
  JSON  
  {  
    "https://w3id.org/ascs-ev/envited-x/envited-x": {  
      "latest": "v0.0.5",  
      "versions": {  
        "v3": "generated/owl/envited-x.ttl",  
        "v2": "generated/owl/envited-x.ttl"   
      }  
    }  
  }

## ---

**3\. The Resolution Strategy (w3id Integration)**

This strategy decouples the w3id server from your file structure. You never need to edit the w3id repository after the initial setup.

### **Step A: The w3id Configuration (Submit Once)**

The .htaccess on w3id.org redirects **everything** to your GitHub Pages resolver.

Apache

RewriteEngine On  
\# Redirect .../envited-x/v3 \-\> index.html?ontology=envited-x\&version=v3  
RewriteRule ^(\[^/\]+)/(v\[0\-9.\]+)$ https://ascs-ev.github.io/ontology-management-base/?ontology=$1\&version=$2 \[R=303,L\]

\# Redirect .../envited-x \-\> index.html?ontology=envited-x\&version=latest  
RewriteRule ^(\[^/\]+)$ https://ascs-ev.github.io/ontology-management-base/?ontology=$1\&version=latest \[R=303,L\]

### **Step B: The Smart Resolver (docs/index.html)**

This script runs in the user's browser. It:

1. Fetches registry.json from the main branch.  
2. Lookups the requested ontology and version.  
3. Constructs the URL to the **Raw GitHub File** for that specific tag.  
4. Redirects the user.

## ---

**4\. Migration Checklist (Execution Guide)**

#### **Phase 1: Structural Reorganization**

1. **Create Folders:**  
   Bash  
   mkdir \-p imports src/linkml src/tools scripts generated/owl generated/shacl tests/fixtures tests/data docs

2. **Migrate Dependencies:**  
   Bash  
   mv base-ontologies/\* imports/  
   rm \-r base-ontologies

3. **Migrate Submodules (If any):**  
   Bash  
   \# Example: git submodule add \<url\> imports/my-submodule

4. **Migrate Python:**  
   Bash  
   mv src/\*.py src/tools/  
   touch src/tools/\_\_init\_\_.py

5. **Migrate Test Data (Example):**  
   Bash  
   mkdir \-p tests/data/envited-x/valid  
   mv envited-x/example/\* tests/data/envited-x/valid/

#### **Phase 2: Registry Implementation**

1. **Create scripts/update\_registry.py:** Use the script provided in the previous discussion.  
2. **Create docs/index.html:** Create the HTML/JS resolver file.  
3. **Enable GitHub Pages:** Go to Repo Settings \-\> Pages \-\> Source: main branch, /docs folder.

#### **Phase 3: CI/CD Setup**

1. **Update release.yml:** Ensure it runs ontoenv init, builds LinkML, runs update\_registry.py, and commits the result.

## ---

**5\. The Unified Workflow**

### **Development**

1. **Edit:** Modify src/linkml/envited-x.yaml.  
2. **Build:** Run make to generate generated/owl/\*.ttl.  
3. **Test:** Run pytest tests/unit or make test to validate against tests/data.

### **Release (CI)**

1. **Tag:** Push v1.0.0.  
2. **CI Action:**  
   * Generates Artifacts.  
   * Scans artifacts for owl:versionIRI.  
   * Updates registry.json (e.g., maps v3 \-\> v1.0.0).  
   * Commits registry.json.  
3. **Resolution:** User visits w3id.org/.../v3 \-\> Redirects to docs/index.html \-\> Reads registry.json \-\> Redirects to raw.githubusercontent.../v1.0.0/generated/owl/envited-x.ttl.