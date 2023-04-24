from django.db import models
from account.models import(
    User
)

#image proccessing================================================================>
class ImageProcess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="image_to_image")
    input = models.ImageField(null=True, blank=True, verbose_name="Input")
    filter_jpg = models.ImageField(null=True, blank=True, verbose_name="Filter Jpg")
    filter_png = models.ImageField(null=True, blank=True, verbose_name="Filter Png")
    sharpe_jpg = models.ImageField(null=True, blank=True, verbose_name="Sharpe Jpg")
    sharpe_png = models.ImageField(null=True, blank=True, verbose_name="Sharpe Png")
    bg_remove = models.ImageField(null=True, blank=True, verbose_name="Background Removed Image")
    pdf = models.FileField(blank=True, null=True, verbose_name="Pdf")
    svg = models.FileField(blank=True, null=True, verbose_name="Svg")

    #resizing
    business_card = models.ImageField(null=True, blank=True)
    instagram_post = models.ImageField(null=True, blank=True)
    instagram_story = models.ImageField(null=True, blank=True)
    email_signature = models.ImageField(null=True, blank=True)
    facebook_cover = models.ImageField(null=True, blank=True)
    letterhead = models.ImageField(null=True, blank=True)
    

    def __str__(self):
        return f"{self.pk}"
    

#pdf proccessing===================================================================>
class PdfToImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="pdf_to_image")
    input = models.FileField(null=True, blank=True, verbose_name="Input")
    images_zip_file = models.FileField(null=True, blank=True, verbose_name="Images Zip File")

    def __str__(self):
        return f"{self.pk}"
