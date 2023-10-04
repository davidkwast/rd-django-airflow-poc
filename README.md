# rd-django-airflow-poc


## Setup

```bash

poetry run pip install "apache-airflow==2.7.1" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.7.1/constraints-3.11.txt"


poetry install # poetry add django

export AIRFLOW_CONFIG="$(pwd)/airflow.cfg" && export AIRFLOW_HOME="$(pwd)/airflow-home" && export AIRFLOW__CORE__DAGS_FOLDER="$(pwd)/dags" && poetry run airflow users create -e email@example.org -f User -l Admin -r Admin -u admin -p admin -u admin

```

## Run

```

export AIRFLOW_CONFIG="$(pwd)/airflow.cfg" && export AIRFLOW_HOME="$(pwd)/airflow-home" && export AIRFLOW__CORE__DAGS_FOLDER="$(pwd)/dags" && poetry run airflow webserver

export AIRFLOW_CONFIG="$(pwd)/airflow.cfg" && export AIRFLOW_HOME="$(pwd)/airflow-home" && export AIRFLOW__CORE__DAGS_FOLDER="$(pwd)/dags" && poetry run airflow scheduler

```

## Django

directory: `project`

## Airflow

