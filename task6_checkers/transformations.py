import numpy as np
import cv2

import settings

points1 = [[332, 240], [1057, 233], [174, 670], [1227, 663]]
ratio =  settings.WIDTH * 1.0 / 1366
points1 = [[int(x * ratio), int(y * ratio)] for x,y in points1 ]
points2 = [[0, 0], [settings.WIDTH, 0], [0, settings.HEIGHT], [settings.WIDTH, settings.HEIGHT]]
points1 = np.array(points1, np.float32)
points2 = np.array(points2, np.float32)
(H, _) = cv2.findHomography(points1, points2)

def drawPoints(img):
    for x, y in points1:
        cv2.circle(img, (x, y), 2, (30, 200, 30), 3)

def getTransformed(img):
    imgH = cv2.warpPerspective(img, H, (settings.WIDTH, settings.HEIGHT))
    return imgH

