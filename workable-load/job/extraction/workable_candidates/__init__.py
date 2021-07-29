import json
import logging
import sys

from .requests import get_rate_limited_request


def get_candidates(subdomain, private_key, updated_after=None):

    api_url = "https://" + subdomain + ".workable.com/spi/v3/"
    api_headers = {"Authorization": "Bearer" + " " + private_key}

    # Get the raw output from the API
    url = api_url + "candidates"

    # 50 is the maximum limit (used to reduce number of calls to databse)
    url += "?limit=50"

    if updated_after:
        url += "&updated_after=" + str(updated_after)

    output = []

    content = None
    # While loop to accommodate multiple pages being returned by the query
    # Pages are appended to the same result and returned as one
    while True:
        result = get_rate_limited_request(url=url, headers=api_headers)
        # Convert the raw string output into JSON format
        convert_to_json = json.loads(result.content)
        # pprint.pprint(convert_to_json)

        if result.status_code != 200:
            logging.info("Error: " + str(result.status_code) + " - " + result.text)
            return output

        content = convert_to_json["candidates"]

        if output:
            output += content  # Only need to add the items, don't need the header
        else:
            output = content
        # If a new page is available, repeat the process.

        try:
            url = convert_to_json["paging"]["next"]
        except KeyError:
            break

    return output
