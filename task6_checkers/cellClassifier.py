from settings import xStep, yStep, CELL_MASK_PATH, CELL_MASK_UNDEFINED_PATH
import numpy as np
import cv2
from snippets import imageShow


class CellType:
    pass


CellType.EMPTY = 1
CellType.RED = 2
CellType.WHITE = 3
CellType.UNDEFINED = 4

typesColors = [[11, 11, 11], [7, 7, 15], [24, 24, 24]]
undefinedColor = [77, 77, 77]

maskImg = cv2.imread(CELL_MASK_PATH)
maskImg = cv2.cvtColor(maskImg, cv2.COLOR_RGB2GRAY)
maskImg = maskImg / 255.0

maskImgUndefined = cv2.imread(CELL_MASK_UNDEFINED_PATH)
maskImgUndefined = cv2.cvtColor(maskImgUndefined, cv2.COLOR_RGB2GRAY)
maskImgUndefined / 255.0


def transformCellMask():
    global maskImg, maskImgUndefined
    points1 = np.array([[0, 0], [maskImg.shape[0], 0], [0, maskImg.shape[1]], [maskImg.shape[0], maskImg.shape[1]]],
                       np.float32)
    points2 = np.array([[0, 0], [xStep, 0], [0, yStep], [xStep, yStep]], np.float32)
    (H, _) = cv2.findHomography(points1, points2)
    maskImg = cv2.warpPerspective(maskImg, H, (xStep, yStep))
    maskImgUndefined = cv2.warpPerspective(maskImgUndefined, H, (xStep, yStep))


transformCellMask()


def getMark(img, i_, j_):
    global typesColors, denim

    subm = img[i_ * yStep: (i_ + 1) * yStep, j_ * xStep: (j_ + 1) * xStep]

    avgA = np.multiply(subm[:, :, 0], maskImg).mean()
    avgB = np.multiply(subm[:, :, 1], maskImg).mean()
    avgC = np.multiply(subm[:, :, 2], maskImg).mean()

    avgAU = np.multiply(subm[:, :, 0], maskImgUndefined).mean()
    avgBU = np.multiply(subm[:, :, 1], maskImgUndefined).mean()
    avgCU = np.multiply(subm[:, :, 2], maskImgUndefined).mean()

    if i_ == 0 and j_ == 3:
        # imageShow(subm)
        k = 12

    undefinedCost = (undefinedColor[0] - avgAU) ** 2 + (undefinedColor[1] - avgBU) ** 2 + (undefinedColor[2] - avgCU) ** 2
    if undefinedCost > 60:
        return 4

    typesCost = []

    for i in range(0, len(typesColors)):
        cc = (typesColors[i][0] - avgA) ** 2 + (typesColors[i][1] - avgB) ** 2 + (typesColors[i][2] - avgC) ** 2
        cc = int(cc)
        typesCost.append(cc)

    minDist = float("inf")
    minI = -1
    for i in range(0, len(typesColors)):
        myDist = typesCost[i]
        if (myDist < minDist):
            minI = i + 1
            minDist = myDist


    return minI
