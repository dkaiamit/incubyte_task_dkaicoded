from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_PATH = os.path.join(BASE_DIR, "scripts", "data_to_db.py")

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 1, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "mainDAG",
    default_args=default_args,
    schedule_interval="0 0 * * *",  
    catchup=False,
)

task = BashOperator(
    task_id="run_data_to_db",
    bash_command="python {}".format(FILE_PATH),
    dag=dag,
)

task
