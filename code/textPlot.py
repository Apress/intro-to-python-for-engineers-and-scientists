import matplotlib.pyplot as pl 
import numpy as np 
x = np.arange(0, 2*np.pi, .01) 
y = np.sin(x) 
pl.plot(x, y, color = 'r');
pl.text(0.1, -0.04, '$sin(0) = 0$')
pl.text(1.5, 0.9, '$sin(90) = 1$')
pl.text(2.0, 0, '$sin(180) = 0$')
pl.text(4.5, -0.9, '$sin(270) = -1$')
pl.text(6.0, 0.0, '$sin(360) = 1$')
pl.annotate('$sin(theta)=0$', xy=(3, 0.1), xytext=(5, 0.7), arrowprops=dict(facecolor='green', shrink=0.05))
pl.title('Inserting text and annotation in plots')
pl.xlabel('$theta$')
pl.ylabel('$y = sin( theta)$')
pl.show()