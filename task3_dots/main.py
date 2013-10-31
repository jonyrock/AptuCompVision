import numpy as np
import cv2
import os

IMAGE_ORIGINAL_PATH = 'resources/original.png'
IMAGE_TRANSFORMED_PATH = 'resources/transformed.png'
THRESHOLD = 0.1

imgA = cv2.imread(IMAGE_ORIGINAL_PATH)
imgAGray = cv2.cvtColor(imgA,cv2.COLOR_BGR2GRAY)
imgB = cv2.imread(IMAGE_TRANSFORMED_PATH)
imgBGray = cv2.cvtColor(imgB,cv2.COLOR_BGR2GRAY)

dstA = cv2.cornerHarris(imgAGray,3,3,0.04)
dstA = cv2.dilate(dstA,None)

dstB = cv2.cornerHarris(imgBGray,3,3,0.04)
dstB = cv2.dilate(dstB,None)

# Threshold for an optimal value, it may vary depending on the image.
imgA[dstA>0.1*dstA.max()]=[0,0,255]
imgB[dstB>0.1*dstB.max()]=[0,0,255]

img = np.concatenate((imgA, imgB), axis=1)

# for ai in range(0, imgA.shape[0]):
#     for aj in range(0, imgA.shape[1]):
        

cv2.imshow('dsttt',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

# output
if not os.path.exists('out'):
    os.mkdir('out')
    
    











