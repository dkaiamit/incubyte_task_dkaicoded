from dagClass import *
import os

current_dir = os.getcwd()
previous_dir = os.path.dirname(current_dir)

dagObj = dagClass()

dag =dagObj.create_dag("mainDAG", schedule_interval="0 1 * * *")

file_name=str(previous_dir) + '/scripts/data_to_db.py'
t1 =dagObj.add_python_script(dag, "Task1", file_name)

t1