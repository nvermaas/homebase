from django.urls import path
from . import views

app_name = 'datacenter'

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    # /homebase/datacenter/items
    path('items/', views.ItemListView.as_view(), name='item-list'),
    path('items/<int:id>', views.ItemListView.as_view(), name='item-detail-view'),

]
