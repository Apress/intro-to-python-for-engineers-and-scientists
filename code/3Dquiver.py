from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(np.pi,-(np.pi),10)
y = np.linspace(np.pi,-(np.pi),10)
(X,Y) = np.meshgrid(x,y)
u = -15*X
v = 5*Y
q = plt.quiver(X,Y,u,v,angles='xy',scale=1000,color='b')
#p = plt.quiverkey(q,1,16.5,50,"50 m/s",coordinates='data',color='r')
xl = plt.xlabel("x (km)")
yl = plt.ylabel("y (km)")
plt.show()