from django.urls import path

from app_employment.views import vacancy_list

urlpatterns = [
    path('vacancy/', vacancy_list, name='vacancy_list')
]
