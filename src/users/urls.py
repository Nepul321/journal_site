from django.urls import path
from .views import (
    LoginView,
    LogoutView,
    UpdateAccountView,
    PasswordView
)

urlpatterns = [
    path('accounts/login/', LoginView, name="login-view"),
    path('accounts/logout/', LogoutView, name="logout-view"),
    path('accounts/your-account/', UpdateAccountView, name="account-view"),
    path('accounts/password/', PasswordView, name="password-view"),
]
