import numpy as np
b = []
# for x in range(5):
#     y = int(input())
#     b.append(y)
arr = np.array(b)
print(arr)
print(arr.shape)

arr = np.arange(1, 10)
print('\n')
arr2 = np.zeros((2,10))
print(arr2)

print('\n')
arr2 = np.full((10), 6)
print(arr2)

print('\n')
arr2 = np.full((2, 10), 6)
print(arr2)

print('\n')
arr2 = np.full((3, 9), range(9))
print(arr2)

print(arr[1:5])
print(arr[1:])
print(arr[:-1:2])
print(arr[::2])

print(arr2[0:1, 2:4])
print('\n')
print(arr2[0:2, 2:4])