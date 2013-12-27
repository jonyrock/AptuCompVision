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



# testImg = cv2.imread('resources/testImg.png')

videoOutFilePath = 'out.avi'

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
    img = cv2.resize(frame, (settings.WIDTH, settings.HEIGHT))
    # imageShow(img)
    img = getTransformed(img)
    

    board = getBoard()
    # imageShow(board)

    marks = cellMarks(img)
    drawCells(board, marks)
    
    return board


#getComicZoneFrame(testImg)

def getOutFrame(img):
    board = getComicZoneFrame(img)
    img = cv2.resize(img, (600, 400))
    board = cv2.resize(board, (400, 400))
    return np.concatenate((img, board), axis=1)

vc = cv2.VideoCapture('resources/vvvv.mpg')
videoWidth = int(vc.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))

videoFps = int(vc.get(cv2.cv.CV_CAP_PROP_FPS))

writer = cv2.VideoWriter(videoOutFilePath, cv2.cv.CV_FOURCC(*'MJPG'), 30,
                             (600+400, 400), True)


allLen = 10000
for i in range(allLen):
        isRead, frame = vc.read()
        if not isRead:
            break
        frame = getOutFrame(frame)
        writer.write(frame)
        print i , allLen
        
writer.release()
# imageShow(getOutFrame(testImg))
