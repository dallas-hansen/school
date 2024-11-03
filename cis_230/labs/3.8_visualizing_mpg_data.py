import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load the mpg data set
mpg = pd.read_csv('mpg.csv')

# Create a new data frame with the columns "weight" and "mpg"
mpgSmall = mpg[['weight', 'mpg']]

print(mpgSmall)

# Create a scatter plot of weight vs mpg with x label "Weight" and y label "MPG"
sns.scatterplot(x='weight', y='mpg', data=mpgSmall)

plt.savefig('mpg_scatter.png')