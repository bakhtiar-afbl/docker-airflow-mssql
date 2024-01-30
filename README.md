# Docker README.md

Follow these steps to set up Apache Airflow with Microsoft SQL Server using Docker:

## Step 1: Setup Docker Desktop
Ensure Docker Desktop is installed and running on your system.

## Step 2: Clone Repository
Clone the repository to your desired location using Git.

## Step 3: Configure Airflow Port (Optional)
Modify the `docker-compose.yml` file to change the Airflow port (default is 9099).

## Build and Run Docker Containers
- Open Command Prompt.
- Navigate to your project location.
- Execute the following commands:

        docker build -t airflow-sqlserver -f Dockerfile . --no-cache
        docker-compose up


## Access Airflow UI
- Once the process is complete, access the Airflow UI in your browser:

  http://localhost:9099/

Replace `9099` with the port you specified if changed.

## Configure MSSQL Connection
- Log in to Airflow:
- Username: airflow
- Password: airflow
- Go to Admin > Connections > Add Connection:
- Connection Id: SQL
- Connection Type: Microsoft SQL Server
- Host: ServerName
- Login: UserName
- Password: Password
- Port: 1433
- Click "Test Connection" to ensure successful setup.

## Create DAG (Directed Acyclic Graph)
- Navigate to the `dag` folder and create a `.py` file with the provided code.
- The code selects data from `[EDW].[dbo].[orders]` and inserts it into `[EDW].[dbo].[orders2]`.

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

## Code Explanation
The DAG selects data from `[EDW].[dbo].[orders]` and inserts it into `[EDW].[dbo].[orders2]`.

Follow these instructions to set up Apache Airflow with MSSQL efficiently.


