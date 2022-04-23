from django.urls import include, path
from django.contrib.auth import views as auth_views
from rest_framework.authtoken import views as rest_auth_views
from . import views

from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'datacenter'

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    # /homebase/items
    path('items/', views.ItemListView.as_view(), name='item-list'),
    path('items/<int:id>', views.ItemListView.as_view(), name='item-detail-view'),

    # authentication
    path('accounts/', include('django.contrib.auth.urls')),

    # specialization of the above, with more control
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html')),

    path('obtain-auth-token', csrf_exempt(obtain_auth_token)),
]
