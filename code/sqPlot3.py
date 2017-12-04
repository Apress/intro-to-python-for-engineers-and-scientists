# import pylab and numpy
from matplotlib import pylab as pl
import numpy as np

# Create a figure of size 9x7 inches, 100 dots per inch
pl.figure(figsize=(9, 7), dpi=100)

# Create a new subplot from a grid of 1x1
pl.subplot(1, 1, 1)

# We wish to plot sin(x) and sin(2x)

# first we define x- axis in terms of pi units

X = np.linspace(-np.pi * 2, np.pi *2, 10e4, endpoint=True)

''' x-axis is defined from -2pi to 2pi with 10000 points 
where last point is also included'''

S, S2 = np.sin(X), np.sin(2*X)

# Plot sin(x) with a blue continuous line of width 1 (pixels)
# labelled as sin(x)
pl.plot(X, S, color="blue", linewidth=1.0, linestyle="-", label = "$sin(x)$")

# Plot sine(2x) with a red continuous line of width 1 (pixels)
# labelled as sin(2x)
pl.plot(X, S2, color="red", linewidth=1.0, linestyle="-", label = "$sin(2x)$")

# Set x limits from -2pi to 2.5*pi
pl.xlim(-2* np.pi, 2.5* np.pi)

# Set x ticks
pl.xticks(np.linspace(-2.5 * np.pi, 2.5 * np.pi, 9, endpoint=True))

# Set y limits from 1.2 to -1.2
pl.ylim(-1.2, 1.2)

# Set y ticks
pl.yticks(np.linspace(-1, 1, 5, endpoint=True))

# Set the tile as 'Sine waves'
pl.title('$sin(x)$ and $sin(2x)$ waves')

# Setting label on x-axis and y-axis

pl.ylabel('$sin(x)$ and $sin(2x)$')
pl.xlabel('$x$')

# Setting the grid to be ON
pl.grid(True)

# To show a legend at one corner for differentiating two curves
pl.legend()

# Show result on screen
pl.show()
