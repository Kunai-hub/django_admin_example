from django.urls import path

from app_goods.views import items_list, update_price


urlpatterns = [
    path('', items_list, name='items_list'),
    path('upload_price/', update_price, name='upload_price'),
]
