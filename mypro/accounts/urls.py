from django.urls import path
from .views import LoginView, profile, LogoutView, SignupView, ProfileUpdateView

app_name = "accounts"

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", profile, name="profile"),
    path("profile/edit/", ProfileUpdateView.as_view(), name="profile_edit"),
]