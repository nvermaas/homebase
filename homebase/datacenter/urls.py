from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import obtain_auth_token
from . import views

app_name = 'datacenter'

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [

    # /datacenter/locations
    url(r'^homebase/locations/$', views.LocationListView.as_view(), name='location-list'),

    #/datacenter/locations/1
    url(r'^homebase/locations/(?P<pk>[0-9]+)/$', views.LocationDetailView.as_view(), name='location-detail-view'),

    # /homebase/items
    url(r'^homebase/items/$', views.ItemListView.as_view(), name='item-list'),
    # /datacenter/items
    url(r'^datacenter/items/$', views.ItemListView.as_view(), name='item-list'),

    # /datacenter/items/1
    url(r'^homebase/items/(?P<pk>[0-9]+)/$', views.ItemDetailView.as_view(), name='item-detail-view'),
    url(r'^datacenter/items/(?P<pk>[0-9]+)/$', views.ItemDetailView.as_view(), name='item-detail-view'),

    url(r'^homebase/users$', views.UserListView.as_view()),
    url(r'^homebase/users/(?P<pk>[0-9]+)/$', views.UserDetailView.as_view()),

    url(r'^homebase/obtain-auth-token/$', csrf_exempt(obtain_auth_token))
]
urlpatterns = format_suffix_patterns(urlpatterns)