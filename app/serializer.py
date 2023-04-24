from rest_framework.serializers import ModelSerializer
from .models import(
    ImageProcess,
    PdfToImage
)

class ImageProcessSerializer(ModelSerializer):
    class Meta:
        model = ImageProcess
        fields = '__all__'


class PdfToImageSerializer(ModelSerializer):
    class Meta:
        model = PdfToImage
        fields = "__all__"
