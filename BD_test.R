#### R Script to calculate Breslow-Day Statistics from sterility outputs
#### Accepts output in the form of a csv file with 8 rows and n columns
#### Rows correspond to F1,F2,F3,...,F8 for 2x2x2 table where F1-F4 in 2x2 and F5-F8 in 2x2
#### BRESLOW DAY TEST WILL NOT WORK IF dataframe[0,0] has a zero value. Placehold with integer to run

library("DescTools")
library("data.table")

DT <- fread("sterility_BD_output_0to2.csv", header=FALSE, sep=',') ## Adjust for correct output file name
df <- setDF(DT)
win_num <- ncol(df)
p_values <- vector(length=win_num)

for (x in 1:win_num) {
	print(x)
	counts <- array(c(df[1,x],df[2,x],df[3,x],df[4,x],df[5,x],df[6,x],df[7,x],df[8,x]),
		dim=c(2,2,2))
	test <- BreslowDayTest(counts, OR= NA, correct= FALSE)$'p.value'
	p_values[x] <- test
	rm(test)
	rm(counts)
}

write.csv(p_values, "BD__final_output_sterility.csv", row.names=FALSE)
