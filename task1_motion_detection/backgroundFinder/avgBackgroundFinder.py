import numpy as np, cv2

from backgroundFinder import BackgroundFinder


class AvgBackgroundFinder(BackgroundFinder):
    def addFrame(self, frame):
        self.sumArr += frame

    def computeBack(self):
        self.sumArr = np.ndarray(shape=(self.height, self.width), dtype=np.long) * 0
        frameCount = 0
        while True:
            isRead, frame = self.vc.read()
            if not isRead:
                break
            frameCount += 1
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            self.addFrame(frame)
        if frameCount == 0:
            raise Exception("Can't read video")
        return self.sumArr / frameCount