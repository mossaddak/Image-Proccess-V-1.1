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
import svgwrite
import io
import base64




# CImage Process==========================================================>
class ImageResolutionView(APIView):
    parser_classes = (MultiPartParser,)
    def post(self, request):
        data = request.data

        print("========================>", request.data)
        serializer = ImageProcessSerializer(data=data)
        img_data = request.data["input"]
        print("IMGdata====================================================>", request.data["input"])

        


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
            img = Image.open(img_data)
            R = img.convert('RGB')
            R.save(f'media/new_img_pdf{LastImg.pk}.pdf')
            LastImg.pdf = f'new_img_pdf{LastImg.pk}.pdf'


            # Open the image
            image = Image.open(img_data)

            # # Convert the image to SVG
            with io.BytesIO() as buffer:
                image.save(buffer, format='PNG')
                image_data = buffer.getvalue()
                image_base64 = base64.b64encode(image_data).decode('utf-8')
                svg_data = svgwrite.Drawing(filename=f'media/image{LastImg.pk}.svg')
                svg_data.add(svgwrite.image.Image(href=f"data:image/png;base64,{image_base64}", insert=(0, 0), size=image.size))
                svg_data.save()
                LastImg.svg = f'image{LastImg.pk}.svg'

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
        



