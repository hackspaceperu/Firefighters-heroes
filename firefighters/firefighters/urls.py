"""firefighters URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from accounts import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('vehicle.urls')),
    url(r'^', include('emergency.urls')),
    url(r'^users/$', views.UserListView.as_view()),
    url(r'^users/(?P<pk>[0-9]+)$', views.UserDetailView.as_view()),
    url(r'^api-token-auth/$', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^signup/$', views.UserRegister.as_view()),
]
