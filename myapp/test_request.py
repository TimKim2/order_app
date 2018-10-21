import requests
from pprint import pprint

URL = 'http://127.0.0.1:8000/api/store/'

menu_json = []
'''
list_menu = [
        {"name": "참치마요네즈", "price": "3000", "??": "맛있다."},
        {"name": "치즈밥버거", "price": "4000", "??": "맛없다."},
]

send_data = {
    "key_number": "1",
    "name": "봉구스밥버거",
    "description": "밥버거집",
    "menu": str(list_menu)
}

'''


send_data = {
    "store_key": "1",
    "product_name": "커피라떼",
}

pprint(send_data)

req = requests.post(URL, send_data)

print(req.status_code, req.reason)