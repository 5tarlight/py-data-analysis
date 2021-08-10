import numpy as np

arr = np.array([[1, 2, 3 ,4], [5, 6, 7, 8]])
print(arr.ndim, arr.shape)

print(np.zeros((2, 4, 2)))
print(np.empty(8, dtype='u4'))

arr = np.array([[1., 2., 3.], [4., 5., 6.]])
print(arr * arr)
print(arr - arr)
print(arr ** 0.5)
arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
print(arr2 > arr)

arr = np.arange(10)
arr_slice = arr[5:8]
arr_slice[1] = 12345 # Broadcasting
