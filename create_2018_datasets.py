import numpy as np 
import pandas as pd 
from sklearn import preprocessing
import sklearn
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

df1 = pd.read_csv('Tuesday-20-02-2018_TrafficForML_CICFlowMeter_final.csv')
df2 = pd.read_csv('Wednesday-14-02-2018_TrafficForML_CICFlowMeter_final.csv')
df3 = pd.read_csv('Wednesday-21-02-2018_TrafficForML_CICFlowMeter_final.csv')
df4 = pd.read_csv('Wednesday-28-02-2018_TrafficForML_CICFlowMeter_final.csv')
df5 = pd.read_csv('Thursday-15-02-2018_TrafficForML_CICFlowMeter_final.csv')
df6 = pd.read_csv('Thursday-22-02-2018_TrafficForML_CICFlowMeter_final.csv')
df7 = pd.read_csv('Thursday-01-03-2018_TrafficForML_CICFlowMeter_final.csv')
df8 = pd.read_csv('Friday-16-02-2018_TrafficForML_CICFlowMeter_final.csv')
df9 = pd.read_csv('Friday-23-02-2018_TrafficForML_CICFlowMeter_final.csv')
df10 = pd.read_csv('Friday-02-03-2018_TrafficForML_CICFlowMeter_final.csv')
df = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10])


df.drop(columns=['Bwd PSH Flags','Bwd URG Flags','Fwd Byts/b Avg','Fwd Pkts/b Avg','Fwd Blk Rate Avg',
	'Bwd Byts/b Avg','Bwd Pkts/b Avg','Bwd Blk Rate Avg','Flow ID', 'Src IP', 
	'Src Port','Dst IP','Dst Port','Protocol','Timestamp' ], inplace=True)



print(df.head())
# new_cols = ['Flow Duration','Tot Fwd Pkts','Tot Bwd Pkts','TotLen Fwd Pkts','TotLen Bwd Pkts','Fwd Pkt Len Max','Fwd Pkt Len Min',
# 'Fwd Pkt Len Mean','Fwd Pkt Len Std','Bwd Pkt Len Max','Bwd Pkt Len Min','Bwd Pkt Len Mean','Bwd Pkt Len Std','Flow Byts/s',
# 'Flow Pkts/s','Flow IAT Mean','Flow IAT Std','Flow IAT Max','Flow IAT Min','Fwd IAT Tot','Fwd IAT Mean','Fwd IAT Std','Fwd IAT Max',
# 'Fwd IAT Min','Bwd IAT Tot','Bwd IAT Mean','Bwd IAT Std','Bwd IAT Max','Bwd IAT Min','Fwd PSH Flags','Fwd URG Flags','Bwd Header Len',
# 'Fwd Pkts/s','Bwd Pkts/s','Pkt Len Min','Pkt Len Max','Pkt Len Mean','Pkt Len Std','Pkt Len Var','FIN Flag Cnt','SYN Flag Cnt',
# 'RST Flag Cnt','PSH Flag Cnt','ACK Flag Cnt','URG Flag Cnt','CWE Flag Count','ECE Flag Cnt','Down/Up Ratio','Pkt Size Avg',
# 'Fwd Seg Size Avg','Bwd Seg Size Avg','Fwd Header Len','Subflow Fwd Pkts','Subflow Fwd Byts','Subflow Bwd Pkts','Subflow Bwd Byts'
# ,'Init Fwd Win Byts','Init Bwd Win Byts','Fwd Act Data Pkts','Fwd Seg Size Min','Active Mean','Active Std','Active Max','Active Min',
# 'Idle Mean','Idle Std','Idle Max','Idle Min','Label']
# df = df[new_cols]
df.drop(df[df['Flow Duration'] <= 0].index, inplace=True)
print(df.head())
print(df.shape)
print(df.info(verbose=True))

df.to_csv('2018-Week-WorkingHours.csv', index=False)


# create a dataframe from the original concatenated dataset
# df = pd.read_csv('2018-Week-WorkingHours.csv')

# create a new np array of only benign labeled rows
two = np.array(df[df['Label'] == 'Benign'])
# create a new np array of only malicious labeled rows
three  = np.array(df[df['Label'] != 'Benign'])
print(df.head())

# create dataframes of these two to be concatenated together for final testing csv
# the purpose of this is just to have consistency with the feature labels
df2 = pd.DataFrame(two, columns=['Flow Duration','Total Fwd Packets','Total Backward Packets','Total Length of Fwd Packets','Total Length of Bwd Packets','Fwd Packet Length Max','Fwd Packet Length Min','Fwd Packet Length Mean','Fwd Packet Length Std','Bwd Packet Length Max','Bwd Packet Length Min','Bwd Packet Length Mean','Bwd Packet Length Std','Flow Bytes/s','Flow Packets/s','Flow IAT Mean','Flow IAT Std','Flow IAT Max','Flow IAT Min','Fwd IAT Total','Fwd IAT Mean','Fwd IAT Std','Fwd IAT Max','Fwd IAT Min','Bwd IAT Total','Bwd IAT Mean','Bwd IAT Std','Bwd IAT Max','Bwd IAT Min','Fwd PSH Flags','Fwd URG Flags','Fwd Header Length','Bwd Header Length','Fwd Packets/s','Bwd Packets/s','Min Packet Length','Max Packet Length','Packet Length Mean','Packet Length Std','Packet Length Variance','FIN Flag Count','SYN Flag Count','RST Flag Count','PSH Flag Count','ACK Flag Count','URG Flag Count','CWE Flag Count','ECE Flag Count','Down/Up Ratio','Average Packet Size','Avg Fwd Segment Size','Avg Bwd Segment Size','Subflow Fwd Packets','Subflow Fwd Bytes','Subflow Bwd Packets','Subflow Bwd Bytes','Init_Win_bytes_forward','Init_Win_bytes_backward','act_data_pkt_fwd','min_seg_size_forward','Active Mean','Active Std','Active Max','Active Min','Idle Mean','Idle Std','Idle Max','Idle Min','Label'])
df3 = pd.DataFrame(three, columns=['Flow Duration','Total Fwd Packets','Total Backward Packets','Total Length of Fwd Packets','Total Length of Bwd Packets','Fwd Packet Length Max','Fwd Packet Length Min','Fwd Packet Length Mean','Fwd Packet Length Std','Bwd Packet Length Max','Bwd Packet Length Min','Bwd Packet Length Mean','Bwd Packet Length Std','Flow Bytes/s','Flow Packets/s','Flow IAT Mean','Flow IAT Std','Flow IAT Max','Flow IAT Min','Fwd IAT Total','Fwd IAT Mean','Fwd IAT Std','Fwd IAT Max','Fwd IAT Min','Bwd IAT Total','Bwd IAT Mean','Bwd IAT Std','Bwd IAT Max','Bwd IAT Min','Fwd PSH Flags','Fwd URG Flags','Fwd Header Length','Bwd Header Length','Fwd Packets/s','Bwd Packets/s','Min Packet Length','Max Packet Length','Packet Length Mean','Packet Length Std','Packet Length Variance','FIN Flag Count','SYN Flag Count','RST Flag Count','PSH Flag Count','ACK Flag Count','URG Flag Count','CWE Flag Count','ECE Flag Count','Down/Up Ratio','Average Packet Size','Avg Fwd Segment Size','Avg Bwd Segment Size','Subflow Fwd Packets','Subflow Fwd Bytes','Subflow Bwd Packets','Subflow Bwd Bytes','Init_Win_bytes_forward','Init_Win_bytes_backward','act_data_pkt_fwd','min_seg_size_forward','Active Mean','Active Std','Active Max','Active Min','Idle Mean','Idle Std','Idle Max','Idle Min','Label'])
df4 = pd.concat([df2,df3])
df4.to_csv('2018-full-dataset.pcap_ISCX.csv', index=False)

# create the relabelled full dataset csv for binary classification (0, 1)
file_handler = open("2018-full-dataset.pcap_ISCX.csv", "r")
df5 = pd.read_csv(file_handler, sep = ",")
file_handler.close()
df5.Label[df5.Label != 'Benign'] = 1
df5.Label[df5.Label == 'Benign'] = 0
# check to ensure this is what we want
print(df5.head())
print(df5.tail())
print(df5.shape)
print(df5.describe())
print(df5.info(verbose=True))
# finally create the csv
df5.to_csv('2018-full-dataset-relabel-No-DP.pcap_ISCX.csv', index=False)

# create the no dest port relabeled csv (dropping destination port to have all numerical data)
# df5.drop(columns=['Destination Port'], inplace=True)
# df5.to_csv('2018-full-dataset-relabel-No-DP.pcap_ISCX.csv', index=False)

# create the minmax and PCA relabeled csvs
df6 = pd.read_csv('2018-full-dataset-relabel-No-DP.pcap_ISCX.csv')
print(df6.head())
print(df6.shape)
print(df6.describe())

# create 2 numpy arrays X = numerical data, y = labels
X = np.array(df6.drop(['Label'], 1))
y = np.array(df6['Label'])
# fit and transform the numerical data to the minmax scaler
scaler = MinMaxScaler()
Xm = scaler.fit_transform(X)

# create the minmax scaled relabeled csv
mmdataset1 = pd.DataFrame(Xm, columns=['Flow Duration','Total Fwd Packets','Total Backward Packets','Total Length of Fwd Packets','Total Length of Bwd Packets','Fwd Packet Length Max','Fwd Packet Length Min','Fwd Packet Length Mean','Fwd Packet Length Std','Bwd Packet Length Max','Bwd Packet Length Min','Bwd Packet Length Mean','Bwd Packet Length Std','Flow Bytes/s','Flow Packets/s','Flow IAT Mean','Flow IAT Std','Flow IAT Max','Flow IAT Min','Fwd IAT Total','Fwd IAT Mean','Fwd IAT Std','Fwd IAT Max','Fwd IAT Min','Bwd IAT Total','Bwd IAT Mean','Bwd IAT Std','Bwd IAT Max','Bwd IAT Min','Fwd PSH Flags','Fwd URG Flags','Fwd Header Length','Bwd Header Length','Fwd Packets/s','Bwd Packets/s','Min Packet Length','Max Packet Length','Packet Length Mean','Packet Length Std','Packet Length Variance','FIN Flag Count','SYN Flag Count','RST Flag Count','PSH Flag Count','ACK Flag Count','URG Flag Count','CWE Flag Count','ECE Flag Count','Down/Up Ratio','Average Packet Size','Avg Fwd Segment Size','Avg Bwd Segment Size','Subflow Fwd Packets','Subflow Fwd Bytes','Subflow Bwd Packets','Subflow Bwd Bytes','Init_Win_bytes_forward','Init_Win_bytes_backward','act_data_pkt_fwd','min_seg_size_forward','Active Mean','Active Std','Active Max','Active Min','Idle Mean','Idle Std','Idle Max','Idle Min'])
mmdataset2 = pd.DataFrame(y, columns = ['Label'])
labels = mmdataset2["Label"]
mmdataset1 = mmdataset1.join(labels)
mmdataset1.to_csv('2018-full-dataset-relabel-No-DP-mmscaled.pcap_ISCX.csv', index=False)

# principal components need to be 10
scaler2 = StandardScaler()
Xs = scaler2.fit_transform(X)
# principal components need to be 10
pcas = PCA(n_components=10)
# fit and transform X to pca
Xp = pcas.fit_transform(Xs)
# show the explained variance and singular values 
# (96% of variance explained by these 10)
print(pcas.explained_variance_ratio_)
print(pcas.singular_values_)
# create separate datasets to ensure header names are not lost
df8 = pd.DataFrame(Xp, columns=['0','1','2','3','4','5','6','7','8','9'])
df9 = pd.DataFrame(y, columns=['Label'])
# then add Labels (BENIGN, etc) back to PCA dataset
labels = df9["Label"]
df8 = df8.join(labels)
print((df8.head()))
# create the csv file
df8.to_csv('2018-full-dataset-relabel-No-DP-std-PCA10.pcap_ISCX.csv', index=False)
df10 = pd.read_csv('2018-full-dataset-relabel-No-DP-std-PCA10.pcap_ISCX.csv')
print(df10.head())
print(df10.shape)
print(df10.describe())

pcam = PCA(n_components=10)
Xmp = pcam.fit_transform(Xm)
# show the explained variance and singular values 
# (96% of variance explained by these 10)
print(pcam.explained_variance_ratio_)
print(pcam.singular_values_)
# create separate datasets to ensure header names are not lost
df11 = pd.DataFrame(Xmp, columns=['0','1','2','3','4','5','6','7','8','9'])
df12 = pd.DataFrame(y, columns=['Label'])
# then add Labels (BENIGN, etc) back to PCA dataset
labels = df12["Label"]
df11 = df11.join(labels)
print((df11.head()))
# create the csv file
df11.to_csv('2018-full-dataset-relabel-No-DP-mm-PCA10.pcap_ISCX.csv', index=False)
df13 = pd.read_csv('2018-full-dataset-relabel-No-DP-mm-PCA10.pcap_ISCX.csv')
print(df13.head())
print(df13.shape)
print(df13.describe())