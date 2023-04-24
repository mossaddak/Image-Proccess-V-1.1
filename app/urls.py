from django.contrib import admin
from django.urls import path, include
from .views import(
    ImageResolutionView,
    PdfToImageView,
    AllImgResolutionDetailsView,
    AllPdfToImageView

)


urlpatterns = [
    path('image-proccess/', ImageResolutionView.as_view()),
    path('image-proccess/<int:pk>/', AllImgResolutionDetailsView.as_view()),
    path('pdf-proccess/', PdfToImageView.as_view()),
    path('pdf-proccess/<int:pk>/', AllPdfToImageView.as_view()),
    
]
