import cv2, numpy as np


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


def testWrite():
    img1 = cv2.imread('test1.jpg')
    img2 = cv2.imread('test1.jpg')
    img3 = cv2.imread('test1.jpg')
    
    height , width , layers =  img1.shape
    
    video = cv2.VideoWriter('video.avi', cv2.cv.CV_FOURCC(*'MJPG'), 1,(width,height))
    
    video.write(img1)
    video.write(img2)
    video.write(img3)
    
    cv2.destroyAllWindows()
    video.release()
    
def testDilate():
    frame = cv2.imread('img1.jpg')
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    # cv2.getStructuringElement()
    kernel = cv2.getStructuringElement(0, (6, 5))
    frame = cv2.erode(frame, kernel)
    imageShow(frame)
    
    
# testWrite()

# testDilate()