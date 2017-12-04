import matplotlib.pyplot as plt
fig = plt.figure() 
# variable fig stores "figure" instance
ax1 = fig.add_subplot(221)
# variable ax1 stores the subplot of figure at 1st place in 2 x 1 matrix 
ax1.plot([-1, 1, 4], [-2, -3, 4]);
# ax1 iscalled and plot fucntion is given to it.
# plot function carries two lists giving x and y axis points for graph
ax2 = fig.add_subplot(222)
ax2.plot([1, -2, 2], [0, 0, 2]);
# same logic as for ax1
ax3 = fig.add_subplot(223)
ax3.plot([10, 20, 30], [10, 20, 30]);
ax4 = fig.add_subplot(224)
ax4.plot([-1, -2, -3], [-10, -20, -30]);
plt.show()
# show the figure on computer terminal