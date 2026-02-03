# Gaia-X Connection

This repository integrates Gaia-X Service Characteristics with ENVITED-X domain ontologies.

## Gaia-X Ontology

The Gaia-X development ontology is stored under `artifacts/gx/` and uses the W3ID IRI:

- `https://w3id.org/gaia-x/development`

It provides the base vocabulary for data exchange components and legal person modeling used in Gaia-X aligned assets.

## How It Connects

- ENVITED-X ontologies reuse Gaia-X classes for data exchange and governance metadata.
- SHACL validation loads the Gaia-X ontology when these classes are referenced.
- The Gaia-X Service Characteristics source is tracked as a submodule and informs the GX alignment.
