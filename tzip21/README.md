# TZIP-21 Rich Metadata Ontology

## Overview

This ontology models the [Tezos TZIP-21 (Rich Metadata)](https://tzip.tezosagora.org/proposal/tzip-21/) standard as a semantic RDF/OWL vocabulary. It is designed to ensure that Non-Fungible Tokens (NFTs) minted within the **ENVITED-X Data Space** carry metadata that is not only compatible with standard Tezos wallets and marketplaces but also machine-readable and compliant with **Gaia-X** specifications.

## Connection to EVES-003

This ontology is a core component of the asset definition and upload process defined in **[EVES-003: ENVITED-X Asset Definition and Upload Process](../../ascs-ev/eves/EVES-337fda9b5a71969ce3b8c02874c4e20137d66453/EVES/EVES-003/eves-003.md)**.

### The Architectural Role

In the context of EVES-003 and Gaia-X:

1.  **The Data Resource (`envited-x:SimulationAsset`):**
    * This is the actual dataset (e.g., an HD Map, Simulation Model).
    * It is described by a domain-specific Self-Description (e.g., `hdmap_instance.json`) and classified as a `gx:DataResource`.
    * It resides on IPFS (encrypted or public) and is referenced by its CID.

2.  **The Service Offering (`tzip21:Asset`):**
    * This is the **NFT Metadata** file (`tzip21_token_metadata.json`) generated during the upload process (Step 2 & 4 of EVES-003).
    * It wraps the Data Resource, adding licensing (`rights`), provenance (`minter`, `creators`), and visual previews (`displayUri`).
    * It acts as the **Gaia-X Service Offering**, representing the tradeable "Data Product" in the catalog.

### Metadata Mapping

As specified in EVES-003, the fields in this ontology map directly to the Simulation Asset's metadata:

| TZIP-21 Property | Mapped Gaia-X/Domain Property | Description |
| :--- | :--- | :--- |
| `tzip21:name` | `gx:name` | The name of the Data Resource. |
| `tzip21:description` | `gx:description` | A summary of the Data Resource. |
| `tzip21:identifier` | `dcterms:identifier` | The unique DID (`@id`) of the underlying Simulation Asset. |
| `tzip21:rights` | `gx:license` | The SPDX license identifier (e.g., "MPL-2.0"). |
| `tzip21:artifactUri` | *IPFS CID* | The link to the actual dataset zip file. |
| `tzip21:attributes` | *Ontologies* | Lists the ontologies used (Reverse Domain Notation) for semantic validation. |

### Usage

When an asset is uploaded via the ENVITED-X Portal:
1.  The portal validates the `domainMetadata.json` (The Data Resource).
2.  It generates the `tzip21_token_metadata.json` (The Service Offering) using this ontology.
3.  This JSON-LD file is pinned to IPFS and linked to the minted NFT.

This ensures that the NFT is not just a "dumb" pointer, but a **Semantic Self-Description** that can be ingested by the Data Space Catalog.
