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


def computeMask(back):
    vc = cv2.VideoCapture(videoFilePath)
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

    for i in range(1):
        isRead, frame = vc.read()
        if not isRead:
            break

        originalFrame = frame
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY).astype(int)
        
        frame -= back.astype(int)
        # frame = tools.map3dTo2d(frame, lambda r, g, b: int(abs(r)) + abs(g) + abs(b))
        frame = diffToMaskMaker(frame, backThreshold).astype(np.uint8)

        # if(i > 1500):
        frame = cv2.dilate(frame, kernel)
        # if i == 3000:
        #     kernel = cv2.getStructuringElement(0, (6, 6))
        # if i == 4500:
        #     kernel = cv2.getStructuringElement(1, (6, 6))

        # cv2.imwrite('img' + str(i) + '.jpg', frame)
        
        # writer.write(originalFrame)
        # writer.write(frame)
        
        cv2.imwrite('img1.jpg', originalFrame)
        dumpPath = 'imgMask.dump'
        f = open(dumpPath, 'w')
        pickle.dump(frame, f)
        f.close()
        # cv2.imshow('window', frame)
        # k = cv2.waitKey()
        # if k == 27:
        #     break

    writer.release()


main()
cv2.destroyAllWindows()
