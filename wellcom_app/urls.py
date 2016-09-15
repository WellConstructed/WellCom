from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^wells/$', views.wells, name='wells'),
    url(r'^well/(?P<well_id>[0-9]+)', views.well_detail, name='well_detail'),

    url(r'^graph_temp/', views.graph_temp, name='graph_temp'),

]
