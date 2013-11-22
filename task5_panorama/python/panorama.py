import cv2
import numpy as np

sift = cv2.SIFT()
bf = cv2.BFMatcher()


def addSecondToFirst(imga, imgb):
    images = [imga, imgb]
    imageKpDes = [sift.detectAndCompute(img, None) for img in images]

    matches = bf.knnMatch(imageKpDes[0][1], imageKpDes[1][1], k=2)

    per20 = len(matches) / 5
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
    cornersRT, cornersRB = corners[0][0], corners[0][1]
    
    rightBorder = max(cornersRT[0], cornersRB[0])

    imgH = cv2.warpPerspective(images[1], H, (rightBorder, images[0].shape[1]))

    # imgLines = drawMatches(images[0], imageKpDes[0][0], images[1], imageKpDes[1][0], good)

    resSize = (images[0].shape[0], rightBorder)
    res = np.zeros(resSize, images[0].dtype)

    for i in range(0, resSize[0]):
        for j in range(0, images[0].shape[1]):
            res[i, j] = images[0][i, j]

    for i in range(0, resSize[0]):
        for j in range(0, imgH.shape[1]):
            res[i, j] = max(imgH[i, j], res[i, j])

    return res