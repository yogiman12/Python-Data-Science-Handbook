import numpy as np
arr = np.array([1, 1, 2, 1, 0])
def Selection_sort(x):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    return x
print(Selection_sort(arr))