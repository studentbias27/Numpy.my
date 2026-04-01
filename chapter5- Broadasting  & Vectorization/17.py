"""types of broadcasting--
1- same no. of elements dimantion - [1,2], [2,3] 
2- single element - [1,2,3], [3]  # 3to1
3- incompatible - [1,2,3], [1,2] # gives error due to dimention or shape mismatch.
but can solve by reshape
"""
import numpy as np
list = np.array([10,20,30])
result = list * [10] # single element
print(result)

"""vector(1d) to matrix(2d)"""

vector = np.array([10,20,30])
matrix = np.array(([20,30,40], [40,50,60]))
result = vector + matrix
print(result)