import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy.stats import linregress

df = pd.DataFrame({
    'Distance (m)': [.09,.095,.1,.1,.1],
    'Time (s)': [.0161,.0167,.0179,.0177,.0176]
})

# Perform Quadratic Regression
coeffs = np.polyfit(df['Time (s)'], df['Distance (m)'], 2)  # 2nd-degree polynomial
a, b, c = coeffs  # Unpack coefficients

slope, intercept, r_value, p_value, std_err = linregress(df['Time (s)'], df['Distance (m)'])
plt.figure(figsize=(9,6))

sns.regplot(x='Time (s)', y='Distance (m)', data=df, order=2, ci=None)

x_max = df['Time (s)'].max()
y_max = df['Distance (m)'].max()

equation = f"y = {a:.4f}x² + {b:.4f}x + {c:.4f}\nR² = {r_value:.4f}"
plt.text(x_max - .001, y_max - .005, equation, fontsize=12, color="black", alpha=0.5)
plt.title('Velocity of spring propelled ball')
plt.show()

