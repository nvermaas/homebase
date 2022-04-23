
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    #path('homebase/', include('taskdatabase.urls')),

    path('homebase/admin/', admin.site.urls),
    path('homebase/api-auth/', include('rest_framework.urls')),

    path('homebase/datacenter/', include('datacenter.urls')),
    path('homebase/', include('datacenter.urls')),

    #url(r'^homebase/admin/', admin.site.urls),
    #url(r'^homebase/api-auth/', include('rest_framework.urls')),

]


