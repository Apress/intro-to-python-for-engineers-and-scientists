import matplotlib.pyplot as pl 
import numpy as np 

r = np.arange(0, 10.0, 0.1)
theta = 2* np.pi * r

pl.polar(theta, r, color ='g') 
pl.show()