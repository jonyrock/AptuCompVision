import numpy as np
import cv2

IMAGE_NOISY_PATH = 'resources/noisy.png'
IMAGE_ORIGINAL_PATH = 'resources/original.png'

img = cv2.imread(IMAGE_NOISY_PATH)
if (img is None):
    print("Can't read image '" + IMAGE_NOISY_PATH + "'")
    exit(1)
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

cv2.imwrite('out.png', img)

    