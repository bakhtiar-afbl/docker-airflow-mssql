from airflow import DAG
from airflow.operators.mssql_operator import MsSqlOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG(
    'select_and_insert_data_dag',
    default_args=default_args,
    description='DAG to select data from MSSQL table and insert into another table',
    schedule_interval=timedelta(seconds=500000),
)


select_orders_data_sql = """
SELECT *
FROM [EDW].[dbo].[orders];
"""

insert_orders2_data_sql = """
INSERT INTO [EDW].[dbo].[orders2] ([order_id], [product_name], [quantity], [is_large_order])
SELECT [order_id], [product_name], [quantity], [is_large_order]
FROM [EDW].[dbo].[orders];
"""

select_orders_data_task = MsSqlOperator(
    task_id='select_orders_data_task',
    mssql_conn_id='sql',  # Connection ID defined in Airflow
    sql=select_orders_data_sql,
    dag=dag,
)

insert_orders2_data_task = MsSqlOperator(
    task_id='insert_orders2_data_task',
    mssql_conn_id='sql',  # Connection ID defined in Airflow
    sql=insert_orders2_data_sql,
    dag=dag,
)

select_orders_data_task >> insert_orders2_data_task
