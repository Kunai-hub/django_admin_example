"""
URL configuration for django_admin_example project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django_admin_example.views import MainPageView


urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('admin/', admin.site.urls),
    path('users/', include('app_users.urls')),
    path('employment/', include('app_employment.urls')),
    path('files/', include('app_media.urls')),
    path('goods/', include('app_goods.urls')),
]
