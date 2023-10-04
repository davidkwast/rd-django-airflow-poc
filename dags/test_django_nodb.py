import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator


import sys
from pathlib import Path
sys.path.append( str( Path(__file__).resolve().parent.parent ) )

from project.test_app.utils import hello



with DAG(
        dag_id="test_django_nodb",
        start_date=datetime.datetime(2023, 10, 1),
        schedule="@daily",
    ):
    
    # EmptyOperator(task_id="task")
    
    @task.python(task_id="python_task")
    def airflow():
        
        print(hello('airlfow'))
    
    
    airflow()