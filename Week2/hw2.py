# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 21:01:25 2018

@author: eleve
"""
import random

def rand():
   random.uniform(-1,1)

import math

def distance(x, y):
   # define your function here!
   X = (x[0] - y[0])**2
   Y = (x[1] - y[1])**2
   ans = math.sqrt(X + Y)
   return ans
   
x = (0, 0)
y = (1, 1)


random.seed(1)
import numpy as np

x = np.array([0, 0])
y = np.array([1, 1])

def in_circle(x, origin = [0]*2):
   return distance(x, origin) < 1
        
#print(in_circle(y,x))

R = 10000
x = []
inside = []
for i in range(R):
    point = [rand(), rand()]
    x.append(point)
    inside.append(in_circle(point, origin=[0]*2))

print(inside)
print(sum(inside) / R)