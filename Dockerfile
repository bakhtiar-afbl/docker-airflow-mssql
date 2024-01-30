<<<<<<< HEAD
FROM apache/airflow:2.7.2

RUN pip install markupsafe==2.0.1 \
	&& pip install apache-airflow-providers-odbc \
	&& pip install pyodbc \
	&& pip install apache-airflow-providers-microsoft-mssql \
	&& pip install apache-airflow-providers-microsoft-mssql[odbc] \
	&& pip install apache-airflow-providers-microsoft-azure \
=======
FROM apache/airflow:2.7.2

RUN pip install markupsafe==2.0.1 \
	&& pip install apache-airflow-providers-odbc \
	&& pip install pyodbc \
	&& pip install apache-airflow-providers-microsoft-mssql \
	&& pip install apache-airflow-providers-microsoft-mssql[odbc] \
	&& pip install apache-airflow-providers-microsoft-azure \
>>>>>>> fecbef9ed70214bdb8e164f6a3a8a241579bc046
	&& pip install gitpython