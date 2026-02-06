# Gaia-X Ontology & SHACL Shapes

> ⚠️ **Important Note:** All SHACL shapes in this folder are defined as **open** (not closed).

> 📝 **Catalog Registration:** The SHACL shapes are now registered in the ontology catalog with IRI `https://w3id.org/gaia-x/development#shapes`. This enables automatic discovery and resolution of shapes during validation workflows.

## Overview

This folder contains the **Gaia-X Trust Framework ontology and SHACL shapes** (version 25.11).

- The **Gaia-X model** (ontology) defines concepts for the Gaia-X Trust Framework including Participants, Services, Credentials, and Compliance.
- The **SHACL shapes** automatically verify that Gaia-X instances conform to the Trust Framework specifications.
- The core Gaia-X ontologies are integrated as a **Git submodule** to ensure version consistency with upstream.

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
- **`gx_instance.json`** – A sample JSON-LD instance of a Gaia-X Participant.
- **`PROPERTIES.md`** – An auto-generated summary of SHACL properties.
- **`README.md`** – This readme file.

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

When a new version of Gaia-X is released:

1. Navigate to the submodule:

   ```bash
   cd submodules/service-characteristics
   ```

2. Check out the new version tag:

   ```bash
   git checkout <new-tag>  # e.g., git checkout 25.12
   ```

3. Return to the root and commit:
   ```bash
   cd ../..
   git add submodules/service-characteristics
   git commit -m "Upgrade Gaia-X to <new-version>"
   ```

---

## See Also

- [Ontology Domains](../../docs/ontologies/catalog.md) – Browse all available ontologies
- [Validation Tools](../../docs/validation/tools.md) – Complete validation tool reference
- [Architecture](../../docs/discovery/catalogs.md) – Technical details about the ontology structure
- [Gaia-X Trust Framework](https://gaia-x.eu/) – Official Gaia-X website
