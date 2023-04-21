from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import (
    status
)

from .models import(
    ImageProcess
)
from .serializer import(
    ImageProcessSerializer
)
import base64
from rest_framework.parsers import MultiPartParser

#image proccessing
import cv2
import numpy as np



# Create your views here.
class ImageResolutionView(APIView):
    parser_classes = (MultiPartParser,)
    def post(self, request):
        data = request.data

        print("========================>", request.data)
        serializer = ImageProcessSerializer(data=data)

        


        if serializer.is_valid():
            serializer.save()
            all_images = ImageProcess.objects.all()
            serializer = ImageProcessSerializer(all_images, many=True)
            LastImg = ImageProcess.objects.last()
            LastImgUrl = LastImg.input.url

            print("last image=============================", LastImgUrl)

            #image process__________________________________________________
            img = cv2.imread(LastImg.input.path)
            print("==================================>",img)
            rows, cols = img.shape[:2]

            #img converting
            output_bil = cv2.bilateralFilter(img, 40, 35, 100)
            cv2.imwrite(f'media/proccessed_img{LastImg.pk}.jpg', output_bil)
            cv2.imwrite(f'media/proccessed_img{LastImg.pk}.png', output_bil)
            
            LastImg.jpg = f'proccessed_img{LastImg.pk}.jpg'
            LastImg.png = f'proccessed_img{LastImg.pk}.png'

            #cv2.imshow('Orgiginal', img)
            cv2.waitKey(0)
            LastImg.save()

            return Response(
                {
                    "data":serializer.data[-1]
                },status=status.HTTP_200_OK
            )
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

