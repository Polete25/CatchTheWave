from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello():
    print("Hola desde tu DAG de trading 🚀")

with DAG("example_trading_dag",
        start_date=datetime(2023, 1, 1), 
        schedule_interval="@daily", 
        catchup=False) as dag:
    tarea = PythonOperator(task_id="saludo", python_callable=hello)
