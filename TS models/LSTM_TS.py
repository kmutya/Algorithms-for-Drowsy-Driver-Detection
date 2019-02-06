#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 16:17:26 2019

@author: Kartik
"""

import pandas as pd
import numpy as np
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential
import time
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from pandas import Series

df = pd.read_csv('test_HI.csv')
case1 = df.loc[df['Engine']==3].HI
case1.plot()

#Expand the series to many other samples based on window size
window_size = 9

case1_s = case1.copy()
for i in range(window_size):
    case1 = pd.concat([case1, case1_s.shift(-(i+1))], axis = 1)
    
case1.dropna(axis=0, inplace=True)

#Split it into train and test
nrow = round(0.8*case1.shape[0])
train = case1.iloc[:nrow, :]
test = case1.iloc[nrow:,:]

#Storing the first element 
first_element = test.iloc[0,9]

#difference
train = train.diff()
test = test.diff()
train = train.dropna()
test = test.dropna()

#Scale the data to [-1,1]
scaler = MinMaxScaler(feature_range=(-1, 1))
scaled_train = scaler.fit_transform(train)
scaled_train = pd.DataFrame(scaled_train)
scaled_test = scaler.fit_transform(test)
scaled_test = pd.DataFrame(scaled_test)



train_X = train.iloc[:,:-1]
train_y = train.iloc[:,-1]
test_X = test.iloc[:,:-1]
test_y = test.iloc[:,-1]



#Converting to numpy arrays
train_X = train_X.values
train_y = train_y.values
test_X = test_X.values
test_y = test_y.values


#Reshaping to be fed into LSTM
train_X = train_X.reshape(train_X.shape[0],train_X.shape[1],1)
test_X = test_X.reshape(test_X.shape[0],test_X.shape[1],1)

#Building the LSTM model
model = Sequential()
model.add(LSTM(input_shape = (window_size,1), output_dim= window_size, return_sequences = True))
model.add(Dropout(0.5))
model.add(LSTM(256))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation("linear"))
model.compile(loss="mse", optimizer="adam")
model.summary()

model.fit(train_X,train_y,batch_size=512,nb_epoch=3,validation_split=0.1)


#Function to predict steps into the future
def moving_test_window_preds(n_future_preds):

    ''' n_future_preds - Represents the number of future predictions we want to make
                         This coincides with the number of windows that we will move forward
                         on the test data
    '''
    preds_moving = []                                    # Use this to store the prediction made on each test window
    moving_test_window = [test_X[0,:].tolist()]          # Creating the first test window
    moving_test_window = np.array(moving_test_window)    # Making it an numpy array
    moving_test_window = moving_test_window
    
    for i in range(n_future_preds):
        preds_one_step = model.predict(moving_test_window) # Note that this is already a scaled prediction so no need to rescale this
        preds_moving.append(preds_one_step[0,0]) # get the value from the numpy 2D array and append to predictions
        preds_one_step = preds_one_step.reshape(1,1,1) # Reshaping the prediction to 3D array for concatenation with moving test window
        moving_test_window = np.concatenate((moving_test_window[:,1:,:], preds_one_step), axis=1) # This is the new moving test window, where the first element from the window has been removed and the prediction  has been appended to the end
        
    preds_moving = np.asarray(preds_moving).reshape(-1,1)    
    preds_moving = scaler.inverse_transform(preds_moving)
    return preds_moving


preds_moving = moving_test_window_preds(22)


# invert scaling
yhat = scaler.inverse_transform(preds_moving)
test_y = test_y.reshape(-1,1)
actual = scaler.inverse_transform(test_y)
# invert differencing
yhat = inverse_difference(case1, yhat, len(test_y)+1-i)

test_y = test_y.reshape(-1,1)
actual = scaler.inverse_transform(test_y)


pyplot.plot(actual)
pyplot.plot(yhat)
pyplot.show()



def rebuild_diffed(series, first_element_original):
    cumsum = series.cumsum()
    return cumsum.fillna(0) + first_element_original

a = pd.Series([2, 6, 4, 6, 2,])
print(a)
a_diff = a.diff()
print(a_diff)

# Rebuilding  

rebuild_diffed(a_diff, a[0])


