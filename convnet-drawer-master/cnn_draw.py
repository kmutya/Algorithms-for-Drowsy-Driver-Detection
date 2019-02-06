#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 23:07:55 2018

@author: Kartik
"""
import os
os.getcwd()
os.chdir('/Users/apple/Desktop/FINAL_FINAL/convnet-drawer-master')

from convnet_drawer import Model, Conv2D, MaxPooling2D, Flatten, Dense
from pptx_util import save_model_to_pptx
from matplotlib_util import save_model_to_file

model2 = Model(input_shape=(61, 61, 3))
model2.add(Conv2D(61, (3,3), padding='same'))
model2.add(Conv2D(61, (3,3)))
model2.add(Conv2D(61, (3,3)))
model2.add(Conv2D(61, (3,3)))
model2.add(MaxPooling2D(pool_size=(2,2)))
model2.add(Conv2D(61, (3,3)))
model2.add(Conv2D(61, (3,3)))
model2.add(Conv2D(61, (3,3)))
model2.add(Conv2D(61, (3,3)))
model2.add(Conv2D(32, (3,3), padding='same'))
model2.add(Conv2D(32, (3, 3)))
model2.add(Conv2D(16, (3,3), padding='same'))
model2.add(Conv2D(16, (3,3), padding='same'))
model2.add(MaxPooling2D(pool_size=(2,2)))
model2.add(Conv2D(16, (3,3), padding='same'))
model2.add(Conv2D(16, (3,3), padding='same'))
model2.add(Conv2D(16, (3, 3)))
model2.add(MaxPooling2D(pool_size=(2,2)))
model2.add(Flatten())
model2.add(Dense(256))
model2.add(Dense(1))
model2.save_fig("example.svg")


