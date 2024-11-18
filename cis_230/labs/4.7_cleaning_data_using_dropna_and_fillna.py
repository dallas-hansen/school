import pandas as pd

# Read in hmeq_small.csv
hmeq = pd.read_csv('hmeq_small.csv')

# Create a new data frame with the rows with missing values dropped
hmeqDelete = hmeq.dropna()

# Create a new data frame with the missing values filled in by the mean of the column
hmeqReplace = hmeq.fillna(hmeq.mean())

# Print the means of the columns for each new data frame
print("Means for hmeqDelete are ", hmeqDelete.mean())

print("Means for hmeqReplace are ", hmeqReplace.mean())