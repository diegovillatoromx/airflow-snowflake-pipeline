import boto3

# Create an instance of the Airflow client 
client = boto3.client('mwaa', region_name='us-east-1')  # Replace 'us-east-1' with your preferred region

# Define Apache Airflow environment configuration 
environment = { 
    'Name': 'my-airflow-environment',  # Change this to your desired name
    'ExecutionRoleArn': 'arn:aws:iam::123456789012:role/service-role/my-mwaa-role',  # Change this to your execution role ARN
    'DagS3Path': 's3://my-dag-bucket',  # Change this to the location of your S3 DAG bucket
    'NetworkConfiguration': {
        'SecurityGroupIds': ['sg-0123456789abcdef0'],  # Change this to your network security groups
        'SubnetIds': ['subnet-0123456789abcdef0'],  # Change this to your VPC subnets
    },
    'SourceBucketArn': 'arn:aws:s3:::my-source-bucket',  # Change this to your source S3 bucket ARN
}

# Create the Apache Airflow environment
response = client.create_environment(
    Name=environment['Name'],
    ExecutionRoleArn=environment['ExecutionRoleArn'],
    DagS3Path=environment['DagS3Path'],
    NetworkConfiguration=environment['NetworkConfiguration'],
    SourceBucketArn=environment['SourceBucketArn']
)

# Print the response
print(response)
