from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    RegisterView,
    ProfileView,
    ForgetPasswordView,
    ResetPasswordView,
    DeleteAccountView
)

urlpatterns = [
    path("register/", RegisterView.as_view()),

    path("login/", TokenObtainPairView.as_view()),

    path("refresh/", TokenRefreshView.as_view()),

    path("profile/", ProfileView.as_view()),

    path("forget-password/", ForgetPasswordView.as_view()),

    path("reset-password/", ResetPasswordView.as_view()),

    path("delete/", DeleteAccountView.as_view())
]