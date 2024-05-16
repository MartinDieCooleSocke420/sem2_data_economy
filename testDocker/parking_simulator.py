from pyngsi.sources.source import Source
from pyngsi.sink.sink import Sink

# Set up NGSI Source and Sink
source = Source()
sink = Sink()

# Define NGSI Entity attributes
entity_id = "ParkingSpot1"
entity_type = "ParkingSpot"
attributes = {
    "status": {
        "type": "Boolean",
        "value": True
    },
    "location": {
        "type": "geo:json",
        "value": {
            "type": "Point",
            "coordinates": [longitude, latitude]
        }
    }
}

# Create NGSI Entity
source.add_entity(entity_id, entity_type, attributes)

# Send entities to NGSI Context Broker
sink.send(source)

# Update NGSI Entity attributes
new_attributes = {
    "status": {
        "type": "Boolean",
        "value": False
    }
}

# Update attributes of existing entity
source.update_entity(entity_id, new_attributes)

# Send updated entity to NGSI Context Broker
sink.send(source)
