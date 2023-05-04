x = int(input())
y = int(input())

import numpy as np
arr =[[0 for j in range(y)] for i in range(x)]

for i in range(x):
    for j in range(y):
        arr[i][j] = i * j

print(arr)