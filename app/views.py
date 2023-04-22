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

#from rembg import remove
from PIL import Image




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

            #bilateral filtering
            output_bil = cv2.bilateralFilter(img, 40, 35, 100)
            cv2.imwrite(f'media/proccessed_img{LastImg.pk}.jpg', output_bil)
            cv2.imwrite(f'media/proccessed_img{LastImg.pk}.png', output_bil)

            #kernel bluring
            LastImg.filter_jpg = f'proccessed_img{LastImg.pk}.jpg'
            LastImg.filter_png = f'proccessed_img{LastImg.pk}.jpg'

            #sharping=================================================================>
            #gauusian blur
            gasusian_blur = cv2.GaussianBlur(img, (7,7), 2)
            #sharping
            sharping2 = cv2.addWeighted(img, 1.5, gasusian_blur, -0.5, 1)
            cv2.imwrite(f'media/sharp_proccessed_img{LastImg.pk}.jpg', sharping2)
            cv2.imwrite(f'media/sharp_proccessed_img{LastImg.pk}.png', sharping2)
            LastImg.sharpe_jpg = f'sharp_proccessed_img{LastImg.pk}.jpg'
            LastImg.sharpe_png = f'sharp_proccessed_img{LastImg.pk}.png'

            #pdf making==============================================================>
            img = Image.open(f'media{"/"}proccessed_img{LastImg.pk}.jpg')
            R = img.convert('RGB')
            R.save(f'media/filter_img_pdf{LastImg.pk}.pdf')
            LastImg.filter_img_pdf = f'filter_img_pdf{LastImg.pk}.pdf'


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

