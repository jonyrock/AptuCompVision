
import cv2

def imageShow(image):
    cv2.namedWindow('window', 0)
    cv2.imshow('window', image)
    cv2.waitKey()

def imageShowTest():
    image = cv2.imread('testImg.jpg')
    imageShow(image)
    
def imageAccessTest():
    image = cv2.imread('testImg.jpg')
    print image[:, 1:3]
