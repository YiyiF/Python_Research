# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 10:28:41 2018

@author: eleve
"""
import pandas as pd
import numpy as np
df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                          'foo', 'bar', 'foo', 'foo'],
                    'B' : ['one', 'one', 'two', 'three',
                          'two', 'two', 'one', 'three'],
                    'C' : np.random.randn(8),
                    'D' : np.random.randn(8)}) 


grouped = df.groupby('A')

grouped = df.groupby(['A', 'B'])



