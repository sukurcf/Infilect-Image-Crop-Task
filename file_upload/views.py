import os

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
import numpy as np
from .serializers import FileSerializer

import cv2

class FileView(APIView):

    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data = request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            img = file_serializer['file']
            if not str(img.value).endswith(('.jpeg', 'jpg', '.png')):
                return Response('Please upload an image file only')
            img = os.getcwd()+img.value
            print(img)
            pts = eval(file_serializer['coordinates'].value)
            print('pts:', type(pts))
            cropfunction(img, pts)
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def cropfunction(img, pts):
    img = cv2.imread(img)
    height = img.shape[0]
    width = img.shape[1]
    pts = eval(pts)
    pts = [(i['x'], i['y']) for i in pts]
    mask = np.zeros((height, width), dtype=np.uint8)
    pts = np.array([pts])
    cv2.fillPoly(mask, pts, (255))
    res = cv2.bitwise_and(img, img, mask=mask)
    rect = cv2.boundingRect(pts)
    cropped = res[rect[1]:rect[1] + rect[3], rect[0]:rect[0] + rect[2]]
    cv2.imwrite('/home/sukumar/Downloads/cropped.png', cropped)
