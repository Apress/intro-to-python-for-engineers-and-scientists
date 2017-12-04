import matplotlib.pyplot as plt
import numpy as np

# defining data for x, y, z axes
x = np.linspace(0,1,100)
y = np.linspace(1,2,100)
(X,Y) = np.meshgrid(x,y)
z = np.sin(X)-np.sin(Y)

# plotting contour
fig = plt.figure()

ax1 = fig.add_subplot(211)
c1 = ax1.contour(x,y,z)
l1 = ax1.clabel(c1)
lx1 = ax1.set_xlabel("x")
ly1 = ax1.set_ylabel("y")


# plotting filled contour
ax2 = fig.add_subplot(212)
c2 = ax2.contourf(x,y,z)
l2 = ax2.clabel(c2)
lx2 = ax2.set_xlabel("x")
ly2 = ax2.set_ylabel("y")

plt.show()

# plotting filled contour