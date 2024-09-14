import os
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime, timezone, timedelta
from square.client import Client
from square.exceptions import api_exception
from square.http.auth.o_auth_2 import BearerAuthCredentials

# Replace with your actual access token
load_dotenv()
access_token = os.getenv('SQUARE_ACCESS_TOKEN')
print(access_token)
start_date = "2024-06-10T00:00:00Z"  # ISO 8601 format
# Get the current date and time
current_time = datetime.utcnow()
# Add 8 hours to the current time
time_plus_8_hours = current_time + timedelta(hours=8)
# Format to ISO 8601 without milliseconds and with 'Z' to indicate UTC
end_date = time_plus_8_hours.strftime('%Y-%m-%dT%H:%M:%SZ')
location_id = 'LW9P0YPD8SSXY'

def convert_datetime(value):
    # Convert to datetime object
    dt = pd.to_datetime(value)
    
    # Convert to desired timezone (optional)
    dt = dt.tz_convert('Australia/Perth')  # Example: converting to New York timezone
    
    # Remove timezone info if you want a naive datetime
    return dt.tz_localize(None)

client = Client(
    bearer_auth_credentials=BearerAuthCredentials(
       access_token=access_token
    ),
    environment='production'  # Use 'production' for live environment
)
orders_api = client.orders

def fetch_order(order_id):
    try:
        result = orders_api.retrieve_order(order_id)
        if result.is_success():
            order = result.body['order']
            line_items = order.get('line_items', [])
            for line_item in line_items:
                line_item['order_id'] = order_id
            return line_items
        elif result.is_error():
            print(f"Error retrieving order {order_id}: {result.errors}")

    except api_exception as e:
        print(f"Failed to retrieve order {order_id}: {e.message}")

# response = client.transactions.list_transactions(location_id = 'LW9P0YPD8SSXY')
def get_all_payments(location_id):
    payments = []
    cursor = None

    while True:
        try:
            # List payments with optional cursor for pagination
            response = client.payments.list_payments(
                location_id=location_id,
                cursor=cursor  # Pagination cursor
            )

            if response.is_success():
                payments.extend(response.body['payments'])
                cursor = response.body.get('cursor', None)

                if not cursor:
                    break  # Exit loop if there are no more pages

            else:
                print(f"Failed to retrieve payments: {response.errors}")
                break

        except api_exception as e:
            print(f"API Exception occurred: {str(e)}")
            break

    return payments

# Retrieve all payments

def main():
    payments = get_all_payments(location_id)
    payments_df = pd.DataFrame(payments)
    payments_df = payments_df[['id','created_at','order_id']]
    payments_df['datetime'] = payments_df['created_at'].apply(convert_datetime)
    payments_df.drop(columns=['created_at'],inplace=True)
    orders = []
    for payment in payments:
        # breakpoint()
        temp_order = fetch_order(payment.get('order_id'))
        if temp_order:
            orders.extend(temp_order)
    orders_df = pd.DataFrame(orders)
    orders_df['base']=orders_df['base_price_money'].apply(lambda x: x['amount']/100)
    orders_df['total']=orders_df['total_money'].apply(lambda x: x['amount']/100)
    orders_df['type']='Physical'
    orders_df = orders_df[['order_id','name','variation_name','quantity','base','total','type']]
    # payments_df['amount_money']=payments_df['amount_money'].apply(lambda x: x['amount']/100)
    all_orders_df = pd.merge(payments_df,orders_df,on='order_id',how='left')
    all_orders_df.drop(columns=['order_id','id'])
    all_orders_df.to_csv('ProcessedData/square_payments.csv',index=False)

if __name__ == '__main__':
    main(False)
