import sys
import numpy as np
import statsmodels.stats.contingency_tables as sm

in_file = sys.argv[1]
out_file = sys.argv[2]

df = np.loadtxt(in_file, dtype=float, delimiter=',')

p_values = []

for i in range(0, df.shape[1]):
	print(i)
	a1 = np.array([[df[0,i], df[1,i]],[df[2,i], df[3,i]]])
	a2 = np.array([[df[4,i], df[5,i]],[df[6,i], df[7,i]]])
	test_array = np.stack((a1, a2), axis=0)
	test_array = test_array + 0.5
	results = sm.StratifiedTable(test_array)
	odds_test = results.test_equal_odds()
	p_values.append(odds_test.pvalue)


listed_windows = open(out_file, 'w')

listed_windows.write("window1"+","+"window2"+","+"p-value"+ '\n')

wi1 = 1
wi2 = 1
window_row2 = 0
cutoff = 2578
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
