from django.http import JsonResponse
from .models import EventLog
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EventLogSerializer

class EventLogCreateView(APIView):
    def post(self, request):
        serializer = EventLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventLogListView(APIView):
    def get(self, request):
        logs = EventLog.objects.all()
        serializer = EventLogSerializer(logs, many=True)
        return Response(serializer.data)
