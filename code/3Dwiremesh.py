from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

a = np.arange(-5, 5, 0.25)
b = np.arange(-5, 5, 0.25)
x, y = np.meshgrid(a, b)
z = np.sqrt(x**2 + y**2)

ax.plot_wireframe(x, y, z, rstride=2, cstride=2)

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z = \sqrt{x^{2}+y^{2}}$')
ax.set_title('Wiremesh type of 3D plot')

plt.show()

