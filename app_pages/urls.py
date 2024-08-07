from django.urls import path

from app_pages.views import translation, greetings_page


urlpatterns = [
    path('', translation, name='translation'),
    path('greetings/', greetings_page, name='greetings_page'),
]
