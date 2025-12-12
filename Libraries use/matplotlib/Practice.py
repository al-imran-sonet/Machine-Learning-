import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,3,4,5])
y=np.array([6,7,8,9,0])
plt.plot(x,y,linestyle=':',color='g',marker='o',mfc='r',mec='r')
plt.show()