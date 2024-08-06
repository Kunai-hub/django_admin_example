from django.urls import path

from app_pages.views import translation


urlpatterns = [
    path('', translation, name='translation')
]
