import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-5*(np.pi), 5*(np.pi),200)
y =np.sin(x)
z =np.cos(x)

ax.scatter(x, y, z, marker='*')

ax.set_xlabel('$x$')
ax.set_ylabel('$y = sin(x)$')
ax.set_zlabel('$z = cos(x)$')
ax.set_title('Scatter plot in 3D')

plt.show()

