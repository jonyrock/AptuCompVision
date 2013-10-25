import numpy as np
import cv2
import os

IMAGE_ORIGINAL_PATH = 'resources/original.png'
IMAGE_TRANSFORMED_PATH = 'resources/transformed.png'

imgA = cv2.imread(IMAGE_ORIGINAL_PATH)
imgB = cv2.imread(IMAGE_TRANSFORMED_PATH)


# output
if not os.path.exists('out'):
    os.mkdir('out')
    
    
import cv2
import numpy as np

filename = IMAGE_ORIGINAL_PATH
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.1*dst.max()]=[0,0,255]

cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()