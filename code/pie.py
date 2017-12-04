import matplotlib.pyplot as pl
import numpy as np 
x = np.array([1,2,3,4,5,6,7,8,9,0])
label = ['a','b','c','d','e','f','g','h','i','j']
explode = [0.2, 0.1, 0.5, 0, 0, 0.3, 0.3, 0.2, 0.1,0]
pl.pie(x, labels=label, explode = explode, shadow=True, autopct='%2.2f%%')
pl.title('Pie Chart')
pl.show()