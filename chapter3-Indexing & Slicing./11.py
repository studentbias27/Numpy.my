"""Fancy indexing""" # selecting multiple element at ones.

import numpy as np
arr = np.array([10,20,30,40,50])
print(arr[[1, 0 ,4]])  # pass as a list

""" boolean masking or filtering data based on conditions"""

import numpy as np
arr = np.array([1,2,3,4,5,6])
print(arr[arr > 3 ])