import cv2
from backgroundFinder.avgBackgroundFinder import AvgBackgroundFinder
import snippents
import numpy as np

# global properties
videoFilePath = 'Cam1_Outdoor.mp4'
videoOutFilePath = 'out.avi'
backgroundFinder = AvgBackgroundFinder(videoFilePath)
backThreshold = 230

#global vars
videoWidth = None
videoHeight = None
videoFps = None

def main():
    print('Start video processing: ' + videoFilePath)
    print('Background computation with: ' + backgroundFinder.__class__.__name__)
    back = backgroundFinder.getBack().astype(np.uint8)
    print('Compute mask')
    computeMask(back)
    print('DONE')


def computeMask(back):
    vc = cv2.VideoCapture(videoFilePath)
    videoWidth = int(vc.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
    videoHeight = int(vc.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
    videoFps = int(vc.get(cv2.cv.CV_CAP_PROP_FPS))

    def ifThreshold(x, t):
        if abs(x) > t:
            return 255
        else:
            return 0

    diffToMaskMaker = np.vectorize(ifThreshold)
    # cv2.namedWindow('window', 0)
    writer = cv2.VideoWriter(videoOutFilePath, cv2.cv.CV_FOURCC(*'MJPG'), videoFps, 
                             (videoWidth, videoHeight), False)

    # while (True):
    for i in range(300):
        isRead, frame = vc.read()
        if not isRead:
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        frame = diffToMaskMaker(frame - back, backThreshold).astype(np.uint8)
        writer.write(frame)
        # cv2.imshow('window', frame)
        # k = cv2.waitKey()
        # if k == 27:
        #     break

    writer.release()


main()
cv2.destroyAllWindows()
