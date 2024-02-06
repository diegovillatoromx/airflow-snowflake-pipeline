from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.snowflake.transfers.s3_to_snowflake import S3ToSnowflakeOperator

default_args = {
    'owner': 'your_name',
    'start_date': datetime(2022, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    's3_to_snowflake',
    default_args=default_args,
    schedule_interval='@daily',
)

s3_to_snowflake_task = S3ToSnowflakeOperator(
    task_id='s3_to_snowflake_task',
    schema='your_snowflake_schema',
    table='your_snowflake_table',
    stage='your_snowflake_stage',
    file_format='your_snowflake_file_format',
    aws_conn_id='aws_default',
    snowflake_conn_id='snowflake_conn',
    copy_options=['COPY_OPTIONS'],
    dag=dag,
)
