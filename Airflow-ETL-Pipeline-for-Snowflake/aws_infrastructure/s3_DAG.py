import boto3

# Set your AWS credentials (you can also use environment variables or IAM roles)
aws_access_key_id = 'YOUR_ACCESS_KEY_ID' 
aws_secret_access_key = 'YOUR_SECRET_ACCESS_KEY'

# Specify the S3 bucket name and region
bucket_name = 'your-dag-bucket-name'
region_name = 'us-east-1'  # Change to your desired region

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

# Create an S3 bucket
try:
    s3.create_bucket(Bucket=bucket_name)
    print(f'S3 bucket "{bucket_name}" created successfully in region "{region_name}".')
except Exception as e:
    print(f'An error occurred while creating the S3 bucket: {e}')

