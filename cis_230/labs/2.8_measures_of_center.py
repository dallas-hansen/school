import pandas as pd

# Read in the file mtcars.csv
cars = pd.read_csv('mtcars.csv')

# Select only the numeric columns and calculate the mean for 'wt'
mean = cars.select_dtypes(include='number').mean()['wt']

# Select only the numeric columns and calculate the median for 'wt'
median = cars.select_dtypes(include='number').median()['wt']


print("mean = {:.5f}, median = {:.3f}".format(mean, median))