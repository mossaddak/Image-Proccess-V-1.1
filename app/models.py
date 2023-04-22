from django.db import models

# Create your models here.
class ImageProcess(models.Model):
    input = models.ImageField(null=True, blank=True, verbose_name="Input")
    filter_jpg = models.ImageField(null=True, blank=True, verbose_name="Filter Jpg")
    filter_png = models.ImageField(null=True, blank=True, verbose_name="Filter Png")
    sharpe_jpg = models.ImageField(null=True, blank=True, verbose_name="Sharpe Jpg")
    sharpe_png = models.ImageField(null=True, blank=True, verbose_name="Sharpe Png")

    bg_remove = models.ImageField(null=True, blank=True, verbose_name="Background Removed Image")

    pdf = models.FileField(blank=True, null=True, verbose_name="Pdf")
    def __str__(self):
        return f"{self.pk}"
