###New script for BD test as alternative to Fisher's
###Produces output for BD R script

import sys
import csv
import numpy as np
import scipy.stats as sp

file_name = sys.argv[1]
number_sterile = int(sys.argv[2])
number_total = int(sys.argv[3])

df = np.loadtxt(file_name, dtype=int, delimiter=',')

fisher_1 = []
fisher_2 = []
fisher_3 = []
fisher_4 = []
fisher_5 = []
fisher_6 = []
fisher_7 = []
fisher_8 = []

for window1 in range(0, df.shape[0]):
	for window2 in range(0, df.shape[0]):
		fisher1 = 0
		fisher2 = 0
		fisher3 = 0
		fisher4 = 0
		for ind in range(0, number_sterile):
			if df[window1, ind] == 0:
				if df[window2, ind] == 2:
					fisher1 += 1
				elif df[window2, ind] == 0:
					fisher3 += 1
				elif df[window2, ind] == 1:
					fisher3 += 1
				elif df[window2, ind] == -999:
					pass
				else:
					pass
			elif df[window1, ind] == 1:
				if df[window2, ind] == 2:
					fisher2 += 1
				elif df[window2, ind] == 0:
					fisher4 += 1
				elif df[window2, ind] == 1:
					fisher4 += 1
				elif df[window2, ind] == -999:
					pass
				else:
					pass
			elif df[window1, ind] == 2:
				if df[window2, ind] == 2:
					fisher2 += 1
				elif df[window2, ind] == 0:
					fisher4 += 1
				elif df[window2, ind] == 1:
					fisher4 += 1
				elif df[window2, ind] == -999:
					pass
				else:
					pass
			elif df[window1, ind] == -999:
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
	for window2 in range(0, df.shape[0]):
		fisher5 = 0
		fisher6 = 0
		fisher7 = 0
		fisher8 = 0
		for ind in range(number_sterile, number_total):
			if df[window1, ind] == 0:
				if df[window2, ind] == 2:
					fisher5 += 1
				elif df[window2, ind] == 0:
					fisher7 += 1
				elif df[window2, ind] == 1:
					fisher7 += 1
				elif df[window2, ind] == -999:
					pass
				else:
					pass
			elif df[window1, ind] == 1:
				if df[window2, ind] == 2:
					fisher6 += 1
				elif df[window2, ind] == 0:
					fisher8 += 1
				elif df[window2, ind] == 1:
					fisher8 += 1
				elif df[window2, ind] == -999:
					pass
				else:
					pass
			elif df[window1, ind] == 2:
				if df[window2, ind] == 2:
					fisher6 += 1
				elif df[window2, ind] == 0:
					fisher8 += 1
				elif df[window2, ind] == 1:
					fisher8 += 1
				elif df[window2, ind] == -999:
					pass
				else:
					pass
			elif df[window1, ind] == -999:
				pass
			else:
				pass
		fisher_5.append(fisher5)
		fisher_6.append(fisher6)
		fisher_7.append(fisher7)
		fisher_8.append(fisher8)
		fisher5 = 0
		fisher6 = 0
		fisher7 = 0
		fisher8 = 0

final_lists = []
final_lists.append(fisher_1)
final_lists.append(fisher_2)
final_lists.append(fisher_3)
final_lists.append(fisher_4)
final_lists.append(fisher_5)
final_lists.append(fisher_6)
final_lists.append(fisher_7)
final_lists.append(fisher_8)

with open('sterility_BD_output.csv', 'w', newline='') as output:
	writer = csv.writer(output)
	writer.writerows(final_lists)
