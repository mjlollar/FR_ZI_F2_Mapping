### Alternative viability script as sanity check to get same values as viability_bet_chr.py
### Generates same values, and runs a bit faster than original script.

import sys
import numpy as np
import random as rd
import scipy.stats as sp

file_name = sys.argv[1]
X_len = int(sys.argv[2])
Chr2_len = int(sys.argv[3])
Chr3_len = int(sys.argv[4])

df = np.loadtxt(file_name, dtype=int, delimiter=',')

len_X = list(range(0, X_len))
len_2 = list(range(X_len, Chr2_len))
len_3 = list(range(Chr2_len, Chr3_len))

def chr_compare(ind, len1, len2):
	for window1 in len1:  
		for window2 in len2:
			fisher1 = 0
			fisher2 = 0
			fisher3 = 0
			fisher4 = 0
			for index in ind:
				if df[window1, index] == 0:
					if df[window2, index] == 2:
						fisher1 += 1
					elif df[window2, index] == 0:
						fisher3 += 1
					elif df[window2, index] == 1:
						fisher3 += 1
					elif df[window2, index] == -999:
						pass
					else:
						pass
				elif df[window1, index] == 1:
					if df[window2, index] == 2:
						fisher2 += 1
					elif df[window2, index] == 0:
						fisher4 += 1
					elif df[window2, index] == 1:
						fisher4 += 1
					elif df[window2, index] == -999:
						pass
					else:
						pass
				elif df[window1, index] == 2:
					if df[window2, index] == 2:
						fisher2 += 1
					elif df[window2, index] == 0:
						fisher4 += 1
					elif df[window2, index] == 1:
						fisher4 += 1
					elif df[window2, index] == -999:
						pass
					else:
						pass
				elif df[window1, index] == -999:
					pass
				else:
					pass
			fisher_1.append(fisher1)
			fisher_2.append(fisher2)
			fisher_3.append(fisher3)
			fisher_4.append(fisher4)
			fisher1 = 0
			fisher2 = 0
			fisher3 = 0
			fisher4 = 0

def fisher_exact_test(F1, F2, F3, F4):
	assert len(F1) == len(F2) == len(F3) == len(F4)
	i=0
	for group in range(0, len(F1)):
		oddsratio, pvalue = sp.fisher_exact([[F1[i], F2[i]], [F3[i], F4[i]]])
		p_values.append(pvalue)
		i+=1
			
def printer(pvalues, group1, group2, group2_windows, spacer1, spacer2):
	listed_windows = open('54_403_viability_output_alt.csv', 'a')

	w1 = 1 + int(spacer1)
	w2 = 1 + int(spacer2)
	window_2 = 0
	for x in p_values:
		window_2 += 1
		if window_2 == group2_windows:
			listed_windows.write(group1+"-"+str(w1) + "," + group2+"-"+str(w2) + "," + str(x) + '\n')
			w2 = 1 + int(spacer2)
			w1 += 1
			window_2 = 0
		else:
			listed_windows.write(group1+"-"+str(w1) + "," + group2+"-"+str(w2) + "," + str(x) + '\n')
			w2 += 1

	listed_windows.close()

listed_windows = open('54_403_viability_output_alt.csv', 'w')
listed_windows.write("window1" + "," + "window2" + "," + "p-value" + '\n')
listed_windows.close()

####
####

names = list(range(0, np.shape(df)[1]))
names = list(map(int, names))

####
####

p_values = []
fisher_1 = []
fisher_2 = []
fisher_3 = []
fisher_4 = []

chr_compare(names, len_X, len_2)
fisher_exact_test(fisher_1, fisher_2, fisher_3, fisher_4)
printer(p_values, "X", "Chr2", 979, 0, 545)

print("X 2 finished")

p_values = []
fisher_1 = []
fisher_2 = []
fisher_3 = []
fisher_4 = []

chr_compare(names, len_X, len_3)
fisher_exact_test(fisher_1, fisher_2, fisher_3, fisher_4)
printer(p_values, "X", "Chr3", 1055, 0, 1525)

print("X 3 finished")

p_values = []
fisher_1 = []
fisher_2 = []
fisher_3 = []
fisher_4 = []

chr_compare(names, len_2, len_3)
fisher_exact_test(fisher_1, fisher_2, fisher_3, fisher_4)
printer(p_values, "Chr2", "Chr3", 1055, 545, 1525)

print("2 3 finished")

p_values = []
fisher_1 = []
fisher_2 = []
fisher_3 = []
fisher_4 = []

chr_compare(names, len_2, len_X)
fisher_exact_test(fisher_1, fisher_2, fisher_3, fisher_4)
printer(p_values, "Chr2", "X", 545, 545, 0)

print("2 X finished")

p_values = []
fisher_1 = []
fisher_2 = []
fisher_3 = []
fisher_4 = []

chr_compare(names, len_3, len_X)
fisher_exact_test(fisher_1, fisher_2, fisher_3, fisher_4)
printer(p_values, "Chr3", "X", 545, 1525, 0)

print("3 X finished")

p_values = []
fisher_1 = []
fisher_2 = []
fisher_3 = []
fisher_4 = []

chr_compare(names, len_3, len_2)
fisher_exact_test(fisher_1, fisher_2, fisher_3, fisher_4)
printer(p_values, "Chr3", "Chr2", 979, 1525, 545)
