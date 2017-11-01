from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from accounts import views

urlpatterns = [
    url(r'^users/$', views.UserListView.as_view()),
    url(r'^users/(?P<pk>[0-9]+)$', views.UserDetailView.as_view()),
    url(r'^api-token-auth/$', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^signup/$', views.UserRegister.as_view()),
    url(r'^profiles/$', views.ProfileListView.as_view()),
    url(r'^profiles/(?P<pk>[0-9]+)$', views.ProfileDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
