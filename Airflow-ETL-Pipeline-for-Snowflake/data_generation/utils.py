import pandas as pd
import random
import hashlib
from datetime import datetime
import json 
import boto3

# Load configuration from config.json
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Configuration variables
cities = config["cities"]
payment_online = config["payment_online"]
os = config["os"]
final_user_event = config["final_user_event"]
phone_models = config["phone_models"]
purchase_statuses = config["purchase_statuses"]
initial_event = config["initial_event"]
second_event = config["second_event"]
third_event = config["third_event"]
event_category = config["event_category"]
city_coords = config["city_coords"]

# Variables de configuración para Kinesis
stream_name = config["stream_name"]
region = config["region"]
KinesisClient = boto3.client('kinesis', region_name=region)

# Create a list of users beforehand
def create_massive_users(n_users):
    users_bank = []

    for i in range(n_users):
        date = pd.to_datetime('today').strftime("%Y-%m-%d %H:%M:%S")
        users_bank.append(str(hashlib.sha256(f"{i} {date}".encode('utf-8')).hexdigest())[:10])

    return users_bank

# Function to get the second event based on random choices
def get_second_event():
    event_2 = random.choice(second_event)
    if event_2 == 'HOME':
        event_3 = random.choice(third_event)
        if event_3 == 'GO_TO_CATEGORY':
            last_event = random.choice(event_category)
            final_event = random.choice(final_user_event)
            if final_event == 'PURCHASE':
                payment = random.choice(payment_online)
                os_source = random.choice(os)
                city = random.choice(cities)
                status = 'COMPLETED'
                order_type = 'PURCHASE'
            elif final_event == 'EXIT_APP':
                payment = 'Null'
                os_source = random.choice(os)
                city = random.choice(cities)
                status = 'UNCONVERTED'
                order_type = 'USER_VISIT'
        elif event_3 == 'EXIT_APP':
            payment = 'Null'
            os_source = random.choice(os)
            city = random.choice(cities)
            status = 'UNCONVERTED'
            order_type = 'USER_VISIT'
            last_event = 'HOME'
    else:
        payment = 'Null'
        os_source = random.choice(os)
        city = random.choice(cities)
        status = 'UNCONVERTED'
        order_type = 'USER_VISIT'
        last_event = 'LAUNCH_APP'
        event_3 = 'Null'
    return initial_event, event_2, event_3, last_event, os_source, city, order_type, status, payment

# Function to get coordinates of a city
def get_coords(city):
    return city_coords.get(city, [0.0, 0.0])

# Function to generate simulated data
def generate_simulated_data(num_records, num_users):
    # Create a list of random users
    user_list = create_massive_users(num_users)

    user_purchase_count = {}
    data_purchase = []
    x = 0

    while x < num_records:
        date = pd.to_datetime('today').strftime("%Y-%m-%d %H:%M:%S")
        event = get_second_event()
        user_id = random.choice(user_list)
        event_user_1 = event[0]
        event_user_2 = event[1]
        event_user_3 = event[2]
        event_user_4 = event[3]
        event_user_os = event[4]
        event_user_city = event[5]
        event_user_order = event[6]
        event_user_status = event[7]
        event_user_payment = event[8]

        current_hour = datetime.now().hour
        current_day = datetime.now().day

        if user_id not in user_purchase_count:
            user_purchase_count[user_id] = {'hourly_count': {current_hour: 1}, 'daily_count': {current_day: 1}}
        else:
            if current_hour in user_purchase_count[user_id]['hourly_count']:
                user_purchase_count[user_id]['hourly_count'][current_hour] += 1
            else:
                user_purchase_count[user_id]['hourly_count'][current_hour] = 1

            if current_day in user_purchase_count[user_id]['daily_count']:
                user_purchase_count[user_id]['daily_count'][current_day] += 1
            else:
                user_purchase_count[user_id]['daily_count'][current_day] = 1

        purchase = {
            'USER_ID': user_id,
            'INITIAL_EVENT': event_user_1,
            'EVENT_2': event_user_2,
            'EVENT_3': event_user_3,
            'EVENT_OUT': event_user_4,
            'OS_USER': event_user_os,
            'CITY': event_user_city,
            'LATITUDE': get_coords(event_user_city)[0],
            'LONGITUDE': get_coords(event_user_city)[1],
            'ORDER_TYPE': event_user_order,
            'STATUS': event_user_status,
            'PAYMENT_METHOD': event_user_payment,
            'CREATED_AT': date,
            'HOURLY_PURCHASE_COUNT': user_purchase_count[user_id]['hourly_count'].get(current_hour, 0),
            'DAILY_PURCHASE_COUNT': user_purchase_count[user_id]['daily_count'].get(current_day, 0)
        }

        # Envío de datos a AWS Kinesis
        record_value = json.dumps(purchase)
        response = KinesisClient.put_record(StreamName=stream_name, Data=record_value, PartitionKey=user_id)
        print("Total data ingested: {}, ReqID: {}, HTTPStatusCode: {}".format(x, response['ResponseMetadata']['RequestId'], response['ResponseMetadata']['HTTPStatusCode']))
        x += 1
        time.sleep(random.choice([1, 1.5, 2]))

    return pd.concat(data_purchase, ignore_index=True)

