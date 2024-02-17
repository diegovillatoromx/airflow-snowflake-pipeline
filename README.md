# Airflow ETL Pipeline for AWS and Snowflake 

## Table of Contents

1. [Data Generation](#data-generation)
2. [AWS Infrastructure](#aws-infrastructure)
3. [Configuration](#configuration)
4. [.gitignore](#gitignore)
5. [README.md](#readmemd)


<p align="center">
  <img src="https://github.com/diegovillatoromx/airflow-snowflake-pipeline/blob/main/architecture.gif" alt="architecture-airflow" width="800">
</p>


```bash    
Airflow-ETL-Pipeline-for-Snowflake/ 
├── data_generation/
│   ├── generate_purchase_data.py     # Python script to simulate sales data generation
│   ├── requirements.txt              # Python dependencies required for the data generation script
│   └── purchase_data_generation.py   # Functions for generating events and users
├── aws_infrastructure/
│   ├── boto3_scripts/
│   │   ├── kinesis_stream_ingestion.py  # Boto3 script to create Kinesis Data Stream ingestion
│   │   ├── s3_stream_ingestion.py       # Boto3 script to create Bucket s3 ingestion
│   └── cli_scripts/
│       └── setup_infrastructure.sh    # AWS CLI scripts to set up resources that cannot be done with Boto3
├── config/
│   ├── credentials.json              # AWS credentials and regional configuration
│   ├── kinesis_ingestion_config.json # Configuration for Kinesis Data Stream ingestion
│   ├── kinesis_processed_config.json # Configuration for Kinesis Data Stream processed
│   ├── kinesis_analytics_config.json # Configuration for Kinesis Data Analytics
│   ├── firehose_config.json          # Configuration for Kinesis Firehose Delivery Stream
│   ├── s3_config.json                # Configuration for S3 bucket
│   ├── lambda_config.json            # Configuration for Lambda function
│   ├── athena_config.json            # Configuration for AWS Athena
│   └── sns_config.json               # Configuration for Amazon SNS
├── .gitignore                        # File to exclude files and folders from Git
└── README.md                         # Project documentation, setup, and deployment information
```
 

## Step 1: Create Snowflake Warehouse, Database, Schema, and Role

1. To Create a Snowflake Warehouse, the execute the SQL command to create a Snowflake Warehouse with the desired configuration.
   ```sql
   CREATE OR REPLACE WAREHOUSE your_warehouse_name
   WAREHOUSE_SIZE = 'X-SMALL'
   AUTO_SUSPEND = 1800
   AUTO_RESUME = TRUE;
   ```
2. To create a Snowflake Database, execute the SQL command to create a Snowflake Database.
   ```sql
   CREATE OR REPLACE DATABASE your_database_name;
   ```
4. To Create a Snowflake Schema, execute the SQL command to create a Snowflake Schema within the database.
   ```sql
   CREATE OR REPLACE SCHEMA your_schema_name;
   ```
6. To create a Snowflake Role, execute the SQL command to create a Snowflake Role.
   ```sql
   CREATE OR REPLACE ROLE your_role_name;
   ```

## Step 2: Define Snowflake Tables
Now, we'll define the Snowflake tables needed for the 'purchase' data structure:

1. To Create a `'users'` Table, execute the SQL command to create a '`users'` table with the specified columns and primary key.
   ```sql
   CREATE OR REPLACE TABLE your_schema_name.users (
    USER_ID STRING PRIMARY KEY,
    OS_USER STRING,
    CITY STRING,
    LATITUDE FLOAT,
    LONGITUDE FLOAT);
   ```
2. To Create an `'events'` Table, execute the SQL command to create an `'events'` table with the specified columns and primary key.
   ```sql
   CREATE OR REPLACE TABLE your_schema_name.events (
    EVENT_ID STRING PRIMARY KEY,
    USER_ID STRING,
    EVENT_NAME STRING,
    EVENT_TIMESTAMP TIMESTAMP_NTZ);
   ```

3. Execute the SQL command to create an `'orders'` table with the specified columns and primary key.

   ```sql
   CREATE OR REPLACE TABLE your_schema_name.orders (
    ORDER_ID STRING PRIMARY KEY,
    USER_ID STRING,
    ORDER_TYPE STRING,
    STATUS STRING,
    PAYMENT_METHOD STRING,
    CREATED_AT TIMESTAMP_NTZ);
    ```
4.  Execute the SQL command to create a `'purchase_counts'` table with the specified columns and a foreign key reference to the `'users'` table.
   ```sql
   CREATE OR REPLACE TABLE your_schema_name.purchase_counts (
    USER_ID STRING,
    HOUR INTEGER,
    DAILY INTEGER,
    HOURLY_PURCHASE_COUNT INTEGER,
    DAILY_PURCHASE_COUNT INTEGER,
    FOREIGN KEY (USER_ID) REFERENCES your_schema_name.users(USER_ID));
   ```


![schema-snowflake](https://github.com/diegovillatoromx/airflow-snowflake-pipeline/blob/main/schema-snowflake.png)
