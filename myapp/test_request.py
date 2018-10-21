import requests
from pprint import pprint

URL = 'http://ec2-18-224-138-249.us-east-2.compute.amazonaws.com:8080/api/store/'

menu_json = []

send_data = {
    "store_key": "2",
    "product_name": "카푸치노",
}

pprint(send_data)

req = requests.post(URL, send_data)

print(req.status_code, req.reason)