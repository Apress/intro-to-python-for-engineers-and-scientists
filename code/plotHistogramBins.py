import matplotlib.pyplot as pt
import numpy as np

a = np.random.rand(50)
pt.hist(a,25) # setting number of bins to 25
pt.show()