-- Create a stage using the IAM role
CREATE OR REPLACE STAGE your_stage_name
URL = 's3://your_s3_bucket/'
CREDENTIALS = (
  AWS_ROLE = 'arn:aws:iam::your_aws_account_id:role/SnowflakeAccessRole'
); 

GRANT READ ON STAGE your_stage_name TO ROLE SnowflakeAccessRole;
