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


i=300
b=32

def time_model_fits_to_csv(interval, batch_size, model, csvin, csvout):

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
		
		df2.columns = ['Destination Port','Flow Duration','Total Fwd Packets','Total Backward Packets','Total Length of Fwd Packets',
		'Total Length of Bwd Packets','Fwd Packet Length Max','Fwd Packet Length Min','Fwd Packet Length Mean','Fwd Packet Length Std',
		'Bwd Packet Length Max','Bwd Packet Length Min','Bwd Packet Length Mean','Bwd Packet Length Std','Flow Bytes/s','Flow Packets/s',
		'Flow IAT Mean','Flow IAT Std','Flow IAT Max','Flow IAT Min','Fwd IAT Total','Fwd IAT Mean','Fwd IAT Std','Fwd IAT Max',
		'Fwd IAT Min','Bwd IAT Total','Bwd IAT Mean','Bwd IAT Std','Bwd IAT Max','Bwd IAT Min','Fwd PSH Flags','Fwd URG Flags',
		'Fwd Header Length','Bwd Header Length','Fwd Packets/s','Bwd Packets/s','Min Packet Length','Max Packet Length','Packet Length Mean',
		'Packet Length Std','Packet Length Variance','FIN Flag Count','SYN Flag Count','RST Flag Count','PSH Flag Count','ACK Flag Count',
		'URG Flag Count','CWE Flag Count','ECE Flag Count','Down/Up Ratio','Average Packet Size','Avg Fwd Segment Size','Avg Bwd Segment Size',
		'Subflow Fwd Packets','Subflow Fwd Bytes','Subflow Bwd Packets','Subflow Bwd Bytes','Init_Win_bytes_forward','Init_Win_bytes_backward',
		'act_data_pkt_fwd','min_seg_size_forward','Active Mean','Active Std','Active Max','Active Min','Idle Mean','Idle Std','Idle Max',
		'Idle Min','Label','Time']

		row_number = df2.shape[0]


		df2.drop(columns=['Time'], inplace=True)
		y = np.array(df2['Label'])
		x = np.array(df2.drop(['Label'], 1))


		start = time.perf_counter()
		fit = model.fit(x,y,batch_size=batch_size)
		end = time.perf_counter()
		timer = (end - start)
		fit_accuracy = fit.history.get('accuracy')[-1]

		with open(csvout,"a+") as out:
				line = "{},{},{},{},{}\n".format(interval,batch_size,row_number,timer,fit_accuracy)
				out.write(line)

		counter += interval
		counter2 = counter + interval
		row_count += row_number
			
		


with open("fit-times-pi-69-{}-{}.csv".format(i,b), "w") as my_empty_csv:
	time_model_fits_to_csv(i,b,'2018_200k_mmscaled_dynamic/','2018-testing-mmscaled-random-timestamp.csv',"fit-times-pi-69-{}-{}.csv".format(i,b))
