# -*- coding: utf-8 -*-
"""
Created on Thu May 21 10:36:22 2020

@author: nelson
"""
import matplotlib.pyplot as plt
import numpy as np

bounds = [-100, 100]

class testfunction:
    # Easom function 2D
    dims = 2
    bounds = bounds
    
    def funeval(vector):
        # Static Method for Rastrigin function
        x1 = vector[0]
        x2 = vector[1]
        fx = -1 * np.cos(x1) * np.cos(x2) * np.exp(-1*( (x1 - np.pi)**2 + (x2 - np.pi)**2))
        
        return(fx)

def plotcontour(lines = 20):
    
    #contour plot
    xlist = np.linspace(bounds[0],bounds[1], 200)
    ylist = np.linspace(bounds[0],bounds[1], 200)
    
    X, Y = np.meshgrid(xlist, ylist)

    Z = testfunction.funeval([X,Y])
    
    fig = plt.figure(figsize=(10,8))
    left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
    ax = fig.add_axes([left, bottom, width, height]) 
    
    Z = testfunction.funeval([X,Y])
    
    cp = ax.contour(X, Y, Z, lines, cmap='RdGy')
    # ax.clabel(cp, inline=True, 
    #           fontsize=2)
    ax.set_title('Contour Plot')
    ax.set_xlabel('x (cm)')
    ax.set_ylabel('y (cm)')
    plt.colorbar(cp)
    
    #adding points
    # plt.scatter(xlist2,ylist2)
    # plt.show()
    print("Type plt.show() to render, you may add scatter points before hand.")
    return(ax)

# surface plot
from mpl_toolkits.mplot3d import Axes3D 

def plotsurface():
    
    
    xlist = np.linspace(bounds[0],bounds[1], 200)
    ylist = np.linspace(bounds[0],bounds[1], 200)
    
    X, Y = np.meshgrid(xlist, ylist)

    Z = testfunction.funeval([X,Y])
    fig = plt.figure() 
    ax = fig.gca(projection='3d') 
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
      cmap='RdGy', linewidth=0.08,
      antialiased=True)    
    # plt.savefig('rastrigin_graph.png')
    return(ax)