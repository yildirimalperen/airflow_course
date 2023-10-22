from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime

with DAG(
    'parallel_dag', 
    start_date = datetime(2022, 1,1),
    schedule_interval = '@daily',
    catchup=False) as dag:

    exctract_a = BashOperator(
        task_id ='extract_a',
        bash_command= 'sleep 10'
    )

    exctract_b = BashOperator(
        task_id ='extract_b',
        bash_command= 'sleep 10'
    )

    load_a = BashOperator(
        task_id ='load_a',
        bash_command= 'sleep 10'
    )

    load_b = BashOperator(
        task_id ='load_b',
        bash_command= 'sleep 10'
    )

    transform = BashOperator(
        task_id ='transform',
        queue = 'high_cpu',
        bash_command ='sleep 30'
    )

    exctract_a >> load_a
    exctract_b >> load_b

    [load_a,load_b] >> transform