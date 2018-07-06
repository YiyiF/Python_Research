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


import numpy as np
import pandas as pd

whisky = pd.read_csv("whiskies.txt")
whisky["Region"] = pd.read_csv("regions.txt")

whisky.head()
whisky.tail()
whisky.iloc[0:10]
whisky.iloc[5:10, 0:5]

whisky.columns
flavors = whisky.iloc[:,2:14]

corr_flavors = pd.DataFrame.corr(flavors)

import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))
plt.pcolor(corr_flavors)
plt.colorbar()
plt.savefig("corr_flavors.pdf")

corr_whisky = pd.DataFrame.corr(flavors.transpose())
plt.figure(figsize=(10,10))
plt.pcolor(corr_whisky)
plt.axis("tight") # no margin
plt.colorbar()
plt.savefig("corr_whisky.pdf")


from sklearn.cluster.bicluster import SpectralCoclustering

model = SpectralCoclustering(n_clusters=6, random_state=0)
model.fit(corr_whisky)
model.rows_

np.sum(model.rows_, axis=1)
np.sum(model.rows_, axis=0)
model.row_labels_

whisky['Group'] = pd.Series(model.row_labels_, index=whisky.index)
whisky = whisky.ix[np.argsort(model.row_labels_)]
whisky = whisky.reset_index(drop=True)

correlations = pd.DataFrame.corr(whisky.iloc[:,2:14].transpose())
correlations = np.array(correlations)


plt.figure(figsize=(14,7))
plt.subplot(121)
plt.pcolor(corr_whisky)
plt.axis("tight") # no margin
plt.subplot(122)
plt.pcolor(correlations)
plt.title("Rearranged")
plt.axis("tight") # no margin
plt.savefig("correlations.pdf")


import pandas as pd 
data = pd.Series([1,2,3,4]) 
data = data.ix[[3,0,1,2]]













