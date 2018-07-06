# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 00:03:00 2018

@author: eleve
"""

def counter(input_string):
    count_letters = {}


    for letter in input_string:
        if letter in alphabet:
            if letter in count_letters:
                count_letters[letter] += 1
            else:
                count_letters[letter] = 1
    return count_letters       


sentence = 'Jim quickly realized that the beautiful gowns are expensive'
counter(sentence)    
print(count_letters)