from django.urls import path
from .views import (
    LoginView,
    LogoutView
)

urlpatterns = [
    path('accounts/login/', LoginView, name="login-view"),
    path('accounts/logout/', LogoutView, name="logout-view"),
]
