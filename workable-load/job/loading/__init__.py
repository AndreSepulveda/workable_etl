import logging

import pandas_gbq


def load(jobs_df, candidates_df, complete_df, candidates_activities_df, project_id, dataset, google_credentials):

    logging.info("Sending data about jobs to BigQuery...")
    pandas_gbq.to_gbq(
        jobs_df,
        f"{dataset}.workable_jobs",
        project_id=project_id,
        credentials=google_credentials,
        if_exists="append",
        progress_bar=True,
    )

    logging.info("Sending data about candidates to BigQuery...")
    pandas_gbq.to_gbq(
        candidates_df,
        f"{dataset}.workable_candidates",
        project_id=project_id,
        credentials=google_credentials,
        if_exists="append",
        progress_bar=True,
    )

    logging.info("Sending complete data about candidates to BigQuery...")
    pandas_gbq.to_gbq(
        complete_df,
        f"{dataset}.workable_complete_candidates",
        project_id=project_id,
        credentials=google_credentials,
        if_exists="append",
        progress_bar=True,
    )

    logging.info("Sending data about candidate activity to BigQuery...")
    pandas_gbq.to_gbq(
        candidates_activities_df,
        f"{dataset}.workable_candidates_activity",
        project_id=project_id,
        credentials=google_credentials,
        if_exists="append",
        progress_bar=True,
    )

    logging.info("Process finished")
