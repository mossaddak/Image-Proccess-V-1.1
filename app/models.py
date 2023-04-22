from django.db import models

# Create your models here.
class ImageProcess(models.Model):
    input = models.ImageField(null=True, blank=True, verbose_name="Input")
    filter_jpg = models.ImageField(null=True, blank=True, verbose_name="Filter Jpg")
    filter_png = models.ImageField(null=True, blank=True, verbose_name="Filter Png")

    #sharp_jpg = models.ImageField(null=True, blank=True, verbose_name="Sharpe Jpg")
    def __str__(self):
        return f"{self.pk}"
