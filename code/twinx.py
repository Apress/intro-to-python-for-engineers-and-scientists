import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0., 100, 1);
y1 = x**2;
# y1 is defined as square of x values
y2 = np.sqrt(x);
# y2 is defined as square root of x values

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(x, y1, 'bo');
ax1.set_ylabel('$x^{2}$');
ax2 = ax1.twinx() # twinx() function is used to show twinned x axes
ax2.plot(x, y2, 'k+');
ax2.set_ylabel('$\sqrt{x}$');
ax2.set_title('Same x axis for both y values');
plt.show()