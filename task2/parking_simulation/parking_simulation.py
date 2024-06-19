import json
import os
import random
import time

import requests


offStreetParking = {
    "id": "urn:ngsi-ld:OffStreetParking:001",
    "type": "OffStreetParking",
    "location": {
        "type": "GeoProperty",
        "value": {"type": "Point", "coordinates": [10.18952, 54.32783]},
    },
    "address": {
        "type": "Property",
        "value": {
            "streetAddress": "Alte Eichen 6, 24113 Kiel",
            "addressLocality": "Kiel",
            "addressCountry": "Germany",
        },
    },
    "name": {
        "type": "Property",
        "value": "Parkplatz an der Schwentine",
    },
    "@context": [
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Parking/master/context.jsonld",
    ],
}


parkingSpots = [
    {
        "id": "urn:ngsi-ld:ParkingSpot:01",
        "type": "ParkingSpot",
        "location": {
            "type": "GeoProperty",
            "value": {"type": "Point", "coordinates": [10.18952, 54.32783]},
        },
        "status": {"type": "Property", "value": "free"},
        "category": {"type": "Property", "value": ["onstreet"]},
        "refParkingSite": {
            "type": "Relationship",
            "object": "urn:ngsi-ld:OffStreetParking:001",
        },
        "@context": [
            "https://raw.githubusercontent.com/smart-data-models/dataModel.Parking/master/context.jsonld",
        ],
    },
    {
        "id": "urn:ngsi-ld:ParkingSpot:02",
        "type": "ParkingSpot",
        "location": {
            "type": "GeoProperty",
            "value": {"type": "Point", "coordinates": [10.18953, 54.32784]},
        },
        "status": {"type": "Property", "value": "free"},
        "category": {"type": "Property", "value": ["onstreet"]},
        "refParkingSite": {
            "type": "Relationship",
            "object": "urn:ngsi-ld:OffStreetParking:001",
        },
        "@context": [
            "https://raw.githubusercontent.com/smart-data-models/dataModel.Parking/master/context.jsonld",
        ],
    },
    {
        "id": "urn:ngsi-ld:ParkingSpot:03",
        "type": "ParkingSpot",
        "location": {
            "type": "GeoProperty",
            "value": {"type": "Point", "coordinates": [10.18954, 54.32785]},
        },
        "status": {"type": "Property", "value": "occupied"},
        "category": {"type": "Property", "value": ["onstreet"]},
        "refParkingSite": {
            "type": "Relationship",
            "object": "urn:ngsi-ld:OffStreetParking:001",
        },
        "@context": [
            "https://raw.githubusercontent.com/smart-data-models/dataModel.Parking/master/context.jsonld",
        ],
    },
    {
        "id": "urn:ngsi-ld:ParkingSpot:04",
        "type": "ParkingSpot",
        "location": {
            "type": "GeoProperty",
            "value": {"type": "Point", "coordinates": [10.18955, 54.32786]},
        },
        "status": {"type": "Property", "value": "free"},
        "category": {"type": "Property", "value": ["onstreet"]},
        "refParkingSite": {
            "type": "Relationship",
            "object": "urn:ngsi-ld:OffStreetParking:001",
        },
        "@context": [
            "https://raw.githubusercontent.com/smart-data-models/dataModel.Parking/master/context.jsonld",
        ],
    },
    {
        "id": "urn:ngsi-ld:ParkingSpot:05",
        "type": "ParkingSpot",
        "location": {
            "type": "GeoProperty",
            "value": {"type": "Point", "coordinates": [10.18956, 54.32787]},
        },
        "status": {"type": "Property", "value": "free"},
        "category": {"type": "Property", "value": ["onstreet"]},
        "refParkingSite": {
            "type": "Relationship",
            "object": "urn:ngsi-ld:OffStreetParking:001",
        },
        "@context": [
            "https://raw.githubusercontent.com/smart-data-models/dataModel.Parking/master/context.jsonld",
        ],
    },
    {
        "id": "urn:ngsi-ld:ParkingSpot:06",
        "type": "ParkingSpot",
        "location": {
            "type": "GeoProperty",
            "value": {"type": "Point", "coordinates": [10.18957, 54.32788]},
        },
        "status": {"type": "Property", "value": "occupied"},
        "category": {"type": "Property", "value": ["onstreet"]},
        "refParkingSite": {
            "type": "Relationship",
            "object": "urn:ngsi-ld:OffStreetParking:001",
        },
        "@context": [
            "https://raw.githubusercontent.com/smart-data-models/dataModel.Parking/master/context.jsonld",
        ],
    },
    {
        "id": "urn:ngsi-ld:ParkingSpot:07",
        "type": "ParkingSpot",
        "location": {
            "type": "GeoProperty",
            "value": {"type": "Point", "coordinates": [10.18958, 54.32789]},
        },
        "status": {"type": "Property", "value": "free"},
        "category": {"type": "Property", "value": ["onstreet"]},
        "refParkingSite": {
            "type": "Relationship",
            "object": "urn:ngsi-ld:OffStreetParking:001",
        },
        "@context": [
            "https://raw.githubusercontent.com/smart-data-models/dataModel.Parking/master/context.jsonld",
        ],
    },
    {
        "id": "urn:ngsi-ld:ParkingSpot:08",
        "type": "ParkingSpot",
        "location": {
            "type": "GeoProperty",
            "value": {"type": "Point", "coordinates": [10.18959, 54.32790]},
        },
        "status": {"type": "Property", "value": "free"},
        "category": {"type": "Property", "value": ["onstreet"]},
        "refParkingSite": {
            "type": "Relationship",
            "object": "urn:ngsi-ld:OffStreetParking:001",
        },
        "@context": [
            "https://raw.githubusercontent.com/smart-data-models/dataModel.Parking/master/context.jsonld",
        ],
    },
    {
        "id": "urn:ngsi-ld:ParkingSpot:09",
        "type": "ParkingSpot",
        "location": {
            "type": "GeoProperty",
            "value": {"type": "Point", "coordinates": [10.18960, 54.32791]},
        },
        "status": {"type": "Property", "value": "occupied"},
        "category": {"type": "Property", "value": ["onstreet"]},
        "refParkingSite": {
            "type": "Relationship",
            "object": "urn:ngsi-ld:OffStreetParking:001",
        },
        "@context": [
            "https://raw.githubusercontent.com/smart-data-models/dataModel.Parking/master/context.jsonld",
        ],
    },
    {
        "id": "urn:ngsi-ld:ParkingSpot:10",
        "type": "ParkingSpot",
        "location": {
            "type": "GeoProperty",
            "value": {"type": "Point", "coordinates": [10.18961, 54.32792]},
        },
        "status": {"type": "Property", "value": "free"},
        "category": {"type": "Property", "value": ["onstreet"]},
        "refParkingSite": {
            "type": "Relationship",
            "object": "urn:ngsi-ld:OffStreetParking:001",
        },
        "@context": [
            "https://raw.githubusercontent.com/smart-data-models/dataModel.Parking/master/context.jsonld",
        ],
    },
]

file = open("subscription_location.txt", "r")
subscription_location = file.read()
file.close()
response = requests.request(
    "GET",
    f"http://localhost:1026{subscription_location}",
)

if response.status_code != 200 or len(subscription_location) <= 0:
    response = requests.request(
        "POST",
        f"http://localhost:1026/ngsi-ld/v1/subscriptions/",
        json={
            "description": "Save historical parking spot data",
            "type": "Subscription",
            "entities": [{"type": "ParkingSpot"}],
            "watchedAttributes": ["status"],
            "notification": {
                "attributes": ["status"],
                "format": "normalized",
                "endpoint": {
                    "uri": "http://quantumleap:8668/v2/notify",
                    "accept": "application/json",
                    "receiverInfo": [{"key": "fiware-service", "value": "parking"}],
                },
            },
            "@context": [
                "https://raw.githubusercontent.com/smart-data-models/dataModel.Parking/master/context.jsonld"
            ],
        },
        headers={"Content-Type": "application/ld+json"},
    )

    if response.status_code == 201:
        print("Subscription created successfully.")
        file = open("subscription_location.txt", "w")
        file.write(response.headers["Location"])
        file.close()
    else:
        print(response.status_code)
        print(response.text)
else:
    print("Subscription already exists.")


# add parking spots if they do not exist
for entity in [offStreetParking, *parkingSpots]:
    response = requests.request(
        "GET",
        f"http://localhost:1026/ngsi-ld/v1/entities/{entity['id']}",
    )

    if response.status_code == 404:
        response = requests.request(
            "POST",
            f"http://localhost:1026/ngsi-ld/v1/entities",
            json=entity,
            headers={"Content-Type": "application/ld+json"},
        )
        if response.status_code == 201:
            print(f"Added entity {entity['id']} to the context broker")
        else:
            print(response.status_code)
            print(response.text)
            print(f"Failed to add entity {entity['id']}")
    elif response.status_code == 200:
        print(f"Entity {entity['id']} already exists in the context broker")
    else:
        print(f"Failed to check if entity {entity['id']} exists in the context broker")


while True:
    parkingSpot = random.choice(parkingSpots)
    if parkingSpot["status"]["value"] == "free":
        parkingSpot["status"]["value"] = "occupied"
    else:
        parkingSpot["status"]["value"] = "free"
    response = requests.request(
        "PUT",
        f"http://localhost:1026/ngsi-ld/v1/entities/{parkingSpot['id']}/attrs/status",
        data=json.dumps(parkingSpot["status"]),
        headers={"Content-Type": "application/json"},
    )
    print(
        f"Changed status of parking spot {parkingSpot['id']} to {parkingSpot['status']['value']}"
    )
    time.sleep(1)
