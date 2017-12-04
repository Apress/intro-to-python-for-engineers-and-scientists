import numpy as np
from matplotlib import pylab as pl
x = np.linspace(0,100)
y1 = x ** 2 # y is square of x
y2 = x ** 2.2 # y is x raised to power 2.2
pl.plot(x,y1)
pl.plot(x,y2)
pl.show()