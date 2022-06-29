# General Dependencies
from datetime import timedelta, datetime
# Airflow Dependencies
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
# Import ETL
from etl import run_etl

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 6, 28),
    'email': ['lrchitala@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'spotify_dag',
    default_args=default_args,
    description='DAG for the tech challenge!',
    schedule_interval=timedelta(days=1),
)


run_etl = PythonOperator(
    task_id='etl',
    python_callable=run_etl,
    dag=dag,
)

run_etl