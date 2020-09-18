from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from authentication.views import (
    register_user,
    login_user,
    delete_user
)

urlpatterns = [
    path('register', register_user, name="register"),
    path('login', login_user, name="login"),
    path('login/refresh', TokenRefreshView.as_view(), name="refresh"),
    path('delete', delete_user, name="delete")
]