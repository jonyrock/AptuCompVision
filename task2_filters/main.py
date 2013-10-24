import numpy as np
import cv2
import os

IMAGE_NOISY_PATH = 'resources/noisy.png'
IMAGE_ORIGINAL_PATH = 'resources/original.png'

OUT_GAUSSIAN_PATH = 'out/gaussian.png'


img = cv2.imread(IMAGE_NOISY_PATH)
if (img is None):
    print("Can't read image '" + IMAGE_NOISY_PATH + "'")
    exit(1)
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


def gaussianFilter():
    return cv2.GaussianBlur(img, (5,5), 5)


# output
if not os.path.exists('out'):
    os.mkdir('out')
imgGaussian = gaussianFilter()
cv2.imwrite(OUT_GAUSSIAN_PATH, imgGaussian)

    