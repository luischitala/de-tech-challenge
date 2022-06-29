import requests
from utils.data_transformation import transform_to_json

# Function that try a request to a given url and returns a response
def request_api(url):
    response = {}
    # Try a request to the given url
    try:
        res = requests.get(url)
        response = transform_to_json(res)
    # Handle the error
    except requests.ConnectionError as e:
        print(e)
    return response