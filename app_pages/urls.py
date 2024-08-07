from django.urls import path

from app_pages.views import translation, greetings_page, welcome, main


urlpatterns = [
    path('', translation, name='translation'),
    path('greetings/', greetings_page, name='greetings_page'),
    path('welcome/', welcome, name='welcome'),
    path('main/', main, name='main'),
]
