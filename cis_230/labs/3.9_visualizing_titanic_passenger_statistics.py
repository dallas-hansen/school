import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load titanic.csv
titanic = pd.read_csv('titanic.csv')

# Subset the titanic dataset to include first class passengers who embarked in Southampton
firstSouth = titanic[(titanic['pclass'] == 1) & (titanic['embark_town'] == 'Southampton')]

# Subset the titanic dataset to include either second or third class passenger
secondThird = titanic[(titanic['pclass'] == 2) | (titanic['pclass'] == 3)]

print(firstSouth.head())
print(secondThird.head())

# Create a bar chart for the first class passengers who embarked in Southampton grouped by sex
sns.barplot(x='sex', y='survived', data=firstSouth)
plt.savefig('titanic_bar_1.png')

# Create a bar chart for the second and third class passengers grouped by survival status
sns.barplot(x='pclass', y='survived', data=secondThird)
plt.legend(labels=["0","1"], title = "survived")
plt.savefig('titanic_bar_2.png')