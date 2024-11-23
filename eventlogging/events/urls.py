from django.urls import path
from . import views

urlpatterns = [
    path('eventlogs/', views.EventLogListView.as_view(), name='eventlog-list'),
    path('eventlogs/create/', views.EventLogCreateView.as_view(), name='eventlog-create'),
]
