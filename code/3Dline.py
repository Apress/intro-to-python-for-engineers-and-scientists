import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection='3d')

x = np.linspace(-10*(np.pi),10*(np.pi),10e4)
y = np.sin(x)
z = np.cos(x)

ax.plot(x, y, z, label='$y=sin(x)$ and $z = cos(x)$')
ax.legend()
ax.set_title('3D line curve')
ax.set_xlabel('$x$')
ax.set_ylabel('$y = sin(x)$')
ax.set_zlabel('$z = cos(x)$')
plt.show()

