# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 11:44:46 2024

@author: mmanc
"""

import numpy as np 

from einsteinpy.geodesic import Timelike
from einsteinpy.plotting.geodesic import GeodesicPlotter, StaticGeodesicPlotter, InteractiveGeodesicPlotter

X = [9.346, np.pi/2 , 0.] #position vector
P = [0., 0., 4] #momentum

a = 0.

steps = 1500

delta = 1.

geod = Timelike(metric = 'Schwarzschild', metric_params=(a,), position = X, momentum = P, steps = steps,
                delta = delta, return_cartesian = True)

gpl = GeodesicPlotter(ax=None, bh_colors=('#000', '#FFC'), draw_ergosphere=False)
#%%

# plot
gpl.plot2D(geod, coordinates=(1, 2), color= 'blue')
gpl.show()
# gpl.plot(geod, color= 'blue')
# gpl.clear()
#%%
#parameters plot
gpl.parametric_plot(geod) #this will plot the variables values
gpl.show()
#%%

help(gpl.plot2D)

print(geod.trajectory)

len(geod.trajectory)
trajectory = geod.trajectory[1]

trajectory[1499]
len(trajectory)


trajectory
trajectory[0]
trajectory[100]
trajectory[500]
print(trajectory)
import matplotlib.pyplot as plt

plt.plot(trajectory, label = 'bho')
# plt.plot(trajectory[0], label = 'traj0', color = 'red')
# plt.plot(trajectory[100], label = 'traj100', color = 'blue')
# plt.plot(trajectory[500], label = 'traj500', color = 'purple')
b = 1000
yl = 50
plt.xlim(0,b)
plt.ylim(-yl,yl)
plt.legend(loc='upper right', bbox_to_anchor=(1.5, 1))
plt.show()

#%%
traj_r = geod.trajectory[1]
phi = np.linspace(0, 2*np.pi)

x_value = traj_r*np.cos(geod.trajectory[0])
y_value = traj_r*np.sin(geod.trajectory[0])

plt.plot(x_value,y_value)
plt.show()

#%%













