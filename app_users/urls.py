from django.urls import path
from app_users.views import login_view, AnotherLoginView, logout_view, AnotherLogoutView

urlpatterns = [
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
    path('another_login/', AnotherLoginView.as_view(), name='another_login'),
    path('another_logout/', AnotherLogoutView.as_view(), name='another_logout'),
]
