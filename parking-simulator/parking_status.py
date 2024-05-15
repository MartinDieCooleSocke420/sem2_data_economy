import requests
import json
import random
import time
import os

# Define the base URL for the Orion context broker
base_url = "http://localhost:1026/v2/"

# Function to create a new entity representing a parking spot
def create_parking_spot(parking_spot_id, location):
    url = base_url + 'entities'
    headers = {'Content-Type': 'application/json'}
    payload = {
        'id': parking_spot_id,
        'type': 'ParkingSpot',
        'location': {
            'type': 'geo:json',
            'value': location
        },
        'status': {
            'type': 'Text',
            'value': 'available'
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print(f"Created parking spot with ID: {parking_spot_id}")

# Function to update the status of a parking spot
def update_parking_status(parking_spot_id, status):
    url = base_url + f'entities/{parking_spot_id}/attrs/status/value'
    headers = {'Content-Type': 'text/plain'}
    response = requests.put(url, headers=headers, data=status)
    print(f"Updated status of parking spot {parking_spot_id} to {status}")

# Simulate parking spots and update their status randomly
def simulate_parking():
    # Define parking spots with their IDs and locations (longitude, latitude)
    parking_spots = {
        'parking_spot_1': {'location': {'type': 'Point', 'coordinates': [-122.4194, 37.7749]}},
        'parking_spot_2': {'location': {'type': 'Point', 'coordinates': [-122.4086, 37.7834]}}
        # Add more parking spots as needed
    }

    # Create parking spots
    for spot_id, spot_info in parking_spots.items():
        create_parking_spot(spot_id, spot_info['location'])

    # Continuously update the status of parking spots
    while True:
        for spot_id in parking_spots:
            # Randomly choose a status: 'available' or 'occupied'
            status = random.choice(['available', 'occupied'])
            update_parking_status(spot_id, status)
        
        # Sleep for some time before updating again (e.g., every 30 seconds)
        interval = int(os.getenv('UPDATE_INTERVAL', '30'))
        time.sleep(interval)

# Run the simulation when the script is executed
if __name__ == '__main__':
    simulate_parking()
