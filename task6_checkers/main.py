import numpy as np
import cv2

import cellClassifier
from cellClassifier import getMark, CellType
import settings
from settings import xStep, yStep, PLAY_SELLS
from snippets import imageShow, waitEnter
from transformations import getTransformed, pointsCell

videoWidth = None
videoHeight = None
videoFps = None

testImg = cv2.imread('resources/testImg.png')


def getBoard():
    img = np.zeros((settings.HEIGHT, settings.WIDTH, 3), np.uint8)
    img.fill(250)

    for (i, j) in PLAY_SELLS:
        cv2.rectangle(img, (j * xStep, i * yStep), ((j + 1) * xStep, (i + 1) * yStep), (30, 30, 30), -1)
    return img


def cellMarks(img):
    marks = {(i, j): getMark(img, i, j) for (i, j) in PLAY_SELLS}
    return marks


def drawCells(img, marks):
    for (i, j) in marks.keys():


        if (marks[(i, j)] == CellType.RED):
            cv2.ellipse(img, 
                        (j * xStep + xStep / 2, i * yStep + yStep / 2), # position 
                        ((xStep - 20) / 2, (yStep - 20) / 2 ), 0,       # size
                        360, 0, (15, 15, 230),                            # from, to angle and color
                        -1)                                             # fill
            # cv2.circle(img, (j * xStep + xStep / 2, i * yStep + yStep / 2), 10, (0, 0, 255), -1)
        if (marks[(i, j)] == CellType.WHITE):
            cv2.ellipse(img, 
                        (j * xStep + xStep / 2, i * yStep + yStep / 2), # position 
                        ((xStep - 20) / 2, (yStep - 20) / 2 ), 0,       # size
                        360, 0, (230, 230, 230),                            # from, to angle and color
                        -1)                                             # fill

        if (marks[(i, j)] == CellType.UNDEFINED):
            cv2.putText(img, '?', (j * xStep + xStep / 2 - 10, i * yStep + yStep / 2 + 7),
                        cv2.cv.CV_FONT_HERSHEY_TRIPLEX, 1.0, (255, 255, 255))


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