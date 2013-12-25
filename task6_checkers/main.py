import numpy as np
import cv2

#global vars
from snippets import imageShow

videoWidth = None
videoHeight = None
videoFps = None

VIDEO_PATH = 'Cam1_Outdoor.mp4'

testImg = cv2.imread('resources/testimg.png')

WIDTH = 800
HEIGHT = 448

points1 = [[332, 240], [1057, 233], [174, 670], [1227, 663]]
ratio =  WIDTH * 1.0 / 1366
points1 = [[int(x * ratio), int(y * ratio)] for x,y in points1 ]
points2 = [[0, 0], [WIDTH, 0], [0, HEIGHT], [WIDTH, HEIGHT]]
points1 = np.array(points1, np.float32)
points2 = np.array(points2, np.float32)

def drawPoints(img):
    for x, y in points1:
        cv2.circle(img, (x, y), 2, (30, 200, 30), 3)
    


def getTransformed(img):
    (H, _) = cv2.findHomography(points1, points2)
    
    imgH = cv2.warpPerspective(img, H, (WIDTH, HEIGHT))
    
    return imgH


def getComicZoneFrame(frame):
    img = cv2.resize(frame, (800, 448))
    drawPoints(img)
    imageShow(img)
    img = getTransformed(img)
    imageShow(img)


getComicZoneFrame(testImg)