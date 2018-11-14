#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 16:08:52 2018

@author: Kartik
"""

import glob
import pandas as pd
import numpy as np
import os


#######Read files and assign unique ID to each win60s event#######

#Test case
df_master = pd.DataFrame()
c=1
path = r'/Users/apple/Google Drive/A&M/Fall 2018/Directed Studies/Data/Test'
for name_file in glob.glob(path + "/*.csv"):
    temp = pd.read_csv(name_file, usecols = ['Event_ID','Steering_Angle','TD','Time','win60s']) #Read only these columns
    temp['win60s'] = temp['win60s'].apply(lambda x: str(x)+'_'+str(c))
    df_master = pd.concat([df_master,temp])
    c+=1
df_master.head()

#Filtering such that data has only event 311    
req_data = df_master[df_master.Event_ID == 311]

def pre(z):
    '''Takes in a dataframe with event 311 assigns TD as 1 for each rolling window,
    removes events with less than 1500 observations'''
    #For each rolling window with TD = 1 assign that series as drowsy
    td1 = z.loc[z.TD == 1].win60s #win60s for Obs where TD = 1
    for y in td1:
        z.loc[z.win60s == y, 'TD'] = 1
    #Remove events with less that 1500obs
    win60s_all = z.win60s.value_counts() #Get counts of all win60s values
    win60s_freq = pd.DataFrame(win60s_all).reset_index() #Create a dataframe of win60s values 
    win60s_freq.columns = ['win60s','freq']
    win60s_nn = win60s_freq.loc[win60s_freq.freq<1500, 'win60s'] #Filter for all those values to be removed i.e below 1500 
    win60s_nn = win60s_nn.as_matrix()
    for j in win60s_nn:
        z = z[z.win60s != j] #win60s Events with <1500 obs now removed
    return(z)
    
req_data = pre(req_data)

test_image_count = len(req_data.win60s.unique()) #229 unique 60s windows remaiing.
len(req_data.loc[req_data.TD == 1, 'win60s'].unique()) #15 Drowsy Images 



###TRAIN CASE###

df_train = pd.DataFrame()
c=1
path = r'/Users/apple/Google Drive/A&M/Fall 2018/Directed Studies/Data/Individual_subjects'
for name_file in glob.glob(path + "/*.csv"):
    temp = pd.read_csv(name_file, usecols = ['Event_ID','Steering_Angle','TD','Time','win60s']) #Read only these columns
    temp['win60s'] = temp['win60s'].apply(lambda x: str(x)+'_'+str(c))
    df_train = pd.concat([df_train,temp])
    c+=1
df_train.head()

#Filtering such that data has only event 311    
df_train = df_train[df_train.Event_ID == 311] #7412742, 5

df_train = pre(df_train)


train_image_count = len(df_train.win60s.unique()) #2095 unique 60s windows remaning.
len(df_train.loc[df_train.TD == 1, 'win60s'].unique()) #58 Drowsy Images 