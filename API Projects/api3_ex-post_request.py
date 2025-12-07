import requests

url = "https://httpbin.org/post"
data = {"username": "John", "password": "1234"}

response = requests.post(url, json=data)
print(response.json())
