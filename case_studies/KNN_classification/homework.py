# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 11:16:15 2018

@author: eleve
"""

# E1
"""
Read in the data as a pandas dataframe using pd.read_csv. 
The data can be found at https://s3.amazonaws.com/demo-datasets/wine.csv.
"""
import pandas as pd
data = pd.read_csv("https://s3.amazonaws.com/demo-datasets/wine.csv")

# E2
"""
Print the first 5 rows of data using the head() method.
The dataset remains stored as data. 
Two columns in data are is_red and color, which are redundant. 
Drop color from the dataset, and save the new dataset as numeric_data.
"""

print(data[:5])
# and
print(data.head())
numeric_data = data.drop("color", axis=1)

# E3
"""
Scale the data using the sklearn.preprocessing function scale() on numeric_data.
Convert this to a pandas dataframe, and store as numeric_data.
Include the numeric variable names using the parameter columns = numeric_data.columns.
Use the sklearn.decomposition module PCA(), and store this as pca.
Use the fit_transform() function to extract the first two principal components \
from the data, and store this as principal_components.
"""
import sklearn.preprocessing
import pandas as pd
scaled_data = sklearn.preprocessing.scale(numeric_data)
numeric_data = pd.DataFrame(scaled_data, columns = numeric_data.columns)

import sklearn.decomposition
pca = sklearn.decomposition.PCA(n_components=2)
principal_components = pca.fit_transform(numeric_data)
principal_components = pca.fit(numeric_data).transform(numeric_data)

# E4
"""
The first two principal components can be accessed using principal_components[:,0] \
and principal_components[:,1]. Store these as x and y respectively, and plot the first two principal components.
Consider: how well are the two groups of wines separated by the first two principal components?
"""

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.backends.backend_pdf import PdfPages
observation_colormap = ListedColormap(['red', 'blue'])
x = principal_components[:,0]
y = principal_components[:,1]

plt.title("Principal Components of Wine")
plt.scatter(x, y, alpha = 0.2,
    c = data['high_quality'], cmap = observation_colormap, edgecolors = 'none')
plt.xlim(-8, 8); plt.ylim(-8, 8)
plt.xlabel("Principal Component 1"); plt.ylabel("Principal Component 2")
plt.show()

# E5
"""
Create a function accuracy(predictions, outcomes) that takes two lists of the same size \
as arguments and returns a single number, which is the percentage of elements that are equal for the two lists.
Use accuracy to compare the percentage of similar elements in x = np.array([1,2,3]) and y = np.array([1,2,4]).
Print your answer.
"""

def accuracy(predictions, outcomes):
    eq = 0
    for i in range(len(predictions)):
        if predictions[i] == outcomes[i]:
            eq += 1
    return eq/len(predictions)

x = np.array([1,2,3])
y = np.array([1,2,4])
accuracy(x, y)

# E6
"""
Use accuracy() to calculate how many wines in the dataset are of low quality. \
Do this by using 0 as the first argument, and data["high_quality"] as the second argument.
Print your result.
"""

predictions = np.zeros(len(data["high_quality"]))
result = accuracy(predictions, data["high_quality"])
print(result)

# or

print(accuracy(0, data["high_quality"]))

# E7
"""
Use knn.predict(numeric_data) to predict which wines are high and low quality \
and store the result as library_predictions.
Use accuracy to find the accuracy of your predictions, using library_predictions \
as the first argument and data["high_quality"] as the second argument.
Print your answer. Is this prediction better than the simple classifier in Exercise 6?
"""

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(numeric_data, data['high_quality'])

library_predictions = knn.predict(numeric_data)
print(accuracy(library_predictions,  data["high_quality"]))

# E8
"""
To circumvent this, fix the random generator using random.seed(123), and select 10 rows \
from the dataset using random.sample(range(n_rows), 10). Store this selection as selection.
"""

n_rows = data.shape[0]
random.seed(123)
selection = random.sample(range(n_rows), 10)

# E9
"""
For each predictor p in predictors[selection], use knn_predict(p, predictors[training_indices,:], outcomes, k=5) \
to predict the quality of each wine in the prediction set, and store these predictions as a np.array called my_predictions.\ 
Note that knn_predict is already defined as in the Case 3 videos.
Using the accuracy function, compare these results to the selected rows from the high_quality variable \
in data using my_predictions as the first argument and data.high_quality[selection] as the second argument. \
Store these results as percentage.
"""

predictors = np.array(numeric_data)
training_indices = [i for i in range(len(predictors)) if i not in selection]
outcomes = np.array(data["high_quality"])

my_predictions = np.array([knn_predict(p, predictors[training_indices,:], outcomes, k=5) for p in predictors[selection]])
percentage = accuracy(my_predictions, data.high_quality[selection])

print(percentage)








