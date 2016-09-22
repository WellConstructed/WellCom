from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^about/$', views.about_us, name='about_us'),
    url(r'^$', views.wells, name='wells'),
    url(r'^wells/(?P<well_id>[0-9]+)', views.well_detail, name='well_detail'),
    url(r'^dd/$', views.test_device_view, name='test_device_data'),
]
