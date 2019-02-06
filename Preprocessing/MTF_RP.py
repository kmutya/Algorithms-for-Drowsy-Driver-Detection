#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 16:28:51 2018

@author: Kartik
"""
import numpy as np
import matplotlib.pyplot as plt
from pyts.image import MTF, GASF, GADF, RecurrencePlots
import pandas as pd
import os
import seaborn as sns


#Read the files to be converted to images
os.getcwd()
os.chdir('/Users/apple/Desktop/FINAL_FINAL/Preprocessing')

#Working with the TEST case first

test = pd.read_csv('test_trimmed_scaled.csv')

#Plotting sample time series and image
x = test.iloc[28, 1:62] #This is what a drowsy time series looks like
ax = sns.tsplot(x)
plt.xlabel('Time')
# Set y-axis label
plt.ylabel('Steering Angle')
plt.savefig('ts_drowsy.eps', format='eps', dpi=300)


y = test.iloc[27, 1:62] #This is what a non-drowsy time series looks like
ax1 = sns.tsplot(y)
plt.xlabel('Time')
# Set y-axis label
plt.ylabel('Steering Angle')
plt.savefig('ts_nondrowsy.eps', format='eps', dpi=300)

sample = np.array(test.iloc[2, 1:62]).reshape(1,-1)
image_size = 61
mtf = MTF(image_size)
X_mtf = mtf.fit_transform(sample)
plt.figure(figsize=(16, 8))
plt.subplot(121)
plt.imshow(X_mtf[0], cmap='rainbow', origin='lower') # This is what the time series looks like as an 61*61 image
plt.title("MTF", fontsize=16)

#Reshaping the test dataframe

test_label = np.array(test.V1) #V1 or drowsy

test_ts = np.array(test.iloc[:, 1:62])

#### MTF ######

def MTF_pyts(ts):
    image_size = 61
    mtf = MTF(image_size)
    X_mtf = mtf.fit_transform(ts)
    return(X_mtf)

def RP_pyts(ts):
    rp = RecurrencePlots(dimension=1,
                     epsilon='percentage_points',
                     percentage=30)
    X_rp = rp.fit_transform(ts)
    return(X_rp)

c = 0
test_image_count = len(test)
x_test = np.zeros((test_image_count,61,61)) #test images
for i in range(test_ts.shape[0]):
    temp = MTF_pyts(np.array(test_ts[i]).reshape(1,-1))
    x_test[c,:,:] = temp
    c = c + 1

test_label.sum() #21 drowsy images

#write array to disk
os.getcwd()
os.chdir('/Users/apple/Desktop/FINAL_FINAL/Preprocessing/Image arrays')
x_test.tofile('x_test_MTF.txt',sep=" ",format="%s") #Writing x_test to file
test_label.tofile('y_test_MTF.txt', sep = " ", format = "%s") #Writing labels of test to file

##################
    
    #Saving high quality MTF images

#Read image array
os.getcwd()
os.chdir('/Users/apple/Desktop/FINAL_FINAL/Preprocessing/Image arrays')

x_test = np.loadtxt('x_test_MTF_j.txt').reshape(204,61,61)

#This is how the images look
f, ax = plt.subplots()
ax.imshow(x_test[28])
#Saving the drowsy image 
f.savefig('MTF_drowsy.eps', format='eps', dpi=300)

f, ax = plt.subplots()
ax.imshow(x_test[27])
#Saving the non-drowsy image 
f.savefig('MTF_nondrowsy.eps', format='eps', dpi=300)


###################

## TRAIN case
train = pd.read_csv('train_balanced_scaled.csv')

#Reshaping the test dataframe

train_label = np.array(train.V1)

train_ts = np.array(train.iloc[:, 1:62])


#Plotting time series of

train.iloc[70, 1:61].plot(title = 'Time series plot for the 70th training sample') #This is what the time series looks like
test.iloc[2, 1:62].plot() #This is what the time series looks like

#Convertin to MTF images

c = 0
train_image_count = len(train)
x_train = np.zeros((train_image_count,61,61)) #test images
for i in range(train_ts.shape[0]):
    temp = MTF_pyts(np.array(train_ts[i]).reshape(1,-1))
    x_train[c,:,:] = temp
    c = c + 1

#This is how the images look
f, axarr = plt.subplots(2)
axarr[0].imshow(x_train[0])
axarr[1].imshow(x_train[1754])
axarr[0].set_title('Drowsy')
axarr[1].set_title('Not Drowsy')
plt.setp(axarr[0].get_xticklabels(), visible=False)


train_label.sum() #1748 drowsy images

#write array to disk
x_train.tofile('x_train_MTF.txt',sep=" ",format="%s") #Writing x_test to file
train_label.tofile('y_train_MTF.txt', sep = " ", format = "%s") #Writing labels of test to file



##################################
train.iloc[70, 1:61].plot(title = 'Time series plot for the 70th training sample')
f, ax = plt.subplots(2)
ax[0].imshow(x_train[0])
train.iloc[70, 1:61].plot()
ax[0].set_title('MTF plot of a 60s training sample')

#################################


#RP on train
c = 0
train_image_count = len(train)
x_train = np.zeros((train_image_count,61,61)) #test images
for i in range(train_ts.shape[0]):
    temp = RP_pyts(np.array(train_ts[i]).reshape(1,-1))
    x_train[c,:,:] = temp
    c = c + 1

#write array to disk
x_train.tofile('x_train_RP.txt',sep=" ",format="%s") #Writing x_test to file
train_label.tofile('y_train_RP.txt', sep = " ", format = "%s") #Writing labels of test to file


c = 0
test_image_count = len(test)
x_test = np.zeros((test_image_count,61,61)) #test images
for i in range(test_ts.shape[0]):
    temp = MTF_pyts(np.array(test_ts[i]).reshape(1,-1))
    x_test[c,:,:] = temp
    c = c + 1

x_test.tofile('x_test_RP.txt',sep=" ",format="%s") #Writing x_test to file
test_label.tofile('y_test_RP.txt', sep = " ", format = "%s") #Writing labels of test to file




##################
    
    #Saving high quality RP images

#Read image array
os.getcwd()
os.chdir('/Users/apple/Desktop/FINAL_FINAL/Preprocessing/Image arrays')

x_test = np.loadtxt('x_test_RP_j.txt').reshape(204,61,61)

#This is how the images look
f, ax = plt.subplots()
ax.imshow(x_test[28])
#Saving the drowsy image 
f.savefig('RP_drowsy.eps', format='eps', dpi=300)

f, ax = plt.subplots()
ax.imshow(x_test[27])
#Saving the non-drowsy image 
f.savefig('RP_nondrowsy.eps', format='eps', dpi=300)


###################
