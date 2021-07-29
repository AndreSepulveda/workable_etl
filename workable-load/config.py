import json
import logging
from os import environ

from google.oauth2.service_account import Credentials

logging.basicConfig(
    level=logging.INFO, format="%(name)s - %(asctime)s - %(levelname)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S"
)


def get_crendentials(google_credentials):
    scopes = (
        "https://www.googleapis.com/auth/bigquery",
        "https://www.googleapis.com/auth/cloud-platform",
        "https://www.googleapis.com/auth/drive",
    )

    google_credentials = json.loads(google_credentials)
    credentials = Credentials.from_service_account_info(google_credentials)
    credentials = credentials.with_scopes(scopes)
    return credentials


mode = environ.get("MODE", "staging")
bigquery_project_id = "restricted"
google_credentials = get_crendentials(environ["GOOGLE_CREDENTIALS"])
dataset = "workable"
subdomain = environ.get("SUBDOMAIN")
private_key = environ.get("PRIVATE_KEY")
