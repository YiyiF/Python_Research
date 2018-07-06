# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 22:34:12 2018

@author: eleve
"""

def password(length):
    pw = str()
    characters = "abcdefhjklmnopq"
    for i in range(length):
        pw = pw + random.choice(characters)
    return pw