from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLogoutView, UserCreateView, UserLoginView

app_name = 'accounts'

urlpatterns = [
    path('accounts/register/', UserCreateView.as_view(), name="register"),
    path('accounts/login/', UserLoginView.as_view(), name="login"),
    path('accounts/logout/', CustomLogoutView.as_view(), name="logout")
]
