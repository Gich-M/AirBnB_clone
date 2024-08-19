import yfinance as yf
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
from keras.models import Sequential
from keras.layers import LSTM,Dropout,Dense
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings("ignore")

#importing the data
df=yf.download('CHF=X',start='2009-01-09',end='2021-09-07')

df.tail(4)

#display the graph
df.index
plt.figure(figsize=(30,12))
plt.plot(df["Low"],label='Price history')

df.dtypes

df.shape

df.isnull().sum()

#df.dropna(inplace=True)


#taking the low price from the dataframe
data=df.filter(['Low'])
dataset=data.values
#split data to train set , 80% to train
training_data_len=math.ceil(len(dataset)*.8)

dataset.shape

print(training_data_len)

#scaling the data
#sc =StandardScaler()
#scaled_data = sc.fit_transform(dataset)
#scaling the data
from sklearn.preprocessing import MinMaxScaler
sc =MinMaxScaler(feature_range=(0, 1))
scaled_data = sc.fit_transform(dataset)

#print length of train set
train_data=scaled_data[0:training_data_len,:]
len(train_data)

#spliting dta to x_train and y_train using train data set
#tutakua tuna tumia previous 60 days ku predict of current day 

x_train=[]
y_train=[]

for i in range(60,len(train_data)):
    x_train.append(train_data[i-60:i, 0])
    y_train.append(train_data[i,0])
  

#convert list to numpy
x_train,y_train=np.array(x_train),np.array(y_train)

len(x_train),len(y_train)

x_train.shape

x_train.shape[0]

x_train.shape[1]

#reshape data ikue 3D since LSTM inachukua 3Dimension data
x_train=np.reshape(x_train,(x_train.shape[0],x_train.shape[1],1))

#taking the last 20% ikue test data

test_data=scaled_data[training_data_len - 60: ,:]
len(test_data)

#spliting test data to x_test and y_test

x_test=[]
y_test=dataset[training_data_len:,:]
for i in range(60,len(test_data)):
    x_test.append(test_data[i-60:i, 0])
 
#convert list to numpy
x_test=np.array(x_test)

len(x_test),len(y_test)

#reshape to 3Dimension
x_test=np.reshape(x_test,(x_test.shape[0],x_test.shape[1],1))

model=Sequential()
model.add(LSTM(units=50, return_sequences=True,input_shape=(x_train.shape[1],1)))

model.add(LSTM(units=50,activation='relu',return_sequences=False))
model.add(Dropout(0.3))

model.add(Dense(128))
model.add(Dense(1))

#model.summary()

model.compile(loss='mean_squared_error',optimizer='Adam')
model.fit(x_train,y_train,epochs=100,batch_size=32)

model.evaluate(x_test,y_test)

predictions=model.predict(x_test)

prediction=sc.inverse_transform(predictions)

rmse=np.sqrt(np.mean(prediction - y_test)**2)
rmse

mse=np.mean((prediction - y_test)**2)
mse

train=data[:training_data_len]
valid=data[training_data_len:]
valid['prediction']=prediction

plt.figure(figsize=(30,12))
plt.xlabel('Date')
plt.ylabel('Highest price')
plt.plot(train['Low'])
plt.plot(valid[['Low','prediction']])
plt.legend(['Train','Val','prediction'],loc='upper left')
plt.show()

f.tail(5).round(4)

subtract=f['prediction']-f['Low']

#subtract.tail(5)

diff=subtract*10000

diff.head(5)

diff.tail(5).round(2)

d=yf.download('CHF=X',start='2009-01-09',end='2021-08-27')
d.dropna(inplace=True)
new=d.filter(['Low'])
#GET last 60 day Highest price and conver the dataframe to array
last=new[-60:].values
lastscale=sc.transform(last)
#create an empty list
X_test=[]
X_test.append(lastscale)
X_test=np.array(X_test)
X_test=np.reshape(X_test,(X_test.shape[0],X_test.shape[1],1))
predprice=model.predict(X_test)
predprice=sc.inverse_transform(predprice)

print(predprice)