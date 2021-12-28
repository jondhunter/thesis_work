
import csv
from csv import reader, writer

# handling unstressed first

outfile = open("eval-stats-averages-pi.csv","a+")

for i in 5, 10, 15, 30, 60, 120, 180, 240, 300, 600:
	for b in 16, 32, 64, 128, 256:
		nsum = 0
		tsum = 0
		#asum = 0
		row_n = 0
		d = 69
		s = 1
		with open("eval-69-01-{}-{}-f.csv".format(i,b), "r") as csvin:
			reader = csv.reader(csvin, delimiter = ",")
		
			for row in reader:
				n = float(row[0])
				nsum = nsum + n
				t = float(row[1])
				tsum = tsum + t
				# a = float(row[4])
				# asum = asum + a
				row_n = row_n + 1

			nfin = nsum / row_n
			#afin = asum / row_n
			tfin = tsum / row_n
			line = "{},{},{},{},{},{}\n".format(d,i,b,nfin,tfin,s)
			outfile.write(line)

for i in 5, 10, 15, 30, 60, 120, 180, 240, 300, 600:
	for b in 16, 32, 64, 128, 256:
		nsum = 0
		tsum = 0
		#asum = 0
		row_n = 0
		d = 10
		s = 1
		with open("eval-10-01-{}-{}-f.csv".format(i,b), "r") as csvin:
			reader = csv.reader(csvin, delimiter = ",")
		
			for row in reader:
				n = float(row[0])
				nsum = nsum + n
				t = float(row[1])
				tsum = tsum + t
				# a = float(row[4])
				# asum = asum + a
				row_n = row_n + 1

			nfin = nsum / row_n
			#afin = asum / row_n
			tfin = tsum / row_n
			line = "{},{},{},{},{},{}\n".format(d,i,b,nfin,tfin,s)
			outfile.write(line)

# now handling stressed

outfile2 = open("eval-stats-averages-pi-stress.csv","a+")

for i in 5, 10, 15, 30, 60, 120, 180, 240, 300, 600:
	for b in 16, 32, 64, 128, 256:
		nsum = 0
		tsum = 0
		#asum = 0
		row_n = 0
		d = 69
		s = 2
		with open("eval-69-02-{}-{}-f.csv".format(i,b), "r") as csvin:
			reader = csv.reader(csvin, delimiter = ",")
		
			for row in reader:
				n = float(row[0])
				nsum = nsum + n
				t = float(row[1])
				tsum = tsum + t
				# a = float(row[4])
				# asum = asum + a
				row_n = row_n + 1

			nfin = nsum / row_n
			#afin = asum / row_n
			tfin = tsum / row_n
			line = "{},{},{},{},{},{}\n".format(d,i,b,nfin,tfin,s)
			outfile2.write(line)

for i in 5, 10, 15, 30, 60, 120, 180, 240, 300, 600:
	for b in 16, 32, 64, 128, 256:
		nsum = 0
		tsum = 0
		#asum = 0
		row_n = 0
		d = 10
		s = 2
		with open("eval-10-02-{}-{}-f.csv".format(i,b), "r") as csvin:
			reader = csv.reader(csvin, delimiter = ",")
		
			for row in reader:
				n = float(row[0])
				nsum = nsum + n
				t = float(row[1])
				tsum = tsum + t
				# a = float(row[4])
				# asum = asum + a
				row_n = row_n + 1

			nfin = nsum / row_n
			#afin = asum / row_n
			tfin = tsum / row_n
			line = "{},{},{},{},{},{}\n".format(d,i,b,nfin,tfin,s)
			outfile2.write(line)