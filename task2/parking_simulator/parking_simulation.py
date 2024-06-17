import requests
import json
import time

url = 'http://context_broker:1026/ngsi-ld/v1/entities/'

headers = {
    'Content-Type': 'application/json',
    'Link': '<https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"'
}

parking_spots = {
    "id": "urn:ngsi-ld:ParkingSpot:001",
    "type": "ParkingSpot",
    "status": {
        "type": "Property",
        "value": "free"
    },
    "location": {
        "type": "GeoProperty",
        "value": {
            "type": "Point",
            "coordinates": [8.6842, 50.1127]
        }
    }
}

def simulate_parking():
    while True:
        parking_spots['status']['value'] = 'free' if parking_spots['status']['value'] == 'occupied' else 'occupied'
        try:
            response = requests.post(url, data=json.dumps(parking_spots), headers=headers)
            print(response.status_code, response.text)
        except Exception as e:
            print(f"Error connecting to {url}: {e}")
        time.sleep(5)

if __name__ == "__main__":
    simulate_parking()
