# -*- coding: utf-8 -*-
"""Exercise_4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UMJfrYbeBllN_l7NAnymD8O5NVOA2cQa

#Importing Necessary libraries
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

"""#Reading the csv file and ploting the graph"""

df = pd.read_csv("/content/canada_per_capita_income.csv")

plt.xlabel('Year')
plt.ylabel('Per capita income(US$)')
plt.scatter(df.year,df.pci, color='green',marker='*')

"""#Making object of regression model and providing parameters to the fit function.

"""

reg = linear_model.LinearRegression()
reg.fit(df[['year']],df.pci)

reg.predict([[2020]])

reg.coef_

reg.intercept_

"""#Checking the formula y= mx+c

"""

828.46507522*2020+(-1632210.7578554575)

"""#Ploting the regression line"""

plt.xlabel('Area(sq.ft)')
plt.ylabel('Price(US$)')
plt.scatter(df.year, df.pci, color='green', marker='*')
plt.plot(df.year, reg.predict(df[['year']]), color='black')

import pickle

with open('model_pickle','wb') as f:
  pickle.dump(reg,f)

with open('model_pickle', 'rb') as f:
  mp = pickle.load(f)

mp.predict([[2020]])

import joblib as jb

jb.dump(reg,'model_joblib')

a= jb.load('model_joblib')

a.predict([[2020]])