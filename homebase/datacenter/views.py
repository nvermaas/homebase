import django_filters
from django_filters import rest_framework as filters

from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Location, Item
from .serializers import LocationSerializer, ItemSerializer

from django.core.urlresolvers import reverse

class LocationFilter(filters.FilterSet):

    timestampContains = django_filters.CharFilter(name="timestamp", lookup_expr='contains') #/query?creationTimeContains=2015

    # the Meta tag is used to generate filters automatically
    class Meta:
        model = Location

        fields = {
            'id': ['lt', 'gt'],                               # ../locations?id__gt=5&id__lt=10
            'latitude': ['lt', 'gt'],
            'longitude': ['lt', 'gt'],
            'username' : ['exact', 'in'],                     # ../locations?username__in=Nico,Erik
                                                              # ../locations/username=nvermaas
            'title': ['exact', 'icontains'],
            'description': ['exact', 'icontains'],
            'timestamp': ['gt','lt','gte','lte','contains','exact','year__lt', 'year__gt', 'month__lt', 'month__gt'],
        }


class LocationListView(generics.ListCreateAPIView):
    # using the Django Filter Backend - https://django-filter.readthedocs.io/en/latest/index.html
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = LocationFilter

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
        queryset = Location.objects.all().order_by('-timestamp')

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
    # permission_classes = (IsAuthenticated,)
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


class ItemListView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    # activate authenticatio requirement for this view
    # permission_classes = (IsAuthenticated,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    # overriding GET get_queryset to access the request
    def get_queryset(self):
        print("get_queryset() : user = " + str(self.request.user))

        # only return the items for users that are listed in the 'restricted_to' field.

        print("query_params = " + str(self.request.query_params))
        print("request.data = " + str(self.request.data))
        queryset = Item.objects.all().order_by('order')

        return queryset


class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    # authentication_classes = (BasicAuthentication)

    # activate authenticatio requirement for this view
    # permission_classes = (IsAuthenticated,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
