## Alternative script to use when only between chromosome windows are considered.

## Need to update output to call appropriate windows on dual output

## For now will just be used to find lowest null p-value in permuations

## Current window cutoffs based on 50kb window markers

import sys
import numpy as np
import scipy.stats as sp

file_name = sys.argv[1]
number_sterile = int(sys.argv[2])
number_total = int(sys.argv[3])
output = sys.argv[4]

fisher_1 = []
fisher_2 = []
fisher_3 = []
fisher_4 = []

individuals = np.loadtxt(file_name, dtype=int, delimiter=',')
individuals = individuals.T


## X to Chr2, Chr3
for value in range(0,545):			#First range changes as a function of windows on the X
	for value2 in range(545,2579):		#Second range changes as a function of windows on Chr2 & Chr3
		fisher1 = 0
		fisher2 = 0
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
	for value2 in range(545,2579):	#Range changes a function of windows on Chr2 & Chr3
		fisher3=0
		fisher4=0
		for window in individuals[number_sterile:number_total,:]:
			if window[value] == 0:
				if window[value2] == 2:
					fisher3 += 1
				elif window[value2] != 2:
					fisher4 += 1
			elif window[value] != 0:
				fisher4 += 1
			else:
				pass
		fisher_3.append(fisher3)
		fisher_4.append(fisher4)
		fisher3=0
		fisher4=0

## Chr2 to X
for value in range(545,1524):			#First range changes as a function of windows on Chr2
	for value2 in range(0,545):		#Second range changes as a function of windows on X
		fisher1 = 0
		fisher2 = 0
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
	for value2 in range(0,545):	#Range changes a function of windows on X
		fisher3=0
		fisher4=0
		for window in individuals[number_sterile:number_total,:]:
			if window[value] == 0:
				if window[value2] == 2:
					fisher3 += 1
				elif window[value2] != 2:
					fisher4 += 1
			elif window[value] != 0:
				fisher4 += 1
			else:
				pass
		fisher_3.append(fisher3)
		fisher_4.append(fisher4)
		fisher3=0
		fisher4=0


## Chr2 to Chr3
for value in range(545,1524):			#First range changes as a function of windows on Chr2
	for value2 in range(1524,2579):		#Second range changes as a function of windows on Chr3
		fisher1 = 0
		fisher2 = 0
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
	for value2 in range(1524,2579):	#Range changes a function of windows on Chr3
		fisher3=0
		fisher4=0
		for window in individuals[number_sterile:number_total,:]:
			if window[value] == 0:
				if window[value2] == 2:
					fisher3 += 1
				elif window[value2] != 2:
					fisher4 += 1
			elif window[value] != 0:
				fisher4 += 1
			else:
				pass
		fisher_3.append(fisher3)
		fisher_4.append(fisher4)
		fisher3=0
		fisher4=0

## Chr3 to X
for value in range(1524,2579):			#First range changes as a function of windows on Chr3
	for value2 in range(0,545):		#Second range changes as a function of windows on X
		fisher1 = 0
		fisher2 = 0
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
	for value2 in range(0,545):	#Range changes a function of windows on X
		fisher3=0
		fisher4=0
		for window in individuals[number_sterile:number_total,:]:
			if window[value] == 0:
				if window[value2] == 2:
					fisher3 += 1
				elif window[value2] != 2:
					fisher4 += 1
			elif window[value] != 0:
				fisher4 += 1
			else:
				pass
		fisher_3.append(fisher3)
		fisher_4.append(fisher4)
		fisher3=0
		fisher4=0

## Chr3 to Chr2
for value in range(1524,2579):			#First range changes as a function of windows on Chr3
	for value2 in range(545,1524):		#Second range changes as a function of windows on Chr2
		fisher1 = 0
		fisher2 = 0
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
	for value2 in range(545,1524):	#Range changes a function of windows on Chr2
		fisher3=0
		fisher4=0
		for window in individuals[number_sterile:number_total,:]:
			if window[value] == 0:
				if window[value2] == 2:
					fisher3 += 1
				elif window[value2] != 2:
					fisher4 += 1
			elif window[value] != 0:
				fisher4 += 1
			else:
				pass
		fisher_3.append(fisher3)
		fisher_4.append(fisher4)
		fisher3=0
		fisher4=0

p_values = []

i=0
counter = 0
for group in range(0, len(fisher_1)):
	oddsratio, pvalue = sp.fisher_exact([[fisher_1[i], fisher_2[i]], [fisher_3[i], fisher_4[i]]])
	p_values.append(pvalue)
	i += 1

min_pvalue = min(p_values)

window_by_window = open(output, 'w')

window_by_window.write(str(min_pvalue))
