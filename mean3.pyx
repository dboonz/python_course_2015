import cython
import numpy as np

@cython.boundscheck(False)
def mean3filter(double[::1] arr):
    # ::1 means that the array is contiguous
    cdef double[::1] arr_out = np.empty_like(arr)
    cdef int i
    for i in range(1, arr.shape[0]-1):
        #for j in range(3):
        arr_out[i] = arr[i-1] + arr[i] + arr[i+1]
        arr_out[i] *= 0.333333333333333333333333
        #arr_out[i] = np.sum(arr[i-1 : i+1]) / 3
    arr_out[0] = (arr[0] + arr[1]) / 2
    arr_out[-1] = (arr[-1] + arr[-2]) / 2
    return np.asarray(arr_out)
