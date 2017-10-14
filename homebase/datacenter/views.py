import django_filters
from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Location
from .serializers import LocationSerializer\

from django.core.urlresolvers import reverse

class LocationListView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    # overriding GET get_queryset to access the request (demoo)
    def get_queryset(self):
        print("query_params = " + str(self.request.query_params))
        print("request.data = " + str(self.request.data))
        queryset = Location.objects.all()

        return queryset

    # overriding the POST that is used to create new records (demo)
    def perform_create(self, serializer):
        print("perform_create():")
        print("Location created by user : "+str(self.request.user))
        serializer.save()

class LocationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (IsAuthenticated,)

    # override the put (from the mixins), to be able to access the request and its methods.
    # http://www.django-rest-framework.org/api-guide/generic-views/
    def put(self, request, *args, **kwargs):
        print("PUT:")

        # examples of accessing information from the request
        print("request.query_params = " + str(self.request.query_params))
        print("request.data = " + str(self.request.data))
        print("request.user = " + str(self.request.user))
        return self.update(request, *args, **kwargs)

    def perform_update(self, serializer):
        print("perform_update():")
        instance = serializer.save()
        print("Location updated by user : " + str(self.request.user))