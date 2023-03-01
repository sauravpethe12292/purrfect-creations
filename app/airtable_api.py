from pyairtable import Table
from django.conf import settings
from decouple import config

API_KEY = 'keyYgaCznKMcBq0qy'
BASE_ID = 'app8wLQrrIMrnn673'
TABLE_NAME = 'tblZBNaHCGVfA9xw1'

def get_orders():
    airtable = Table(config("API_KEY"), config("BASE_ID"), config("TABLE_NAME"))
    airtable= Table(API_KEY, BASE_ID, TABLE_NAME)
    orders = []
    records = airtable.all() #has a 1000 rows so getting them all at once
    for record in records:
        order = {
            'order_id': record['fields']['order_id'],
            'order_placed': record['fields']['order_placed'],
            'product_name': record['fields']['product_name'],
            'price': record['fields']['price'],
            'first_name': record['fields']['first_name'],
            'last_name': record['fields']['last_name'],
            'address': record['fields']['address'],
            'email': record['fields']['email'],
            'order_status': record['fields']['order_status']
        }
        orders.append(order)

    return orders

# todo make dashboard more beautiful add more panels and have pagination enabled somehow?
# add readme

