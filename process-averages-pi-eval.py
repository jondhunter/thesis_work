
import csv
from csv import reader, writer


outfile = open("eval-averages-pi.csv","a+")

for i in 5, 10, 15, 30, 60, 120, 180, 240, 300, 600:
	for b in 16, 32, 64, 128, 256:
		nsum = 0
		tsum = 0
		asum = 0
		row_n = 0
		d = 69
		with open("evaluate-times-pi-69-{}-{}.csv".format(i,b), "r") as csvin:
			reader = csv.reader(csvin, delimiter = ",")
		
			for row in reader:
				n = float(row[2])
				nsum = nsum + n
				t = float(row[3])
				tsum = tsum + t
				a = float(row[4])
				asum = asum + a
				row_n = row_n + 1

			nfin = nsum / row_n
			afin = asum / row_n
			tfin = tsum / row_n
			line = "{},{},{},{},{},{}\n".format(d,i,b,nfin,tfin,afin)
			outfile.write(line)

for i in 5, 10, 15, 30, 60, 120, 180, 240, 300, 600:
	for b in 16, 32, 64, 128, 256:
		nsum = 0
		tsum = 0
		asum = 0
		row_n = 0
		d = 10
		with open("evaluate_times-pi-10-{}-{}.csv".format(i,b), "r") as csvin:
			reader = csv.reader(csvin, delimiter = ",")
		
			for row in reader:
				n = float(row[2])
				nsum = nsum + n
				t = float(row[3])
				tsum = tsum + t
				a = float(row[4])
				asum = asum + a
				row_n = row_n + 1

			nfin = nsum / row_n
			afin = asum / row_n
			tfin = tsum / row_n
			line = "{},{},{},{},{},{}\n".format(d,i,b,nfin,tfin,afin)
			outfile.write(line)


outfile = open("eval-averages-pi-stress.csv","a+")

for i in 5, 10, 15, 30, 60, 120, 180, 240, 300, 600:
	for b in 16, 32, 64, 128, 256:
		nsum = 0
		tsum = 0
		asum = 0
		row_n = 0
		d = 69
		with open("evaluate-times-pi-69-{}-{}-stress.csv".format(i,b), "r") as csvin:
			reader = csv.reader(csvin, delimiter = ",")
		
			for row in reader:
				n = float(row[2])
				nsum = nsum + n
				t = float(row[3])
				tsum = tsum + t
				a = float(row[4])
				asum = asum + a
				row_n = row_n + 1

			nfin = nsum / row_n
			afin = asum / row_n
			tfin = tsum / row_n
			line = "{},{},{},{},{},{}\n".format(d,i,b,nfin,tfin,afin)
			outfile.write(line)

for i in 5, 10, 15, 30, 60, 120, 180, 240, 300, 600:
	for b in 16, 32, 64, 128, 256:
		nsum = 0
		tsum = 0
		asum = 0
		row_n = 0
		d = 10
		with open("evaluate_times-pi-10-{}-{}-stress.csv".format(i,b), "r") as csvin:
			reader = csv.reader(csvin, delimiter = ",")
		
			for row in reader:
				n = float(row[2])
				nsum = nsum + n
				t = float(row[3])
				tsum = tsum + t
				a = float(row[4])
				asum = asum + a
				row_n = row_n + 1

			nfin = nsum / row_n
			afin = asum / row_n
			tfin = tsum / row_n
			line = "{},{},{},{},{},{}\n".format(d,i,b,nfin,tfin,afin)
			outfile.write(line)