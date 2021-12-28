#!/bin/bash
# this script is meant to automate the process of running python evaluate and fit on pi
# need to run dstats simultaneously, output results of dstats to a csv file, parse that data so that it can be
# used for graphing

# begin with evaluate 16-256

for j in 5 10 15 30 60 120 180 240 300 600
do
	for i in 16 32 64 128 256
	do
		dstat -c -m -C all --noheaders --nocolor --output eval-69-01-$j-$i.csv > /dev/null &
		python3 evaluate-69-$j-$i.py
		pkill -f 'python2 /usr/bin/dstat'
		dstat -c -m -C all --noheaders --nocolor --output fit-69-01-$j-$i.csv > /dev/null &
		python3 fit-69-$j-$i.py
		pkill -f 'python2 /usr/bin/dstat'
		dstat -c -m -C all --noheaders --nocolor --output eval-10-01-$j-$i.csv > /dev/null &
		python3 evaluate-10-$j-$i.py
		pkill -f 'python2 /usr/bin/dstat'
		dstat -c -m -C all --noheaders --nocolor --output fit-10-01-$j-$i.csv > /dev/null &
		python3 fit-10-$j-$i.py
		pkill -f 'python2 /usr/bin/dstat'
	done

stress-ng --cpu 4 --all 4 &

	for i in 16 32 64 128 256
	do
		dstat -c -m -C all --noheaders --nocolor --output eval-69-02-$j-$i.csv > /dev/null &
		python3 evaluate-69-$j-$i-stress.py
		pkill -f 'python2 /usr/bin/dstat'
		dstat -c -m -C all --noheaders --nocolor --output fit-69-02-$j-$i.csv > /dev/null &
		python3 fit-69-$j-$i-stress.py
		pkill -f 'python2 /usr/bin/dstat'
		dstat -c -m -C all --noheaders --nocolor --output eval-10-02-$j-$i.csv > /dev/null &
		python3 evaluate-10-$j-$i-stress.py
		pkill -f 'python2 /usr/bin/dstat'
		dstat -c -m -C all --noheaders --nocolor --output fit-10-02-$j-$i.csv > /dev/null &
		python3 fit-10-$j-$i-stress.py
		pkill -f 'python2 /usr/bin/dstat'
	done
processId=$(ps -ef | grep 'stress-ng --cpu 4 --all 4' | grep -v 'grep' | awk '{ printf $2 }')
kill $processId
pkill -f 'stress-ng'

done


# now need to process each tegrastat csv file iteratively then concatenate them together (can do all in a
# single python script using pandas/csv)

# have to edit all csv files first -- noheader does not work as expected
python3 parseall-10.py
python3 parseall-69.py
