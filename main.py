import cv2
from backgroundFinder.avgBackgroundFinder import AvgBackgroundFinder
import snippents
import numpy as np

# global properties
videoFilePath = 'Cam1_Outdoor.avi'
backgroundFinder = AvgBackgroundFinder(videoFilePath)


def main():
    print('Start video processing: ' + videoFilePath)
    print('Background computation with: ' + backgroundFinder.__class__.__name__)
    back = backgroundFinder.getBack()
    print('Compute mask')
    computeMask(back)
    print('DONE')


def computeMask(back):
    vc = cv2.VideoCapture(videoFilePath)
    diffToMaskMaker = np.vectorize(lambda a,b : abs(a - b))
    while(True):
        isRead, frame = vc.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        frame = diffToMaskMaker(frame - back, 100)
        snippents.imageShow(frame)
        break



main()