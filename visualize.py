# -*- coding: utf-8 -*-
"""
Created on Wed May 27 11:51:18 2020

@author: nelson

To visualize the test functions
"""

import random
from testfunc.easom import testfunction
import testfunc.easom as testfunc
import numpy as np
import matplotlib.pyplot as plt

#testing the class.
testfunction.funeval([1,1])
testfunction.bounds

testfunc.plotsurface()
testfunc.plotcontour(50)
