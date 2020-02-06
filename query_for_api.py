import requests
import json

request_api = requests.get('https://reqres.in/api/users')
result = request_api.json()

for user in result['data']:
    print(user['email'])
