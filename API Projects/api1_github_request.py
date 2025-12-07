import requests

response = requests.get("https://api.github.com")

print("Status: ", response.status_code) # 200 = OK
print("Data: ", response.json())        # Parses JSON into a Python Dict