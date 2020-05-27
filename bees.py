# -*- coding: utf-8 -*-
"""
Created on Mon May 18 10:10:04 2020

@author: nelson
"""

# implementation of Artificial Bee Colony algorithm
# accepts any number of input variables.
# unrestricted optimization
# changes one variable at a time

import random
from testfunc.himmelblau import testfunction
import testfunc.himmelblau as testfunc
import numpy as np
import matplotlib.pyplot as plt
import seaborn
from matplotlib import animation

employedbee_count = 10
onlookerbee_count = 50
scoutlimit = 5
epsilon = 0.15
global_min = 1e09
update = 0
globalmins = []

#testing the class.
testfunction.funeval([1,1])
testfunction.bounds

# testfunc.plotsurface()

class globalmin:
    def __init__(self, vector, funeval, loop):
        self.vector = vector
        self.funeval = funeval
        self.loop = loop

class employedbee:
    def __init__(self, in_vector):
        self.vector = in_vector
        self.limit = 0

# Initialise our employed bees.
employedbees = []

for i in range(employedbee_count):
    employedbees.append(
        employedbee([random.uniform(testfunction.bounds[0],testfunction.bounds[1]),
                     random.uniform(testfunction.bounds[0],testfunction.bounds[1])]))
    employedbees[i].funeval = testfunction.funeval(employedbees[i].vector)

# Start the loop

# Fitness function is based on minimization
fitness = []
funeval = []
for bee in employedbees:
    fx = bee.funeval
    funeval.append(fx)
    if fx > 0:
        fitness.append(1/(1+fx))
    else:
        fitness.append(-fx)

weights = [x / sum(fitness) for x in fitness]

#wrap new vector generation in a function
def generatenewvector(index):
    
    # generate new input variables to test by
    #1. selecting 1 variable to adjust
    var = random.randint(0, testfunction.dims-1)
    
    #2. selecting another bee for referencing.    
    otherbee = random.randint(0, employedbee_count-1)
    
    while otherbee == index:
        otherbee = random.randint(0, employedbee_count-1)
        
    new_vector = employedbees[index].vector
    ref_vector = employedbees[otherbee].vector
    
    new_vector[var] = new_vector[var] + random.uniform(-epsilon,epsilon)* (new_vector[var]- ref_vector[var])
    
    # check if the variable is still within bounds
    if new_vector[var] > testfunction.bounds[1]:
        new_vector[var] = testfunction.bounds[1]
    elif new_vector[var] < testfunction.bounds[0]:
        new_vector[var] = testfunction.bounds[0]
    
    return(new_vector)

# Start onlooker bee loop

# tracking food sources every loop.
employed_log = []
onlooker_log = []
total_log = []
globalmin_log = []

# running for 1000 loops.
for loop in range(1000):
    #logging for visualization
    onlookers_vector = []
    for onlooker in range(onlookerbee_count):
        #pick a employed bee to work with.
        employed = random.choices(list(range(employedbee_count)), weights)[0]
    
        # compute a funeval based on new vector, and compare to current employed bee
        onlooker_vector = generatenewvector(employed)
        
        new_funeval = testfunction.funeval(onlooker_vector)
        
        if new_funeval < employedbees[employed].funeval:
            employedbees[employed] = employedbee(onlooker_vector)
            employedbees[employed].funeval = new_funeval
            update = update + 1
        
        # compare to current global min
        if new_funeval < global_min:
           global_min = new_funeval
           global_min_vector = [onlooker_vector[0], onlooker_vector[1]]
           globalmins.append(globalmin(global_min_vector, new_funeval, loop))
    
        onlookers_vector.append([onlooker_vector[0], onlooker_vector[1]])
        
    total_log.append(onlookers_vector)
    onlooker_log.append(onlookers_vector)
    
    # employed bees check their current food source.
    for i in range(employedbee_count):
           
        #adjust the selected employed bee's solution
        new_employed_vector = generatenewvector(i)
    
        new_funeval = testfunction.funeval(new_employed_vector)
        
        if new_funeval < employedbees[i].funeval:
            employedbees[i] = employedbee(new_employed_vector)
            employedbees[i].funeval = new_funeval
        else:
            employedbees[i].limit = employedbees[i].limit+1
        
        # compare to current global min
        if new_funeval < global_min:
           global_min = new_funeval
           global_min_vector = [new_employed_vector[0], new_employed_vector[1]]
           globalmins.append(globalmin(global_min_vector, new_funeval, loop))
           
        # if scoutlimit has been reached, the employed bee becomes a scout bee
        # spawn a new random solution
        
        if employedbees[i].limit >= scoutlimit:
            print("ABANDON FOOD SOURCE AT {}".format(i))
            employedbees[i] = employedbee([random.uniform(testfunction.bounds[0],testfunction.bounds[1]),
                         random.uniform(testfunction.bounds[0],testfunction.bounds[1])])
            employedbees[i].funeval = testfunction.funeval(employedbees[i].vector)
    
    #logging the foodsources
    employed_logging = []
    for bee in employedbees:
        employed_logging.append([bee.vector[0],bee.vector[1]])
    employed_log.append(employed_logging)
    total_log.append(employed_logging)
    
    globalmin_log.append(global_min)

#plotting some points

i = 0

from matplotlib.lines import Line2D
legend_elements = [Line2D([0], [0], marker='o', color = 'w', markerfacecolor='k', ms = 10, label='Employed Bee'),
                   Line2D([0], [0], marker='o', color = 'w', markerfacecolor='g', ms = 10, label='Onlooker Bee')]

for loops in total_log[0:30]:
    ax = testfunc.plotcontour(50)
    ax.legend(handles=legend_elements, loc = 'upper right')
    for bee in loops:
        if len(loops) > 10:
            marker = 'go'
        else:
            marker = 'ko'
        ax.plot(bee[0],bee[1], marker, ms=10)
    
    filename = 'myplot{}.png'.format(i)
    i = i+1
    plt.savefig(filename)
    plt.show()

# line plot for global min
    
fig = plt.figure()
ax = plt.axes()
plt.xlabel("Cycles")
plt.ylabel("log(funeval)");

x = np.linspace(1, 1000, 1000)
ax.plot(x, np.log10(globalmin_log));
plt.savefig('lineplot(himm).png')
plt.show()
