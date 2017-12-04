import matplotlib.pyplot as pl
import numpy as np
 
x = np.arange(10)
y1 = np.random.rand(10)
y2 = np.random.rand(10)

fig = pl.figure()


ax1 = fig.add_subplot(221)
ax1.plot(x,y1)

ax2 = fig.add_subplot(222)
ax2.scatter(x,y2)

ax3 = fig.add_subplot(223)
ax3.hist(y1)

ax4 = fig.add_subplot(224)
ax4.barh(x,y2)

pl.show()