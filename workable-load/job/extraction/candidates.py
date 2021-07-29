import logging
from datetime import datetime

import pandas as pd
from google.cloud.bigquery import Client

from .workable_candidates import get_candidates
from .workable_candidates_activities import get_candidates_activities
from .workable_complete_candidates import get_complete_candidates


def get_last_candidate_update(project_id, google_credentials):
    logging.info("Querying last candidate update...")

    sql = f"""
        SELECT 
            updated_at
        FROM 
            `restricted.workable.workable_candidates`
        ORDER BY updated_at DESC
        LIMIT 1
    """

    try:
        client = Client(project_id, google_credentials)
        rows = client.query(sql).result()
        results_df = rows.to_dataframe()

    except Exception as e:
        logging.info(e)
        results_df

    return results_df


def import_all_candidates(subdomain, private_key, last_update):
    logging.info("Importing Workable candidates info...")

    """
    Retrieve all candidates from the Workable since last_update
    """

    candidates_list = get_candidates(subdomain, private_key, updated_after=last_update)
    candidates = pd.DataFrame(candidates_list)
    candidates["extraction_date"] = datetime.today()
    return candidates


def import_complete_candidates(subdomain, private_key, candidate_id):
    logging.info("Importing Workable complete candidates info...")

    """
    Import complete candidate info from the Workable database into the local database
    """
    complete_df = pd.DataFrame()
    for id in candidate_id:
        candidate = get_complete_candidates(subdomain, private_key, id=id)
        if candidate is not None:
            candidate = pd.DataFrame([candidate])
            complete_df = complete_df.append(candidate)
    complete_df["extraction_date"] = datetime.today()
    return complete_df


def import_candidates_activities(subdomain, private_key, candidate_id):
    logging.info("Importing Workable candidates activities info...")

    """
    Import candidate activities from the Workable database into the local database
    """
    candidate_activities_df = pd.DataFrame()
    for id in candidate_id:
        candidate = get_candidates_activities(subdomain, private_key, id=id)
        if candidate is not None:
            candidate = pd.DataFrame(candidate)
            candidate["candidate_id"] = id
            candidate_activities_df = candidate_activities_df.append(candidate)
    candidate_activities_df["extraction_date"] = datetime.today()
    return candidate_activities_df
