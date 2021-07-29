from config import subdomain, private_key

from .candidates import (
    get_last_candidate_update,
    import_all_candidates,
    import_complete_candidates,
    import_candidates_activities,
)
from .jobs import import_all_jobs


def extract(project_id, google_credentials):

    jobs_df = import_all_jobs(subdomain, private_key)

    last_update_df = get_last_candidate_update(project_id, google_credentials)
    candidates_df = import_all_candidates(subdomain, private_key, last_update_df.loc[0, "updated_at"])
    complete_candidates_df = import_complete_candidates(subdomain, private_key, candidates_df["id"])
    candidates_activities_df = import_candidates_activities(subdomain, private_key, candidates_df["id"])

    return jobs_df, candidates_df, complete_candidates_df, candidates_activities_df
