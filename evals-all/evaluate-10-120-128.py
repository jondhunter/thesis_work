
import pandas as pd
import numpy as np 
import time
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Model, load_model
import csv
from csv import reader, writer
from itertools import islice
import sys


i=120
b=128

def time_model_evaluates_to_csv(interval, batch_size, model, csvin, csvout):

	n = 799999
	model = keras.models.load_model(model)
	df1 = pd.read_csv(csvin)

	

	timer = 0
	counter = 0
	interval = interval
	counter2 = counter + interval
	row_count = 0
	batch_size = batch_size
	he = df1.at[799999,'Time']

	while row_count < n:

		l = df1[df1['Time']>=counter].index[0]

		if he <= counter2:
			h = n		
		else:
			h = df1[df1['Time']>=counter2].index[0]
		
		df2 = pd.DataFrame(df1[l:h])
		# print(l)
		# print(h)
		df2.columns = ['0','1','2','3','4','5','6','7','8','9','Label','Time']

		row_number = df2.shape[0]


		df2.drop(columns=['Time'], inplace=True)
		y = np.array(df2['Label'])
		x = np.array(df2.drop(['Label'], 1))


		start = time.perf_counter()
		evaluate = model.evaluate(x,y,batch_size=batch_size)
		end = time.perf_counter()
		timer = (end - start)
		evaluate_accuracy = evaluate[1]

		with open(csvout,"a+") as out:
				line = "{},{},{},{},{}\n".format(interval,batch_size,row_number,timer,evaluate_accuracy)
				out.write(line)

		counter += interval
		counter2 = counter + interval
		row_count += row_number
		# print(counter, counter2, row_number, row_count, timer)		
		
with open("evaluate_times-pi-10-{}-{}.csv".format(i,b), "w") as my_empty_csv:
	time_model_evaluates_to_csv(i,b,'2018_200k_mm_PCA_dynamic/','2018-testing-mm-PCA10-random-timestamp.csv',"evaluate_times-pi-10-{}-{}.csv".format(i,b))
