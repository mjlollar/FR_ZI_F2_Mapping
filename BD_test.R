#### R Script to calculate Breslow-Day Statistics from sterility outputs
#### Accepts output in the form of a csv file with 8 rows and n columns
#### Rows correspond to F1,F2,F3,...,F8 for 2x2x2 table where F1-F4 in 2x2 and F5-F8 in 2x2
#### A Haldane-Anscombe correction is applied to the dataset

library("DescTools")
library("data.table")

###Specify input and output in commandline
args = commandArgs(trailingOnly=TRUE)
in_file <- args[1]
out_file <- args[2]

#### Read in data and convert to dataframe
DT <- fread(in_file, header=FALSE, sep=',')
df <- setDF(DT)
win_num <- ncol(df)

#### Initialise empty vector for p_values to improve speed (vector not copied each loop iteration)
p_values <- vector(length=win_num)

### Array for Haldane correction
HA_correct <- rep(0.5, 8)
HA.array <- array(HA_correct, dim=c(2,2,2))

#### Perform Breslow-Day test for each window
for (x in 1:win_num) {
	counts <- array(c(df[1,x],df[2,x],df[3,x],df[4,x],df[5,x],df[6,x],df[7,x],df[8,x]),
		dim=c(2,2,2))
	test.array <- counts + HA.array
	BD_output <- BreslowDayTest(test.array, OR= NA, correct= FALSE)$'p.value'
	p_values[x] <- BD_output
}

#### Formatting adjustment (personal preference)
p_values_final <- vector(replace(p_values, x=='NaN', 999))

#####output to txt or csv with fwrite
out_ps <- as.data.frame(p_values_final)
fwrite(out_ps, out_file, sep=",", row.names=FALSE)

