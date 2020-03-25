### Test for Y-Mito incompatibilities against a "0" value ancestry
### Input format: python Y_Mito_0focal.py <input.csv> <number_sterile_focal> <number_sterile_nonfocal> <number_fertile_focal> <number_fertile_non-focal> <output.csv>
### Requires ordered columns in input file where individuals from left to right are: sterile_focal, sterile_NF, fertile_focal, fertile_NF

import sys
import numpy as np
import scipy.stats as sp

file_name = sys.argv[1]
sterile_focal = int(sys.argv[2])
sterile_non_focal = sterile_focal + int(sys.argv[3])
fertile_focal = sterile_non_focal + int(sys.argv[4])
fertile_nonfocal = fertile_focal + int(sys.argv[5])
output = sys.argv[6]

individuals = np.loadtxt(file_name, dtype=int, delimiter=',')
individuals = individuals.T

fisher_1_temp1 = []
fisher_2_temp1 = []
fisher_1_temp2 = []
fisher_2_temp2 = []

fisher_3_temp1 = []
fisher_4_temp1 = []
fisher_3_temp2 = []
fisher_4_temp2 = []

for value in range(0, individuals.shape[1]):
	fisher1 = 0
	fisher2 = 0
	fisher3 = 0
	fisher4 = 0

	## Sterile groups with focal Y chromosome
	for window in individuals[0:sterile_focal]:
		if window[value] == 2:
			fisher1 += 1
			fisher2 += 0
		elif window[value] == 0:
			fisher2 += 1
			fisher1 += 0
		elif window[value] == 1:
			fisher2 += 1
			fisher1 += 0
		elif window[value] == -999:
			fisher1 += 0
			fisher2 += 0
		else:
			pass
	fisher_1_temp1.append(fisher1)
	fisher_2_temp1.append(fisher2)
	fisher1 = 0
	fisher2 = 0 
		
	## Sterile groups with non-focal Y chromosome (all in 2 if not no call)		
	for window in individuals[sterile_focal:sterile_non_focal]:
		if window[value] == -999:
			fisher1 += 0
			fisher2 += 0
		elif window[value] != -999:
			fisher2 += 1
			fisher1 += 0
		else:
			pass
	fisher_1_temp2.append(fisher1)
	fisher_2_temp2.append(fisher2)
	fisher1 = 0
	fisher2 = 0

	## Fertile group with focal Y chromosome
	for window in individuals[sterile_non_focal:fertile_focal]:
		if window[value] == 2:
			fisher3 += 1
			fisher4 += 0
		elif window[value] == 0:
			fisher4 += 1
			fisher3 += 0
		elif window[value] == 1:
			fisher4 += 1
			fisher3 += 0
		elif window[value] == -999:
			fisher3 += 0
			fisher4 += 0
		else:
			pass
	fisher_3_temp1.append(fisher3)
	fisher_4_temp1.append(fisher4)
	fisher3 = 0
	fisher4 = 0
	
	## Fertile group with non-focal Y Chromosome (all in 4 if not no call)
	for window in individuals[fertile_focal:fertile_nonfocal]:
		if window[value] == -999:
			fisher3 += 0
			fisher4 += 0
		elif window[value] != -999:
			fisher3 += 0
			fisher4 += 1
		else:
			pass
	fisher_3_temp2.append(fisher3)
	fisher_4_temp2.append(fisher4)
	fisher3 = 0
	fisher4 = 0

fisher_1 = [sum(i) for i in zip(fisher_1_temp1, fisher_1_temp2)]
fisher_2 = [sum(i) for i in zip(fisher_2_temp1, fisher_2_temp2)]
fisher_3 = [sum(i) for i in zip(fisher_3_temp1, fisher_3_temp2)]
fisher_4 = [sum(i) for i in zip(fisher_4_temp1, fisher_4_temp2)]
assert len(fisher_1) == len(fisher_2) == len(fisher_3) == len(fisher_4)

p_values = []

i=0
for group in range(0, len(fisher_1)):
	oddsratio, pvalue = sp.fisher_exact([[fisher_1[i], fisher_2[i]], [fisher_3[i], fisher_4[i]]])
	p_values.append(pvalue)
	i += 1

outfile = open(output, 'w')

outfile.write("window"+','+"p-value"+'\n')

window = 1
for x in p_values:
	outfile.write(str(window)+','+str(x)+'\n')
	window += 1
outfile.close()
