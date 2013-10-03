from abc import abstractmethod
import cv2
import pickle
import os


class BackgroundFinder:
    def __init__(self, path):
        self.path = path
        self.vc = cv2.VideoCapture(path)
        self.width = int(self.vc.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
        self.height = int(self.vc.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))


    def getBack(self):
        dumpPath = self.__class__.__name__ + '_computeBack.dump'
        if os.path.exists(dumpPath):
            f = open(dumpPath, 'r')
            res = pickle.load(f)
            f.close()
            return res
        res = self.computeBack()
        f = open(dumpPath, 'w')
        pickle.dump(res, f)
        f.close()
        return res

    @abstractmethod
    def computeBack(self):
        raise Exception('Not implemented')