import sys
import numpy as np
import scipy.stats as sp

file_name = sys.argv[1]
number_sterile = int(sys.argv[2])
number_fertile = int(sys.argv[3])

individuals = np.loadtxt(file_name, dtype=int)
individuals = individuals.T

fisher_1 = []
fisher_2 = []
fisher_3 = []
fisher_4 = []

for value in range(0,individuals.shape[1]):
	for value2 in range(0, individuals.shape[1]):
		fisher1=0
		fisher2=0
		for window in individuals[0:number_sterile,:]:
			if window[value] == 0:
				if window[value2] == 2:
					fisher1 += 1
				elif window[value2] != 2:
					fisher2 += 1
				else:
					pass
			elif window[value] != 0:
				fisher2 += 1
			else:
				pass
		fisher_1.append(fisher1)
		fisher_2.append(fisher2)
		fisher1=0
		fisher2=0
	for value2 in range(0, individuals.shape[1]):
		fisher3=0
		fisher4=0
		for window in individuals[number_sterile:number_fertile,:]:
			if window[value] == 0:
				if window[value2] == 2:
					fisher3+= 1
				elif window[value2] != 2:
					fisher4 += 1
			elif window[value] != 0:
				fisher4 += 1
			else:
				pass
		fisher_3.append(fisher1)
		fisher_4.append(fisher2)
		fisher3=0
		fisher4=0

assert len(fisher_1) == len(fisher_2) == len(fisher_3) == len(fisher_4)

p_values = []

i=0
for group in range(0, len(fisher_1)):
	oddsratio, pvalue = sp.fisher_exact([[fisher_1[i], fisher_2[i]], [fisher_3[i], fisher_4[i]]])
	p_values.append(pvalue)
	i += 1
