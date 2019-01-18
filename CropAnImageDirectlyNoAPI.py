import numpy as np
import cv2
import os

full_path = input('Enter full path of the image file including extension: ')
coordinates = input("Enter coordinates in the form of dictionary list - [{'x':value, 'y':value},{'x':value, 'y':value},...]: ")
save_path = input('Enter complete path of the cropped file to save including extension: ')
image = cv2.imread(full_path)
height = image.shape[0]
width = image.shape[1]
coordinates = eval(coordinates)
coordinates  = [(i['x'],i['y']) for i in coordinates]
mask = np.zeros((height, width), dtype=np.uint8)
points = np.array([coordinates ])
cv2.fillPoly(mask, points, (255))
res = cv2.bitwise_and(image, image, mask = mask)
rect = cv2.boundingRect(points)
cropped = res[rect[1]:rect[1]+rect[3], rect[0]:rect[0]+rect[2]]
cv2.imwrite(save_path, cropped)
