from django.contrib import admin
from django.urls import path, include
from .views import(
    SingUp,
    VerifyOTPview,
    LoginView,
    ProfileView
)

urlpatterns = [
    path('account/sing-up/', SingUp.as_view()),
    path('account/verify/', VerifyOTPview.as_view()),
    path('account/login/', LoginView.as_view()),
    path('account/profile/', ProfileView.as_view()),
]
