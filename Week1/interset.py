# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 22:31:08 2018

@author: eleve
"""
def interset(s1,s2):
    res = []
    for x in s1:
        if x in s2:
            res.append(x)
    return res
