from django.contrib import admin
from django.urls import path
from .views import (
    PasswordReset,
    ResetPasswordAPI
)

urlpatterns = [
    path('reset-password/', PasswordReset.as_view(), name="reset-password"),
    path('reset-password/<str:encoded_pk>/<str:token>/',ResetPasswordAPI.as_view(), name="reset-password"),
]
