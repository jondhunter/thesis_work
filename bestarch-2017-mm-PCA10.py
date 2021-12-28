from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Model, load_model
from tensorflow.keras import callbacks

import pandas as pd 
import numpy as np 
import tensorflow as tf 
import io

# create dataset (including multiple for easier switching btw datasets)
# printing head, shape and types to be sure dataset and variables are correct
# df = pd.read_csv('/home/jhunter/dl-testing/TrainingMLCVE/finalpaperCSVs/2017-training-100k-DP-mm-PCA10.pcap_ISCX.csv')
# df = pd.read_csv('/home/jhunter/dl-testing/TrainingMLCVE/finalpaperCSVs/2017-training-hulk-DP-mm-PCA10.pcap_ISCX.csv')
# df = pd.read_csv('/home/jhunter/dl-testing/TrainingMLCVE/finalpaperCSVs/2017-training-ddos-DP-mm-PCA10.pcap_ISCX.csv')
# df = pd.read_csv('/home/jhunter/dl-testing/TrainingMLCVE/finalpaperCSVs/2017-training-100k-noDP-mm-PCA10.pcap_ISCX.csv')
# df = pd.read_csv('/home/jhunter/dl-testing/TrainingMLCVE/finalpaperCSVs/2017-training-hulk-noDP-mm-PCA10.pcap_ISCX.csv')
# df = pd.read_csv('/home/jhunter/dl-testing/TrainingMLCVE/finalpaperCSVs/2017-training-ddos-noDP-mm-PCA10.pcap_ISCX.csv')
df = pd.read_csv('/home/jhunter/git/Jetson-MachineLearning/data-mod/2018-training-mm-PCA10.csv')

# using np.array drop instead of iloc to make switching between different feature 
# numbers on different datasets easier
x = np.array(df.drop(['Label'], 1))
y = np.array(df['Label'])


# train test split with 80% training 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

# input units for different feature numbers
input_units = x_train.shape[1]

output_units = 1

start_units = 5
max_units = 100

max_epochs = 10
model = Sequential()
score = 0
best_accuracy = 0
best_units = 0
best_layers = 0
counter = 0

# using callbacks.EarlyStopping to achieve the optimal number of epochs within the 50 and prevent overfitting
earlystopping = callbacks.EarlyStopping(monitor="val_loss",mode="min",patience=5,restore_best_weights=True)

def get_model_summary(model):
	stream = io.StringIO()
	model.summary(print_fn=lambda x: stream.write(x + '\n'))
	summary_string = stream.getvalue()
	stream.close()
	return summary_string

for max_layers in range(1, 6):
		for units in range(start_units, max_units+1):
			model = Sequential()		# https://www.tensorflow.org/guide/keras/sequential_model

			# We have to add an input layer..
			model.add(Dense(units=input_units))

			# HIDDEN LAYERS
			# model.add(Dense(units=start_units, activation='relu', name='Layer1'))

			# for loop for testing 1-7 hidden layers with 1-100 unit
			for num_layers in range(1, max_layers+1):
				model.add(Dense(units=units, activation='tanh'))

			model.add(Dense(units=output_units, activation = 'tanh', name='Output'))
			# Compile the model.
			# loss = 'binary_crossentropy' because this is a binary classification problem 
			model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

			# Fit the model.
			model.fit(x=x_train,y=y_train,validation_data=(x_test, y_test),batch_size=256,epochs=max_epochs,verbose=1,callbacks=[earlystopping])
			counter +=1
			print("counter == " +str(counter) + " units == " +str(units) + " layers == " +str(max_layers))
			
			# Get the models scores
			score = model.evaluate(x_test, y_test, verbose=1)
			if score[1]  >= best_accuracy:
				best_accuracy = score[1]
				best_units = units
				best_layers = max_layers
				summary = get_model_summary(model)

# f = open("2017-100k-DP-mm-PCA10-bestarch.txt", "w+")
# f = open("2017-hulk-DP-mm-PCA10-bestarch.txt", "w+")
# f = open("2017-ddos-DP-mm-PCA10-bestarch.txt", "w+")
# f = open("2017-100k-noDP-mm-PCA10-bestarch.txt", "w+")
# f = open("2017-hulk-noDP-mm-PCA10-bestarch.txt", "w+")
# f = open("2017-ddos-noDP-mm-PCA10-bestarch.txt", "w+")
f = open("2018-training-mm-PCA10-bestarch.txt")
f.write("Best Accuracy == " +str(best_accuracy) + "\n")
f.write("Best Units == " +str(best_units) + "\n")
f.write("Best Layers == " +str(best_layers) + "\n")
f.write("counter == " +str(counter) + "\n")
f.write(summary)
f.close()