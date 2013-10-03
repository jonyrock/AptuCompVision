from abc import ABCMeta, abstractmethod
import cv2


class BackgroundFinder:
    def __init__(self, path):
        self.path = path
        self.vc = cv2.VideoCapture(path)
        self.width = int(self.vc.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
        self.height = int(self.vc.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))

    @abstractmethod
    def getBack(self):
        raise Exception('Not implemented')