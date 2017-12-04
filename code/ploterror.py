import matplotlib.pyplot as pl
import numpy as np 
x = np.arange(0, 4, 0.2) # generated data point from 0 to 4 with step of 0.2
y = x*2 # y = e^(-x)
err = np.array([ 0,.1,.1,.2,.1,.5,.9,.2,.9,.2,.2,.2,.3,.2,.3,.1,.2,.2,.3,.4]) 
pl.errorbar(x, y, yerr=err, ecolor='r')
pl.title('Error bar chart with symmetrical error')
pl.xlabel('$x$')
pl.ylabel('$y$')
pl.show()