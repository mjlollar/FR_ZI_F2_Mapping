#Script to filter out window comparisons that have lower p-values than null p-value

import sys
import csv

in_name = sys.argv[1] #Input file containing three columns [window1, window2, p-value]
out_name = sys.argv[2] #File name for output 

with open(in_name, 'r') as infile, open(out_name, 'w') as outfile:
	reader = csv.DictReader(infile)
	fieldnames = ['window1', 'window2', 'p-value']
	writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter=',')
	writer.writeheader()
	for row in reader:
		if row['p-value'] <= '0.0003797': # ADAPT to null p-value of choice
			writer.writerow(row)
		else:
			pass
infile.close()
outfile.close()
