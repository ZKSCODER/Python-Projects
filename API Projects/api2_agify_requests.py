import requests

url = "https://api.agify.io"
params = {"name": "Alexander"}

response = requests.get(url, params=params)
print("Status: ", response.status_code) # 200 = OK

headers = response.headers

print("Data: ", headers.get("x-rate-limit-limit")) 
print("Data: ", headers.get("x-rate-limit-remaining"))        # Parses JSON into a Python Dict