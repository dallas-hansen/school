import statsmodels.stats as st
from statsmodels.stats.proportion import proportions_ztest
import pandas as pd

# Read in gpa.csv
gpa = pd.read_csv('gpa.csv')

# Get the value of the proportion for the null hypothesis
value = float(input())
# Get the gpa cutoff
cutoff = float(input())

# Determine the number of students with a gpa higher than cutoff
counts = gpa[gpa['gpa'] > cutoff].shape[0]

# Determine the total number of students
nobs = gpa.shape[0]

# Perform z-test for counts, nobs, and value
# Modify prop_var parameter
ztest = proportions_ztest(count=counts, nobs=nobs, value=value, prop_var=value)
print("(", end="")
print('%.3f' % ztest[0] + ", ", end="")
print('%.3f' % ztest[1] + ")")


if ztest[1] < 0.01:
    print("The two-tailed p-value, ", end="")
    print('%.3f' % ztest[1] + ", is less than \u03B1. Thus, sufficient evidence exists to support the hypothesis that the proportion is different from", value)
else:
    print("The two-tailed p-value, ", end="")
    print('%.3f' % ztest[1] + ", is greater than \u03B1. Thus, insufficient evidence exists to support the hypothesis that the proportion is different from", value)