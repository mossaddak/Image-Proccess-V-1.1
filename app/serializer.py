from rest_framework.serializers import ModelSerializer
from .models import(
    ImageProcess
)

class ImageProcessSerializer(ModelSerializer):
    class Meta:
        model = ImageProcess
        fields = '__all__'
