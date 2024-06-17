import requests
import json

url = 'http://localhost:1026/ngsi-ld/v1/subscriptions/'

subscription = {
    "id": "urn:ngsi-ld:Subscription:001",
    "type": "Subscription",
    "entities": [{"type": "WaterMeasurement"}],
    "watchedAttributes": ["temperature", "pH"],
    "notification": {
        "endpoint": {
            "uri": "http://quantumleap:8668/v2/notify",
            "accept": "application/json"
        }
    }
}

response = requests.post(url, data=json.dumps(subscription), headers={'Content-Type': 'application/json'})
print(response.status_code, response.text)
