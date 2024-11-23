# scripts/simulate_events.py

import requests
import random
import json
from datetime import datetime

# Define possible event types and source apps
event_types = ['Login', 'Data Upload', 'Transaction']
source_apps = ['App1', 'App2', 'App3']

# URL of your local API endpoint
url = 'http://127.0.0.1:8000/api/logs/'

# Simulate 10 random events and send them to the API
for _ in range(10):
    event = {
        'event_type': random.choice(event_types),
        'timestamp': datetime.now().isoformat(),
        'source_application_id': random.choice(source_apps),
        'data_payload': {'data': 'random data'}
    }

    # Send the event to the API
    response = requests.post(url, json=event)

    # Print the response from the API
    print(response.json())
