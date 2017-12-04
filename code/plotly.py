import numpy as np
import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('username','APIkey')
data = Data([Scatter(x=np.arange(100),y=np.random.randn(100),name='trace 0')])
fig = Figure(data=data)
plot_url = py.plot(fig)
