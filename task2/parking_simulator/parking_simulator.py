from random import randint
import requests

# Replace with your Context Broker information
HOST = "http://task1-orion-1:1026"
SERVICE = "parking"  # Not used in this code, but could be relevant for future use
ENTITY_TYPE = "ParkingSpot"

# Define attributes for a parking spot
attributes = [
    {"id": "id", "type": "string"},
    {"id": "status", "type": "string", "enumValues": ["free", "occupied"]},
]


def create_entity_type(entity_type, attributes):
    """
    Creates an entity type in the Context Broker.
    """
    url = f"{HOST}/v2/entities/types/{entity_type}"
    headers = {"Content-Type": "application/json"}
    payload = {"id": entity_type, "attrs": attributes}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise exception for non-200 status codes
        print(f"Entity type '{entity_type}' created successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error creating entity type: {e}")


def create_entity(entity_id, entity_type, attributes):
    """
    Creates an entity in the Context Broker.
    """
    url = f"{HOST}/v2/entities/{entity_type}/{entity_id}"
    headers = {"Content-Type": "application/json"}
    payload = {"id": entity_id, "type": entity_type, "attrs": attributes}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        print(f"Entity '{entity_id}' created successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error creating entity: {e}")


def update_entity(entity_id, entity_type, attribute, value):
    """
    Updates an attribute of an entity in the Context Broker.
    """
    url = f"{HOST}/v2/entities/{entity_type}/{entity_id}/attrs/{attribute}"
    headers = {"Content-Type": "application/json"}
    payload = {"value": value}

    try:
        response = requests.patch(url, headers=headers, json=payload)
        response.raise_for_status()
        print(f"Entity '{entity_id}' attribute '{attribute}' updated.")
    except requests.exceptions.RequestException as e:
        print(f"Error updating entity: {e}")


def main():
    # Check if entity type exists
    url = f"{HOST}/v2/entities/types/{ENTITY_TYPE}"
    response = requests.get(url)

    if response.status_code == 404:
        create_entity_type(ENTITY_TYPE, attributes)

    # Create parking spot entities (optional, uncomment if needed)
    # for i in range(1, 11):
    #     entity_id = f"parking_spot_{i}"
    #     create_entity(entity_id, ENTITY_TYPE, [{"id": "id", "type": "String", "value": entity_id}])

    while True:
        # Randomly update parking spot status with probability weighting
        occupied_probability = 0.7  # Adjust probability as needed
        status = "occupied" if randint(0, 100) < occupied_probability * 100 else "free"
        entity_id = f"parking_spot_{randint(1, 10)}"

        try:
            update_entity(entity_id, ENTITY_TYPE, "status", status)
        except requests.exceptions.RequestException as e:
            print(f"Error updating entity: {e}")
            # Optional: Implement logic to handle potential errors gracefully

if __name__ == "__main__":
    main()
