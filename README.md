# Real-time Mobile App Data Processing with Snowflake ELT Pipeline

## Table of Contents

1. [Description](#description)
2. [Design Components](#design-components)
3. [Architecture](#architecture)
4. [Dataset](#dataset)
5. [Methodology and Modular Code Overview](#methodology-and-modular-code-overview)
6. [Data Modeling](#data-modeling)
7. [Contribution](#contribution)
8. [Contact](#contact)


## Description:
This project focuses on processing real-time data generated by events from a mobile application, such as purchases, interactions, and user actions. Utilizing a real-time data stream, data is continuously extracted and streamed to Snowflake, a highly scalable cloud data warehouse. Once in Snowflake, the data undergoes an Extraction, Load, and Transformation (ELT) process, where transformation and preparation for further analysis take place. This ELT pipeline enables efficient real-time data transformation, ensuring data integrity and quality for subsequent analysis and data-driven decision-making.


## Design Components

The high-level design components of our system are as follows:

### Data Streaming and Ingestion
We require a robust solution for streaming and ingesting real-time data from mobile app events into our data pipeline. This component must handle large volumes of data efficiently and ensure minimal latency for processing.

#### Technologies Considered:
- **Amazon Kinesis Data Streams:** Offers scalable and real-time data streaming capabilities, ideal for ingesting data from mobile app events.
- **Amazon Kinesis Data Firehose:** Provides a managed service for loading streaming data into Snowflake, simplifying the data delivery process.

### Data Processing
Our system needs compute capabilities to process the ingested data efficiently. Whether it's real-time or batch processing, reliability and fast performance are essential for timely data transformation.

#### Technologies Considered:
- **AWS Lambda:** Enables serverless compute for processing events in real-time, offering scalability and cost-effectiveness.
- **Amazon EMR:** Provides a managed Hadoop framework for processing large-scale data sets, suitable for batch processing tasks.

### Data Storage
A scalable and performant data storage solution is crucial for storing and managing processed data. This component must support Snowflake integration and ensure data integrity.

#### Technologies Considered:
- **Amazon S3:** Simple Storage Service offers highly scalable object storage, suitable for storing processed data and integrating with Snowflake.
- **Snowflake:** A cloud-based data warehouse designed for scalability and performance, providing seamless integration with various data sources and analytics tools.

### Data Transformation and Loading
Efficient data transformation and loading processes are essential for preparing data for analysis in Snowflake. This component must handle complex transformations and ensure data quality.

#### Technologies Considered:
- **Apache Airflow:** Provides a platform for orchestrating complex data workflows, including data transformation and loading tasks.
- **AWS Glue:** Offers managed ETL (Extract, Transform, Load) service for preparing and loading data into Snowflake, with support for schema discovery and data cataloging.

### Data Query and Analysis
To enable data-driven decision-making, we need tools for querying and analyzing data stored in Snowflake.

#### Technologies Considered:
- **Amazon Athena:** Allows ad hoc querying of data in S3 using standard SQL, providing flexibility and cost-effectiveness for data analysis.
- **Snowflake:** Offers a powerful SQL-based interface for querying and analyzing data, with support for complex analytics and reporting tasks.

These design choices were made based on their suitability and alignment with the requirements of our real-time data processing and analysis pipeline. Services marked with an asterisk (*) were utilized in the creation of the project.


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
