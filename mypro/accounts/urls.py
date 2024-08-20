from django.urls import path, include
from .views import LoginView, profile, LogoutView, SignupView, ProfileUpdateView
from . import api

app_name = "accounts"

urlpatterns_api_v1 = [
    path("status/", api.status, name="status"),
]

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", profile, name="profile"),
    path("profile/edit/", ProfileUpdateView.as_view(), name="profile_edit"),
]