import numpy as np
import cv2
import os

IMAGE_ORIGINAL_PATH = 'resources/original.png'
IMAGE_TRANSFORMED_PATH = 'resources/transformed.png'

imgA = cv2.imread(IMAGE_ORIGINAL_PATH)
imgAGray = cv2.cvtColor(imgA,cv2.COLOR_BGR2GRAY)
imgB = cv2.imread(IMAGE_TRANSFORMED_PATH)
imgBGray = cv2.cvtColor(imgB,cv2.COLOR_BGR2GRAY)

dst = cv2.cornerHarris(imgAGray,3,3,0.04)
dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
imgA[dst>0.1*dst.max()]=[0,0,255]


cv2.imshow('dsttt',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

# output
if not os.path.exists('out'):
    os.mkdir('out')
    
    











