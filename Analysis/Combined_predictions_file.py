#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 20:49:37 2018

@author: Kartik
"""

import os
import pandas as pd

os.getcwd()
os.chdir('/Users/apple/Desktop/FINAL_FINAL/Analysis')

#Read csv files of all predicted values
custom_cnn = pd.read_csv('custom_cnn_predicted.csv')
cnn = custom_cnn.iloc[:, 2] 

roc_mtf_16 = pd.read_csv('roc_mtf_16_predicted.csv')
VGG16_mtf = roc_mtf_16.iloc[:, 2]

roc_rp_16 = pd.read_csv('roc_rp_16_predicted.csv')
VGG16_rp = roc_rp_16.iloc[:, 2]

roc_mtf_19 = pd.read_csv('roc_mtf_19_predicted.csv')
VGG19_mtf = roc_mtf_19.iloc[:, 2]

roc_rp_19 = pd.read_csv('roc_rp_19_predicted.csv')
VGG19_rp = roc_rp_19.iloc[:, 2]

cnn_lstm = pd.read_csv('CNN_LSTM_76.csv')
#cnn_lstm output has two columns indicating both 0 and 1 probability
#We need a pandasseries such that the prediction column has prob from 0th prediction column if label is 0
#and prob from 1th prediction column if label is 1.

#Reading the test file which has the labels
test = pd.read_csv('test_file.csv')
test_label = test.iloc[:, 0]

#concating labels to cnn_lstm predictions
cnn_lstm = pd.concat([test_label, cnn_lstm], axis = 1)

cnn_lstm_0 = cnn_lstm[cnn_lstm.V1 == 0]
cnn_lstm_0 = cnn_lstm_0.iloc[:, [0,2]]
cnn_lstm_0.columns = ['label', 'prob']

cnn_lstm_1 = cnn_lstm[cnn_lstm.V1 == 1]
cnn_lstm_1 = cnn_lstm_1.iloc[:, [0,3]]
cnn_lstm_1.columns = ['label', 'prob']

cnn_lstm_final = pd.concat([cnn_lstm_0,cnn_lstm_1], axis = 0)
cnn_lstm_final = cnn_lstm_final.sort_index()
cnn_lstm_prob = cnn_lstm_final.iloc[:, 1]

#Reading in the time series predictions
y_pred_boss = pd.read_csv('y_pred_boss.csv')
y_pred_saxvsm = pd.read_csv('y_pred_saxvsm.csv')
y_pred_knn = pd.read_csv('y_pred_knn.csv')


all_pred = pd.concat([test_label, cnn, VGG16_mtf, VGG16_rp, VGG19_mtf, VGG19_rp, 
                      cnn_lstm_prob, y_pred_boss, y_pred_saxvsm, y_pred_knn ], axis = 1)
all_pred.columns = ['Label', 'CNN', 'VGG16_mtf', 'VGG16_rp', 'VGG19_mtf', 'VGG19_rp', 'CNN_LSTM', 'boss', 'SAXVSM', 'KNN']

#Write the file to disk
all_pred.to_csv('all_pred.csv', index = False)



