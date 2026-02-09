# Gaia-X Ontology & SHACL Shapes

> ⚠️ **Important Note:** All SHACL shapes in this folder are defined as **open** (not closed).

> 📝 **Catalog Registration:** The SHACL shapes are now registered in the ontology catalog with IRI `https://w3id.org/gaia-x/development#shapes`. This enables automatic discovery and resolution of shapes during validation workflows.

## Overview

This folder contains the **Gaia-X Trust Framework ontology and SHACL shapes** (version 25.11+fix.1).

- The **Gaia-X model** (ontology) defines concepts for the Gaia-X Trust Framework including Participants, Services, Credentials, and Compliance.
- The **SHACL shapes** automatically verify that Gaia-X instances conform to the Trust Framework specifications.
- The core Gaia-X ontologies are integrated as a **Git submodule** to ensure version consistency with upstream.
- The **VERSION file** in this directory tracks the Gaia-X release version for tooling and documentation.

### Current Version: 25.11+fix.1

This version is based on the official **25.11 release** with the following additional fixes:

- **Commit c41d423**: Fix double hash fragments in IRIs (fixes enum IRI generation)

The `+fix.1` suffix indicates this is a post-release patch on top of 25.11. When the upstream releases 25.12 or a later version that includes this fix, we will update to the official release tag.

## IRI Notes (Enum Values)

The OWL generator now uses a non-hash enum separator (`/`) to avoid double-hash
fragments in enum IRIs. As a result, enum IRIs are emitted like:

```
https://w3id.org/gaia-x/development#GaiaXTermsAndConditions/<hash>
```

This change causes a large diff in the generated OWL because all enum IRIs are
rewritten. It also introduces percent-encoding for reserved characters in enum
values (for example `%20` for spaces and `%2F` for `/`). This is expected and
keeps IRIs valid.

---

## Capabilities

- Describe Gaia-X Participants, Services, and Credentials in **JSON-LD**.
- Validate instances against Gaia-X Trust Framework requirements.
- Ensure compliance with official Gaia-X specifications.

---

## Contents of this folder

- **`gx.owl.ttl`** – The Gaia-X ontology defining core trust framework concepts.
- **`gx.shacl.ttl`** – SHACL validation shapes for Gaia-X instances.
- **`gx.context.jsonld`** – JSON-LD context for GX terms.
- **`PROPERTIES.md`** – An auto-generated summary of SHACL properties.
- **`VERSION`** – Current Gaia-X version (e.g., `25.11+fix.1`).
- **`VERSIONING.md`** – Detailed versioning scheme and post-release patch documentation.
- **`README.md`** – This readme file.
- **`update-from-submodule.sh`** – Helper script to sync artifacts from submodule.
- **`verify-version.sh`** – Verify VERSION file matches submodule tag.

---

## Submodule Integration

The core Gaia-X ontologies are maintained in an upstream GitLab repository:

- **Upstream Source:** [Gaia-X Service Characteristics](https://gitlab.com/gaia-x/technical-committee/service-characteristics-working-group/service-characteristics)
- **Current Version:** `25.11`
- **Submodule Location:** `submodules/service-characteristics`

> **Note:** The `gx/` directory contains copies of the ontology and shapes for local examples and validation. The actual submodule is located at `submodules/service-characteristics`.

---

## How to Initialize the Submodule

If you haven't already initialized the Gaia-X submodule, run:

```bash
git submodule update --init --recursive
```

To verify the current version:

```bash
cd submodules/service-characteristics
git status
# Should show tag 25.11 is checked out
```

---

## How to Run SHACL Validation Tests

See the root guide for the canonical commands and explanations:  
[Running Tests Locally](../../README.md#validation)

Example command for this folder:

```bash
python3 -m src.tools.validators.validation_suite \
  --run check-data-conformance \
  --domain gx
```

---

## Updating to a New Gaia-X Version

### Automated update (recommended)

Use the provided helper script:

```bash
cd artifacts/gx
./update-from-submodule.sh 25.12  # Update to specific version
# OR
./update-from-submodule.sh        # Use current submodule version
```

The script will:
1. Check out the specified tag in the submodule (if provided)
2. Copy artifacts (OWL, SHACL, context) from submodule to artifacts/gx/
3. Update the VERSION file automatically
4. Show next steps for documentation regeneration

### Manual update

When a new version of Gaia-X is released:

1. Navigate to the submodule:

   ```bash
   cd submodules/service-characteristics
   ```

2. Check out the new version tag:

   ```bash
   git checkout <new-tag>  # e.g., git checkout 25.12
   ```

3. Copy the updated artifacts to `artifacts/gx/`:

   ```bash
   cd ../..
   cp submodules/service-characteristics/ontology.owl.ttl artifacts/gx/gx.owl.ttl
   cp submodules/service-characteristics/shapes.shacl.ttl artifacts/gx/gx.shacl.ttl
   cp submodules/service-characteristics/context.jsonld artifacts/gx/gx.context.jsonld
   ```

4. **Update the VERSION file** to match the new tag:

   ```bash
   echo "25.12" > artifacts/gx/VERSION
   ```

5. Regenerate documentation and commit:

   ```bash
   python3 -m src.tools.utils.registry_updater
   python3 -m src.tools.utils.properties_updater
   git add artifacts/gx/ submodules/service-characteristics
   git commit -m "chore(gx): upgrade Gaia-X to 25.12"
   ```

### Verify version sync

To check if the VERSION file matches the submodule tag:

```bash
cd artifacts/gx
./verify-version.sh
```

!!! warning "VERSION file is critical"
    The `VERSION` file is used by the documentation build system to determine where to copy GX artifacts. Always keep it synchronized with the submodule tag.

---

## See Also

- [Ontology Domains](../../docs/ontologies/catalog.md) – Browse all available ontologies
- [Validation Tools](../../docs/validation/tools.md) – Complete validation tool reference
- [Architecture](../../docs/discovery/catalogs.md) – Technical details about the ontology structure
- [Gaia-X Trust Framework](https://gaia-x.eu/) – Official Gaia-X website
