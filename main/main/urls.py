"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


# register all the api endpoints so we can use React JS for the front-end

urlpatterns = [

    path('admin/', admin.site.urls),
    path('user/', include('users.urls')),
    path('competitions/', include('competitions.urls')),
    path('players/',include('competitions.squads.players.urls')),
    path('squads/',include('competitions.squads.urls')),
    path('fixtures/',include('competitions.fixtures.urls')),
    path('',include('rest_framework.urls')),
    # token authentication
    path('token-auth/',TokenObtainPairView.as_view(),name='token_create'),
    path('token-auth/refresh/',TokenRefreshView.as_view(),name='token_refresh')
]