import numpy as np
import cv2
import os

IMAGE_NOISY_PATH = 'resources/noisy.png'
IMAGE_ORIGINAL_PATH = 'resources/original.png'

OUT_GAUSSIAN_PATH = 'out/gaussian.png'


img = cv2.imread(IMAGE_NOISY_PATH)
imgOriginal = cv2.imread(IMAGE_ORIGINAL_PATH)

if (img is None):
    print("Can't read image '" + IMAGE_NOISY_PATH + "'")
    exit(1)
    
if (imgOriginal is None):
    print("Can't read origial image '" + IMAGE_ORIGINAL_PATH + "'")
    exit(1)
    
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
imgOriginal = cv2.cvtColor(imgOriginal, cv2.COLOR_RGB2GRAY)

def noiseDiff(otherImage):
    diffSum = 0
    for i in range(0, otherImage.shape[0]):
        for j in range(0, otherImage.shape[1]):
            diffSum += max(img[i, j], imgOriginal[i, j]) - min(img[i, j], imgOriginal[i, j])
    return diffSum / (otherImage.shape[0] * otherImage.shape[1] * 1.0)

def gaussianFilter():
    return cv2.GaussianBlur(img, (5,5), 5)


# output
if not os.path.exists('out'):
    os.mkdir('out')
imgGaussian = gaussianFilter()

print("Gaussian noise cost: " + str(noiseDiff(imgGaussian)))

cv2.imwrite(OUT_GAUSSIAN_PATH, imgGaussian)

    