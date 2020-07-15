"""django_oauth_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from dictionary_ui.views import Home_Page

#   path('dictionary_api/', dictionary_api.urls),
urlpatterns = [
    re_path(r'^dictionary/?$', Home_Page.as_view(), name='home'),
    path('dictionary/ui/', include('dictionary_ui.urls')),
    path('dictionary/api/', include('dictionary_api.urls')),
    re_path(r'^', include('social_django.urls', namespace='social')),
]
