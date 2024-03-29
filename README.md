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
- **Amazon Kinesis Data Streams*:** Offers scalable and real-time data streaming capabilities, ideal for ingesting data from mobile app events.
- **Amazon Kinesis Data Firehose*:** Provides a managed service for loading streaming data into Snowflake, simplifying the data delivery process.

### Data Processing
Our system needs compute capabilities to process the ingested data efficiently. Whether it's real-time or batch processing, reliability and fast performance are essential for timely data transformation.

#### Technologies Considered:
- **AWS Lambda:** Enables serverless compute for processing events in real-time, offering scalability and cost-effectiveness.
- **Amazon EMR:** Provides a managed Hadoop framework for processing large-scale data sets, suitable for batch processing tasks.

### Data Storage
A scalable and performant data storage solution is crucial for storing and managing processed data. This component must support Snowflake integration and ensure data integrity.

#### Technologies Considered:
- **Amazon S3*:** Simple Storage Service offers highly scalable object storage, suitable for storing processed data and integrating with Snowflake.
- **Snowflake:** A cloud-based data warehouse designed for scalability and performance, providing seamless integration with various data sources and analytics tools.

### Data Transformation and Loading
Efficient data transformation and loading processes are essential for preparing data for analysis in Snowflake. This component must handle complex transformations and ensure data quality.

#### Technologies Considered:
- **Apache Airflow*:** Provides a platform for orchestrating complex data workflows, including data transformation and loading tasks.
- **AWS Glue:** Offers managed ETL (Extract, Transform, Load) service for preparing and loading data into Snowflake, with support for schema discovery and data cataloging.

### Data Query and Analysis
To enable data-driven decision-making, we need tools for querying and analyzing data stored in Snowflake.

#### Technologies Considered:
- **Amazon Athena:** Allows ad hoc querying of data in S3 using standard SQL, providing flexibility and cost-effectiveness for data analysis.
- **Snowflake*:** Offers a powerful SQL-based interface for querying and analyzing data, with support for complex analytics and reporting tasks.

These design choices were made based on their suitability and alignment with the requirements of our real-time data processing and analysis pipeline. Services marked with an asterisk (*) were utilized in the creation of the project.

### Architecture

This project is dedicated to constructing a robust Data Pipeline leveraging cutting-edge cloud technologies including AWS (Amazon Web Services), Snowflake, Kinesis, and Apache Airflow. An efficient Data Pipeline serves as the backbone for ingesting, processing, and analyzing vast amounts of both real-time and batch data, enabling streamlined and insightful data-driven decision-making processes.

The architecture of our Data Pipeline is designed to handle the diverse and dynamic nature of modern data streams, ensuring scalability, reliability, and flexibility throughout the entire data lifecycle. By harnessing the power of AWS services such as Kinesis for real-time data ingestion, Snowflake for cloud-native data warehousing, and Apache Airflow for workflow orchestration, we establish a robust foundation for seamless data processing and analysis.

The integration of AWS services offers unparalleled scalability and resilience, allowing our Data Pipeline to adapt to changing data volumes and processing requirements effortlessly. Snowflake's innovative architecture enables efficient storage and querying of structured and semi-structured data, empowering data analysts and stakeholders with fast and reliable access to critical insights.

Additionally, Apache Airflow serves as the central orchestrator for our Data Pipeline, providing a unified platform for defining, scheduling, and monitoring data workflows. With Airflow's intuitive interface and extensible architecture, data engineers can easily manage complex data pipelines, ensuring the timely and accurate delivery of data to downstream systems and applications.

In summary, the architecture of our Data Pipeline embodies the principles of scalability, reliability, and efficiency, leveraging the synergies between AWS, Snowflake, Kinesis, and Apache Airflow to unlock the full potential of our data assets and drive meaningful business outcomes.

<p align="center">
  <img src="https://github.com/diegovillatoromx/airflow-snowflake-pipeline/blob/main/architecture.gif" alt="architecture-airflow" width="800">
</p>

### Dataset

The dataset provided in the [Mobile App Events Generation Dataset for Simulation](https://github.com/diegovillatoromx/Mobile-App-Events-Generation-Dataset-for-Simulation) repository serves as a comprehensive collection of simulated mobile app events, meticulously crafted to mimic real-world user interactions within a mobile application environment.

The dataset encompasses various types of events commonly encountered in mobile applications, including but not limited to user registrations, logins, purchases, interactions, and actions. Each event entry is enriched with contextual information such as timestamps, user IDs, device information, and event attributes, enabling detailed analysis and exploration of user behavior patterns.

Through the meticulous generation process, the dataset captures the nuances and complexities of user interactions, providing valuable insights into user engagement, app usage patterns, and user journey analysis. This rich and diverse dataset serves as a valuable resource for data engineers, data scientists, and analysts seeking to develop and evaluate data-driven solutions, such as recommendation systems, personalized user experiences, and predictive analytics models.

The dataset's structured format and extensive documentation facilitate easy integration into data pipelines and analytics workflows, empowering organizations to derive actionable insights and drive informed decision-making processes. Whether it's analyzing user churn rates, optimizing marketing campaigns, or understanding feature adoption trends, the Mobile App Events Generation Dataset for Simulation offers a wealth of opportunities for data-driven innovation and experimentation.


### Methodology and Modular Code Overview

This section provides an overview of the methodology employed in the development of the ETL (Extract, Transform, Load) pipeline using Apache Airflow for Snowflake data warehouse integration. Additionally, it outlines the modular structure of the codebase, highlighting key components and their functionalities.

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
#### Methodology
The ETL pipeline follows a structured approach, encompassing the following stages:

1. **Data Extraction**: Simulated data generation scripts (`generate_purchase_data.py`) are utilized to simulate sales data generation, providing a realistic dataset for pipeline testing and development.

2. **Data Transformation**: The extracted data undergoes transformation processes to ensure compatibility and optimization for Snowflake data warehouse ingestion. Python scripts such as `purchase_data_generation.py` are employed to perform necessary data transformations and enhancements.

3. **Data Loading**: Transformed data is loaded into Snowflake data warehouse using optimized ingestion methods, leveraging AWS infrastructure and services like Kinesis Data Streams and S3 buckets.

#### Modular Code Overview

The codebase is organized into several modules within the project structure:

- **`data_generation/`**: Contains Python scripts for generating simulated purchase data, along with associated dependencies specified in `requirements.txt`.

- **`aws_infrastructure/`**: Houses Boto3 and AWS CLI scripts responsible for setting up and configuring AWS infrastructure components required for data ingestion and processing, such as Kinesis Data Streams and S3 buckets.

- **`config/`**: Stores configuration files (`*.json`) containing AWS credentials, regional settings, and specific configurations for various AWS services utilized in the pipeline, including Kinesis Data Streams, S3 buckets, Lambda functions, Athena, and SNS.

- **`.gitignore`**: Specifies files and folders to be excluded from version control using Git, ensuring clean repository management.

- **`README.md`**: Provides comprehensive documentation, setup instructions, and deployment information for the project, facilitating easy onboarding and collaboration for team members and stakeholders.

This modular structure enhances code maintainability, scalability, and reusability, allowing for seamless integration of new features, optimizations, and enhancements into the ETL pipeline.

## Data Modeling

Data modeling is a critical aspect of designing the schema for efficient storage and retrieval of data in Snowflake. We adopt a structured approach to model our data, capitalizing on Snowflake's relational database capabilities.

![schema-snowflake](https://github.com/diegovillatoromx/airflow-snowflake-pipeline/blob/main/schema-snowflake.png)

### Table Structure

We structure our data in Snowflake using the following attributes:

| Attribute          | Description                                                                |
|--------------------|----------------------------------------------------------------------------|
| USER_ID            | Unique identifier of the user.                                             |
| INITIAL_EVENT      | First event performed by the user.                                         |
| EVENT_2            | Second event performed by the user.                                        |
| EVENT_3            | Third event performed by the user.                                         |
| EVENT_OUT          | Final event performed by the user.                                          |
| OS_USER            | Operating system used by the user.                                         |
| CITY               | City of the user.                                                          |
| LATITUDE           | Latitude of the user's location.                                            |
| LONGITUDE          | Longitude of the user's location.                                           |
| ORDER_TYPE         | Type of order made by the user.                                             |
| STATUS             | Status of the order made by the user.                                       |
| PAYMENT_METHOD     | Payment method used by the user.                                            |
| CREATED_AT         | Date and time of the record creation.                                       |
| HOURLY_PURCHASE_COUNT | Number of purchases made by the user in the last hour.                    |
| DAILY_PURCHASE_COUNT  | Number of purchases made by the user in the current day.                  |

### Sample Item Attributes

```json
{
    "USER_ID": "12345",
    "INITIAL_EVENT": "login",
    "EVENT_2": "search",
    "EVENT_3": "view",
    "EVENT_OUT": "logout",
    "OS_USER": "iOS",
    "CITY": "New York",
    "LATITUDE": 40.7128,
    "LONGITUDE": -74.0060,
    "ORDER_TYPE": "online",
    "STATUS": "completed",
    "PAYMENT_METHOD": "credit_card",
    "CREATED_AT": "2022-02-20T12:00:00",
    "HOURLY_PURCHASE_COUNT": 3,
    "DAILY_PURCHASE_COUNT": 10
}
```

Snowflake will provide us with a powerful, scalable platform to build and execute our ETL pipeline, enabling us to efficiently manage the data generated by our mobile application and derive meaningful insights for business decision-making.

### Step 1: Create Snowflake Warehouse, Database, Schema, and Role

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

### Step 2: Define Snowflake Tables
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

## Contribution

We would love to receive contributions from the community to improve and expand our Passport Photo Validation project! If you have ideas, suggestions for improvements, or would like to collaborate on development, please let us know! You can contribute in various ways, including:

- Reporting issues or bugs you encounter.
- Proposing new features or enhancements.
- Submitting pull requests with code to address issues or implement new features.

We look forward to working with you to grow this project and make it even better!

## Contact

If you have any questions, comments, or simply want to get in touch with us, please feel free to do so. You can find us on the following platforms:

- **GitHub:** [Link to Repository]([https://github.com/diegovillatoromx/passport-facial-analysis-automation/edit/main/README.md])
- **Email:** diegovillatoromx@gmail.com
- **Twitter:** [@diegovillatomx](https://twitter.com/diegovillatomx)
- **LinkedIn:** [DiegoVillatoromx](https://www.linkedin.com/in/diegovillatoromx)

We look forward to hearing from you soon!




