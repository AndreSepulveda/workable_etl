import logging
from datetime import datetime

import pandas as pd

from .workable_jobs import get_jobs


def import_all_jobs(subdomain, private_key):
    logging.info("Importing Workable jobs info...")

    """
    Retrieve jobs data from Workable
    """

    jobs_list = get_jobs(subdomain, private_key)
    jobs = pd.DataFrame(jobs_list)
    jobs["extraction_date"] = datetime.today()
    return jobs
