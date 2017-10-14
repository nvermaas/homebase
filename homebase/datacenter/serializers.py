from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Location

class LocationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'

