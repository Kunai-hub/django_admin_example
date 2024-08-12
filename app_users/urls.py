from django.urls import path
from app_users.views import login_view, AnotherLoginView, logout_view, AnotherLogoutView, register_view, \
    register_view_extend, restore_password
from rest_framework import routers
from app_users.api import UserViewSet


urlpatterns = [
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
    path('another_login/', AnotherLoginView.as_view(), name='another_login'),
    path('another_logout/', AnotherLogoutView.as_view(), name='another_logout'),
    path('register/', register_view, name='register'),
    path('another_register/', register_view_extend, name='another_register'),
    path('restore_password/', restore_password, name='restore_password'),
]

router = routers.DefaultRouter()
router.register('api', UserViewSet)
urlpatterns += router.urls
