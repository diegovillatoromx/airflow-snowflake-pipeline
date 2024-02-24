-- Create a Snowflake schema for the 'purchase' data structure

-- Create a schema
CREATE OR REPLACE SCHEMA your_schema_name;
 
-- Create a 'users' table
CREATE OR REPLACE TABLE your_schema_name.users (
    USER_ID STRING PRIMARY KEY,
    OS_USER STRING,
    CITY STRING,
    LATITUDE FLOAT,
    LONGITUDE FLOAT
);

-- Create an 'events' table
CREATE OR REPLACE TABLE your_schema_name.events (
    EVENT_ID STRING PRIMARY KEY,
    USER_ID STRING,
    EVENT_NAME STRING,
    EVENT_TIMESTAMP TIMESTAMP_NTZ
);

-- Create an 'orders' table
CREATE OR REPLACE TABLE your_schema_name.orders (
    ORDER_ID STRING PRIMARY KEY,
    USER_ID STRING,
    ORDER_TYPE STRING,
    STATUS STRING,
    PAYMENT_METHOD STRING,
    CREATED_AT TIMESTAMP_NTZ
);

-- Create an 'purchase_counts' table
CREATE OR REPLACE TABLE your_schema_name.purchase_counts (
    USER_ID STRING,
    HOUR INTEGER,
    DAILY INTEGER,
    HOURLY_PURCHASE_COUNT INTEGER,
    DAILY_PURCHASE_COUNT INTEGER,
    FOREIGN KEY (USER_ID) REFERENCES your_schema_name.users(USER_ID)
);
