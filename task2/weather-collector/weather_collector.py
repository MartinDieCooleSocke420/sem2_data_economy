import os
import requests
import json
import time

# Configuration
ORION_URL = "http://orion:1026/v2/entities"
API_KEY = "5ffdb0ee1227cfcae4c747025b6e73b6"
CITY_ID = "2891122"  # Use OpenWeatherMap city ID
UNIT = "metric"  # Use "metric" for Celsius

def fetch_weather_data():
    url = f"http://api.openweathermap.org/data/2.5/weather?id={CITY_ID}&appid={API_KEY}&units={UNIT}"
    response = requests.get(url)
    data = response.json()
    return data

def send_to_orion(data):
    headers = {
        "Content-Type": "application/json",
    }
    payload = {
        "id": "WeatherData",
        "type": "Weather",
        "temperature": {
            "value": data["main"]["temp"],
            "type": "Number"
        },
        "humidity": {
            "value": data["main"]["humidity"],
            "type": "Number"
        }
    }
    response = requests.post(ORION_URL, headers=headers, data=json.dumps(payload))
    print(response.text)

def main():
    while True:
        weather_data = fetch_weather_data()
        send_to_orion(weather_data)
        time.sleep(300)  # Sleep for 5 minutes (300 seconds)

if __name__ == "__main__":
    main()
