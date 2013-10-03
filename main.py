import cv2
from backgroundFinder.avgBackgroundFinder import AvgBackgroundFinder
import snippents

videoFilePath = 'Cam1_Outdoor.avi'
backgroundFinder = AvgBackgroundFinder(videoFilePath)


def main():
    print('Start video processing: ' + videoFilePath)
    print('Background computation with: ' + backgroundFinder.__class__.__name__)
    computeMask()
    print('DONE')

def computeMask():
    
    back = backgroundFinder.getBack()
    # snippents.imageShow(cv2.cv.fromarray(back.T))
    cv2.imshow('Image', back.T)
    


main()