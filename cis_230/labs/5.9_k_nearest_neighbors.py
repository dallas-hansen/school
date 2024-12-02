# Import needed packages for classification
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Iport packages for evaluation
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Load the dataset
skySurvey = pd.read_csv('SDSS.csv')

# Create a new feature from u - g
skySurvey['u_g'] = skySurvey['u'] - skySurvey['g']

# Create dataframe X with features redshift and u_g
X = skySurvey[['redshift', 'u_g']]

# Create dataframe y with feature class
y = skySurvey[['class']]

np.random.seed(42)

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Initialize model with k=3
skySurveyKnn = KNeighborsClassifier(n_neighbors=3)

# Fit model using X_train and y_train
skySurveyKnn.fit(X_train, y_train)

# Find the predicted classes for X_test
y_pred = skySurveyKnn.predict(X_test)

# Calculate accuracy score
score = metrics.accuracy_score(y_test, y_pred)

# Print accuracy score
print('Accuracy score is ', end="")
print('%.3f' % score)

# Print confusion matrix 
print(metrics.confusion_matrix(y_test, y_pred))