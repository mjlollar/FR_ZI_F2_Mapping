#Generates 1000 randomized files of real data, such that sterile/fertile assignment is random
#Maintains recombination profile of individuals, used for permutations to generate null p-value
#Requires input csv file of real-data individuals with header row from 1-#total


import random as rd
import sys
import csv

for x in range(0,1000):
	filename = "perm_out_%d.csv" % x
	with open(sys.argv[1], 'r') as infile, open(filename, 'w') as outfile:
		rand_ind = rd.sample(range(1,185), 184)
		int_str = ' '.join(map(str, rand_ind))
		fieldnames = int_str.split()
		writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter=',')
		writer.writeheader()
		for row in csv.DictReader(infile):
			writer.writerow(row)

for x in range (1,1000):
	filename = "perm_out_%d.csv" % x 
	filename2 = "perms_out_%d.csv" % x
	with open(filename, 'r') as file:
		with open(filename2, 'w') as new_file:
			next(file)
			for line in file:
				new_file.write(line)
