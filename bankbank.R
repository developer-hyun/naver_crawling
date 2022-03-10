setwd("C:\\Users\\ksy74\\Videos\\Downloads")
rm(list=ls())
bank = read.csv("BankChurners.csv",header = T)

# 데이터 전처리
bank = bank[,-c(1,22,23)]
colnames(bank)

numer = bank[,c(2,9:20)]
length(numer)
cat = bank[,c(1,3,5,6,7,8)]
bank = cbind(cat,numer)
colnames(bank)
str(bank)
summary(bank)
# 데이터 EDA

library(ggplot2)
library(gridExtra)
library(gmodels)

bank$Attrition_Flag[which(bank$Attrition_Flag == "Attrited Customer")] = 1
bank$Attrition_Flag[which(bank$Attrition_Flag == "Existing Customer")] = 0

plot_list = list()
for(i in 2:length(cat)){
  assign(paste0("V",i),c())
}
V2 = ggplot(bank, aes(Attrition_Flag, fill = bank[,2]))+ geom_bar()
V3 = ggplot(bank, aes(Attrition_Flag, fill = bank[,3]))+ geom_bar()
V4 = ggplot(bank, aes(Attrition_Flag, fill = bank[,4]))+ geom_bar()
V5 = ggplot(bank, aes(Attrition_Flag, fill = bank[,5]))+ geom_bar()
V6 = ggplot(bank, aes(Attrition_Flag, fill = bank[,6]))+ geom_bar()
grid.arrange(V2,V3,V4,V5,V6, nrow = 2, ncol = 3)

##Customer_Age
summary(bank$Customer_Age) ## 최소 26, 최대 73 , 9개의 그룹으로 범주화
t = plot(table(bank$Customer_Age))


i = 25
a = 1
while(i<75){
  bank$Customer_Age[which(bank$Customer_Age>=i & bank$Customer_Age < i+5)] = a
  i = i + 5
  a = a + 1
}

table(bank$Customer_Age)
bank$Customer_Age[which(bank$Customer_Age==10)] = 9
bank$Customer_Age = as.factor(bank$Customer_Age)

## 총 거래금액
summary(bank$Total_Trans_Amt)
plot(density(bank$Total_Trans_Amt))
ggplot(bank, aes(Total_Trans_Amt)) + geom_bar()


## 총거래횟수

summary(bank$Total_Trans_Ct)
plot(density(bank$Total_Trans_Ct))
ggplot(bank,aes(Total_Trans_Ct)) + geom_bar()

### 총 거래횟수가 올라갈수록 대체적으로 총 거래금액도 올라간다.
#다만 세 집단으로 나눠지는 경향이 있어 세 집단으로 나누어서 상관성을 다시 본다 
plot(bank$Total_Trans_Amt,bank$Total_Trans_Ct)

plot(density(bank$Total_Trans_Amt[which(bank$Total_Trans_Amt>5000&bank$Total_Trans_Amt<7500)]))
## 이면 대략 6250에서 한 번 끊고
plot(density(bank$Total_Trans_Amt[which(bank$Total_Trans_Amt>10000&bank$Total_Trans_Amt<12000)]))
## 이면 대략 11000에서 한 번 끊으면 될 것 같다
## 임시 파생변수를 만들어준다

bank$group = 0
bank$group[which(bank$Total_Trans_Amt<6250)] = 1
bank$group[which(bank$Total_Trans_Amt>6250 & bank$Total_Trans_Amt<11000)] = 2
bank$group[which(bank$Total_Trans_Amt>=11000)] =3 
head(bank)
bank$group = as.factor(bank$group)
summary(bank)

ggplot(bank, aes(x = Total_Trans_Amt, y = Total_Trans_Ct,color = group))+ geom_point()

## group 1 에서는 다소 총 거래금액이 증가함에 따라 총 거래횟수도 증가한다. 하지만 group 2 와 3에서는 그렇지 않아보인다.


ggplot(bank, aes(x = Total_Trans_Amt, y = Total_Trans_Ct,color = Attrition_Flag))+ geom_point()
## 나누어진 곳이 1, 2, 3 집단이라고 할 때 소비액수와 횟수가 가장 큰 3집단에서는 Attired Customer가 나타나지 않는다. 그리고 1,2 집단에서는 총 소비액수에 비해 구매건수가 적은 사람들이 attired customer 인 것을 보아 파생변수 '1회 평균 구매액' 을 생성한다
colnames(bank)
bank$aver = bank$Total_Trans_Amt/bank$Total_Trans_Ct


ggplot(bank, aes(x = Total_Trans_Amt, y = Credit_Limit,color = Attrition_Flag))+ geom_point()

# 총 거래 금액이 특이하게 3개의 집단으로 나누어진다는 것을 바탕으로 다른 변수들과도 점을 찍어봤을 때 또 한가지 발견할 수 있었던 것은 평균 카드 사용률과의 관계에서는( 3집단에서는 attired customer 가 아예 발생하지 않고) 1 집단에서 약 2500-5000 횟수의 사용자들에게서도 avg_utilization 과 관계없이 나타나지 않는다는 것이다.
ggplot(bank, aes(x = Total_Trans_Amt, y = Avg_Utilization_Ratio,color = Attrition_Flag))+ geom_point()

# 이로 보았을 때 Attrition_Flag를 3개가 아닌 4개의 범주로 나누어서 분류하는 것이 의미가 있다고 생각하게 되었다.

plot(density(bank$Total_Trans_Amt))
## 아마 density plot 의 0과5000사이의 최솟값으로 지정하면 되지 않을까 싶다.
plot(density(bank$Total_Trans_Amt[which(bank$Total_Trans_Amt>2500&bank$Total_Trans_Amt<3500)]),)
axis(1,at = seq(2500,3500,by = 100)) ## 3050 정도에서 끊자

bank$group[which(bank$Total_Trans_Amt<6250 & bank$Total_Trans_Amt >=3050)] = 1
bank$group[which(bank$Total_Trans_Amt<3050)] = 4
ggplot(bank, aes(x = Total_Trans_Amt, y = Total_Trans_Ct,color = group))+ geom_point()
ggplot(bank, aes(x = Total_Trans_Amt, y = Avg_Utilization_Ratio,color = Attrition_Flag))+ geom_point()
ggplot(bank, aes(x = Total_Trans_Amt, y = Avg_Utilization_Ratio,color = group))+ geom_point()

CrossTable(bank$group, Attrition_Flag , prop.t=FALSE, expected=TRUE, chisq = T) # 카이-검정을 했을 때 p-value가 0에 수렴하는 값으로 매우 작게 나오기 때문에 분류가 유의미하다고 판단.