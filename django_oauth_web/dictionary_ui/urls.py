from django.urls import path, re_path
from . import views

app_name = 'ui'

urlpatterns = [
    path('list/', views.Dictionary_List.as_view()),
    path('add/', views.Dictionary_Add.as_view()),
    re_path('update/(?P<word>[^/]+)/$', views.Dictionary_Update.as_view()),
]
