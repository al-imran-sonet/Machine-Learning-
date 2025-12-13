#  Scatter 

import matplotlib.pyplot as plt
import numpy as np

""" x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.scatter(x,y) # show only the point 
plt.show() """


""" # first plot 
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.scatter(x,y,color='r')
# second plot 
x= np.array([27,35,45,54,655])
y= np.array([19,2,32,43,55])
plt.scatter(x,y,color='g') # multyple color scatter plot 

plt.grid()
plt.show() """

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])


plt.scatter(x,y,c=colors ,cmap='flag')  # lots of cmap(color map) is available in https://www.w3schools.com/python/matplotlib_scatter.asp
plt.colorbar()
plt.show()


# to be continued 