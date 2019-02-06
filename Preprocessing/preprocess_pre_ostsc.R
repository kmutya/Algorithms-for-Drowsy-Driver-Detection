
library(data.table)
library(OSTSC) #Over Sampling for Time Series Classification
library(tidyverse)


#First for the test case 
setwd("/Users/apple/Google Drive/A&M/Fall 2018/Directed Studies/Data/Test")
fullData = NULL  #Creating a Data frame
drives = list.files() #getting list of files in working Directory

for(drive in drives){#creating for loop in the wd 
  temp = fread(drive)[,c("Event_ID","RunName","TD","win60s","Time","Steering_Angle","Brake_Pedal_Pos","Acceler_Pedal_Pos")]
  temp = arrange(temp, Time)
  temp = group_by(temp, RunName, win60s,Event_ID)  
################################

  temp$nTime = floor(temp$Time*1)
  temp$drowsy = !is.na(temp$TD)
  temp = group_by(temp, RunName,win60s,Event_ID,nTime) %>% summarize(Steering_Angle=median(Steering_Angle, na.rm=T), drowsy=any(drowsy), Brake_Pedal_Pos=median(Brake_Pedal_Pos, na.rm=T), Acceler_Pedal_Pos=median(Acceler_Pedal_Pos, na.rm=T))
##Need to normalize time
  for(i in c(1:(max(temp$win60s)))){
  temp[temp$win60s == i, ]$nTime = temp[temp$win60s == i, ]$nTime - min(temp[temp$win60s ==i, ]$nTime)
  }
  temp = group_by(temp, RunName, win60s,Event_ID)
  temp = mutate(temp, dd=any(drowsy))
  temp$drowsy = temp$dd
  temp$dd = NULL


  if(max(temp$nTime) <= 60){
    #temp = spread(temp, key=nTime,value=Steering_Angle, sep="_")
    #temp = subset(temp, is.na(nTime_60) == F)
    #For Steering Angle Data only
    temp1=temp[temp$Event_ID=='311',c("nTime","win60s","RunName","drowsy","Steering_Angle")] #only choosing event 311
    xmin=min(temp1$win60s)
    temp1=temp1[temp1$win60s!=xmin,]
    temp1 = spread(temp1, key=nTime,value=Steering_Angle, sep="_")
    temp1 = subset(temp1, is.na(nTime_60) == F)
    #for Acceleration Data only
    temp2=temp[temp$Event_ID=='311',c("nTime","win60s","RunName","Acceler_Pedal_Pos")] 
    temp2=temp2[temp2$win60s!=xmin,]
    temp2 = spread(temp2, key=nTime,value=Acceler_Pedal_Pos, sep="_")
    temp2 = subset(temp2, is.na(nTime_60) == F)
    #for Breaking Pedal Data only
    temp3=temp[temp$Event_ID=='311',c("nTime","win60s","RunName","Brake_Pedal_Pos")] 
    temp3=temp3[temp3$win60s!=xmin,]
    temp3 = spread(temp3, key=nTime,value=Brake_Pedal_Pos, sep="_")
    temp3 = subset(temp3, is.na(nTime_60) == F)
    temp=cbind(temp1,temp2[,3:63],temp3[,3:63])
    
    fullData = rbind(fullData, temp)
  }
  
}
 
#Renaming column names
sa=  sprintf("snTime_%d", 0:60)
colnames(fullData)[4:64]=sa
ap=sprintf("anTime_%d", 0:60)
colnames(fullData)[65:125]=ap
bp=sprintf("bnTime_%d", 0:60)
colnames(fullData)[126:186]=bp
  
setwd("/Users/apple/Google Drive/A&M/Fall 2018/Directed Studies/Final/Ap2")
write.csv(fullData,"pre_ostsc_test.csv")


###################################

#First for the test case 
setwd("/Users/apple/Google Drive/A&M/Fall 2018/Directed Studies/Data/Individual_subjects")
drives = list.files() #getting list of files in working Directory


fullData = NULL  #Creating a Data frame



for(drive in drives){#creating for loop in the wd 
  temp = fread(drive)[,c("Event_ID","RunName","TD","win60s","Time","Steering_Angle","Brake_Pedal_Pos","Acceler_Pedal_Pos")]
  temp = arrange(temp, Time)
  temp = group_by(temp, RunName, win60s,Event_ID)  
  ################################
  
  temp$nTime = floor(temp$Time*1)
  temp$drowsy = !is.na(temp$TD)
  temp = group_by(temp, RunName,win60s,Event_ID,nTime) %>% summarize(Steering_Angle=median(Steering_Angle, na.rm=T), drowsy=any(drowsy), Brake_Pedal_Pos=median(Brake_Pedal_Pos, na.rm=T), Acceler_Pedal_Pos=median(Acceler_Pedal_Pos, na.rm=T))
  ##Need to normalize time
  for(i in c(1:(max(temp$win60s)))){
    temp[temp$win60s == i, ]$nTime = temp[temp$win60s == i, ]$nTime - min(temp[temp$win60s ==i, ]$nTime)
  }
  temp = group_by(temp, RunName, win60s,Event_ID)
  temp = mutate(temp, dd=any(drowsy))
  temp$drowsy = temp$dd
  temp$dd = NULL
  
  
  if(max(temp$nTime) <= 60){
    #temp = spread(temp, key=nTime,value=Steering_Angle, sep="_")
    #temp = subset(temp, is.na(nTime_60) == F)
    #For Steering Angle Data only
    temp1=temp[temp$Event_ID=='311',c("nTime","win60s","RunName","drowsy","Steering_Angle")] #only choosing event 311
    xmin=min(temp1$win60s)
    temp1=temp1[temp1$win60s!=xmin,]
    temp1 = spread(temp1, key=nTime,value=Steering_Angle, sep="_")
    temp1 = subset(temp1, is.na(nTime_60) == F)
    #for Acceleration Data only
    temp2=temp[temp$Event_ID=='311',c("nTime","win60s","RunName","Acceler_Pedal_Pos")] 
    temp2=temp2[temp2$win60s!=xmin,]
    temp2 = spread(temp2, key=nTime,value=Acceler_Pedal_Pos, sep="_")
    temp2 = subset(temp2, is.na(nTime_60) == F)
    #for Breaking Pedal Data only
    temp3=temp[temp$Event_ID=='311',c("nTime","win60s","RunName","Brake_Pedal_Pos")] 
    temp3=temp3[temp3$win60s!=xmin,]
    temp3 = spread(temp3, key=nTime,value=Brake_Pedal_Pos, sep="_")
    temp3 = subset(temp3, is.na(nTime_60) == F)
    temp=cbind(temp1,temp2[,3:63],temp3[,3:63])
    
    fullData = rbind(fullData, temp)
  }
  
}

#Renaming column names
sa=  sprintf("snTime_%d", 0:60)
colnames(fullData)[4:64]=sa
ap=sprintf("anTime_%d", 0:60)
colnames(fullData)[65:125]=ap
bp=sprintf("bnTime_%d", 0:60)
colnames(fullData)[126:186]=bp

setwd("/Users/apple/Google Drive/A&M/Fall 2018/Directed Studies/Final/Ap2")
write.csv(fullData,"pre_ostsc_train.csv")

