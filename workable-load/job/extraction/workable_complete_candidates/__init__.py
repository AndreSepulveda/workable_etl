import json
import logging
import sys

from .requests import get_rate_limited_request


def get_complete_candidates(subdomain, private_key, id=None):

    api_url = "https://" + subdomain + ".workable.com/spi/v3/"
    api_headers = {"Authorization": "Bearer" + " " + private_key}

    # Get the raw output from the API
    url = api_url + "candidates/" + id

    # 50 is the maximum limit (used to reduce number of calls to database)
    url += "?limit=50"

    output = []

    content = None

    result = get_rate_limited_request(url=url, headers=api_headers)
    # Convert the raw string output into JSON format
    convert_to_json = json.loads(result.content)
    # pprint.pprint(convert_to_json)

    if result.status_code != 200:
        logging.info("Error: " + str(result.status_code) + " - " + result.text)
        return content

    content = convert_to_json["candidate"]

    if output:
        output += content  # Only need to add the items, don't need the header
    else:
        output = content

    return output
