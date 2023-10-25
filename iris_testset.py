# -*- coding: utf-8 -*-
"""iris_testset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EvxVjKuUv4gR-lZlMOzMAVCfZ4L_BODE
"""

# @title Default title text
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn import datasets
iris = datasets.load_iris()

X = iris.data[:,]
y=iris.target

print ("Features : ", iris['feature_names'])
iris_dataframe = pd.DataFrame(data=np.c_[iris['data'],iris['target']], columns=iris['feature_names']+['target'])
plt.figure()
grr = pd.plotting.scatter_matrix(iris_dataframe, c=iris['target'], figsize=(15,5), s=60, alpha=1)
plt.show()

import seaborn as sns
dataplot = sns.heatmap(iris_dataframe.corr(), annot=True)
plt.show()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

from sklearn.naive_bayes import GaussianNB

NB = GaussianNB()
NB.fit(X_train, y_train)

y_pred = NB.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
df_cm = pd.DataFrame(cm, columns=np.unique(y_test), index= np.unique(y_test))

df_cm.index.name= 'Actual'
df_cm.columns.name = 'Predicted'

sns.heatmap(df_cm, annot=True)
plt.show()