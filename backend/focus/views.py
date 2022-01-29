from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import serializers, viewsets
from rest_framework import permissions
from rest_framework.decorators import permission_classes

from focus.models import UpcomingEvents, Events, FocusTeam, Images, TechnologyClubs
from .serializers import UpcomingEventsSerializer, EventsSerializer, FocusTeamSerializer, ImagesSerializer, TechnologyClubsSerializer

# Create your views here.

class UpcomingEventsViewSet(viewsets.ModelViewSet):
    queryset = UpcomingEvents.objects.all()
    serializer_class = UpcomingEventsSerializer
    permission_classes = [permissions.IsAdminUser]

class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    permission_classes = [permissions.IsAdminUser]

class FocusTeamViewSet(viewsets.ModelViewSet):
    queryset = FocusTeam.objects.all()
    serializer_class = FocusTeamSerializer
    permission_classes = [permissions.IsAdminUser]

class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer
    permission_classes = [permissions.IsAdminUser]

class TechnologyClubsViewSet(viewsets.ModelViewSet):
    queryset = TechnologyClubs.objects.all()
    serializer_class = TechnologyClubsSerializer
    permission_classes = [permissions.IsAdminUser]








def home(request):
    return HttpResponse("HELLO")