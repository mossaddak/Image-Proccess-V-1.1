from django.contrib import admin
from .models import(
    ImageProcess,
    PdfToImage
)

# Register your models here.
admin.site.register(ImageProcess)
admin.site.register(PdfToImage) 
