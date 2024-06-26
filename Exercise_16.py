# -*- coding: utf-8 -*-
"""Exercise 16.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OaihHVq4ZsNDt0di8xmCWpOUx3UQMs1m
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

ld= load_digits()
x= ld.data
y= ld.target

df = pd.DataFrame(ld.data)
df.head()

df['target'] = ld.target
df.head()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(x_train, y_train)

knn.score(x_test, y_test)

y_predicted = knn.predict(x_test)

cm = confusion_matrix(y_test, y_predicted)
cm

import seaborn as sn
plt.figure(figsize=(10,7))
sn.heatmap(cm, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')

print(classification_report(y_test, y_predicted))

