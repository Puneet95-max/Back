from django.contrib import admin
from django.urls import path
from .views import register, login
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', register, name='register_user'),
    path('login/', login, name='login_user'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
