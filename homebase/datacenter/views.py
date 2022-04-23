import django_filters
from django_filters import rest_framework as filters

from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import viewsets, response, permissions

from .models import Item
from django.contrib.auth.models import User
from .serializers import ItemSerializer

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

        print("query_paramss = " + str(self.request.query_params))
        print("request.data = " + str(self.request.data))

        user = str(self.request.user)
        print("user : " + user)
        print("auth : " + str(self.request.auth))

        # permissions...
        # https://docs.djangoproject.com/en/1.11/ref/models/querysets/
        # only return the queryset that has restricted_to = null or restricted_to = user

        queryset = Item.objects.filter(restricted_to=user) | Item.objects.filter(restricted_to=None) | Item.objects.filter(restricted_to='')
        queryset = Item.objects.all()
        return queryset


class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    # authentication_classes = (BasicAuthentication)

    # activate authenticatio requirement for this view
    # permission_classes = (IsAuthenticated,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
