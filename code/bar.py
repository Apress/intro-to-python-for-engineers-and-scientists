import matplotlib.pyplot as pl
import numpy as np 
x = np.array([1,2,3,4,5,6,7,8,9,0])
y = np.array([1,4,2,3,4,5,7,6,8,7])
pl.bar(x, y)
pl.title('Vertical Bar chart')
pl.xlabel('$x$')
pl.ylabel('$y$')
pl.show()