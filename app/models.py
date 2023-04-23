from django.db import models

#image proccessing================================================================>
class ImageProcess(models.Model):
    input = models.ImageField(null=True, blank=True, verbose_name="Input")
    filter_jpg = models.ImageField(null=True, blank=True, verbose_name="Filter Jpg")
    filter_png = models.ImageField(null=True, blank=True, verbose_name="Filter Png")
    sharpe_jpg = models.ImageField(null=True, blank=True, verbose_name="Sharpe Jpg")
    sharpe_png = models.ImageField(null=True, blank=True, verbose_name="Sharpe Png")

    bg_remove = models.ImageField(null=True, blank=True, verbose_name="Background Removed Image")

    pdf = models.FileField(blank=True, null=True, verbose_name="Pdf")
    svg = models.FileField(blank=True, null=True, verbose_name="Svg")
    def __str__(self):
        return f"{self.pk}"
    

#pdf proccessing===================================================================>
class PdfToImage(models.Model):
    input = models.FileField(null=True, blank=True, verbose_name="Input")
    images_zip_file = models.FileField(null=True, blank=True, verbose_name="Images Zip File")

    def __str__(self):
        return f"{self.pk}"
