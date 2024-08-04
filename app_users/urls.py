from django.urls import path
from app_users.views import login_view, AnotherLoginView

urlpatterns = [
    path('login/', login_view, name='login_view'),
    path('another_login/', AnotherLoginView.as_view(), name='another_login')
]
