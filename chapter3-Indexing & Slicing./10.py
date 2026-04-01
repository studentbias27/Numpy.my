"""Indexing """

import numpy as np
#2d array
arr = np.array(([10,20,30],
                [40,50,60],
                [70,80,90]))
print(arr[1,1])

""" Slicing--[start:end]""" #[start,end,step] exact portion in list
import numpy as np
arr = np.array([10,20,30,40,50,60])
print(arr[1:4])  # ending index = n-1(elemnet )
print(arr[:4])
print(arr[::2])
print(arr[0:5:2])
print(arr[1:4:2])
print(arr[0:5:3])
print(arr[::-1])   # - used  for reversing
print(arr[:-2])
print(arr[::-2])
print(arr[::-1])
