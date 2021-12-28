from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Model, load_model
from tensorflow.keras import callbacks

import pandas as pd 
import numpy as np 
import tensorflow as tf 
import io

df = pd.read_csv('/home/jhunter/git/Jetson-MachineLearning/data-mod/2018-training-mmscaled.csv')
x = np.array(df.drop(['Label'],1))
y = np.array(df['Label'])

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

input_units=x_train.shape[1]
units=81
output_units=1
max_epochs=1000
model=Sequential()

earlystopping=callbacks.EarlyStopping(monitor="val_accuracy",mode="max",patience=50,restore_best_weights=True)

# We have to add an input layer..
model.add(Dense(units=input_units,name='Input'))
model.add(Dense(units=units,activation='relu',name='hidden1'))
model.add(Dense(units=units,activation='relu',name='hidden2'))
model.add(Dense(units=units,activation='relu',name='hidden3'))
model.add(Dense(units=units,activation='relu',name='hidden4'))
model.add(Dense(units=units,activation='relu',name='hidden5'))
model.add(Dense(units=output_units,activation='relu',name='Output'))
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(x=x_train,y=y_train,validation_data=(x_test, y_test),batch_size=256,epochs=max_epochs,verbose=1,callbacks=[earlystopping])
model.save('2018_200k_mmscaled/')
score = model.evaluate(x_test, y_test, verbose=1)
accuracy=score[1]
f=open("2018_200k_mmscaled.txt","w+")
f.write("Accuracy == "+str(accuracy)+"\n")
f.close()