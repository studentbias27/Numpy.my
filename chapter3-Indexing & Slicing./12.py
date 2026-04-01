"""reshape ---""" # reshape (row, column) if dimention are match
# does not return copy only gives view

import numpy as np 
arr = np.array([1,2,3,4,5,6,7,8])
#reshape_arr = arr.reshape(3,2)  - if element are 1,2,3,4,5,6
reshape_arr = arr.reshape(2,2,2)

print(reshape_arr)

"""Flattening - from multi dimentional array to 1d , opsite of reshape""" 
# ravel -- views
#flatten -- copy

import numpy as np
arr = np.array(([1,2,3], [4,5,6]))
print(arr.ravel())
print(arr.flatten())
