import pickle
import cv2, numpy as np

def waitEnter():
    while True: 
        key = cv2.waitKey()
        if key == 1048586 or key == 10:
            break

def imageShow(image):
    # cv2.namedWindow('window', 0)
    cv2.imshow('window', image)
    waitEnter()


def imageShowTest():
    image = cv2.imread('testImg.jpg')
    imageShow(image)


def imageAccessTest():
    image = cv2.imread('testImg.jpg')
    print image[:, 1:3]



