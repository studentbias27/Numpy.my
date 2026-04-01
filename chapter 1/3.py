# with default -
#no.zeros(shape) (3) for 1d, (3,3) 2d

import numpy as np
zeros_array = np.zeros(3) #shape 1d
#zeros_array[2] = 1
print(zeros_array)

#for ones

import numpy as np
array = np.ones((3,2)) # shape 3,2

print(array)

# for specific
#full(shape, value)
import numpy as np
s_array = np.full((2,2),5) # shape 3,2

print(s_array)


