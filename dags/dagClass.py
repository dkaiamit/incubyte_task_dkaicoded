from airflow import DAG
from airflow.models.dag import ScheduleInterval
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

class dagClass:
    def __init__(self) -> None:
        self.module_path = "/home/data.admin/data-warehouse/galaxy"
        self.dag = None
# start date needs to be set atleast 24 hours before the execution time, otherwise airflow wont run the script
#even if the schedule time is met.
        self.args={
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': datetime.now()-timedelta(days=1), 
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
        }
    def create_dag(self,dagName, is_email_failure=False, schedule_interval = "39 8 * * *"):
        print(type(self.args))
        self.args['email_on_failure'] = is_email_failure
        self.dag=DAG(dagName, 
        default_args=self.args,
        schedule_interval=schedule_interval,max_active_runs=16)
        return self.dag


    def add_python_script(self,dag,taskID, scriptPath, optionalCommands="pwd"):


        return BashOperator(
            task_id = taskID,
            bash_command = '{};export PYTHONPATH="{}";python3 {}'.format(optionalCommands,self.module_path,scriptPath),
            dag = dag
        )

    def add_bash_command(self,dag,taskID, bashCommand):

        return BashOperator(
            task_id = taskID,
            bash_command = bashCommand,
            dag = dag
        )