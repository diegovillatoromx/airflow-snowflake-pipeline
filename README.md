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
├── data_processing/
│   ├── glue_jobs/
│   │   └── data_transformation.py    # AWS Glue script for data transformation
│   └── athena_queries/
│       └── query_definitions.sql     # SQL query definitions for Athena
├── monitoring/
│   ├── cloudwatch/
│   │   └── monitoring_config.json    # Configuration for CloudWatch monitoring
│   └── grafana/
│       └── dashboards/
│           └── sales_dashboard.json  # Grafana dashboard definition for data visualization
├── aws_services/
│   ├── sns/
│   │   └── send_sns_message.py       # Python script to send SNS messages from Lambda
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
