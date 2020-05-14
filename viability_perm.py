import sys
import numpy as np
import random as rd
import scipy.stats as sp

file_name = sys.argv[1]
X_len = int(sys.argv[2])
Chr2_len = int(sys.argv[3])
Chr3_len = int(sys.argv[4])

df = np.loadtxt(file_name, dtype=int, delimiter='\t')

len_X = list(range(0, X_len))
len_2 = list(range(X_len, Chr2_len))
len_3 = list(range(Chr2_len, Chr3_len))

#Function ensures lists are not identical at any index
global list2
def list_checker(list1, list2):
	i=0
	length = int(len(list1))
	while i < length:
		if list1[i] != list2[i]:
			pass
			i += 1
		elif list1[i] == list2[i]:
			rd.shuffle(list2)
			i=0
			continue
		else:
			pass

def chr_compare(ind1, ind2, len1, len2):
	for window1 in len1:  
		for window2 in len2:
			fisher1 = 0
			fisher2 = 0
			fisher3 = 0
			fisher4 = 0
			i=0
			for index in ind1:
				if df[window1, index] == 0:
					if df[window2, ind2[i]] == 2:
						fisher1 += 1
					elif df[window2, ind2[i]] == 0:
						fisher3 += 1
					elif df[window2, ind2[i]] == 1:
						fisher3 += 1
					elif df[window2, ind2[i]] == -999:
						pass
					else:
						pass
				elif df[window1, index] == 1:
					if df[window2, ind2[i]] == 2:
						fisher2 += 1
					elif df[window2, ind2[i]] == 0:
						fisher4 += 1
					elif df[window2, ind2[i]] == 1:
						fisher4 += 1
					elif df[window2, ind2[i]] == -999:
						pass
					else:
						pass
				elif df[window1, index] == 2:
					if df[window2, ind2[i]] == 2:
						fisher2 += 1
					elif df[window2, ind2[i]] == 0:
						fisher4 += 1
					elif df[window2, ind2[i]] == 1:
						fisher4 += 1
					elif df[window2, ind2[i]] == -999:
						pass
					else:
						pass
				elif df[window1, index] == -999:
					pass
				else:
					pass
				i += 1
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
			
####
####

names = list(range(0, np.shape(df)[1]))
names = list(map(int, names))
names2 = rd.sample(names, len(names))
list_checker(names, names2)

####
####

p_values = []
fisher_1 = []
fisher_2 = []
fisher_3 = []
fisher_4 = []

chr_compare(names, names2, len_X, len_2)
fisher_exact_test(fisher_1, fisher_2, fisher_3, fisher_4)

fisher_1 = []
fisher_2 = []
fisher_3 = []
fisher_4 = []

chr_compare(names, names2, len_X, len_3)
fisher_exact_test(fisher_1, fisher_2, fisher_3, fisher_4)

fisher_1 = []
fisher_2 = []
fisher_3 = []
fisher_4 = []

chr_compare(names, names2, len_2, len_3)
fisher_exact_test(fisher_1, fisher_2, fisher_3, fisher_4)

fisher_1 = []
fisher_2 = []
fisher_3 = []
fisher_4 = []

chr_compare(names, names2, len_2, len_X)
fisher_exact_test(fisher_1, fisher_2, fisher_3, fisher_4)

fisher_1 = []
fisher_2 = []
fisher_3 = []
fisher_4 = []

chr_compare(names, names2, len_3, len_X)
fisher_exact_test(fisher_1, fisher_2, fisher_3, fisher_4)

fisher_1 = []
fisher_2 = []
fisher_3 = []
fisher_4 = []

chr_compare(names, names2, len_3, len_2)
fisher_exact_test(fisher_1, fisher_2, fisher_3, fisher_4)

####

lowest_p = min(p_values)
listed_p = open('54_403_perm_viability_output.csv', 'a')
listed_p.write(lowest_p + '\n')
listed_p.close()
