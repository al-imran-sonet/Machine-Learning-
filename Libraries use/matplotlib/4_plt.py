# sub plot 


import matplotlib.pyplot as plt
import numpy as np


# plot 1
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1,2,1)
plt.plot(x,y,marker='*')
plt.title("Practice graph 1",loc='right')  # title possition 
plt.xlabel("x values ",loc='left') # by default center but we can change it 
plt.ylabel("y values ")
plt.grid()


# plot 2 
y = np.array([0, 1, 2, 3])
x = np.array([3, 8, 1, 10])
plt.subplot(1,2,2)
plt.plot(x,y,marker='o')
plt.title("Practice graph 2 ",loc='right')  # title possition 
plt.xlabel("x values ",loc='left')  # by default center but we can change it 
plt.ylabel("y values ")
plt.grid()


plt.suptitle("Sub graph practice")
plt.show()  # you have to use show function at once 
