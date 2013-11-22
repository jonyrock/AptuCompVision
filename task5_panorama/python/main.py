import cv2
import numpy as np
import panorama

IMAGE_01 = 'resources/shanghai/01.jpg'
IMAGE_02 = 'resources/shanghai/02.jpg'
IMAGE_03 = 'resources/shanghai/03.jpg'


imagePaths = [IMAGE_01, IMAGE_02, IMAGE_03]

images = [cv2.resize(cv2.imread(imgPath, 0), (500, 500)) for imgPath in imagePaths]

res = images[0]
images = images[1:]
while len(images) > 0:
    res = panorama.addSecondToFirst(res, images[0])
    images = images[1:]

cv2.imshow('Lines', res)

while (cv2.waitKey() != 1048586): None
# plt.imshow(img3),plt.show()






