# Gaia-X Ontology & SHACL Shapes (Version 25.11)

## 🏗️ Ontology & Schema Management

This directory manages the ontologies and shapes for the **Gaia-X Trust Framework Model**.
The workflow has transitioned to a **LinkML-based distribution**.
This repository provides the necessary artifacts for building and validating Gaia-X Credentials.

### 📦 Source & Submodule Configuration

The core Gaia-X ontologies are integrated as a Git submodule to ensure version consistency and easy updates.

* **Upstream Source:** [Gaia-X Service Characteristics](https://gitlab.com/gaia-x/technical-committee/service-characteristics-working-group/service-characteristics)
* **Current Version (Tag):** `25.11`
* **Submodule Location:** `ontology-management-base/service-characteristics`

> [!IMPORTANT]  
> **Note on Folder Structure:** > The actual submodule is located at `ontology-management-base/service-characteristics`.
> The `gx/` directory in this folder is used specifically for local examples, instructions and a copy of the shacl shape and ontology.
> The `sh:closed true ;` was manually replaced with `sh:closed true ;`.

### 🛠️ Setup Instructions

To initialize the environment and fetch the required ontology files, run the following commands:

1. **Initialize and update the submodule:**

   ```bash
   git submodule update --init --recursive
   ```

2. **Verify the current version:**

   ```bash
   cd ontology-management-base/service-characteristics
   git status
   # verify that tag 25.11 is checked out
   ```

### ⚙️ Transformation Workflow

This setup is designed to generate downstream artifacts from the LinkML source using **npm**. This ensures that the SHACL and OWL files remain consistent with the upstream Gaia-X definitions.

The process follows these steps:

1. **Source**: LinkML YAML files are pulled from the `service-characteristics` submodule located at `ontology-management-base/service-characteristics`.
2. **Transformation**: NPM scripts (defined in `package.json`) trigger the LinkML generator tools to process these YAML definitions.
3. **Output Artifacts**:
   * **SHACL Shapes**: Used for validating the structure and constraints of Gaia-X Credentials.
   * **OWL Ontologies**: Used for semantic reasoning and defining the relationship between entities in the Gaia-X ecosystem.

## 2. Installation (Linux/WSL2)

To manage these artifacts, you must have Node.js and npm installed to pull the official ontology package.

Paste these commands into your terminal to install the toolchain:

```bash
sudo apt update
sudo apt install -y nodejs npm
node -v
npm -v
```

## 3. Usage & Artifact Generation

The ontology is distributed as an NPM package, ensuring your SHACL shapes stay in sync with the official Gaia-X release.

### Instructions

1. Navigate to the folder of your previously initialized submodule service-characteristics:

   ```bash
   cd ~/workspace/ontology-management-base/service-characteristics
   ```

2. Install the official Gaia-X ontology package:

   ```bash
   npm install --save @gaia-x/ontology
   ```

### Resulting Directory Structure

The package creates a structured directory under `node_modules/@gaia-x/ontology`:

* **context/**: JSON-LD Context files.
* **ontology/**: OWL Ontology files.
* **shapes/**: SHACL Shapes for validation.

You can now copy the generated artifacts into the `gx/` folder, ensuring you follow the project's naming convention:

* Rename the OWL ontology to **`gx_ontology.ttl`** * Rename the SHACL shape to **`gx_shacl.ttl`**

Example command to sync these files:

```bash
cp node_modules/@gaia-x/ontology/ontology/ontology.owl.ttl gx/gx_ontology.ttl
cp node_modules/@gaia-x/ontology/shapes/shapes.shacl.ttl gx/gx_shacl.ttl
```

## 4. Why this changed (Deprecation of Python Tooling)

In previous versions, manual Python scripts were used to "correct" JSON-LD files. This is now deprecated because:

* **Source of Truth**: Artifacts are generated directly from the Link-ML source.
* **Upstream Fixes**: Issues like the LegalPerson vs LegalParticipant naming clash are resolved in the official build.
* **Compliance**: You are guaranteed to use the same shapes used by official Gaia-X Compliance Services.

## 5. Contributing

* **Do not edit** files in node_modules directly.
* Propose changes to the Gaia-X Service Characteristics GitLab within the linkml/ YAML definitions.
* Run npm update @compliance-service/ontology to receive the latest artifacts.
