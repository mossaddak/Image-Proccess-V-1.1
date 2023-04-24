from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import (
    status
)
from .models import(
    ImageProcess,
    PdfToImage
)
from .serializer import(
    ImageProcessSerializer,
    PdfToImageSerializer
)
import base64
from rest_framework.parsers import MultiPartParser
from django.db import IntegrityError
from .models import (
    User
)
from rest_framework.permissions import (
    IsAuthenticated
)
from rest_framework_simplejwt.authentication import (
    JWTAuthentication
)

#image proccessing
import cv2
import numpy as np

#from rembg import remove
from PIL import Image
import svgwrite
import io
import base64
import os
import zipfile
from rembg import remove

from django.http import (
    Http404
)


# CImage Process==========================================================>
class ImageResolutionView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    parser_classes = (MultiPartParser,)

    def post(self, request):
        data = request.data
        print("========================>", request.data)
        if request.user.is_authenticated:
            serializer = ImageProcessSerializer(data=data)
            img_data = request.data["input"]
            if not img_data:
                return Response(
                    {
                        'message': 'Please provide a image file.'
                    }, status=status.HTTP_400_BAD_REQUEST)
            print("IMGdata====================================================>", request.data["input"])

            if serializer.is_valid():
                serializer.save()
                all_images = ImageProcess.objects.all()
                serializer = ImageProcessSerializer(all_images, many=True)
                LastImg = ImageProcess.objects.last()
                LastImgUrl = LastImg.input.url
                LastImg.user = request.user

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


                #background remove ===============================================>
                img = Image.open(LastImg.input.path)
                R = remove(img)
                R.save(f'media/bg_remove{LastImg.pk}.png')
                LastImg.bg_remove = f'bg_remove{LastImg.pk}.png'


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
                        'message': 'Image successfully processed.',
                        "data":serializer.data[-1]
                    },status=status.HTTP_200_OK
                )
            
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        else:
            return Response(
                {
                    "message":"Please log into your account."
                },status=status.HTTP_400_BAD_REQUEST 
            )
        
    def get(self,request):
        if request.user.is_superuser:
            all_proccessed_img = ImageProcess.objects.all()
            serializer = ImageProcessSerializer(all_proccessed_img, many=True)
            return Response(
                {
                    "data":serializer.data,
                    "message":"data fetch"
                }, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    "message":"You don't have the permission for this."
                }, status=status.HTTP_403_FORBIDDEN
            )


class AllImgResolutionDetailsView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get_processed_img(request, pk):
        try:
            return ImageProcess.objects.get(pk=pk)
        except ImageProcess.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        if request.user.is_superuser:
            processed_img = self.get_processed_img(pk)
            serializer = ImageProcessSerializer(processed_img)
            return Response(
                {
                    "data":serializer.data,
                    "message":"data fetch"
                },status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    "message":"you don't have permission for this action."
                },status=status.HTTP_204_NO_CONTENT
            )


    
    def delete(self, request, pk):
        if request.user.is_superuser:
            processed_img = self.get_processed_img(pk).delete()
            return Response(
                {
                    "message":"Item Successfully Deleted."
                }, status=status.HTTP_204_NO_CONTENT
            )
        else:
            return Response(
                {
                    "message":"you don't have permission for this action."
                }, status=status.HTTP_403_FORBIDDEN
            )
        



#pdf manupulation================================================================>
class PdfToImageView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    parser_classes = (MultiPartParser,)
    def post(self, request):
        data = request.data

        if request.user.is_authenticated:
            pdf_file = request.data.get('input', None)
            if not pdf_file:
                return Response({'error': 'Please provide a PDF file.'}, status=status.HTTP_400_BAD_REQUEST)

            serializer = PdfToImageSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                last_pdf = PdfToImage.objects.last()
                last_pdf_url = last_pdf.input
                last_pdf.user = request.user
                poppler_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'poppler-23.01.0', 'Library', 'bin'))
                pdf_path = last_pdf_url.path
                saving_folder = "media/"
                from pdf2image import convert_from_path
                
                pages=convert_from_path(pdf_path=pdf_path,poppler_path=poppler_path)
                print("New Last URL=========================================================>", last_pdf_url)
                zip_filename = f'new_img{last_pdf.pk}.zip'
                with zipfile.ZipFile(os.path.join(saving_folder, zip_filename), 'w') as myzip:
                    c=1
                    for page in pages:
                        img_name = f"img-{c}.png"
                        with myzip.open(img_name, 'w') as myfile:
                            page.save(myfile, 'PNG')
                        c += 1

                last_pdf.images_zip_file = f'new_img{last_pdf.pk}.zip'
                last_pdf.save()
                return Response(
                    {
                        'message': 'PDF to image successfully converted.',
                        'data':serializer.data,
                    }, status=status.HTTP_201_CREATED
                )
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {
                    "message":"Please log into your account."
                },status=status.HTTP_400_BAD_REQUEST
            )
    
    def get(self,request):
        if request.user.is_superuser:
            all_proccessed_img = PdfToImage.objects.all()
            serializer = PdfToImageSerializer(all_proccessed_img, many=True)
            
            return Response(
                {
                    "data":serializer.data,
                    "message":"data fetch"
                }, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    "message":"You don't have the permission for this."
                }, status=status.HTTP_403_FORBIDDEN
            )
        



class AllPdfToImageView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get_processed_img(request, pk):
        try:
            return PdfToImage.objects.get(pk=pk)
        except PdfToImage.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        if request.user.is_superuser:
            processed_img = self.get_processed_img(pk)
            serializer = PdfToImageSerializer(processed_img)
            return Response(
                {
                    "data":serializer.data,
                    "message":"data fetch"
                },status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    "message":"you don't have permission for this action."
                },status=status.HTTP_204_NO_CONTENT
            )


    
    def delete(self, request, pk):
        if request.user.is_superuser:
            self.get_processed_img(pk).delete()
            return Response(
                {
                    "message":"Item Successfully Deleted."
                }, status=status.HTTP_204_NO_CONTENT
            )
        else:
            return Response(
                {
                    "message":"you don't have permission for this action."
                }, status=status.HTTP_403_FORBIDDEN
            )