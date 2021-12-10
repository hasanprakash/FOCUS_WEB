from django.contrib.auth.models import User, Group
from .models import UpcomingEvents, Events, FocusTeam, Images, TechnologyClubs
from rest_framework import serializers

class UpcomingEventsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UpcomingEvents
        fields = ['title', 'subtitle', 'imageUrl']


class EventsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Events
        fields = ['name', 'description', 'imageUrl']

class FocusTeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FocusTeam
        fields = ['collegeId', 'name', 'role', 'imageUrl', 'groupName']


class ImagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Images
        fields = ['imageName', 'url']

class TechnologyClubsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TechnologyClubs
        fields = ['clubName', 'technology', 'description', 'mainPerson', 'theirRole', 'clubLogo']
