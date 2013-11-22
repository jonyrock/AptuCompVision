import cv2
import panorama
import tests


imagePaths = tests.test3
images = [cv2.resize(cv2.imread(imgPath, 0), None, fx = 0.2, fy = 0.2) for imgPath in imagePaths]

res = images[0]
images = images[1:]
while len(images) > 0:
    res = panorama.addSecondToFirst(res, images[0])
    images = images[1:]

cv2.imshow('Lines', res)

while (cv2.waitKey() != 1048586): None
# plt.imshow(img3),plt.show()






