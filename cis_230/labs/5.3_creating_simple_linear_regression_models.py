# Import the necessary modules
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Read in nbaallelo_slr.csv
nba = pd.read_csv('nbaallelo_slr.csv')

# Create a new column in the data frame that is the difference between pts and opp_pts
nba['y'] = nba['pts'] - nba['opp_pts']

# Store relevant columns as variables
X = nba[['elo_i']].values
y = nba['y'].values.reshape(-1, 1)

# Initialize the linear regression model
SLRModel = LinearRegression()
# Fit the model on X and y
SLRModel.fit(X, y)

# Print the intercept
intercept = SLRModel.intercept_
print('The intercept of the linear regression line is ', end="")
print('%.3f' % intercept[0] + ". ")

# Print the slope
slope = SLRModel.coef_
print('The slope of the linear regression line is ', end="")
print('%.3f' % slope[0][0] + ". ")

# Compute the proportion of variation explained by the linear regression using the LinearRegression object's score method
score = SLRModel.score(X, y)
print('The proportion of variation explained by the linear regression model is ', end="")
print('%.3f' % score + ". ")