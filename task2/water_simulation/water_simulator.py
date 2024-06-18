import json
import os
import random
import sys
import time
from datetime import datetime, timedelta, timezone

import requests




response = requests.request(
    "GET",
    f"http://localhost:1026/ngsi-ld/v1/entities/urn:ngsi-ld:WaterQualityObserved:1",
)
WaterObservedExists = response.status_code == 200

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
            "description": "Save historical water data",
            "type": "Subscription",
            "entities": [{"type": "WaterQualityObserved"}],
            "watchedAttributes": [
                "pH",
                "temperature",
                "flow",
                "alkalinity",
                "TKN",
                "NO2",
                "N-TOT",
                "P-TOT",
                "P-PO4",
                "Al",
                "As",
                "B",
                "Ba",
                "Cd",
                "Cr",
                "Cr-III",
                "Cr-VI",
                "Cu",
                "Fe",
                "fluoride",
                "Hg",
                "THC",
                "Ni",
                "TO",
                "Pb",
                "Se",
                "Sn",
                "sulphate",
                "sulphite",
                "anionic-surfactants",
                "cationic-surfactants",
                "non-ionic-surfactants",
                "total-surfactants",
                "Zn",
            ],
            "notification": {
                "attributes": [
                    "pH",
                    "temperature",
                    "flow",
                    "alkalinity",
                    "TKN",
                    "NO2",
                    "N-TOT",
                    "P-TOT",
                    "P-PO4",
                    "Al",
                    "As",
                    "B",
                    "Ba",
                    "Cd",
                    "Cr",
                    "Cr-III",
                    "Cr-VI",
                    "Cu",
                    "Fe",
                    "fluoride",
                    "Hg",
                    "THC",
                    "Ni",
                    "TO",
                    "Pb",
                    "Se",
                    "Sn",
                    "sulphate",
                    "sulphite",
                    "anionic-surfactants",
                    "cationic-surfactants",
                    "non-ionic-surfactants",
                    "total-surfactants",
                    "Zn",
                ],
                "format": "normalized",
                "endpoint": {
                    "uri": "http://quantumleap:8668/v2/notify",
                    "accept": "application/json",
                    "receiverInfo": [
                        {"key": "fiware-service", "value": "water_simulation"},
                        {"key": "fiware-servicepath", "value": "/water_simulation"},
                    ],
                },
            },
            "@context": [
                "https://raw.githubusercontent.com/smart-data-models/dataModel.WaterQuality/master/context.jsonld"
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

current_time = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
waterObserved = {
    "id": "urn:ngsi-ld:WaterQualityObserved:1",
    "type": "WaterQualityObserved",
    "dateObserved": {
        "type": "Property",
        "value": {"type": "DateTime", "value": current_time},
    },
    "location": {
        "type": "GeoProperty",
        "value": {"type": "Point", "coordinates": [10.185684, 54.327577]},
    },
    "pH": {"type": "Property", "value": round(random.uniform(6.5, 8.5), 4)},
    "temperature": {
        "type": "Property",
        "value": round(random.uniform(20.0, 30.0), 4),
    },
    "flow": {"type": "Property", "value": round(random.uniform(100.0, 200.0), 4)},
    "alkalinity": {
        "type": "Property",
        "value": round(random.uniform(0.05, 0.15), 4),
    },
    "TKN": {"type": "Property", "value": round(random.uniform(0.5, 1.5), 4)},
    "NO2": {"type": "Property", "value": round(random.uniform(0.05, 0.15), 4)},
    "N-TOT": {"type": "Property", "value": round(random.uniform(4.0, 8.0), 4)},
    "P-TOT": {"type": "Property", "value": round(random.uniform(0.4, 0.8), 4)},
    "P-PO4": {"type": "Property", "value": round(random.uniform(0.3, 0.7), 4)},
    "Al": {"type": "Property", "value": round(random.uniform(0.005, 0.015), 5)},
    "As": {"type": "Property", "value": round(random.uniform(0.0, 0.001), 5)},
    "B": {"type": "Property", "value": round(random.uniform(0.1, 0.3), 4)},
    "Ba": {"type": "Property", "value": round(random.uniform(0.0, 0.001), 5)},
    "Cd": {"type": "Property", "value": round(random.uniform(0.0, 0.005), 5)},
    "Cr": {"type": "Property", "value": round(random.uniform(0.0, 0.001), 5)},
    "Cr-III": {"type": "Property", "value": round(random.uniform(0.0, 0.001), 5)},
    "Cr-VI": {"type": "Property", "value": round(random.uniform(0.0, 0.001), 5)},
    "Cu": {"type": "Property", "value": round(random.uniform(0.0, 0.001), 5)},
    "Fe": {"type": "Property", "value": round(random.uniform(6.0, 8.0), 4)},
    "fluoride": {"type": "Property", "value": round(random.uniform(0.0, 0.001), 5)},
    "Hg": {"type": "Property", "value": round(random.uniform(0.0, 0.001), 5)},
    "THC": {"type": "Property", "value": round(random.uniform(0.0, 0.001), 5)},
    "Ni": {"type": "Property", "value": round(random.uniform(0.0, 0.001), 5)},
    "TO": {"type": "Property", "value": round(random.uniform(0.005, 0.015), 5)},
    "Pb": {"type": "Property", "value": round(random.uniform(0.0, 0.001), 5)},
    "Se": {"type": "Property", "value": round(random.uniform(0.0, 0.001), 5)},
    "Sn": {"type": "Property", "value": round(random.uniform(0.0, 0.001), 5)},
    "sulphate": {
        "type": "Property",
        "value": round(random.uniform(100.0, 200.0), 4),
    },
    "sulphite": {"type": "Property", "value": round(random.uniform(0.0, 0.001), 5)},
    "anionic-surfactants": {
        "type": "Property",
        "value": round(random.uniform(0.1, 0.3), 4),
    },
    "cationic-surfactants": {
        "type": "Property",
        "value": round(random.uniform(0.1, 0.3), 4),
    },
    "non-ionic-surfactants": {
        "type": "Property",
        "value": round(random.uniform(0.05, 0.15), 4),
    },
    "total-surfactants": {
        "type": "Property",
        "value": round(random.uniform(0.1, 0.3), 4),
    },
    "Zn": {"type": "Property", "value": round(random.uniform(0.0, 0.001), 5)},
    "@context": [
        "https://raw.githubusercontent.com/smart-data-models/dataModel.WaterQuality/master/context.jsonld"
    ],
}

while True:
    current_time = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    waterObserved["dateObserved"]["value"]["value"] = current_time
    for key in waterObserved.keys():
        if key not in [
            "id",
            "type",
            "@context",
            "location",
            "dateObserved",
            "coordinates",
        ]:
            original_value = waterObserved[key]["value"]
            fraction = random.uniform(-0.1, 0.1)
            noise = random.uniform(-0.01, 0.01)
            new_value = original_value + (original_value * fraction) + noise

            if key in ["pH"]:
                new_value = max(6.0, min(9.0, new_value))
            elif key in ["temperature"]:
                new_value = max(0.0, min(40.0, new_value))
            elif key in ["flow"]:
                new_value = max(0.0, min(500.0, new_value))
            elif key in ["alkalinity"]:
                new_value = max(0.0, min(1.0, new_value))
            elif key in ["TKN", "NO2"]:
                new_value = max(0.0, min(2.0, new_value))
            elif key in ["N-TOT"]:
                new_value = max(0.0, min(10.0, new_value))
            elif key in ["P-TOT", "P-PO4"]:
                new_value = max(0.0, min(1.0, new_value))
            elif key in [
                "Al",
                "As",
                "Ba",
                "Cd",
                "Cr",
                "Cr-III",
                "Cr-VI",
                "Cu",
                "fluoride",
                "Hg",
                "THC",
                "Ni",
                "Pb",
                "Se",
                "Sn",
                "sulphite",
                "Zn",
            ]:
                new_value = max(0.0, min(0.01, new_value))
            elif key in ["Fe"]:
                new_value = max(0.0, min(10.0, new_value))
            elif key in ["sulphate"]:
                new_value = max(0.0, min(300.0, new_value))
            elif key in [
                "anionic-surfactants",
                "cationic-surfactants",
                "non-ionic-surfactants",
                "total-surfactants",
            ]:
                new_value = max(0.0, min(1.0, new_value))

            waterObserved[key]["value"] = round(new_value, 2)

    if WaterObservedExists:
        if "id" in waterObserved:
            del waterObserved["id"]
        if "type" in waterObserved:
            del waterObserved["type"]
        response = requests.request(
            "PATCH",
            f"http://localhost:1026/ngsi-ld/v1/entities/urn:ngsi-ld:WaterQualityObserved:1/attrs",
            headers={"Content-Type": "application/ld+json"},
            data=json.dumps(waterObserved),
        )
        if response.status_code != 204:
            print(response.status_code, file=sys.stderr)
            print(response.text, file=sys.stderr)
    else:
        response = requests.request(
            "POST",
            f"http://localhost:1026/ngsi-ld/v1/entities",
            json=waterObserved,
            headers={"Content-Type": "application/ld+json"},
        )
        WaterObservedExists = True
        if response.status_code != 201:
            print(response.status_code, file=sys.stderr)
            print(response.text, file=sys.stderr)

    print(f"{current_time}:", end=" ")
    keys = list(waterObserved.keys())
    for key in keys:
        if (
            key != "id"
            and key != "type"
            and key != "@context"
            and key != "location"
            and key != "dateObserved"
            and key != "coordinates"
        ):
            print(f"{key}: {waterObserved[key]['value']}", end=", ")
    print("", flush=True)

    time.sleep(5)
