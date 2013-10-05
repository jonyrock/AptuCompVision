import pickle
import cv2
from backgroundFinder.avgBackgroundFinder import AvgBackgroundFinder
import snippents
import numpy as np
import tools

# global properties
# videoFilePath = 'Cam1_Outdoor.mp4'
videoFilePath = 'car-overhead-1.avi'

videoOutFilePath = 'out.avi'
backgroundFinder = AvgBackgroundFinder(videoFilePath)
backThreshold = 30

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


def drawObjects(img, xs_recs):
    for (x, y, w, h) in xs_recs:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0))


def findObjects(mask):
    zeroMask = np.zeros((videoHeight + 2, videoWidth + 2)).astype(np.uint8)
    # snippents.imageShow(mask)
    res = []
    for i in range(videoHeight):
        for j in range(videoWidth):
            c = mask[i, j]
            if c == np.uint8(255) or c == np.uint8(100):
                continue
            (floodRes, floodRec) = cv2.floodFill(mask, zeroMask, (j, i), 100)
            
            res.append(floodRec)
            
    # snippents.imageShow(mask)
    return filter(lambda (x,y,w,h): w * h > 30 ,  res)


def computeMask(back):
    vc = cv2.VideoCapture(videoFilePath)
    global videoWidth, videoHeight, videoFps, zeroMask
    videoWidth = int(vc.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
    videoHeight = int(vc.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
    videoFps = int(vc.get(cv2.cv.CV_CAP_PROP_FPS))
    

    def ifThreshold(x, t):
        if abs(x) > t:
            return 0
        else:
            return 255

    diffToMaskMaker = np.vectorize(ifThreshold)
    # cv2.namedWindow('window', 0)
    writer = cv2.VideoWriter(videoOutFilePath, cv2.cv.CV_FOURCC(*'MJPG'), videoFps,
                             (videoWidth, videoHeight), True)

    # while (True):
    kernel = cv2.getStructuringElement(0, (1, 1))
    for i in range(1300):
        vc.read()

    for i in range(10):
        isRead, frame = vc.read()
        if not isRead:
            break

        originalFrame = frame
        mask = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY).astype(int)
        mask -= back.astype(int)
        mask = diffToMaskMaker(mask, backThreshold).astype(np.uint8)
        mask = cv2.dilate(mask, kernel)
        recs = findObjects(mask)
        drawObjects(originalFrame, recs)
        writer.write(originalFrame)

    writer.release()


main()
cv2.destroyAllWindows()
