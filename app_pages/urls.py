from django.urls import path
from django.views.decorators.cache import cache_page

from app_pages.views import translation, greetings_page, welcome, main


urlpatterns = [
    path('', translation, name='translation'),
    path('greetings/', greetings_page, name='greetings_page'),
    path('welcome/', cache_page(30)(welcome), name='welcome'),
    path('main/', main, name='main'),
]
