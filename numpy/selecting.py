import numpy as np

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Jeo'])
data = np.random.randn(7, 4)
print(data[names == 'Bob'])
print(data[names == 'Bob', 2:])
print(data[~(names == 'Bob')])
cond = names == 'Bob'
print(data[~cond]) # ~ : not, | : or, & : and
print(data[data < 0])
data[names != 'Joe'] = 7
print(data)

# Fancy selection
arr = np.arange(32).reshape((8, 4))
print(arr[[1, 5, 7, 2], [0, 3, 1, 2]]) # (1, 0), (5, 3) ...
print(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])

arr = np.arange(15).reshape((3, 5))
print(arr)
print(arr.T) # 축 전치

arr = np.random.randn(6, 3)
print(np.dot(arr.T, arr))

arr = np.arange(16).reshape((2, 2, 4))
print(arr)
print(arr.transpose((1, 0, 2)))
print(arr.swapaxes(1, 2))