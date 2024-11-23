from django.db import models
import hashlib
import json
from datetime import datetime

class EventLog(models.Model):
    event_type = models.CharField(max_length=100)
    timestamp = models.DateTimeField(default=datetime.now)
    source_application_id = models.CharField(max_length=100)
    data_payload = models.JSONField()
    prev_hash = models.CharField(max_length=64, null=True, blank=True)
    hash = models.CharField(max_length=64)

    def save(self, *args, **kwargs):
        """
        Overridden save method to generate the hash based on the current log's details
        and the previous log's hash.
        """
        # Prepare the data to calculate the hash: Event log details + previous log's hash
        event_data = f"{self.event_type}{self.timestamp}{self.source_application_id}{json.dumps(self.data_payload)}{self.prev_hash}"

        # Generate the current hash using SHA256
        self.hash = hashlib.sha256(event_data.encode()).hexdigest()

        # If it's the first log (i.e., no previous log), set prev_hash to None
        if not self.prev_hash:
            self.prev_hash = None

        # Call the parent class save method to save the instance to the database
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Event {self.event_type} at {self.timestamp}"
