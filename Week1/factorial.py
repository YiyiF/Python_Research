# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 22:57:11 2018

@author: eleve
"""

def factorial(n):
   if n == 0:
     return 1
   else:
     N = 1
     for i in range(1, n+1):
       N = n * factorial(n-1)
       #N *= i
     return(N)