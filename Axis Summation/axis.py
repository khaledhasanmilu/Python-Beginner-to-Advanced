import numpy as np
arr1 = np.array([1,2,3,4])
print(np.sum(arr1))
mat = np.array([
    [1,2,3],
    [4,5,6],
    [3,4,5]
])
mat.shape
print("Colum wise Sum:")
print(np.sum(mat,axis=1)) # colum wisw aum
print("Row wise Sum:")
print(np.sum(mat,axis=0)) #row wise sum
#3d  array
mat = np.array([
    [
        [1,2,3],
        [2,3,3],
        [2,3,3]
    ],
    [
        [1,2,3],
        [2,3,3],
        [2,3,3]
    ]
])
print(mat.shape)
print(np.sum(mat,axis=0))
print(np.sum(mat,axis=1))
print(np.sum(mat,axis=2))