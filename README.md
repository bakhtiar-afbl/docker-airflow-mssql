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

## Code Explanation
The DAG selects data from `[EDW].[dbo].[orders]` and inserts it into `[EDW].[dbo].[orders2]`.

Follow these instructions to set up Apache Airflow with MSSQL efficiently.


