#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 20:57:10 2018

@author: Kartik
"""

import numpy as np
import matplotlib.pyplot as plt
from itertools import product
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from pyts.classification import (BOSSVSClassifier, SAXVSMClassifier,
                                 KNNClassifier)
import os
import pandas as pd

os.getcwd()
os.chdir('/Users/apple/Desktop/FINAL_FINAL/Preprocessing')

train = pd.read_csv('train_balanced_scaled.csv')
train = train.iloc[:, 0:62]
X_train = train.iloc[:, 1:62]
y_train = train.iloc[:, 0]


#Shufling the data
idx = np.random.permutation(train)
X_train = idx[:, 1:62]
y_train = idx[:, 0]


# BOSSVSClassifier
bossvs = BOSSVSClassifier(n_coefs=4, window_size=24)
bossvs.fit(X_train, y_train)


#Read in the test data
test = pd.read_csv('test_trimmed_scaled.csv')

X_test = test.iloc[:, 1:62]
y_pred_boss = bossvs.predict(X_test)
y_pred_boss = pd.DataFrame(y_pred_boss)


# SAXVSMClassifier
saxvsm = SAXVSMClassifier()
saxvsm.fit(X_train, y_train)
y_pred_saxvsm = saxvsm.predict(X_test)
y_pred_saxvsm = pd.DataFrame(y_pred_saxvsm)

# KNNClassifier
knn = KNNClassifier()
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)
y_pred_knn = pd.DataFrame(y_pred_knn)

#Write all the predictions

os.chdir('/Users/apple/Desktop/FINAL_FINAL/Analysis')

y_pred_boss.to_csv('y_pred_boss.csv', index = False)
y_pred_saxvsm.to_csv('y_pred_saxvsm.csv', index = False)
y_pred_knn.to_csv('y_pred_knn.csv', index = False)

