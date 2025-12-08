import requests
import os
from dotenv import load_dotenv

load_dotenv()

city = input("Enter city name: ")
api_key = os.getenv("MY_API_KEY") # Replace with your actual API key

def get_weather(city):
    base_url = f"https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"
    response = requests.get(base_url)
    return response.json()

location_data = get_weather(city)

print(location_data)
    
