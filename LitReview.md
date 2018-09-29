This document contains a review of relevant publications pertaining to this domain.

1. McDonald, A., Schwarz, C., Lee, J. and Brown, T. (2012). Real-Time Detection of Drowsiness Related Lane Departures Using Steering Wheel Angle. Proceedings of the Human Factors and Ergonomics Society Annual Meeting, 56(1), pp.2201-2205.


> Aim of this study was to design and evaluate an algorithm to classify drowsiness-related lane departures using steering wheel angle as the independent variable.

Under the *Introduction* section, the author mentions various inputs used for drowsiness identification and points out that the three most successful measures are electroencephalogram (EEG), percentage eye closure (PERCLOS), and steering wheel angle. He then talks about how EEG is not feasible for practical applications and the adoption of PERCLOS in Co-Pilot. He then talks about the different labels of drowsiness and their limitations.

In table 1, the author mentions various machine learning approaches used, their training procedure and other relevant details. He then makes a case for using the random forest algorithm by mentioning how it alleviates the need for pre-processing of steering wheel angle.

*Algorithm development*, In this section the author given a detailed explanation regarding the simulation conducted and the data acquisition process. Regarding the output, he mentions that each departure was manually coded using the Observer Rating of Drowsiness (ORD) Scale into five bins: not drowsy (ORD < 12), slightly drowsy (12 ≤ ORD < 37), moderately drowsy (37 ≤ ORD < 62), very drowsy (62 ≤ ORD < 90), and extremely drowsy (ORD ≥ 90).
Segments under the moderately, very, or
extremely drowsy were labeled drowsy. Hence making this a binary classification problem. The final evaluation data set consisted of 578 total instances, with 162 drowsy instances, 80 alert cases matched to driver and road segment, and 336 alert cases matched to only road segment.

He then talks about the independent variable i.e steering wheel angle stating that the data were collected from a diverse set of road conditions and that no variability was removed from the data. Important to note that, data were organized by steering angle at each second from 60s before a lane departure (or matched case) to 6 s before the lane departure. This 6-s buffer was to facilitate time between detection and notification.

The author then talks about the evaluation metric i.e ROC curve. ROC curve was chosen as this is a biased classification problem. Statistical comparison between various algorithms is performed using a nonparametric method i.e U-statistics. It is used to estimate
a covariance matrix for the ROC curves and
compares multiple curves using contrasts. It was proposed by DeLong, and Clarke-Pearson (1988).

Table 3 entails a detailed evaluation of the developed algorithm against various other classification algorithms. Figure 1, contains a comparison of ROC curves.

The author then states three reasons to use this algorithm even though there isn't a significant performance difference.
1. Better ROC curve at nearly all thresholds.
2. Previous research has shown that random-forest models generally outperform simple decision trees and frequently outperform boosted tree models.
3. Both decision tree and boosted tree algorithms tend to overfit training data and fail to generalize to new data.

*Algorithm Evaluation*, In this section the author compares this algorithm to the current gold standard PERCLOS. He mentions some of PERCLOS's significant drawbacks such as: miss incidents in which a driver enters a microsleep and briefly drifts out of his or her lane, measurement error of the eye tracking system. He mentions how RF is not prey to these drawbacks.
He then goes onto talk about some drawbacks of the proposed model: 1. Lack of feature insight. 2. Perfomance not a major step up.

With this premise he states that this model might benefit by moderating its predictions using a hierarchical classification structure, such as a Bayesian network and that by incorporating longer-term indicators, such as time of day and time on task, prediction performance could improve.

He then concludes by stating two more limitations: 1. Limited data 2. Simulated data and mentioning how this paper centers drowsiness classification on a specific consequence of drowsy driving rather than a general operator state. This is particularly useful as it increases the likelihood that the driver will understand and trust the warnings and feedback provided by the vehicle.

2. McDonald, A. D., Lee, J. D., Schwarz, C., & Brown, T. L. (2018). A contextual and temporal algorithm for driver drowsiness detection. Accident Analysis & Prevention, 113, 25-37. doi:10.1016/j.aap.2018.01.005

> Aim of this study was to develop a develop a drowsy detection algorithm that utilises road context features along with driver behavioural features and evaluate that algorithm with other existing drowsy detection algorithms.

This paper extends on the Dynamic Bayesian approach briefly mentioned in McDonald et al., 2012.
*Introduction*, In this section the author mentions how DBN's explicitly model the time dependent nature of driver drowsiness and allow the inclusion of contextual factors that influence drowsy driving, such as prior sleep behaviour and road type. He provides some intuition by mentioning that DBN models consist of graph structures ,nodes, connected by directed edges that mimic the dependencies in the underlying problem, and an associated group of probabilities that model the likelihood of model state transitions. The dynamic components of the model specify dependencies across time. DBN algorithms can encode facts about drowsiness such as drivers that are drowsy are likely to stay drowsy and that drivers that are awake tend to stay awake.

He provides some background regarding various DBN methods used for drowsiness detection such as Ji et al 2006, Yang et al., 2010.

*Materials and Method*, He then talks about the experimental setup, data acquisition process, the target variable and the evaluation metric which are similar to McDonald et al., 2012. The author then talks about the features used for this study. They are of two types: 1. Driver behavioural measures 2. Road context measures. Both of these require pre-processing to be converted from their raw form to algorithm input. Driver behavioural features were pre-processed using a random forest algorithm and road context measures via Symbolic Aggregate Approximation (SAX).

1. Driver behavioural features: The driver behavioural measures used in this algorithm consist of steering wheel angle, accelerator pedal input, and brake pedal input. This study generated features from these inputs using Fourier transform, distributional statistics, a neural network, a Support Vector Machine, a k-Nearest Neighbor model, a Naïve Bayes classifier, a Decision Tree, and a random forest. All these methods were then assessed relative to their information gain on the training data post which random forest method was chosen.

2. Road context features: This study captured contextual information using speed, lateral acceleration, and longitudinal acceleration of the vehicle. These measures capture both general road characteristics, such as the differences between driving on a state highway and through a suburban neighbourhood, and also provide a direct link into these behaviours and the intentions of the driver. These mesaures were processed using Symbolic Aggregate Approximation (SAX), it converts continuous time-series data into discrete symbols. Then author then elaborates on the conversion method using SAX.

*Parameter evaluation and model selection*, The author then mentions that this study explored 4 different model structures differing in their inclusion of road type context and their treatment of maneuver-level context. Maneuver context was treated in 2 ways for model building:

1. Including the maneuver context features with the driver behavioural measures. This combination
of features was then used to train a random forest. The trained random forest votes were then used as features for the DBN.

![](assets/LitReview-300fc082.jpg)

2. Training three separate random forest models and then incorporated them into the DBN model as a multivariate normal observation.

The author mentions how using these two different model building approaches tests the value of the maneuver context features when considered independently of the driver behavioural features versus dependently. The road context inclusion and exclusion allows one to test the value of maneuver versus high-level road context and the hypothesis that with road and maneuver context combined, algorithm performance will improve on road situations that commonly involve drowsiness.

These 4 structures and 12 SAX variations produced a total of 48 different models which were compared using the ROC curve. The model with the highest AUC was a random forest with no high level road context, with a window size of 10 s, and an alphabet size of 3 (MLC_DBN) hence indicating that an algorithm without high-level context might be preferred because it achieves the same predictive performance with fewer input variables.

*Results*, The algorithm was then evaluated against 3 other algorithms a steering-based random forest algorithm (McDonald et al., 2013b), a DBN algorithm including steering and pedal input, and PERCLOS (Dinges and Grace, 1998).

According to the ROC plots, the maneuver-level context (MLC) DBN does not provide a benefit in the lower regions of the curve but provides a substantial benefit for much of the rest of the curve, particularly over the PERCLOS (PCLS) and Steering Random Forest (RF) algorithms.

![](assets/LitReview-83862ced.jpg)

The author then analyses false positives across contexts at a fixed threshold to show the contexts where the algorithm improves classification performance. He also explores false positives by simulator event.

*Conclusion*, The results of this study show that the context based algorithm developed by the author has a significantly better detection performance than simpler algorithms and PERCLOS. The author then mentions ways to improve the algorithm performance i.e reduce the no . of false positives by treating some false positives as early detection and by setting up a mitigation system to reset the state of the MLC DBN to awake after the driver has received a warning signal and then proceed with subsequent predictions as evidence is accumulated.

3. Patel, M., Lal, S., Kavanagh, D., & Rossiter, P. (2011). Applying neural network analysis on heart rate variability data to assess driver fatigue. Expert Systems with Applications, 38(6), 7235-7242. doi:10.1016/j.eswa.2010.12.028

> The aim of this study was to use a neural network to detect fatigue in drivers using heart rate variability (HRV) as the independent variable.

The author defines HRV as: 'the measure of variation in heart beats and is calculated by analyzing the time series of beat to beat interval.'

This study can be summarised in 5 steps:

1. The author applies Fast Fourier transformation to heart rate time series data to convert it into the frequency domain. He also applies convolution using a Hanning window to reduce aliasing.
2. He then generates a Spectral image of 30 x 30 pixels. This spectral image was then converted to a vector of dimensions 900 x 1 to serve as an input to the NN.
3. The author uses a shallow neural network with a bipolar logistic activation function and delta learning rule for training.
4. Five data set each (five for alert and five for fatigue) were used to train the neural network, two data sets used for validation and five data sets were used for testing the neural network.
5. The highest accuracy of 90% was obtained by using a learning constant of 0.5.

The author concludes by stating that with the help of this study HRV along with neural network can be used for the development of in-vehicle alerting and warning devices to act as a countermeasure for fatigue casualties. However, he mentions that this finding needs to be validated with a larger sample size.
