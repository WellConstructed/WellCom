from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from wellcom_app import views

router = routers.DefaultRouter()
router.register(r'note', views.NoteViewSet)
router.register(r'device_data', views.DeviceDataViewSet)
router.register(r'usage', views.UsageViewSet)
router.register(r'water_test', views.WaterTestViewSet)
router.register(r'well', views.WellViewSet)
router.register(r'device_output', views.DeviceOutputViewSet)
router.register(r'test', views.TestViewSet)
router.register(r'hourly_usage', views.HourlyUsageViewSet)
# router.register(r'well_name', views.WellNameViewSet)
router.register(r'hourly', views.WellNameHourlyUsageViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('wellcom_app.urls')),
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
]
