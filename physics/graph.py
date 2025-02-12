import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

y = [-10, -10, -10, -10, -17, -17, -17, -17]
x = [.61, .618, .565, .582, .424, .424, .424, .424]

df = pd.DataFrame({'distance': x, 'angle': y})
print(df)


sns.scatterplot(data=df, x=df.index, y=df['angle'], color='purple', label='Data Points')
sns.scatterplot(data=df, x=df.index, y=df['distance'], color='red', label='Data Points')

plt.title('Exponential Graph')
plt.xlabel('Trial Number')
plt.legend()
plt.show()