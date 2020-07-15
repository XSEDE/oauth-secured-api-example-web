from django.urls import path, re_path
from . import views

app_name = 'api'

urlpatterns = [
    re_path('^add/(?P<word>[^/]+)/$', views.Dictionary_API.as_view()),
    re_path('^update/(?P<word>[^/]+)/$', views.Dictionary_API.as_view()),
    re_path('^delete/(?P<word>[^/]+)/$', views.Dictionary_API.as_view()),
]
