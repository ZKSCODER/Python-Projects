import requests
import os
from dotenv import load_dotenv

load_dotenv()

city = input("Enter city name: ")
api_key = os.getenv("MY_API_KEY") # Replace with your actual API key. You can remove "os.getenv" if code is not in a online 

def get_weather(city: str):
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    
    return response.json()

location_data = get_weather(city)

print(f"City = {city}")
print(f"Temperature = {location_data["main"]["temp"]}°F")
    
