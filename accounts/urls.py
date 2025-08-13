from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import login_view, register_view, CustomLogoutView

app_name = 'accounts'

urlpatterns = [
    path('accounts/register/', register_view, name="register"),
    path('accounts/login/', login_view, name="login"),
    path('accounts/logout/', CustomLogoutView.as_view(), name="logout")
]
