"""broadcasting - used for faster exucution for heavy data and skip loops need
allows arithmetic opertion in different-2 shapes and size.

"""

import numpy as np
prices = np.array([100,200,300])
discount = 15
final_prices = prices - (prices * discount/100)
print(final_prices)

