#Import base libraries and try a connection to database
from utils.db import *
from utils.data_transformation import *
from utils.request import *
from utils import urls
import logging
import time

#Docker URL
database_url = urls.DATABASE_URL
# External API URLS
transport_unit_url = urls.TRANSPORT_UNIT_URL
mayoralty_url = urls.MAYORALTY_URL
# Try to create the session
connected = False
attempts = 1

while not connected:
    try:
        session = database_creation(database_url)
        connected = True
        print("Connected Successfully")
    except:        
        time.sleep(10)
        print("Attemtp {}, failed. Trying to connect".format(attempts))
        print(attempts)
        attempts += 1


def run_etl():
    #Request logic, request, transform and load information from the alcaldias endpoint to store in the database as geom data
    mayoralties = request_api(mayoralty_url)
    #Validate if there are records in the response
    if mayoralties['result']['records'] != {}:
        #Retrieve only the result 
        records = mayoralties['result']['records']
        process_normal_records(session, records)
    else:
        print('Failed to persist into the database')

    #Request logic, request, transform and load information from the metrobus endpoint to store in the database as geom data
    transport_units = request_api(transport_unit_url)
    # Validate that the response is not empty
    if transport_units['result']['records'] != {}:
        #Retrieve only the records
        records = transport_units['result']['records']
        #Iterate the parsed response
        process_geom_records(session, records, 'POINT')
    else:
        print('Failed to persist into the database')

if connected:
    run_etl()