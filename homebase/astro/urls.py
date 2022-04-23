from django.urls import include, path

from . import views

app_name = 'astro'

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    # /homebase/astro/moonphases
    path('', views.MoonPhasesView.as_view({'get': 'list'}), name='moonphases-list'), # remove after moontides update
    path('moonphases/', views.MoonPhasesView.as_view({'get': 'list'}), name='moonphases-list'),
]
