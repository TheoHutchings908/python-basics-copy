import requests
import json

response = requests.get('https://jsonplaceholder.typicode.com/posts/11')

print(type(response.text))

response_json = json.loads(response.text)

print(response_json)

for key, value in response_json.items():
    print(f'key: {key}, value: {value}')

print(response.headers.get('content-type'))
