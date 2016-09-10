from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from wellcom_app import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('wellcom_app.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
