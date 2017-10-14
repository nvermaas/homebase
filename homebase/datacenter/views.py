
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Location
from .serializers import LocationSerializer

from django.core.urlresolvers import reverse

class LocationListView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    # activate authenticatio requirement for this view
    # permission_classes = (IsAuthenticated,)
    # permission_classes = (IsAuthenticatedOrReadOnly,)

    # overriding GET get_queryset to access the request (demoo)
    def get_queryset(self):
        print("get_queryset() : user = " + str(self.request.user))
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
    print("LocationDetailView()")
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    # authentication_classes = (BasicAuthentication)

    # activate authenticatio requirement for this view
    permission_classes = (IsAuthenticated,)
    # permission_classes = (IsAuthenticatedOrReadOnly,)

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

    # overriding GET get_queryset to access the request
    def get_queryset(self):
        print("get_queryset() : user = " + str(self.request.user))
        print("query_params = " + str(self.request.query_params))
        print("request.data = " + str(self.request.data))
        queryset = Location.objects.all()

        return queryset