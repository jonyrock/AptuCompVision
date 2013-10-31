import numpy as np
import cv2

IMAGE_ORIGINAL_PATH = 'resources/original.png'

OUT_NOISY_PATH = 'out/noisy.png'
OUT_GAUSSIAN_PATH = 'out/gaussian.png'
OUT_BILATERIAL_PATH = 'out/bilaterial.png'
OUT_NONLOCALMEANS_PATH = 'out/nonlocalmeans.png'

imgOriginal = cv2.imread(IMAGE_ORIGINAL_PATH)

if (imgOriginal is None):
    print("Can't read original image '" + IMAGE_ORIGINAL_PATH + "'")
    exit(1)

imgOriginal = cv2.cvtColor(imgOriginal, cv2.COLOR_RGB2GRAY)

def getNoised(image):
    noise = np.zeros(image.shape)
    cv2.randn(noise, 0, 5)
    noise = noise.astype(np.int32)
    noise[noise < 0] = 0
    res = image.astype(np.int32) + noise
    res[res < 0] = 0
    res[res > 255] = 255
    return res.astype(np.uint8)
    
imgNoisy = getNoised(imgOriginal)

def noiseDiff(otherImage):
    resMat = np.zeros(otherImage.shape).astype(otherImage.dtype)
    for i in range(0, otherImage.shape[0]):
        for j in range(0, otherImage.shape[1]):
            resMat[i, j] = max(otherImage[i, j], imgOriginal[i, j]) - min(otherImage[i, j], imgOriginal[i, j])
    return resMat


def gaussianFilter():
    return cv2.GaussianBlur(imgNoisy, (5, 5), 5)


def bilaterialFilter():
    return cv2.bilateralFilter(imgNoisy, 5, 50, 100)


def nonlocalmeansFilter():
    return cv2.fastNlMeansDenoising(imgNoisy, h=5, templateWindowSize=10)


line0 = np.concatenate((imgOriginal, imgNoisy, noiseDiff(imgNoisy)), axis=1)
imgGaussian = gaussianFilter()
line1 = np.concatenate((imgNoisy, imgGaussian, noiseDiff(imgGaussian)), axis=1)

imgBilaterial = bilaterialFilter()
line2 = np.concatenate((imgNoisy, imgBilaterial, noiseDiff(imgBilaterial)), axis=1)
imgNonlocalmeans = nonlocalmeansFilter()
line3 = np.concatenate((imgNoisy, imgNonlocalmeans, noiseDiff(imgNonlocalmeans)), axis=1)

resKartina = np.concatenate((line1, line2, line3), axis=0)
cv2.imshow('Noisy image / Filtered / Diff', resKartina)

while (cv2.waitKey() != 27): None