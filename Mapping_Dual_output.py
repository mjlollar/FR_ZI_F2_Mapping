import sys
import numpy as np
import scipy.stats as sp

file_name = sys.argv[1]
number_sterile = int(sys.argv[2])
number_total = int(sys.argv[3])

individuals = np.loadtxt(file_name, dtype=int, delimiter='\t')
individuals = individuals.T

fisher_1 = []
fisher_2 = []
fisher_3 = []
fisher_4 = []

j=0
for value in range(0,individuals.shape[1]):
	print(j)
	j+=1
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
	print(i)
	i += 1

window_by_window = open('output_sterile_LW_03082020.csv', 'w')

header = list(range(1,6444))
header = map(str, header)
window_by_window.write(",".join(header)+'\n')

window_row = []
cutoff = 6443
for x in range(0, len(p_values)):
	window_row.append(str(p_values[x]))
	if len(window_row) == cutoff:
		window_by_window.write(','.join(window_row) + '\n')
		window_row = []
	else:
		pass

window_by_window.close()


listed_windows = open('output_LW_03082020.csv', 'w')

listed_windows.write("window1"+","+"window2"+","+"p-value"+ '\n')

wi1 = 1
wi2 = 1
window_row2 = 0
for x in p_values:
	window_row2 +=1
	if window_row2 == cutoff:
		listed_windows.write(str(wi1) + "," + str(wi2) + "," + str(x) + '\n')
		wi2 = 1
		wi1 +=1
		window_row2 = 0
	else:
		listed_windows.write(str(wi1) + "," + str(wi2) + "," + str(x) + '\n')
		wi2 += 1

listed_windows.close()

