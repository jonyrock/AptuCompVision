import numpy as np
import cv2

import cellClassifier
from cellClassifier import getMark, CellType
import settings
from settings import xStep, yStep, PLAY_SELLS
from snippets import imageShow, waitEnter
from transformations import getTransformed

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