from _weakref import CallableProxyType
import numpy as np
import cv2

#global vars
import settings
from snippets import imageShow, waitEnter
from transformations import getTransformed

videoWidth = None
videoHeight = None
videoFps = None

VIDEO_PATH = 'Cam1_Outdoor.mp4'

testImg = cv2.imread('resources/testimg.png')

PLAY_SELLS = [(i, j) for i in range(0, 8) for j in range(0, 8) if (i + j) % 2 == 1]

xStep = settings.WIDTH / 8
yStep = settings.HEIGHT / 8


class CellType:
    pass


CellType.EMPTY = 1
CellType.RED = 2
CellType.WHITE = 3
CellType.UNDEFINED = 4


def getBoard():
    img = np.zeros((settings.HEIGHT, settings.WIDTH, 3), np.uint8)
    img.fill(250)

    for (i, j) in PLAY_SELLS:
        cv2.rectangle(img, (j * xStep, i * yStep), ((j + 1) * xStep, (i + 1) * yStep), (30, 30, 30), -1)
    return cv2.GaussianBlur(img, (3, 3), 2)


def getMark(img, i, j):
    subm = img[i * yStep: (i + 1) * yStep, j * xStep: (j + 1) * xStep]
    avgA = subm[:, :, 0].mean()
    avgB = subm[:, :, 1].mean()
    avgC = subm[:, :, 2].mean()

    typesColors = [[70, 70, 70], [50, 50, 80], [110, 110, 110]]
    typesCost = []
    
    for i in range(0, len(typesColors)):
        cc = (typesColors[i][0] - avgA) ** 2 + (typesColors[i][1] - avgB) ** 2 + (typesColors[i][2] - avgC) ** 2
        typesCost.append(cc)
    
    minDist = float("inf")
    minI = -1
    for i in range(0, len(typesColors)):
        myDist = typesCost[i]
        if (myDist < minDist):
            minI = i + 1
            minDist = myDist


    return minI


def cellMarks(img):
    marks = {(i, j): getMark(img, i, j) for (i, j) in PLAY_SELLS}
    return marks


def drawCells(img, marks):
    for (i, j) in marks.keys():
        if (marks[(i, j)] == CellType.RED):
            cv2.circle(img, (j * xStep + xStep / 2, i * yStep + yStep / 2), 10, (0, 0, 255), -1)
        if (marks[(i, j)] == CellType.WHITE):
            cv2.circle(img, (j * xStep + xStep / 2, i * yStep + yStep / 2), 10, (255, 266, 266), -1)


def getComicZoneFrame(frame):
    img = cv2.resize(frame, (800, 448))

    # imageShow(img)
    img = getTransformed(img)
    imageShow(img)

    board = getBoard()
    # imageShow(board)

    marks = cellMarks(img)
    drawCells(board, marks)
    imageShow(board)


getComicZoneFrame(testImg)