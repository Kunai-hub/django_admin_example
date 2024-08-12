from django.urls import path

from app_goods.views import items_list, update_price, items_list_api, ItemList


urlpatterns = [
    path('', items_list, name='items_list'),
    path('upload_price/', update_price, name='upload_price'),
    path('items_api/', items_list_api, name='items_list_api'),
    path('items_api_ser/', ItemList.as_view(), name='items_list_api_ser'),
]
