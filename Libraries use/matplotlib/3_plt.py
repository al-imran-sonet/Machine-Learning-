# labels and grid

import matplotlib.pyplot as plt
import numpy as np

""" basic titel and labels 
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x,y)
plt.title("Practice graph ")
plt.xlabel("x values ")
plt.ylabel("y values ")
plt.show() """


x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x,y)
plt.title("Practice graph ",loc='right')  # title possition 
plt.xlabel("x values ",loc='left') # by default center but we can change it 
plt.ylabel("y values ")
plt.grid()  # it will create graph paper like apparence  
plt.show()
