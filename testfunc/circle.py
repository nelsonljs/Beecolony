# -*- coding: utf-8 -*-
"""
Created on Thu May 21 10:36:22 2020

@author: nelson
"""
import math

class testfunction:
    # Circle function 2D
    dims = 2
    bounds = [-10, 10]
    
    def funeval(vector):
        # Static Method for Rastrigin function
        x1 = vector[0]
        x2 = vector[1]
        fx = x1*x1 + x2*x2
        
        return(fx)