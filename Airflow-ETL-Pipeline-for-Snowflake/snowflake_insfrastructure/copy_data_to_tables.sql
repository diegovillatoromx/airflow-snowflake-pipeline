-- Copy data from Parquet files in S3 to 'users' table
COPY INTO your_schema_name.users
  FROM @your_snowflake_stage 
  FILE_FORMAT = (TYPE = 'PARQUET')
  PATTERN = 'users/*.parquet'
  ON_ERROR = 'CONTINUE';

-- Copy data from Parquet files in S3 to 'events' table
COPY INTO your_schema_name.events
  FROM @your_snowflake_stage
  FILE_FORMAT = (TYPE = 'PARQUET')
  PATTERN = 'events/*.parquet'
  ON_ERROR = 'CONTINUE';

-- Copy data from Parquet files in S3 to 'orders' table
COPY INTO your_schema_name.orders
  FROM @your_snowflake_stage
  FILE_FORMAT = (TYPE = 'PARQUET')
  PATTERN = 'orders/*.parquet'
  ON_ERROR = 'CONTINUE';

-- Copy data from Parquet files in S3 to 'purchase_counts' table
COPY INTO your_schema_name.purchase_counts
  FROM @your_snowflake_stage
  FILE_FORMAT = (TYPE = 'PARQUET')
  PATTERN = 'purchase_counts/*.parquet'
  ON_ERROR = 'CONTINUE';
