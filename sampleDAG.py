#*************** This is a sample DAG which is a .py configuration file containing all tasks and dependencies*******************

#*************** Step1 : Import all necessary and custom libraries here **********************

import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import timedelta

#*************** Step2 : Set-up default arguments using a python dict **********************
default_args = {
    'start_date': airflow.utils.dates.days_ago(0),
    'retries': 1,
    #if a task fails retry once after waiting for 5 mins
    'retry_delay': timedelta(minutes=5),
    #depends on status of previous run i.e. if for a daily run we set this as TRUE and revious run failed, then today nothing would be triggered
    'depends_on_past': False,
    'email' : ['harpreet.sonam@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False
    
}

#*************** Step3 : Instantiate a DAG **********************
dag = DAG(
    'airflow_first_dag',
    default_args=default_args,
    description='This is very first dag',
    schedule_interval=timedelta(minutes=5),
    dagrun_timeout=timedelta(minutes=5))

#************** Step4: Create tasks******************************

t1 = BashOperator(
    task_id='bash1',
    bash_command='echo test',
    dag=dag)
    
t2 = BashOperator(
    task_id='bash2',
    bash_command='date',
    dag=dag)
    
#************** Step5: Set Task dependencies******************************
#Here, we are specifying a list of tasks to run after t1 is successfully completed
t1.set_downstream([t2])
