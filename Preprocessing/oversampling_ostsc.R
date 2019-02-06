getwd()
setwd('/Users/apple/Google Drive/A&M/Fall 2018/Directed Studies/Final/Ap2')

library(data.table)
library(OSTSC) #Over Sampling for Time Series Classification
library(plyr)

train=fread("pre_ostsc_train.csv")
test=fread("pre_ostsc_test.csv")
train = train[, 2:187]
test = test[,2:187]

train_balanced=OSTSC(sample=train[,4:186],label=train[,3]) #oversample time series data

x_train=as.data.table(train_balanced$sample)
y_train=as.data.table(train_balanced$label)

table(y_train) #Balanced 1/0 i.e 1743

train_balanced = cbind(y_train, x_train)
train_balanced = train_balanced[,1:62] #Only keeping label and steering wheel angle measurments

#rename column of train_balanced
sa =  sprintf("snTime_%d", 0:60)
colnames(train_balanced)[2:62] = sa

write.csv(train_balanced,"train_oversampled.csv", row.names = FALSE)


test_trimmed=test[,3:64]
test_trimmed$drowsy = mapvalues(test_trimmed$drowsy,c('TRUE','FALSE'),to=c('1','0'))
table(test_trimmed$drowsy)

write.csv(test_trimmed,"test_trimmed.csv", row.names = FALSE)



