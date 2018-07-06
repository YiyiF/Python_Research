# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 12:35:38 2018

@author: eleve
"""

import pandas as pd
x = pd.Series([6, 3, 8, 6])

x = pd.Series([6, 3, 8, 6], index=["q", "w", "e", "r"])
# call
x["w"]; x[["e", "w"]]

x.reindex(sorted(x.index))

y = pd.Series([7, 3, 5, 2], index=["e", "q", "r", "t"])

x + y #  plus the same index then returns a NAN

age = {"Tim":29, "Jim":31, "Pam":27, "Sam":35}
x = pd.Series(age)

data = {'name': ['Tim', 'Jim', 'Pam', 'Sam'],
        'age': [29, 31, 27, 35],
        'ZIP': ['02115', '02130', '67700', '00100']}
x = pd.DataFrame(data, columns = ["name", "age", "ZIP"])

#x["name"]; x.name


frequency = ['frequent', 'infrequent', 'unique']


