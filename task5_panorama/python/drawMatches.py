import numpy as np
import cv2
import random

def drawMatches(imga, kpa, imgb, kpb, matches):
    linea = np.concatenate((imga, imgb), axis=1)
    linea = cv2.cvtColor(linea, cv2.COLOR_GRAY2RGB)
    for m in matches:
        pta = (int(kpa[m.queryIdx].pt[0]), int(kpa[m.queryIdx].pt[1]))
        ptb = (int(kpb[m.trainIdx].pt[0]) + imga.shape[0], int(kpb[m.trainIdx].pt[1]))
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        cv2.line(linea, pta, ptb, color, 1)
    return linea
