#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 00:20:56 2018

@author: Kartik
"""


import os
from keras.models import Model
from keras.layers import Input, PReLU, Dense, LSTM, multiply, concatenate, Activation
from keras.layers import Conv1D, BatchNormalization, GlobalAveragePooling1D, Permute, Dropout

os.getcwd()
os.chdir('/Users/apple/Desktop/FINAL_FINAL/LSTM-CNN')


from constants import MAX_SEQUENCE_LENGTH_LIST, NB_CLASSES_LIST
from keras_utils import train_model, evaluate_model, set_trainable, visualize_context_vector, visualize_cam, fit_model
from layer_utils import AttentionLSTM

DATASET_INDEX = 0

MAX_SEQUENCE_LENGTH = MAX_SEQUENCE_LENGTH_LIST[DATASET_INDEX]
NB_CLASS = NB_CLASSES_LIST[DATASET_INDEX]

TRAINABLE = True


def generate_model():
    ip = Input(shape=(1, MAX_SEQUENCE_LENGTH))

    x = LSTM(8)(ip)
    x = Dropout(0.8)(x)

    y = Permute((2, 1))(ip)
    y = Conv1D(128, 8, padding='same', kernel_initializer='he_uniform')(y)
    y = BatchNormalization()(y)
    y = Activation('relu')(y)

    y = Conv1D(256, 5, padding='same', kernel_initializer='he_uniform')(y)
    y = BatchNormalization()(y)
    y = Activation('relu')(y)

    y = Conv1D(128, 3, padding='same', kernel_initializer='he_uniform')(y)
    y = BatchNormalization()(y)
    y = Activation('relu')(y)

    y = GlobalAveragePooling1D()(y)

    x = concatenate([x, y])

    out = Dense(NB_CLASS, activation='softmax')(x)

    model = Model(ip, out)

    model.summary()

    # add load model code here to fine-tune

    return model


def generate_model_2():
    ip = Input(shape=(1, MAX_SEQUENCE_LENGTH))

    x = AttentionLSTM(8)(ip)
    x = Dropout(0.8)(x)

    y = Permute((2, 1))(ip)
    y = Conv1D(128, 8, padding='same', kernel_initializer='he_uniform')(y)
    y = BatchNormalization()(y)
    y = Activation('relu')(y)

    y = Conv1D(256, 5, padding='same', kernel_initializer='he_uniform')(y)
    y = BatchNormalization()(y)
    y = Activation('relu')(y)

    y = Conv1D(128, 3, padding='same', kernel_initializer='he_uniform')(y)
    y = BatchNormalization()(y)
    y = Activation('relu')(y)

    y = GlobalAveragePooling1D()(y)

    x = concatenate([x, y])

    out = Dense(NB_CLASS, activation='softmax')(x)

    model = Model(ip, out)

    model.summary()

    # add load model code here to fine-tune

    return model


#if __name__ == "__main__":
    #model = generate_model_2()

model = generate_model()

#train_model(model, DATASET_INDEX, dataset_prefix='drowsy', epochs=2, batch_size=32)

evaluate_model(model, DATASET_INDEX, dataset_prefix='drowsy', batch_size=128)

ypred = fit_model(model, DATASET_INDEX, dataset_prefix = 'drowsy', batch_size = 128) ##I createdd

os.chdir('/Users/Apple/Desktop')
import pandas as pd
from keras.utils import to_categorical
import numpy as np
test = pd.read_csv('Kartik_TRAIN.csv')
test = test.iloc[:, 0:1]
test = to_categorical(test, len(np.unique(test)))
from sklearn.metrics import roc_auc_score
roc_auc_score(test, ypred)

#ypred = pd.DataFrame(ypred)
#ypred.to_csv('ypred_76.csv')

#roc = np.column_stack((test, ypred))
#roc_df=pd.DataFrame(roc)
#os.chdir('/Users/apple/Desktop/FINAL_FINAL/ROC')
#roc_df.to_csv("custom_cnn_lstm_predicted.csv")


visualize_context_vector(model, DATASET_INDEX, dataset_prefix='drowsy', visualize_sequence=True,
                         visualize_classwise=True, limit=1)

visualize_cam(model, DATASET_INDEX, dataset_prefix='drowsy', class_id=0)

