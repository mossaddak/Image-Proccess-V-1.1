from django.contrib import admin
from django.urls import path
from .views import StripePaymentView

urlpatterns = [
    path('stripe-payment/', StripePaymentView.as_view(), name='stripe_payment'),
]