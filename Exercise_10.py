# -*- coding: utf-8 -*-
"""Exercise 10.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EZKjfIyjS3aqX7z-o-T-dp87Em6jc5TM
"""

import pandas as pd
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

ds = load_digits()

dir(ds)

df = pd.DataFrame(ds.data,ds.target)
df

x_train,x_test,y_train,y_test = train_test_split(df ,ds.target,test_size=0.2)

len(x_train)

len(x_test)

#Linear one works well with nearly 98% accuracy
from sklearn.svm import SVC
s = SVC(C=10,gamma=70,kernel='linear')
#from sklearn.svm import SVC
#s = SVC(C=0.1,gamma=0.001,kernel='rbf')
s.fit(x_train,y_train)
s.score(x_test,y_test)