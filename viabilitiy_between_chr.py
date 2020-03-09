# Lines with "#ADAPT" will need to be adapted for correct window breaks in input file
# Input file should be .csv file with individuals as columns and rows as windows


import sys
import numpy as np
import scipy.stats as sp

file_name = sys.argv[1]
Xbreak = int(sys.argv[2])
Chr2break = int(sys.argv[3])

individuals = np.loadtxt(file_name, dtype=int, delimiter='\t')

individuals = individuals.T

X = individuals[:,0:Xbreak]
Chr2 = individuals[:,Xbreak:Chr2break]
Chr3 = individuals[:,Chr2break:]

fisher_1 = []
fisher_2 = [] 
fisher_3 = []
fisher_4 = []

def chr_compare(array1, array2):
	for column in range(0, array1.shape[1]):
		for column2 in range(0, array2.shape[1]):
			fisher1=0
			fisher2=0
			fisher3=0
			fisher4=0
			for row in range(0, array1.shape[0]):
				if array1[row,column] == 0:
					if array2[row, column2] == 2:
						fisher1 += 1
					elif array2[row, column2] != 2:
						fisher3 += 1
					else:
						pass
				elif array1[row,column] != 0:
					if array2[row, column2] == 2:
						fisher2 +=1
					elif array2[row, column2] != 2:
						fisher4 += 1
					else:
						pass
				else:
					pass
			fisher_1.append(fisher1)
			fisher_2.append(fisher2)
			fisher_3.append(fisher3)
			fisher_4.append(fisher4)
			fisher1=0
			fisher2=0
			fisher3=0
			fisher4=0

def fisher_exact_test(F1, F2, F3, F4):
	assert len(F1) == len(F2) == len(F3) == len(F4)
	i=0
	for group in range(0, len(F1)):
		oddsratio, pvalue = sp.fisher_exact([[F1[i], F2[i]], [F3[i], F4[i]]])
		p_values.append(pvalue)
		i+=1

def printer(pvalues, group1, group2, group2_windows):
	listed_windows = open('viability_output_03092020.csv', 'a')

	w1 = 1
	w2 = 1
	window_2 = 0
	for x in p_values:
		window_2 += 1
		if window_2 == group2_windows:
			listed_windows.write(group1+"-"+str(w1) + "," + group2+"-"+str(w2) + "," + str(x) + '\n')
			w2 = 1
			w1 += 1
			window_2 = 0
		else:
			listed_windows.write(group1+"-"+str(w1) + "," + group2+"-"+str(w2) + "," + str(x) + '\n')
			w2 += 1

	listed_windows.close()

listed_windows = open('viability_output_03092020.csv', 'w')
listed_windows.write("window1" + "," + "window2" + "," + "p-value" + '\n')
listed_windows.close()


p_values = []

chr_compare(X, Chr2)
fisher_exact_test(fisher_1, fisher_2, fisher_3, fisher_4)
printer(p_values, "X", "Chr2", 2) # ADAPT

p_values = []
fisher_1 = []
fisher_2 = []
fisher_3 = []
fisher_4 = []

chr_compare(X, Chr3)
fisher_exact_test(fisher_1, fisher_2, fisher_3, fisher_4)
printer(p_values, "X", "Chr3", 3) #ADAPT

p_values = []
fisher_1 = []
fisher_2 = []
fisher_3 = []
fisher_4 = []

chr_compare(Chr2, Chr3)
fisher_exact_test(fisher_1, fisher_2, fisher_3, fisher_4)
printer(p_values, "Chr2", "Chr3", 3) # ADAPT

p_values = []
fisher_1 = []
fisher_2 = []
fisher_3 = []
fisher_4 = []

chr_compare(Chr2, X)
fisher_exact_test(fisher_1, fisher_2, fisher_3, fisher_4)
printer(p_values, "Chr2", "X", 2) # ADAPT

p_values = []
fisher_1 = []
fisher_2 = []
fisher_3 = []
fisher_4 = []

chr_compare(Chr3, X)
fisher_exact_test(fisher_1, fisher_2, fisher_3, fisher_4)
printer(p_values, "Chr3", "X", 2) # ADAPT

p_values = []
fisher_1 = []
fisher_2 = []
fisher_3 = []
fisher_4 = []

chr_compare(Chr3, Chr2)
fisher_exact_test(fisher_1, fisher_2, fisher_3, fisher_4)
printer(p_values, "Chr3", "Chr2", 2) # ADAPT
