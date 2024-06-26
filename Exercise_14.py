# -*- coding: utf-8 -*-
"""Exercise 14.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TmQF2YwBZ43-71cEm3kDuNrKOwRpC5li
"""

import pandas as pd
from sklearn.datasets import load_wine
wine = load_wine()
df = pd.DataFrame(wine.data, columns=wine.feature_names)
df

feature = wine.feature_names
feature

df['target'] = wine.target
df

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(wine.data, df['target'], test_size=0.2)

from sklearn.naive_bayes import GaussianNB, MultinomialNB
gnb = GaussianNB()
mnb = MultinomialNB()
gnb.fit(X_train, y_train)
mnb.fit(X_train, y_train)

gnb.predict(X_test)

mnb.predict(X_test)

y_test

gnb.score(X_test, y_test)

mnb.score(X_test, y_test)