# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 21:13:44 2024

@author: mmanc
"""

import numpy as np 

from einsteinpy.geodesic import Nulllike # null like for light
from einsteinpy.plotting.geodesic import GeodesicPlotter, StaticGeodesicPlotter, InteractiveGeodesicPlotter

X = [3, np.pi/2 , 0] #position vector
P = [0., 0., 1] #momentum set p_phi = 1

a = 0.

steps = 100 

delta = 1.

geod = Nulllike(metric = 'Schwarzschild', metric_params=(a,), position = X, momentum = P, steps = steps,
                delta = delta, return_cartesian = True)

gpl = GeodesicPlotter(ax=None, bh_colors=('#000', '#FFC'), draw_ergosphere=False)
#%%

# plot using einsteinpy default plotting code
gpl.plot2D(geod, coordinates=(1, 2), color= 'orange')
gpl.show()
#%%
# parameters plot
gpl.parametric_plot(geod) #t his will plot the variables values
gpl.show()

#%%
#plots using my own code
import matplotlib.pyplot as plt
trajectory = geod.trajectory[1]
x1_list = []
x2_list = []
iterations = []
for i in range(0,steps):
    x1 = trajectory[i][1] # X1 values
    x2 = trajectory[i][2] # X2 values 
    ite = i # keep the iteartions
    x1_list.append(x1)
    x2_list.append(x2)
    iterations.append(ite)
# plotting the results
plt.plot(iterations, x1_list, color = 'red', label = r'$X_1$ (cartesian)')
plt.plot(iterations, x2_list, color = 'blue', label = r'$X_2$ (cartesian)')
plt.legend(loc = 'upper right', bbox_to_anchor = (1.5, 1))
plt.title(r'$X_1$ and $X_2$ in cartesian')
plt.xlabel(r'Affine parameter $\lambda$')
plt.ylabel('Coordinates')
plt.show()
#%%
rs = 2 # since G=M=c=1 

circle = plt.Circle((0, 0), rs, color='black', alpha=0.5, label = r'Singularity of radius $R_s$')
# Plot the trajectory in the xy-plane
plt.plot(x1_list, x2_list, label = 'orbit', color = 'orange')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.gcf().gca().add_artist(circle)

lim = 4 # set 20 or 5 for unstable circular orbit
plt.xlim(-lim,lim)
plt.ylim(-lim,lim)



plt.ylabel(r'$\frac{y}{R_s}$')
plt.xlabel(r'$\frac{x}{R_s}$')
plt.title('Photo-sphere')
#plt.title('Unstable circular orbit')
#plt.title('Stable circular orbit')
plt.legend(loc='upper right', bbox_to_anchor=(1.8, 1))
plt.show()
#%%
