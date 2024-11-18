import pandas as pd
from sklearn import preprocessing

hmeq = pd.read_csv('hmeq_small.csv')

# Standardize the data
standardized = preprocessing.scale(hmeq)

# Output the standardized data as a data frame
hmeqStand = pd.DataFrame(standardized, columns=hmeq.columns)

# Normalize the data
normalized = preprocessing.MinMaxScaler().fit_transform(hmeq)

# Output the normalized data as a data frame
hmeqNorm = pd.DataFrame(normalized, columns=hmeq.columns)

# Print the means and standard deviations of hmeqStand and hmeqNorm
print("The means of hmeqStand are ", hmeqStand.mean())
print("The standard deviations of hmeqStand are ", hmeqStand.std())
print("The means of hmeqNorm are ", hmeqNorm.mean())
print("The standard deviations of hmeqNorm are ", hmeqNorm.std())