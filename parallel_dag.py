from airflow import DAG
from airflow.operators.bash import BashOperator
# from airflow.operators.subdag import SubDagOperator
# from subdags.subdag_parallel_dag import subdag_parallel_dag
from airflow.utils.task_group import TaskGroup

from datetime import datetime

default_args = {
    'start_date': datetime(2021, 1, 1)
}


with DAG('parallel_dag', 
         schedule_interval='@daily', 
         default_args=default_args, 
         catchup=False) as dag:
    
    task_1 = BashOperator(
        task_id='task_1',
        bash_command='sleep 3'
    )

    with TaskGroup('processing_tasks') as processing_tasks:


        task_2 = BashOperator(
            task_id='task_2',
            bash_command='sleep 3'
        )
        with TaskGroup('spark_tasts') as spark_tasks:
            task_3 = BashOperator(
                task_id='task_3',
                bash_command='sleep 3'
            )
        with TaskGroup('flink_tasts') as flink_tasts:
            task_3 = BashOperator(
                task_id='task_3',
                bash_command='sleep 3'
            )
    # 不要用
    # processing = SubDagOperator(
    #     task_id='processing_tasks',
    #     subdag=subdag_parallel_dag('parallel_dag', 'processing_tasks', default_args=default_args)
    # )

    task_4 = BashOperator(
        task_id='task_4',
        bash_command='sleep 3'
    )

    task_1 >> processing_tasks >> task_4