#"""append """"  ---# adding elements next to array

import numpy as np
arr = np.array([90,80,60])
arr1 = np.append(arr,[10,20,30])
print(arr)
print(arr1)

"""np.concatenate""" #-- merging two array

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.concatenate((arr1,arr2))
print(np.hstack((arr1,arr2)))
print(arr)


"""revome element - .delete"""

"""arr = np.array([10,20,20,30])
arr = np.delete(arr, [2])  
print(arr)""" # 1d

#2d 
arr_2d = arr.reshape(2,3)
print(arr_2d)
arr_2d = np.delete(arr_2d,[1],1)
print(arr_2d)#   0 = row - horizontla, 1 = column, vertical, 2 = depth 
