from django.contrib import admin
from .models import(
    User,
    ProfilePicture
)

# Register your models here.
admin.site.register(User)
admin.site.register(ProfilePicture)
