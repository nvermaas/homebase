from django.conf.urls import url, include
from django.contrib.auth.models import User

from . import views
from rest_framework import routers

app_name = 'datacenter'


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    # === REST VIEWS ===
    #url(r'^$', views.api_root), # this would short cut the index url
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # /datacenter/locations
    url(r'^locations/$', views.LocationListView.as_view(), name='location-list'),

    #/datacenter/locations/1
    url(r'locations/(?P<pk>[0-9]+)/$', views.LocationDetailView.as_view(), name='location-detail-view'),


]
