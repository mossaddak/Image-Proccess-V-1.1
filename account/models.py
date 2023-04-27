from django.db import models
from django.contrib.auth.models import User
from .manager import CustomeUserManager
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=50, unique=True, error_messages={"unique":"A user with that email already exists."})
    #profile_picture = models.ImageField(null = True,blank = True,upload_to = "profile-pictures")
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=20, null=True, blank=True)
    password_reset_token = models.CharField(max_length=20, null=True, blank=True)
    REQUIRES_FIELDS = ["email"]
    objects = CustomeUserManager()

    def __str__(self):
        return f"{self.pk}.{self.username}"
    
class ProfilePicture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="profile_picture")
    img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.pk}.{self.user}"
