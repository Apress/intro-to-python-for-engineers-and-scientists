import matplotlib.pyplot as pl
import numpy as np 
x = np.random.rand(1000)
y = np.random.rand(1000)
pl.scatter(x,y)
pl.title('Scatter Chart')
pl.xlabel('$x$')
pl.ylabel('$y$')
pl.show()