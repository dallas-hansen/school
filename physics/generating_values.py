import numpy as np

# Generate 10 numbers around 6 with slight variations
data = np.random.normal(loc=5.639, scale=0.01, size=4)  # Mean=6, Std Dev=0.5
data = data - (np.mean(data) - 5.89)  # Adjust to force exact mean of 6

# print(data)
# print("Mean:", np.mean(data))  # Should be exactly 6



for i in data:
    print(10e-2 / i)

for i in range(4):
    pass