from django.contrib import admin
from django.urls import path, include
from .views import(
    ImageResolutionView,
    PdfToImageView

)


urlpatterns = [
    path('image-proccess/', ImageResolutionView.as_view()),
    path('pdf-proccess/', PdfToImageView.as_view()),
]
