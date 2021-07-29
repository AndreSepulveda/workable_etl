import datetime as dt
from os import environ

from airflow import DAG
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator

NAME = "workable-load"
SCHEDULE_INTERVAL = "0 9/4 * * *"
ENV_VARS = {
    "GOOGLE_CREDENTIALS": environ["GOOGLE_CREDENTIALS_RESTRICTED"],
    "PRIVATE_KEY": environ["PRIVATE_KEY"],
    "SUBDOMAIN": environ["SUBDOMAIN"],
    "MODE": "staging",
}


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": True,
    "email_on_retry": False,
    "retries": 3,
    "retry_delay": dt.timedelta(minutes=10),
    "start_date": dt.datetime(2019, 1, 1),
}

with DAG(dag_id=NAME, default_args=default_args, schedule_interval=SCHEDULE_INTERVAL, catchup=False) as dag:
    KubernetesPodOperator(
        name=NAME,
        task_id=NAME,
        image=f"oficial/{NAME}",
        env_vars=ENV_VARS,
        namespace="default",
        image_pull_policy="Always",
        image_pull_secrets="regcred",
        is_delete_operator_pod=True,
        dag=dag,
    )
