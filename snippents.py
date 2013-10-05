import pickle
import cv2, numpy as np
import tools


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

    height, width, layers = img1.shape

    video = cv2.VideoWriter('video.avi', cv2.cv.CV_FOURCC(*'MJPG'), 1, (width, height))

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


def getPObject(path):
    f = open(path)
    res = pickle.load(f)
    f.close()
    return res


def testFloodFill():
    frame = getPObject('imgMask.dump')
    img = cv2.imread('img1.jpg')
    mask = np.zeros((frame.shape[0] + 2, frame.shape[1] + 2), np.uint8)
    rec = cv2.floodFill(frame, mask, (263, 184), (10, 10, 10), 10, 10)
    (x, y, w, h) = rec[1]
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0))
    imageShow(img)


def testFloodFill2():
    img = cv2.imread('input2.png')
    seedPoint = (200, 200)
    # image, seed_point, new_val, lo_diff=None, up_diff=None, flags=None, mask=None
    mask = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    mask = tools.extendMat(mask, np.uint8(1)) * 0

    flags = 4 | cv2.FLOODFILL_FIXED_RANGE
    res = cv2.floodFill(img, mask, seedPoint, (0, 0, 255), (20, 20, 20), (20, 20, 20), flags)
    # cv2.circle(img, seedPoint, 3, 10, 3, 8)
    imageShow(img)

# testWrite()

testFloodFill()

# testDilate()
