from django.db import models

# Create your models here.
class ImageProcess(models.Model):
    input = models.ImageField(null=True, blank=True, verbose_name="Input")
    output = models.ImageField(null=True, blank=True, verbose_name="Output")
    def __str__(self):
        return f"{self.pk}"
