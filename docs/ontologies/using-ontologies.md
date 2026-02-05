# Using the Ontologies

The ontologies are published with stable W3ID IRIs and mirrored locally under `artifacts/`.

## W3ID Basics

W3ID provides persistent identifiers that redirect to the current location of the ontology files. Use W3ID IRIs in your data and contexts, not raw GitHub URLs.

Example patterns:

- ENVITED-X: `https://w3id.org/ascs-ev/envited-x/{domain}/{version}`
- Gaia-X4PLC-AAD: `https://w3id.org/gaia-x4plcaad/ontologies/{domain}/{version}`
- Gaia-X development: `https://w3id.org/gaia-x/development`

## Files You Will Use

- `*.owl.ttl` defines the ontology vocabulary
- `*.shacl.ttl` defines validation constraints
- `*.context.jsonld` provides JSON-LD prefixes and mappings

## Recommended Consumption Flow

1. Choose the ontology version from `docs/registry.json`.
2. Use the W3ID IRI in your `@context` and `@type` values.
3. Validate data with SHACL shapes before publishing.

## Local Development

For local development, the validator resolves W3ID IRIs using the XML catalogs. You do not need network access to validate data.

