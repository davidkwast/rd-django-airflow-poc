import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.python import PythonOperator


import sys
from pathlib import Path
sys.path.append( str( Path(__file__).resolve().parent.parent ) )


import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()
from project.test_app import models



with DAG(
        dag_id="test_django_withdb",
        start_date=datetime.datetime(2023, 10, 1),
        schedule="@daily",
    ):
    
    @task.python(task_id="python_task")
    def airflow():
        
        models.Test_Table.objects.create(text='airflow test')
    
    
    airflow()