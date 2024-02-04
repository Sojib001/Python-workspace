import numpy as np
import math as m
arr = np.array(range(10))
print(arr)

print(np.sqrt(arr))
list = list(map(m.sqrt, arr))
# list = list(map(np.sqrt, arr))
print(list)

print(np.max(arr))
print(np.mean(arr))
print(np.median(arr))
print(np.sign(arr))


