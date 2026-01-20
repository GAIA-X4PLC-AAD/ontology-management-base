import os

import requests

import authhelper.keycloakhandling

##########################################################################
# DEPRECATED: LEGACY VERSION ONLY SUPPORTING ADDING NEW SCHEMAS TO THE FEDERATED CATALOGUE
# USE THE NEW VERSION IN src/fc_upload_with_update.py instead.
# WILL BE REMOVED IN FUTURE.
##########################################################################

# ENVIRONMENT PROPERTIES
ROOT_DIRECTORY = os.getcwd()
FOLDER_TO_UPLOAD = os.environ.get("FOLDER_TO_UPLOAD")
FEDERATED_CATALOGUE_URL = os.environ.get(
    "FEDERATED_CATALOGUE_URL", default="https://fc-server.gxfs.gx4fm.org"
)


# FUNCTIONS
def main():
    """
    The main function controls the overall program flow.
    It uploads .ttl files in a specified folder into the Federated Catalogue.
    """
    for directory in next(os.walk(ROOT_DIRECTORY))[1]:
        if directory == FOLDER_TO_UPLOAD:
            full_directory_path = os.path.join(ROOT_DIRECTORY, directory)
            for filename in os.listdir(full_directory_path):
                full_filepath = os.path.join(full_directory_path, filename)
                if filename.endswith(".ttl"):
                    with open(full_filepath, "r") as new_turtle_file:
                        new_turtle_file_text = new_turtle_file.read()
                        print(
                            post_to_catalogue(
                                "/schemas", request_body=new_turtle_file_text
                            )
                        )


def post_to_catalogue(endpoint: str, request_body: str) -> requests.Response:
    """Perform a http-post-request on the Federated Catalogue

    Keyword arguments:
    endpoint -- the API POST-endpoint you want to query
    request_body -- the request body of your query

    return the answer from the Federated Catalogue
    """

    auth_header = authhelper.keycloakhandling.get_auth_header()
    auth_header["Content-Type"] = "text/turtle"
    return requests.post(
        FEDERATED_CATALOGUE_URL + endpoint, headers=auth_header, data=request_body
    )


if __name__ == "__main__":
    main()
