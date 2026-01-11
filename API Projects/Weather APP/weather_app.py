import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather(city: str):
            base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={unit_type}"
            response = requests.get(base_url)
            
            return response.json()
api_key = os.getenv("MY_API_KEY") # Replace with your actual API key. You can remove "os.getenv" if code is not in a online repository

while True:
    try:
        city1 = input("Enter city name: ")
        city = city1.lower()

        if city == "exit":
            break
        if not city:
             print("Please enter a valid city name")
             continue
        
        else:
            unit_type = input("Enter a unit type (metric, imperial): ")
            location_data = get_weather(city)
            print(f"City = {city1}")
            if unit_type == "imperial":
                print(f"Temperature = {location_data["main"]["temp"]}°F")
            else:
                print(f"Temperature = {location_data["main"]["temp"]}°C")

    except KeyError:
        print("City not found. Please try again")
        continue
    


