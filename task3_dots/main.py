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