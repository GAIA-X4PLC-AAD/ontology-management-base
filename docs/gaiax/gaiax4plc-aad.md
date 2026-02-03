# Gaia-X 4 PLC-AAD and Federated Catalog

Gaia-X 4 PLC-AAD established the publishing and validation workflow for this repository.

## Project Context

The Gaia-X 4 PLC-AAD project aligned automotive simulation assets with Gaia-X requirements. The ontologies in this repository implement those requirements and extend them with ENVITED-X domain models.

## Federated Catalog Upload

Publishing to the federated catalog is supported by `src/tools/uploaders/fc_upload_with_update.py`.

Required environment variables:

- `FOLDER_TO_UPLOAD` selects the domain folder under `artifacts/`
- `FEDERATED_CATALOGUE_URL` sets the catalog endpoint
- `DRY_RUN` toggles upload execution
- `KEYCLOAK_USER` and `KEYCLOAK_PASSWORD` authenticate against Keycloak
- `KEYCLOAK_CLIENT_ID`, `KEYCLOAK_REALM_NAME`, and `KEYCLOAK_SERVER_URL` can override defaults

Example:

```bash
export FOLDER_TO_UPLOAD=hdmap
export FEDERATED_CATALOGUE_URL=https://fc-server.gxfs.gx4fm.org
export DRY_RUN=true

python3 -m src.tools.uploaders.fc_upload_with_update
```

The uploader authenticates through Keycloak, checks existing schemas, and creates or updates OWL and SHACL files accordingly.
