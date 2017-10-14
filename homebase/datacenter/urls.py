from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'datacenter'

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [

    # /datacenter/locations
    url(r'^locations/$', views.LocationListView.as_view(), name='location-list'),

    #/datacenter/locations/1
    url(r'locations/(?P<pk>[0-9]+)/$', views.LocationDetailView.as_view(), name='location-detail-view'),


]
urlpatterns = format_suffix_patterns(urlpatterns)