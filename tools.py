import numpy as np


def map3dTo2d(arr, f):
    '''
        Get ndarray with size (w,h,3) and function f: a->a->-a->b
        and return ndarray[w,h] type b
    '''
    ftype = type(f(arr[0, 0, 0], arr[0, 0, 1], arr[0, 0, 2]))
    (height, width, _) = arr.shape
    res = np.ndarray(shape=(height, width), dtype=ftype)
    for i in range(0, height):
        for j in range(0, width):
            res[i, j] = f(arr[i, j, 0], arr[i, j, 1], arr[i, j, 2])
    return res
