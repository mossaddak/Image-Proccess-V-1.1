from django.db import models

# Create your models here.
class ImageProcess(models.Model):
    input = models.ImageField(null=True, blank=True, verbose_name="Input")
    jpg = models.ImageField(null=True, blank=True, verbose_name="Jpg")
    png = models.ImageField(null=True, blank=True, verbose_name="Png")
    def __str__(self):
        return f"{self.pk}"
