from django.urls import path

from app_shops.views import page_with_cached_fragments


urlpatterns = [
    path('', page_with_cached_fragments, name='page_with_cached_fragments')
]
