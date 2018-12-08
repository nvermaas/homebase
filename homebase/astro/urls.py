from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'astro'

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [

    # /homebase/moonphases
    url(r'^homebase/moonphases/$', views.MoonPhasesView.as_view({'get': 'list'}), name='moonphases-list'),
    # /datacenter/moonphases
    url(r'^datacenter/moonphases/$', views.MoonPhasesView.as_view({'get': 'list'}), name='moonphases-list'),

]
urlpatterns = format_suffix_patterns(urlpatterns)