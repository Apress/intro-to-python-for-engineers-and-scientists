import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0., 10, 0.01)

fig = plt.figure()

ax1 = fig.add_subplot(221)
y1 = np.log(x)
ax1.plot(x, y1);
ax1.grid(True)
ax1.set_ylabel('$y = log(x)$');
ax1.set_title('y-axis in log scale')

ax2 = fig.add_subplot(222)
y2 = np.sin(np.pi*x/2.)
ax2.semilogx(x, y2, basex = 3);
ax2.grid(True)
ax2.set_title('x-axis in log scale')

ax3 = fig.add_subplot(223)
y3 = np.sin(np.pi*x/3.)
ax3.loglog(x, y3, basex=2);
ax3.grid(True)
ax3.set_ylabel('both axes in log');

ax4 = fig.add_subplot(224)
y4 = np.cos(2*x)
ax4.loglog(x, y3, basex=10);
ax4.grid(True)

plt.show()