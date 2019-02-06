# Confusion Matrix
library(data.table)
library(caret)
library(pROC)
# while(!round(roc(df$actual, df$random)$auc,2) == 0.5){
#   df$random = runif(nrow(df))
# }

setwd("/Users/apple/Desktop/FINAL_FINAL/Analysis")

df= fread("all_pred.csv")

cnn = roc(df$Label, df$CNN, ci = T)

cnn_lstm = roc(df$Label, df$CNN_LSTM, ci =T)

vgg16_mtf = roc(df$Label, df$VGG16_mtf, ci = T)

vgg16_rp = roc(df$Label, df$VGG16_rp, ci =T)

vgg19_mtf = roc(df$Label, df$VGG19_mtf, ci =T)

vgg19_rp = roc(df$Label, df$VGG19_rp, ci = T)

boss = roc(df$Label, df$boss, ci = T )

saxvsm = roc(df$Label, df$SAXVSM, ci =T)

knn = roc(df$Label, df$KNN, ci =T)



##############
plot.roc(cnn, xlim=c(1,0), col='blue', legacy.axes=TRUE)
plot.roc(cnn_lstm, legacy.axes=TRUE, xlim=c(0.5,0), add=TRUE,
         col='red')
plot.roc(vgg16_mtf, legacy.axes=TRUE, xlim=c(1,0), add=TRUE,
         col='magenta')

plot.roc(vgg16_rp, legacy.axes=TRUE, xlim=c(1,0), add=TRUE,
         col='darkgreen')
plot.roc(vgg19_mtf, legacy.axes=TRUE, xlim=c(1,0), add=TRUE,
         col='cyan')
plot.roc(vgg19_rp, legacy.axes=TRUE, xlim=c(1,0), add=TRUE,
         col='pink')
plot.roc(boss, legacy.axes=TRUE, xlim=c(1,0), add=TRUE)
plot.roc(saxvsm, legacy.axes=TRUE, xlim=c(1,0), add=TRUE)
plot.roc(knn, legacy.axes=TRUE, xlim=c(1,0), add=TRUE)

abline(h=0.56, lty=2, col="grey")


# legend("bottomright", legend=c("DT=0.4806-0.6805 ", "RF=0.4898-0.6698",
#                                "SVM=0.4022-0.5872",
#                                "ANN=0.52-0.6965", "CNN=0.5422-0.7221"),
#        col=c('cyan2', "darkgreen","magenta","blue","red"), lwd=2)
#dev.off()

cols=c("#e41a1c","#377eb8","#4daf4a","#984ea3","yellow","orange","pink")

pdf("Final Results smoothed.pdf",pointsize=10)
plot(smooth(cnn), print.auc=F, main="",xaxt="n",ylab="True Positive Rate", xlab="False Positive Rate",col=cols[1])
plot(smooth(cnn_lstm), print.auc=F, main="",xaxt="n",ylab="True Positive Rate", xlab="False Positive Rate",col=cols[2],add=T)
plot(smooth(vgg16_rp), print.auc=F, main="",xaxt="n",ylab="True Positive Rate", xlab="False Positive Rate",col=cols[3],add=T)
plot(smooth(vgg19_mtf), print.auc=F, main="",xaxt="n",ylab="True Positive Rate", xlab="False Positive Rate",col=cols[4],add=T)
plot(boss, print.auc=F, main="",xaxt="n",ylab="True Positive Rate", xlab="False Positive Rate",col=cols[5],add=T)
plot(saxvsm, print.auc=F, main="",xaxt="n",ylab="True Positive Rate", xlab="False Positive Rate",col=cols[6],add=T)
plot(knn, print.auc=F, main="",xaxt="n",ylab="True Positive Rate", xlab="False Positive Rate",col=cols[7],add=T)
#abline(h=0.56, lty=2, col="grey")
legend(0.3,0.3,legend=c(paste("CNN: ",round(as.numeric(cnn$ci)[2],2),sep=""),
                        paste("CNN-LSTM:  ",round(as.numeric(cnn_lstm$ci)[2],2),sep=""),
                        paste("VGG16 (RP):  ", round(as.numeric(vgg16_rp$ci)[2],2),sep=""),
                        paste("VGG19 (MTF):  ", round(as.numeric(vgg19_mtf$ci)[2],2),sep=""),
                        paste("BOSSVS:  ", round(as.numeric(boss$ci)[2],2),sep=""),
                        paste("SAXVSM:  ", round(as.numeric(saxvsm$ci)[2],2),sep=""),
                        paste("KNN:  ", round(as.numeric(knn$ci)[2],2),sep="")),bty="o",bg="white",box.col="white",
       col=cols,lwd=2)
axis(1, at=seq(1,0,by=-0.2), labels=c("0.0","0.2","0.4","0.6","0.8","1.0"),pos=-0.04)
dev.off()

png("Final Results smoothed.png",pointsize=10)
plot(smooth(cnn), print.auc=F, main="",xaxt="n",ylab="True Positive Rate", xlab="False Positive Rate",col=cols[1])
plot(smooth(cnn_lstm), print.auc=F, main="",xaxt="n",ylab="True Positive Rate", xlab="False Positive Rate",col=cols[2],add=T)
plot(smooth(vgg16_rp), print.auc=F, main="",xaxt="n",ylab="True Positive Rate", xlab="False Positive Rate",col=cols[3],add=T)
plot(smooth(vgg19_mtf), print.auc=F, main="",xaxt="n",ylab="True Positive Rate", xlab="False Positive Rate",col=cols[4],add=T)
plot(boss, print.auc=F, main="",xaxt="n",ylab="True Positive Rate", xlab="False Positive Rate",col=cols[5],add=T)
plot(saxvsm, print.auc=F, main="",xaxt="n",ylab="True Positive Rate", xlab="False Positive Rate",col=cols[6],add=T)
plot(knn, print.auc=F, main="",xaxt="n",ylab="True Positive Rate", xlab="False Positive Rate",col=cols[7],add=T)
#abline(h=0.56, lty=2, col="grey")
legend(0.3,0.3,legend=c(paste("CNN: ",round(as.numeric(cnn$ci)[2],2),sep=""),
                        paste("CNN-LSTM:  ",round(as.numeric(cnn_lstm$ci)[2],2),sep=""),
                        paste("VGG16 (RP):  ", round(as.numeric(vgg16_rp$ci)[2],2),sep=""),
                        paste("VGG19 (MTF):  ", round(as.numeric(vgg19_mtf$ci)[2],2),sep=""),
                        paste("BOSSVS:  ", round(as.numeric(boss$ci)[2],2),sep=""),
                        paste("SAXVSM:  ", round(as.numeric(saxvsm$ci)[2],2),sep=""),
                        paste("KNN:  ", round(as.numeric(knn$ci)[2],2),sep="")),bty="o",bg="white",box.col="white",
       col=cols,lwd=2)
axis(1, at=seq(1,0,by=-0.2), labels=c("0.0","0.2","0.4","0.6","0.8","1.0"),pos=-0.04)
dev.off()

