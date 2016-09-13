from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^allwells/$', views.all_wells, name='all_wells'),
    url(r'^well/(?P<pk>[0-9]+)', views.well_detail, name='well_detail'),
    # url(r'^allwells/$', views.WellViewSet.as_view(), name='all_wells')
]
