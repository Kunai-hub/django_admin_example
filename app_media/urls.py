from django.urls import path

from app_media.views import upload_file

urlpatterns = [
    path('upload_file/', upload_file, name='upload_file'),
]
