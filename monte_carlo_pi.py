# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 14:06:08 2020

@author: Ivan52x53
"""

import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation, PillowWriter

def get_random():
    """Returns a random number between -1 and 1"""
    sign = random.randint(1,2)
    if sign ==1:
        num = random.random()
    else:
        num = -random.random()
    return num

def get_random_point():
    """Returns a random point with coordinates between -1 and 1"""
    x,y = get_random(), get_random()
    x_list.append(x)
    y_list.append(y)
    return x,y

def distance(p):
    """Calculates the distance to a point from the origin"""
    return np.sqrt(p[0]**2 + p[1]**2)

# Initiate required lists and figures for the animation
x_list = []
y_list = []
pi_list = []
x, y = [], []
iteration_list = []
fig, ax = plt.subplots()
points, = plt.plot([], [], ls="", marker=".")

def init():
    # Plot circle
    circle = plt.Circle((0,0), 1, color="r", fill=False)
    ax.add_artist(circle)
    
    # Ax limits
    ax.set_xlim(-1,1)
    ax.set_ylim(-1,1)
    
def update(i):
    x.append(x_list[i]) # Updates x with a new element from x_list
    y.append(y_list[i]) # Same for y
    points.set_data(x, y) # Use these updated lists for the graph "points"
    ax.set_title("Pi estimate = {:.4f}, iteration: {}".format(pi_list[i], iteration_list[i])) # Update title


N = 1000 # Max number of iterations
n = 0 # number of points outside the circle
iteration = 0 # stores the current iteration
for i in range(N):
    iteration += 1
    d = distance(get_random_point()) # generates a point and checks whether it's in the circle or not
    if d >= 1:
        n += 1
    pi = 4*(1-n/iteration)
    iteration_list.append(iteration)
    pi_list.append(pi)
    
    #ax.plot(x_list, y_list, ls="", marker=".", color="black")
    #ax.set_title("Pi estimate = {:.4f}".format(pi))
    #plt.savefig("plots/" + str(iteration))

ani = FuncAnimation(fig, update, range(len(x_list)), init_func=init, interval=1, repeat_delay=5000)
writer = PillowWriter(fps=25)
ani.save("Monte_Carlo_pi.gif", writer=writer)
plt.show() 

"""    
print(4*(1-n/N))

fig, ax = plt.subplots()
ax.plot(x_list, y_list, ls="", marker=".")
"""