# Algorithms-for-Drowsy-Driver-Detection

Drowsy detection algorithms are/have been developed using machine learning and shallow neural network approaches. However, there have been no attempts in utilizing deep neural networks to design such algorithms. This repository is a by-product of a study adopting a convolutional neural network and CNN Long Short-Term Memory Network ( CNN-LSTM ) approach to design drowsy detection algorithms by transforming a time series feature such as the steering wheel angle into images using markov transition field (MTF) and recurrence plots  (RP). The algorithms utilized and developed are then compared against state of the art drowsy detection and time series classification algorithms. Empirical results show that the algorithm utilized coupled with appropriate pre-processing techniques outperform state of the art drowsy detection and time series classification algorithms.

Below is a plot of the AUC curve compared against SOTA TSC algorithms namely: Bag of symbols in vector space (BOSSVS) and Symbolic Aggregate approximation and Vector Space Model (SAX-VSM)

![AUC plot of all the models](/Users/apple/Documents/github/Algorithms-for-Drowsy-Driver-Detection/Analysis/Final_smoothed.png)

Below is the architecture of the CNN used:

![AUC plot of all the models](/Users/apple/Documents/github/Algorithms-for-Drowsy-Driver-Detection/convnet-drawer-master/CNN.png)

LSTM-CNN implementation was from this paper : https://arxiv.org/pdf/1709.05206.pdf
