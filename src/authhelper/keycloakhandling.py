import os

from keycloak.keycloak_openid import KeycloakOpenID

# Authentification
KEYCLOAK_USER = str(os.environ.get("KEYCLOAK_USER"))
KEYCLOAK_PASSWORD = str(os.environ.get("KEYCLOAK_PASSWORD"))

KEYCLOAK_CLIENT_SECRET_KEY = os.environ.get("KEYCLOAK_CLIENT_SECRET_KEY")
KEYCLOAK_SERVER_URL = os.environ.get(
    "KEYCLOAK_SERVER_URL", default="https://fc-keycloak.gxfs.gx4fm.org"
)
KEYCLOAK_CLIENT_ID = os.environ.get("KEYCLOAK_CLIENT_ID", default="federated-catalogue")
KEYCLOAK_REALM_NAME = os.environ.get("KEYCLOAK_REALM_NAME", default="gaia-x")

KEYCLOAK_OPENID = KeycloakOpenID(
    server_url=KEYCLOAK_SERVER_URL,
    client_id=KEYCLOAK_CLIENT_ID,
    realm_name=KEYCLOAK_REALM_NAME,
    client_secret_key=KEYCLOAK_CLIENT_SECRET_KEY,
)


def get_auth_header() -> dict[str, str]:
    """get authentication header for POST request on Fed. Cat.
    return Authorization-Header
    """
    if KEYCLOAK_USER is not None:
        print("Keycloak user is set")
    else:
        print("Keycloak user is not set")
    token = get_token_keycloak()
    return {"Authorization": "Bearer {}".format(token["access_token"])}


def get_token_keycloak() -> dict[str, str]:
    """get keycloak token for authentication header
    return keycloaktoken
    """
    token = KEYCLOAK_OPENID.token(KEYCLOAK_USER, KEYCLOAK_PASSWORD)
    return token
