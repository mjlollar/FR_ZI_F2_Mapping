import sys
import pandas as pd

df = pd.read_csv(sys.argv[1])
outfile = sys.argv[2]

window1_value = []
window2_value = []

def printer(p_values, group1, group2, group2_windows, spacer1, spacer2):
	w1 = 1 + int(spacer1)
	w2 = 1 + int(spacer2)
	window_2 = 0
	for x in p_values:
		window_2 += 1
		if window_2 == group2_windows:
			window1_value.append(group1+"-"+str(w1))
			window2_value.append(group2+"-"+str(w2))
			w2 = 1 + int(spacer2)
			w1 += 1
			window_2 = 0
		else:
			window1_value.append(group1+"-"+str(w1))
			window2_value.append(group2+"-"+str(w2))
			w2 += 1

p1 = range(0,533555)
p2 = range(0,574975)
p3 = range(0,1032845)

printer(p1, "X", "Chr2", 979, 0, 545)
printer(p2, "X", "Chr3", 1055, 0, 1524)
printer(p3, "Chr2", "Chr3", 1055, 545, 1524)

df["window1"] = window1_value
df["window2"] = window2_value

df.to_csv(outfile, index=False)
