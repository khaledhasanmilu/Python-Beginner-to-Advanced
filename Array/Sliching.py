import numpy as np
mat = np.array([
    [1,2,3],
    [4,5,6]
])
temp = mat[:,::2] # first to last
temp=mat[:,::-2]    #last to first
temp = mat[0:,1:]
print(temp)