import cv2
import numpy as np
from drawMatches import drawMatches

sift = cv2.SIFT()
bf = cv2.BFMatcher()


def addSecondToFirst(imga, imgb):
    
    
    images = [
        # cv2.cvtColor(imga, cv2.COLOR_RGB2GRAY).astype(np.uint8), 
        # cv2.cvtColor(imgb, cv2.COLOR_RGB2GRAY).astype(np.uint8)
        imga,
        imgb
    ]
    
    imageKpDes = [sift.detectAndCompute(img, None) for img in images]

    matches = bf.knnMatch(imageKpDes[0][1], imageKpDes[1][1], k=2)

    per20 = len(matches) / 6
    good = sorted(matches, key=lambda (m, n): m.distance - n.distance)[:per20]
    good = [m[0] for m in good]

    leftPts = np.float32([imageKpDes[0][0][m.queryIdx].pt for m in good])
    rightPts = np.float32([imageKpDes[1][0][m.trainIdx].pt for m in good])

    H, mask = cv2.findHomography(rightPts, leftPts, cv2.RANSAC)

    cornerRT = np.float32([images[1].shape[1], 0])
    cornerRB = np.float32([images[1].shape[1], images[1].shape[0]])
    corners = np.float32([cornerRT, cornerRB])
    corners = np.float32([corners])
    corners = cv2.perspectiveTransform(corners, H)
    
    
    rightBorder = max(corners[0][0][0], corners[0][1][0])

    imgH = cv2.warpPerspective(images[1], H, (rightBorder, images[0].shape[0]))
    # cv2.imshow('sad',imgH)

    imgLines = drawMatches(images[0], imageKpDes[0][0], images[1], imageKpDes[1][0], good)
    cv2.imshow('img',imgLines)
    cv2.waitKey()

    resSize = (images[0].shape[0], rightBorder)
    res = np.zeros(resSize, images[0].dtype)

    for i in range(0, resSize[0]):
        for j in range(0, images[0].shape[1]):
            res[i, j] = images[0][i, j]

    for i in range(0, resSize[0]):
        for j in range(0, imgH.shape[1]):
            res[i, j] = max(imgH[i, j], res[i, j])

    return res