-- Create a Snowflake warehouse
CREATE OR REPLACE WAREHOUSE your_warehouse_name
WAREHOUSE_SIZE = 'X-SMALL'  -- Choose the desired size
AUTO_SUSPEND = 1800  -- Set the auto-suspend time (in seconds)
AUTO_RESUME = TRUE;  -- Enable auto-resume;

-- Create a database
CREATE OR REPLACE DATABASE your_database_name;

-- Create a schema within the database
CREATE OR REPLACE SCHEMA your_schema_name;

-- Create a role
CREATE OR REPLACE ROLE your_role_name;
