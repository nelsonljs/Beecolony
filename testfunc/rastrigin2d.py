# -*- coding: utf-8 -*-
"""
Created on Thu May 21 10:36:22 2020

@author: nelson
"""
import math

class testfunction:
    # Rastrigin function 2D
    dims = 2
    bounds = [-5.12, 5.12]
    
    def funeval(vector):
        # Static Method for Rastrigin function
        A = 10
        x1 = vector[0]
        x2 = vector[1]
        fx = A*2 + (x1*x1 - A*math.cos(2*math.pi*x1)) + (x2*x2 - A*math.cos(2*math.pi*x2))
        
        return(fx)