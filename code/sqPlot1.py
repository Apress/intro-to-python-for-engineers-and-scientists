# Plotting number using pylab
import numpy as np
from matplotlib import pylab as pl
x = np.linspace(0,100)
y = x ** 2
pl.plot(x,y)
pl.show()