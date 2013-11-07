import cv2
import numpy as np
import random

IMAGE_ORIGINAL_PATH = 'resources/original.png'
IMAGE_TRANSFORMED_PATH = 'resources/transformed.png'
THRESHOLD = 0.09

img1 = cv2.imread(IMAGE_ORIGINAL_PATH, 0)       # queryImage
img2 = cv2.imread(IMAGE_TRANSFORMED_PATH, 0)    # trainImage

# Initiate SIFT detector
sift = cv2.SIFT()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)

# Apply ratio test
good = []
for m, n in matches:
    if m.distance < THRESHOLD * n.distance:
        good.append([m])


def drawMatches(imga, kpa, imgb, kpb, matches):
    linea = np.concatenate((imga, imgb), axis=1)
    linea = cv2.cvtColor(linea, cv2.COLOR_GRAY2RGB)
    for m in matches:
        pta = (int(kpa[m[0].queryIdx].pt[0]), int(kpa[m[0].queryIdx].pt[1]))
        ptb = (int(kpb[m[0].trainIdx].pt[0]) + imga.shape[0], int(kpb[m[0].trainIdx].pt[1]))
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        cv2.line(linea, pta, ptb, color, 1)
        # cv2.line(linea, pt1, pt2, (0,0,255), 3)
        # None

    return linea


# cv2.drawMatchesKnn expects list of lists as matches.
imgRes = drawMatches(img1, kp1, img2, kp2, good)
cv2.imshow('Result', imgRes)


# goodGood = []
# for m, n in good:
#     rightFriend = n[0]
#     for m, n in good:    

imgRes2 = drawMatches(img1, kp1, img2, kp2, good)
cv2.imshow('Result', imgRes)

while (cv2.waitKey() != 10): None
# plt.imshow(img3),plt.show()






