from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from imageprocessing.settings import MEDIA_ROOT
from .serializers import FileSerializer

import base64
import os
import numpy as np
import cv2


class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            imgpath = file_serializer['file']
            if not str(imgpath.value).endswith(('.jpeg', 'jpg', '.png')):
                return Response('Please upload an image file only')
            imgpath = os.getcwd() + imgpath.value
            pts = eval(file_serializer['coordinates'].value)
            cropped_image_path = cropfunction(imgpath, pts)
            with open(cropped_image_path, 'rb') as imgfile:
                encoded_string = base64.b64encode(imgfile.read())
                return Response(encoded_string)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def cropfunction(imgpath, pts):
    img = cv2.imread(imgpath)
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
    image_path = os.path.join(MEDIA_ROOT, os.path.splitext(imgpath)[0] + '_cropped.png')
    cv2.imwrite(image_path, cropped)
    return image_path
