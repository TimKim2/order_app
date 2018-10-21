import requests

URL = 'http://ec2-18-224-138-249.us-east-2.compute.amazonaws.com:8080/api/store?store_key=2'

req = requests.get(URL)

print(req.text)

