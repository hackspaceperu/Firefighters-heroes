from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from emergency import views

urlpatterns = [
    url(r'^emergency_type/$', views.EmergencyTypeListView.as_view()),
    url(r'^emergency_type/(?P<pk>[0-9]+)$', views.EmergencyTypeDetailView.as_view()),
    url(r'^emergencies/$', views.EmergencyListView.as_view()),
    url(r'^emergency/(?P<pk>[0-9]+)$', views.EmergencyTypeDetailView.as_view()),
    url(r'^vehicle_emergency/$', views.VehicleEmergencyListView.as_view()),
    url(r'^vehicle_emergency/(?P<pk>[0-9]+)$', views.VehicleEmergencyDetailView.as_view()),
    url(r'^roles/$', views.RoleListView.as_view()),
    url(r'^role/(?P<pk>[0-9]+)$', views.RoleDetailView.as_view()),
    url(r'^user_asistance/$', views.UserAssistanceListView.as_view()),
    url(r'^user_asistance/(?P<pk>[0-9]+)$', views.UserAssistanceDetailView.as_view()),
    url(r'^fire_code/$', views.FireCodeListView.as_view()),
    url(r'^fire_code/(?P<pk>[0-9]+)$', views.FireCodeDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
