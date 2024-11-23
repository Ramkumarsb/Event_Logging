from rest_framework import serializers
from .models import EventLog

class EventLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventLog
        fields = ['event_type', 'timestamp', 'source_application_id', 'data_payload', 'prev_hash', 'hash']
