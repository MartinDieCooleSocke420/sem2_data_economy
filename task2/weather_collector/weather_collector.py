import requests
import json
import time
import random

url = 'http://context_broker:1026/ngsi-ld/v1/entities/'  # Use service name instead of localhost

headers = {
    'Content-Type': 'application/json',
    'Link': '<https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"'
}

water_measurement = {
    "id": "urn:ngsi-ld:WaterMeasurement:001",
    "type": "WaterMeasurement",
    "temperature": {
        "type": "Property",
        "value": 0.0
    },
    "pH": {
        "type": "Property",
        "value": 7.0
    },
    "location": {
        "type": "GeoProperty",
        "value": {
            "type": "Point",
            "coordinates": [8.6842, 50.1127]
        }
    }
}

def generate_random_data():
    water_measurement['temperature']['value'] = round(random.uniform(10, 25), 2)
    water_measurement['pH']['value'] = round(random.uniform(6.5, 8.5), 2)
    try:
        response = requests.post(url, data=json.dumps(water_measurement), headers=headers)
        print(response.status_code, response.text)
    except Exception as e:
        print(f"Error connecting to {url}: {e}")

def simulate_water_measurements():
    while True:
        generate_random_data()
        time.sleep(5)

if __name__ == "__main__":
    simulate_water_measurements()
