# basic plotting 


import matplotlib.pyplot as plt
import numpy as np 

"""make the basic graph 
xpoints= np.array([1,2,3,43,4,5,6])
ypoints=np.array([6,7,8,9,0,5,4])
plt.plot(xpoints,ypoints)
plt.show()

"""


""" plot only the points 
xpoints= np.array([1,2,3,43,4,5,6])
ypoints=np.array([6,7,8,9,0,5,4])
plt.plot(xpoints,ypoints,'o')
plt.show()

"""

""" auto fill the X point like (1,6),(2,7),(3,8) 
ypoints=np.array([6,7,8,9,0,5,4])
plt.plot(ypoints)
plt.show()

"""