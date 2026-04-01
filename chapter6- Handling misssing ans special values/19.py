""" missing - 
built in function- 
1- np.isnan: detect missing values. nan = not a number. give boolean ans.
2- np.nan-to-num() : replaceing a no. with detected missing no.
3- np.isinf() : for detecting infinite values.
"""

import numpy as np
arr = np.array([np.nan,10,20,np.nan,40,50])
print(np.isnan(arr))
#print(np.nan = np.nan) means we can't compare it directly.

new_arr = np.nan_to_num(arr, nan = 100) # default value = 0
print(new_arr)

arr1 = np.array([1,2,3,np.inf,4,-np.inf])
print(np.isinf(arr1))
#print(np.isnan(arr1))



replace_arr1 = np.nan_to_num(arr1, posinf = 1000, neginf = -1000 ) 
print(replace_arr1)  # posinf = +ve, neginf = -ve

