import boto3

# Create a new AWS IAM client
iam_client = boto3.client('iam')

# Define the IAM role name
role_name = 'SnowflakeAccessRole'

# Define the trust policy for Snowflake (assuming you have a Snowflake account)
trust_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "redshift.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}

# Create the IAM role
try:
    create_role_response = iam_client.create_role(
        RoleName=role_name,
        AssumeRolePolicyDocument=json.dumps(trust_policy)
    )

    # Attach the necessary policies to the role (e.g., AmazonS3ReadOnlyAccess)
    iam_client.attach_role_policy(
        RoleName=role_name,
        PolicyArn='arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess'
    )

    print(f'IAM Role "{role_name}" created and policies attached successfully.')

except Exception as e:
    print(f"Error creating IAM role: {str(e)}")
