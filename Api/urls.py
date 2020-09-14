"""Api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from core.views import TestView, PostView, PostCreateView, PostListCreateView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('', TestView.as_view(), name='test'),
    path('post/', PostView.as_view(), name='post'),
    path('create', PostCreateView.as_view(), name='create'),
    path('list-create', PostListCreateView.as_view(), name='listcreate'),
    path('api-auth', include('rest_framework.urls')),
    path('api/token', obtain_auth_token, name='obtain-token')
]
