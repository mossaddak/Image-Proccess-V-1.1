from django.contrib import admin
from django.urls import path, include
from .views import(
    SingUp,
    VerifyOTPview,
    LoginView
)

urlpatterns = [
    path('account/sing-up/', SingUp.as_view()),
    path('account/verify/', VerifyOTPview.as_view()),
    path('account/login/', LoginView.as_view()),
]
