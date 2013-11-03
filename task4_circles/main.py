import cv2
import numpy as np

# img = cv2.imread('resources/polygonsDrawedBold.png')
# img = cv2.imread('resources/map_s.png')
img = cv2.imread('resources/test2.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

edges = cv2.Canny(img, 150, 250)
edgesToDraw = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)


circles = cv2.HoughCircles(edges, cv2.cv.CV_HOUGH_GRADIENT, 2, 50) 
if circles != None:
    for x,y,r in circles[0]:
        cv2.circle(edgesToDraw, (x,y), r, (0, 255, 0), 2)

cv2.imshow('houghlines', edgesToDraw)
while (cv2.waitKey() != 10): None


cv2.destroyAllWindows()