import numpy as np
import cv2

import settings

points1 = [[332, 240], [1057, 233], [174, 670], [1227, 663]]
ratioX =  settings.WIDTH * 1.0 / 1366
ratioY =  settings.HEIGHT * 1.0 / 768
points1 = [[int(x * ratioX), int(y * ratioY)] for x,y in points1 ]
pointsCell = [[0, 0], [settings.WIDTH, 0], [0, settings.HEIGHT], [settings.WIDTH, settings.HEIGHT]]
points1 = np.array(points1, np.float32)
pointsCell = np.array(pointsCell, np.float32)
(H, _) = cv2.findHomography(points1, pointsCell)

def drawPoints(img):
    for x, y in points1:
        cv2.circle(img, (x, y), 2, (30, 200, 30), 3)

def getTransformed(img):
    imgH = cv2.warpPerspective(img, H, (settings.WIDTH, settings.HEIGHT))
    return imgH

