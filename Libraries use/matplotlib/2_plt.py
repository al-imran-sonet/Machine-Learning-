# marker and lines 

import matplotlib.pyplot as plt
import numpy as np 

"""make graph line with point dot  
xpoints= np.array([2,3,4,5,6])
ypoints= np.array([1,2,3,4,55])
plt.plot(xpoints,ypoints,marker='o')   # we cane use different marker *, + etc 
                                      # see more in https://www.w3schools.com/python/matplotlib_markers.asp 
plt.show() """


""" short cut notation of marker line type and color of line 
xpoints= np.array([2,3,4,5,6])
ypoints= np.array([1,2,3,4,55])
plt.plot(xpoints,ypoints,'o:g')   # shortcut notation (fmt) marker|line|color
                                      # see more in https://www.w3schools.com/python/matplotlib_markers.asp
plt.show() """

""" 
colours and shape of markers 
xpoints= np.array([2,3,4,5,6])
ypoints= np.array([1,2,3,4,55])
plt.plot(xpoints,ypoints,marker='o',ms=10,mfc='r',mec='r') # circle size ms, marker face color mfc , marker edge color mec
plt.show() 
"""

""" line style colour 
 xpoints= np.array([2,3,4,5,6])
ypoints= np.array([1,2,3,4,55])
plt.plot(xpoints,ypoints,marker='o',mec='r',mfc='r',linestyle='dotted',color = 'g')   # many other types are available dashed 
plt.show() 

"""