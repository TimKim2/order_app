import requests
import json

URL = 'http://127.0.0.1:8000/api/store?store_key=1'

req = requests.get(URL)

print(req.text)

