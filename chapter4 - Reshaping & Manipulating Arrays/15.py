"""stacking-- combing all arrays in  vertically and Hori.."""
# vstack() - row
#hstack() - column

import numpy as np
arr = np.array([1,2,3])
arr1 = np.array([4,5,6])

print(np.vstack((arr,arr1)))
print(np.hstack((arr,arr1)))


"""spiliting""" # - converting array into subarrays
""" np.split : equal
np.hsplit - hori
np.vsplit - vetrical

"""
import numpy as np
arr = np.array([1,2,3,4,5,6])
print(np.split(arr, 2))
print(np.hsplit(arr, 2))
#print(np.vsplit(arr, 2))  - only work on 2d or more dimention

