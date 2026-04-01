"""insert"""

import numpy as np
arr = np.array([1,2,3,4,5,6,7])
print(arr)

arr = np.insert(arr, 2, 10) # insert 10 at index 2
print(arr)

"""arr_2d = arr.reshape(2,4)
print(arr_2d)
print(arr_2d.ndim)

new_arr_2d = np.insert(arr_2d, 1, [9,0,], axis=0) # act in row  
new_arr_2d = np.insert(arr_2d, 1, [9,0,3], axis=1) #act in column - shape based
print(new_arr_2d)
"""

"""for 3d """
arr_3d = arr.reshape(2,2,2) # [block, row, column]
print(arr_3d)
arr_3d = np.insert(arr_3d, 2, [[11,22] ,[33,44]], axis = 0)
print(arr_3d)        

                    #"""| = which array
                            #| = page 
                                #| =elements
                                                    #| = 
#"""

"""reshape(2,2,2) 
          |=page 
            |=row
            | =column """


