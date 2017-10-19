from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from vehicle import views

urlpatterns = [
    url(r'^vehicle_type/$', views.VehicleTypeListView.as_view()),
    url(r'^vehicle_type/(?P<pk>[0-9]+)$', views.VehicleTypeDetailView.as_view()),
    url(r'^vehicle/$', views.VehicleListView.as_view()),
    url(r'^vehicle/(?P<pk>[0-9]+)$', views.VehicleDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
