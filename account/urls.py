from django.contrib import admin
from django.urls import path, include
from .views import(
    SingUp,
    VerifyOTPview,
    LoginView,
    ProfileView,
    ProfilePictureView,
    VerifiCationOtpSentView
)
from rest_framework.routers import DefaultRouter
router = DefaultRouter()


router.register(r"profile-picture", ProfilePictureView) 

urlpatterns = [
    path('account/sing-up/', SingUp.as_view()),
    path('account/verify/', VerifyOTPview.as_view()),
    path('account/login/', LoginView.as_view()),
    path('account/profile/', ProfileView.as_view()),
    path('account/account-verify-code/', VerifiCationOtpSentView.as_view()),
]+router.urls
