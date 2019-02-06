
library(pROC)
library(ggplot2)
#creating a function to plot roc with CI
roc_plot = function(label, pred){
  roc(label, pred)
  roc_plot_temp <- roc(label, pred, 
                         percent=TRUE,
                       # arguments for plot
                         plot=TRUE, auc.polygon=TRUE, max.auc.polygon=TRUE, grid=TRUE,
                         print.auc=TRUE, show.thres=TRUE)
  return(roc_plot_temp)
}


#Location with prediction files
getwd()
setwd('/Users/apple/Desktop/FINAL_FINAL/ROC')

#Predictions of custom_cnn
custom_cnn = read.csv('custom_cnn_predicted.csv')
custom_cnn = custom_cnn[-1]
#ROC
roc_plot(custom_cnn$X0, custom_cnn$X1)
sens.ci <- ci.se(roc_plot(custom_cnn$X0, custom_cnn$X1), specificities=seq(0, 100, 5))
plot(sens.ci, type="shape", col="lightblue")
plot(sens.ci, type="bars")

#Predictions of custom LSTM-CNN
custom_lstm_cnn = read.csv('custom_cnn_lstm_predicted.csv')
custom_lstm_cnn = custom_lstm_cnn[-1]
#ROC
roc_plot(custom_lstm_cnn$X0, custom_lstm_cnn$X2)
sens.ci <- ci.se(roc_plot(custom_lstm_cnn$X0, custom_lstm_cnn$X2), specificities=seq(0, 100, 5))
plot(sens.ci, type="shape", col="lightblue")
plot(sens.ci, type="bars")

#Predictions of VGG16 on MTF
vgg16_MTF = read.csv('roc_mtf_16_predicted.csv')
vgg16_MTF = vgg16_MTF[-1]
#ROC
roc_plot(vgg16_MTF$X0, vgg16_MTF$X1)
sens.ci <- ci.se(roc_plot(vgg16_MTF$X0, vgg16_MTF$X1), specificities=seq(0, 100, 5))
plot(sens.ci, type="shape", col="lightblue")
plot(sens.ci, type="bars")

#Predictions of VGG16 on RP
vgg16_RP = read.csv('roc_rp_16_predicted.csv')
vgg16_RP = vgg16_RP[-1]
#ROC
roc_plot(vgg16_RP$X0, vgg16_RP$X1)
sens.ci <- ci.se(roc_plot(vgg16_RP$X0, vgg16_RP$X1), specificities=seq(0, 100, 5))
plot(sens.ci, type="shape", col="lightblue")
plot(sens.ci, type="bars")


#Predictions of VGG19 on MTF
vgg19_MTF = read.csv('roc_mtf_19_predicted.csv')
vgg19_MTF = vgg19_MTF[-1]
#ROC
roc_plot(vgg19_MTF$X0, vgg19_MTF$X1)
sens.ci <- ci.se(roc_plot(vgg19_MTF$X0, vgg19_MTF$X1), specificities=seq(0, 100, 5))
plot(sens.ci, type="shape", col="lightblue")
plot(sens.ci, type="bars")


#Predictions of VGG16 on RP
vgg19_RP = read.csv('roc_rp_19_predicted.csv')
vgg19_RP = vgg19_RP[-1]
#ROC
roc_plot(vgg19_RP$X0, vgg19_RP$X1)
sens.ci <- ci.se(roc_plot(vgg19_RP$X0, vgg19_RP$X1), specificities=seq(0, 100, 5))
plot(sens.ci, type="shape", col="lightblue")
plot(sens.ci, type="bars")

#Plot of all AUC 
#Define ROC for all
custom_cnn_1 = roc(custom_cnn$X0, custom_cnn$X1)
custom_lstm_cnn_1 = roc(custom_lstm_cnn$X0, custom_lstm_cnn$X2)
vgg16_MTF_1 = roc(vgg16_MTF$X0, vgg16_MTF$X1)
vgg_16_RP_1 = roc(vgg16_RP$X0, vgg16_RP$X1)
vgg_19_MTF_1 = roc(vgg19_MTF$X0, vgg19_MTF$X1)
vgg_19_RP_1 = roc(vgg19_RP$X0, vgg19_RP$X1)
# Multiple curves:
g2 <- ggroc(list(Custom_CNN_62.95 = custom_cnn_1, Custom_lstm_cnn_75.98 = custom_lstm_cnn_1, VGG16_MTF_66.61 = vgg16_MTF_1,
                 VGG16_RP_70.75 = vgg_16_RP_1, VGG19_MTF_70 = vgg_19_MTF_1, VGG19_RP_66.3 = vgg_19_RP_1))
g2 + ggtitle("Roc plot of all models") 



