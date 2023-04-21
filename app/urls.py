from django.contrib import admin
from django.urls import path, include
from .views import(
    ImageResolutionView,

)


urlpatterns = [
    path('image-proccess/', ImageResolutionView.as_view())
]
