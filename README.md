# Airflow ETL Pipeline for AWS and Snowflake 

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
 

```terminal
-- 1. Create a Warehouse with the smallest size
CREATE WAREHOUSE your_warehouse_name
    WAREHOUSE_SIZE = 'X-SMALL'
    WAREHOUSE_TYPE = 'STANDARD'
    AUTO_SUSPEND = 300
    AUTO_RESUME = TRUE;

-- 2. Create a Database
CREATE DATABASE your_database_name;

-- 3. Create a Schema
CREATE SCHEMA your_schema_name;

-- 4. Create a Role
CREATE ROLE your_role_name;
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
