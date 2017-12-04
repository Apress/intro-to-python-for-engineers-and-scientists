from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(121, projection='3d')
x = np.linspace(2*np.pi,-2*(np.pi),1000)
y = np.linspace(2*np.pi,-2*(np.pi),1000)
X,Y = np.meshgrid(x,y)
Z = np.sin(X) + np.sin(Y)

cont = ax1.contour(X, Y, Z)
ax1.clabel(cont, fontsize=9, inline=1)
ax1.set_xlabel('$x$')
ax1.set_ylabel('$y$')
ax1.set_title('Contour for $z=sin(x)+sin(y)$')

ax2 = fig.add_subplot(122, projection='3d')
Z = np.sin(X) + np.sin(Y)
cont = ax2.contourf(X, Y, Z)
ax2.clabel(cont, fontsize=9, inline=1)
ax2.set_xlabel('$x$')
ax2.set_ylabel('$y$')
ax2.set_title('Filled Contour for $z=sin(x)+sin(y)$')



plt.show()

